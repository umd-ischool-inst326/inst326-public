all: index.html exercise1

index.html: README.adoc ../../../includes/navigation.html exercise1
	asciidoctor README.adoc -o index.html

exercise1: exercise07_people.adoc ../../../includes/navigation.html
	asciidoctor -o exercise07_people.html exercise07_people.adoc

clean:
	rm -f index.html exercise07_people.html
