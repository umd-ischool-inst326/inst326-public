all: index.html

index.html: README.adoc ../../../includes/navigation.html
	asciidoctor README.adoc -o index.html

clean:
	rm -f index.html exercise01.html exercise02.html
