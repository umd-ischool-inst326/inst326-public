all: index slides exercises_dir

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.adoc
	asciidoctor-revealjs slides.adoc -o slides.html

exercises_dir:
	cd exercises && $(MAKE)

clean:
	rm -f index.html slides.html
