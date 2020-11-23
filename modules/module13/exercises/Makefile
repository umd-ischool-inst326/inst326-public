all: index.html exercise1 exercise2

index.html: README.adoc ../../../includes/navigation.html exercise1
	asciidoctor README.adoc -o index.html

exercise1: exercise13_iris.adoc ../../../includes/navigation.html
	asciidoctor -o exercise13_iris.html exercise13_iris.adoc

exercise2: exercise13_airbnb.adoc ../../../includes/navigation.html
	asciidoctor -o exercise13_airbnb.html exercise13_airbnb.adoc

clean:
	rm -f index.html exercise13_airbnb.html exercise13_iris.html
