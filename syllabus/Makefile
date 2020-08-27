all: index current

index: README.md
	pandoc -s README.md \
	       -o index.html \
	       --template=Github.html5 \
	       -B ../includes/navigation.html

current: fa2020.tex
	pdflatex fa2020.tex > /dev/null
	rm *.out *.log *.aux

clean:
	rm -f index.html fa2020.pdf
