all: index.html exercise1 exercise2

index.html: README.adoc ../../../includes/navigation.html exercise1 exercise2
	asciidoctor README.adoc -o index.html

exercise1: exercise05_songs.adoc ../../../includes/navigation.html
	asciidoctor -o exercise05_songs.html exercise05_songs.adoc

exercise2: exercise05_books.adoc ../../../includes/navigation.html
	asciidoctor -o exercise05_books.html exercise05_books.adoc

clean:
	rm -f index.html exercise05_books.html  exercise05_songs.html 
