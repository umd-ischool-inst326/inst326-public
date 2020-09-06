all: index slides

index: README.adoc ../../includes/navigation.html
	asciidoctor README.adoc -o index.html

slides: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

clean:
	rm -f index.html slides.html
