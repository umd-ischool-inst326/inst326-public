all: index slides exercises_dir lab_dir

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

# slides: slides.md
# 	pandoc --to revealjs --standalone --output slides.html slides.md
slides: slides.adoc
	asciidoctor-revealjs slides.adoc -o slides.html

exercises_dir:
	cd exercises && $(MAKE)

lab_dir:
	cd lab && $(MAKE)

clean:
	rm index.html
	rm slides.html
	cd exercises && $(MAKE) clean
	cd lab && $(MAKE) clean
