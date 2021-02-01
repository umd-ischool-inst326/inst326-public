all: index.html exercise1 exercise2 exercise3

index.html: README.adoc ../../../includes/navigation.html exercise1 exercise2
	asciidoctor README.adoc -o index.html

exercise1: exercise01_rock_paper_scissors.adoc ../../../includes/navigation.html
	asciidoctor -o exercise01_rock_paper_scissors.html exercise01_rock_paper_scissors.adoc

exercise2: exercise01_easter_date.adoc ../../../includes/navigation.html
	asciidoctor -o exercise01_easter_date.html exercise01_easter_date.adoc

exercise3: exercise01_covid_testing.adoc ../../../includes/navigation.html
	asciidoctor -o exercise01_covid_testing.html exercise01_covid_testing.adoc

clean:
	rm -f *.html
