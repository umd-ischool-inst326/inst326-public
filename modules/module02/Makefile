all: index slides

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.adoc
	asciidoctor-revealjs slides.adoc -o slides.html

clean:
	rm -f index.html slides.html
