all: index.html exercise1 exercise2 exercise3

index.html: README.adoc ../../../includes/navigation.html exercise1 exercise2
	asciidoctor README.adoc -o index.html

exercise1: exercise05_songs.adoc ../../../includes/navigation.html
	asciidoctor -o exercise05_songs.html exercise05_songs.adoc

exercise2: exercise05_books.adoc ../../../includes/navigation.html
	asciidoctor -o exercise05_books.html exercise05_books.adoc

exercise3: exercise05_covid.adoc ../../../includes/navigation.html
	asciidoctor -o exercise05_covid.html exercise05_covid.adoc

clean:
	rm -f *.html
