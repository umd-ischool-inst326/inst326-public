all: index slides slides_gabriel exercises_dir

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides_gabriel: slides_gabriel.adoc
	asciidoctor-revealjs slides_gabriel.adoc -o slides_gabriel.html

slides: slides_gabriel.adoc
	asciidoctor-revealjs slides_gabriel.adoc -o slides.html

exercises_dir:
	cd exercises && $(MAKE)

clean:
	rm -f index.html slides.html
	cd exercises && $(MAKE) clean