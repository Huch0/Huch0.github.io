# Academic homepage — common tasks
#
#   make serve   run the site locally with live reload
#   make build   build the static site into _site/
#   make cv      regenerate assets/files/cv.pdf from _data/*.yml (Python + XeLaTeX)
#   make clean   remove build artifacts

.PHONY: serve build cv clean

serve:
	bundle exec jekyll serve --livereload

build:
	bundle exec jekyll build

# Single source of truth: _data/*.yml -> cv/cv.tex (generated) -> assets/files/cv.pdf
# The .tex is a render target; never edit CV facts in LaTeX, edit the YAML.
cv:
	python3 cv/generate_cv.py
	cd cv && xelatex -interaction=nonstopmode cv.tex >/dev/null && xelatex -interaction=nonstopmode cv.tex >/dev/null
	mkdir -p assets/files
	cp cv/cv.pdf assets/files/cv.pdf
	@echo "✓ assets/files/cv.pdf regenerated"

clean:
	rm -rf _site .jekyll-cache cv/cv.aux cv/cv.log cv/cv.out cv/cv.tex cv/cv.pdf
