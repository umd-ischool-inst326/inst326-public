all: index.html exercise01 exercise02

index.html: README.adoc ../../../includes/navigation.html
	asciidoctor README.adoc -o index.html

exercise01: exercise01.adoc ../../../includes/navigation.html
	asciidoctor exercise01.adoc -o exercise01.html

exercise02: exercise02.adoc ../../../includes/navigation.html
	asciidoctor exercise02.adoc -o exercise02.html

clean:
	rm -f index.html exercise01.html exercise02.html
