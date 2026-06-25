#!/usr/bin/env python3
"""Generate cv/cv.tex from _data/*.yml — the single source of truth.

Run via `make cv`, which then compiles the result with XeLaTeX. CV facts are NEVER
hand-edited in LaTeX; edit the YAML in _data/ and regenerate.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency. Run: pip install pyyaml jinja2")
try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    sys.exit("Missing dependency. Run: pip install pyyaml jinja2")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "_data")
CVDIR = os.path.join(ROOT, "cv")

_SPECIAL = {
    "\\": r"\textbackslash{}",
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}
_PATTERN = re.compile("|".join(re.escape(k) for k in sorted(_SPECIAL, key=len, reverse=True)))


def texesc(value):
    if value is None:
        return ""
    return _PATTERN.sub(lambda m: _SPECIAL[m.group()], str(value))


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def main():
    env = Environment(
        loader=FileSystemLoader(CVDIR),
        block_start_string="((*", block_end_string="*))",
        variable_start_string="(((", variable_end_string=")))",
        comment_start_string="((#", comment_end_string="#))",
        trim_blocks=True, lstrip_blocks=True, autoescape=False,
    )
    env.filters["tex"] = texesc

    ctx = {
        "profile": load("profile.yml"),
        "cv": load("cv.yml"),
        "publications": load("publications.yml"),
    }
    rendered = env.get_template("cv.tex.j2").render(**ctx)
    out = os.path.join(CVDIR, "cv.tex")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(rendered)
    print("✓ cv/cv.tex generated from _data/*.yml")


if __name__ == "__main__":
    main()
