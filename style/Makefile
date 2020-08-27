all: index guide pdf

index: README.adoc
	asciidoctor README.adoc -o index.html

guide: style-guide.adoc
	asciidoctor style-guide.adoc -o style-guide.html

pdf: style-guide.adoc
	asciidoctor-pdf style-guide.adoc -o style-guide.pdf

clean:
	rm -f index.html style-guide.html style-guide.pdf
