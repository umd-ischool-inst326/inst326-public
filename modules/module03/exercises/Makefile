all: index.html exercises

index.html: README.adoc ../../../includes/navigation.html
	asciidoctor README.adoc -o index.html

exercises:
	asciidoctor exercise_bulk_pricing.adoc  -o exercise_bulk_pricing.html
	asciidoctor exercise_testing.adoc       -o exercise_testing.html
	asciidoctor exercise_covid_testing.adoc -o exercise_covid_testing.html

clean:
	rm -f index.html exercise_bulk_pricing.html exercise_testing.html
