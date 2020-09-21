all: index

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.adoc
	asciidoctor-revealjs -o slides.html slides.adoc

clean:
	rm -f index.html slides.html
