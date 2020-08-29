all: index slides

index: README.md ../../includes/navigation.html
	pandoc -s README.md \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html \
	       -o index.html

slides: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

clean:
	rm index.html
	rm slides.html
