all: sp2019-101.pdf sp2019-105.pdf fa2019-103.pdf

sp2019-101.pdf: sp2019-101.tex
	pdflatex sp2019-101.tex > /dev/null
	rm *.out *.log *.aux

sp2019-105.pdf: sp2019-105.md
	pandoc --pdf-engine=xelatex sp2019-105.md -o sp2019-105.pdf

fa2019-103.pdf: fa2019-103.tex
	pdflatex fa2019-103.tex > /dev/null
	rm *.out *.log *.aux
