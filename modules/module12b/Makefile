all: index exercises_dir slides

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.adoc
	asciidoctor-revealjs slides.adoc -o slides.html

exercises_dir:
	cd exercises && $(MAKE)

clean:
	rm index.html
	rm slides.html
	cd exercises && $(MAKE) clean
