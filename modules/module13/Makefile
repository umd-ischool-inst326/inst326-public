all: index

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html
	asciidoctor exercise.adoc -o exercise.html
	asciidoctor-revealjs slides.adoc -o slides.html

clean:
	rm -f index.html slides.html
