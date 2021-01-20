all: index slides exercises_dir

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

exercises_dir:
	cd exercises && $(MAKE)

clean:
	rm -f index.html slides.html
	cd exercises && $(MAKE) clean