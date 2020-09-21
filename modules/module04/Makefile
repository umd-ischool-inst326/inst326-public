all: index slides exercises_dir

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.adoc
	asciidoctor-revealjs -o slides.html slides.adoc

exercises_dir:
	cd exercises && $(MAKE)

clean:
	rm -f index.html slides.html
