all: index.html exercise1

index.html: README.adoc ../../../includes/navigation.html exercise1
	asciidoctor README.adoc -o index.html

exercise1: exercise08_marathon.adoc ../../../includes/navigation.html
	asciidoctor -o exercise08_marathon.html exercise08_marathon.adoc

clean:
	rm -f index.html exercise08_marathon.html
