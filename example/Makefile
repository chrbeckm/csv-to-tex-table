all: build/3-tex.pdf

build/output.csv: 1-python.py | build
	python 1-python.py

build/output.tex: 2-sed.sh build/output.csv | build
	bash 2-sed.sh

build/3-tex.pdf: build/output.tex

build/3-tex.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
		--interaction=batchmode \
		--halt-on-error \
	3-tex.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
