all: exercises

exercises: exercise_car.adoc exercise_appointment.adoc
	asciidoctor -o exercise_car.html exercise_car.adoc
	asciidoctor -o exercise_appointment.html exercise_appointment.adoc

clean:
	rm -f exercise_car.html exercise_appointment.html

