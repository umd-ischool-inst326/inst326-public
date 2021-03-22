all: index pizza enron covid

index: README.adoc ../../../includes/navigation.html
	asciidoctor README.adoc -o index.html

pizza: exercise09_pizza.adoc
	asciidoctor exercise09_pizza.adoc -o exercise09_pizza.html

enron: exercise09_enron.adoc
	asciidoctor exercise09_enron.adoc -o exercise09_enron.html

covid: exercise09_covid.adoc
	asciidoctor exercise09_covid.adoc -o exercise09_covid.html

clean:
	rm *.html
