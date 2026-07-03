#!/usr/bin/env python3
"""Generate the CV LaTeX from _data/*.yml — the single source of truth.

Builds both languages: English -> cv/cv.tex, Korean -> cv/cv-kr.tex, from the same
YAML. `*_kr` fields hold Korean translations; anything without a `_kr` falls back to
the English value (e.g., publication titles stay English). `make cv` compiles both.
CV facts are never hand-edited in LaTeX — edit the YAML and regenerate.
"""
import os
import re
import sys

try:
    import yaml
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    sys.exit("Missing dependency. Run: pip install pyyaml jinja2")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "_data")
CVDIR = os.path.join(ROOT, "cv")

LANGS = ("en", "kr")

LABELS = {
    "en": {
        "education": "Education", "experience": "Experience",
        "publications": "Publications", "patents": "Patents",
        "awards": r"Awards \& Honors", "projects": "Projects",
        "mentoring": "Mentoring", "class_projects": "Class Projects",
        "equal": "Equal contribution", "inventors": "Inventors", "assignee": "Assignee",
    },
    "kr": {
        "education": "학력", "experience": "경력",
        "publications": "논문", "patents": "특허",
        "awards": "수상 및 장학", "projects": "프로젝트",
        "mentoring": "멘토링", "class_projects": "수업 프로젝트",
        "equal": "공동 기여", "inventors": "발명자", "assignee": "출원인",
    },
}

_SPECIAL = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}
_PATTERN = re.compile("|".join(re.escape(k) for k in sorted(_SPECIAL, key=len, reverse=True)))


def texesc(value):
    if value is None:
        return ""
    return _PATTERN.sub(lambda m: _SPECIAL[m.group()], str(value))


def make_L(lang):
    """Return an accessor: L(obj, 'field') -> Korean field with English fallback."""
    def L(obj, key):
        if not obj:
            return ""
        if lang == "kr":
            v = obj.get(key + "_kr")
            if v not in (None, ""):
                return v
        return obj.get(key, "") or ""
    return L


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main():
    data = {
        "profile": load("profile.yml"),
        "cv": load("cv.yml"),
        "publications": load("publications.yml"),
        "projects": load("projects.yml"),
    }
    for lang in LANGS:
        env = Environment(
            loader=FileSystemLoader(CVDIR),
            block_start_string="((*", block_end_string="*))",
            variable_start_string="(((", variable_end_string=")))",
            comment_start_string="((#", comment_end_string="#))",
            trim_blocks=True, lstrip_blocks=True, autoescape=False,
        )
        env.filters["tex"] = texesc
        env.globals["L"] = make_L(lang)
        rendered = env.get_template("cv.tex.j2").render(lang=lang, labels=LABELS[lang], **data)
        out = os.path.join(CVDIR, "cv.tex" if lang == "en" else "cv-%s.tex" % lang)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(rendered)
        print("✓ %s generated from _data/*.yml" % os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
