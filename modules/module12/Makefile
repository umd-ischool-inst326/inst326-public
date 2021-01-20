all: index slides exercise

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

exercise: exercise.adoc ../../includes/navigation.html
	asciidoctor exercise.adoc -o exercise.html

slides: slides.adoc
	asciidoctor-revealjs slides.adoc -o slides.html

clean:
	rm -f index.html slides.html 
