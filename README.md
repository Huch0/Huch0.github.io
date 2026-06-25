# Chiyeong Heo — Academic Homepage

A clean, data-driven academic homepage built with **plain Jekyll** (no theme gem) and
deployed to GitHub Pages. All personal facts live in `_data/*.yml` as a **single source of
truth**; the website pages and the **LaTeX CV** are both generated from it, so they never
drift apart.

Live at **https://huch0.github.io**.

## Run locally

Requires **Ruby 3.x** (via `rbenv`/`chruby`/Homebrew — the macOS system Ruby 2.6 is too old).

```bash
bundle install      # first time only
make serve          # http://127.0.0.1:4000  (live reload)
# or: make build    # one-off build into _site/
```

## Edit content (no HTML needed)

Everything is in `_data/`:

| File | Controls |
|------|----------|
| `_data/profile.yml` | profile card: name, affiliation, advisor, email, social links, photo, CV link |
| `_data/publications.yml` | publications (About + Publications pages **and** the CV) |
| `_data/projects.yml` | the Projects page |
| `_data/cv.yml` | bio, research interests, education, experience, patents, awards (About page **and** the CV) |

Conventions:
- **Author highlighting:** in a publication's `authors`, set `me: true` to bold your name and
  `eq: true` to add an equal-contribution dagger (†). Names are kept exactly as published.
- **Placeholders:** mark unknown items with `todo: true` — they render as an italic note on the
  web and are omitted from the PDF, so nothing unverified is ever published.
- **Links:** a link with `url: "TODO"` renders a dashed, non-clickable placeholder button.

Replace the placeholder headshot by overwriting `assets/img/profile.jpg`.

## Regenerate the CV (PDF)

The CV is **generated from the same YAML**, not hand-written. Edit `_data/cv.yml` /
`_data/publications.yml`, then:

```bash
make cv     # _data/*.yml -> cv/cv.tex (Python+Jinja2) -> assets/files/cv.pdf (XeLaTeX)
```

Requires **Python 3** (`pyyaml`, `jinja2`) and **XeLaTeX**. The Atkinson Hyperlegible font is
bundled in `cv/fonts/`, so the build is self-contained. Commit the regenerated
`assets/files/cv.pdf`. Style lives in `cv/cv.tex.j2` (edit only to restyle, never for facts).

## Restyle the design

All colors (light + dark), fonts, spacing, and sizing are CSS variables in **one file**:
`_sass/_tokens.scss`. Change the look there without touching any markup. Readers can switch
font (Atkinson / Source Serif / System) and light/dark from the top bar; choices persist.

## Deployment

Pushing to `master` triggers `.github/workflows/pages-deploy.yml`, which builds the site with
Jekyll (Ruby 3.3, `JEKYLL_ENV=production`) and publishes it to GitHub Pages. No manual steps.

## Outstanding TODOs

- Undergraduate education in `_data/cv.yml`
- Experience and Awards & Honors in `_data/cv.yml`
- MMTB `code` / `dataset` URLs in `_data/publications.yml`
- Real headshot at `assets/img/profile.jpg`
- Run `make cv` once your real CV content is in (current PDF is generated from the scaffold)

## Layout

```
_data/        single source of truth (YAML)
_layouts/     base HTML document
_includes/    profile card, nav, controls, publication/project partials, icons
_sass/        _tokens.scss (design system) + base/layout/components
assets/       css, bib, favicons, files/cv.pdf, img/profile.jpg
cv/           LaTeX CV pipeline: cv.tex.j2 (template) + generate_cv.py + fonts/
docs/adr/     architecture decision records
index.md publications.md projects.md cv.md
```

Built on the old Chirpy blog's history — the previous site is preserved on the
`backup/chirpy-blog` branch and the `chirpy-archive` tag.
