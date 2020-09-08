all: index.html exercise01 exercise02 exercise03 exercise04 exercise05

index.html: README.adoc ../../../includes/navigation.html
	asciidoctor README.adoc -o index.html

exercise01: exercise01.adoc ../../../includes/navigation.html
	asciidoctor exercise01.adoc -o exercise01.html

exercise02: exercise02.adoc ../../../includes/navigation.html
	asciidoctor exercise02.adoc -o exercise02.html

exercise03: exercise03.adoc ../../../includes/navigation.html
	asciidoctor exercise03.adoc -o exercise03.html

exercise04: exercise04.adoc ../../../includes/navigation.html
	asciidoctor exercise04.adoc -o exercise04.html

exercise05: exercise05.adoc ../../../includes/navigation.html
	asciidoctor exercise05.adoc -o exercise05.html

clean:
	rm -f index.html exercise01.html exercise02.html exercise03.html exercise04.html exercise05.html
