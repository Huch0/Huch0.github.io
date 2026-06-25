# Academic homepage

Data-driven academic homepage on plain Jekyll (no theme gem), deployed to GitHub Pages via
Actions. Content lives in `_data/*.yml` as a single source of truth; the website pages and the
LaTeX CV are generated from it.

## Run locally

Requires Ruby 3.x.

```bash
bundle install      # first time
make serve          # http://127.0.0.1:4000 (live reload)
make build          # one-off build into _site/
```

## Edit content

All in `_data/`:

| File | Controls |
|------|----------|
| `profile.yml` | profile card: name, affiliation, advisor, email, links, photo, CV |
| `publications.yml` | publications (About + Publications pages and the CV) |
| `projects.yml` | Projects page (featured / mentoring / class projects) |
| `cv.yml` | bio, research interests, education, experience, patents, awards (About + CV) |

Conventions:
- Author keys: `me: true` bolds an author; `eq: true` adds an equal-contribution dagger (†).
- `todo: true` renders an italic placeholder on the web and is omitted from the PDF.
- A link with `url: "TODO"` renders a dashed, non-clickable placeholder.
- Replace the profile photo by overwriting `assets/img/profile.jpg`.

## Regenerate the CV

The CV PDF is generated from the same YAML — never hand-written:

```bash
make cv     # _data/*.yml -> cv/cv.tex (Python+Jinja2) -> assets/files/cv.pdf (XeLaTeX)
```

Requires Python 3 (`pyyaml`, `jinja2`) and XeLaTeX. The font is bundled in `cv/fonts/`, so the
build is self-contained. Commit the regenerated `assets/files/cv.pdf`. Style lives in
`cv/cv.tex.j2` (edit only to restyle, not for content).

## Restyle

Colors (light + dark), fonts, spacing, and sizing are CSS variables in `_sass/_tokens.scss`.
Visitors can switch font, light/dark theme, and accent color from the top bar; choices persist
in `localStorage`.

## Deployment

Pushing to `master` triggers `.github/workflows/pages-deploy.yml`, which builds with Jekyll
(`JEKYLL_ENV=production`) and publishes to GitHub Pages.

## Layout

```
_data/        single source of truth (YAML)
_layouts/     base HTML document
_includes/    profile card, nav, controls, publication/project partials, icons
_sass/        _tokens.scss (design system) + base / layout / components
assets/       css, bib, favicons, files/cv.pdf, img/profile.jpg
cv/           LaTeX CV pipeline: cv.tex.j2 + generate_cv.py + fonts/
docs/adr/     architecture decision records
index.md publications.md projects.md cv.md
```
