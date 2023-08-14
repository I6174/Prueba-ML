Para que la API funcione se debe tener lo siguiente:

1.- Se debe tener instaladas las siguientes dependencias
	pip install Flask spacy
	python -m spacy download es_core_news_sm

2.- Desde la línea de comando hay que navegar hasta el archivo 'app.py' y ejecuta
	python app.py

3.- La API ya esta lista para peticiones POST en 
	http://127.0.0.1:5000/ner

4.- Se puede hacer la petición de POST con 'Postman', el cuerpo del JSON debe ser:
	{
    		"oraciones": [
        		"Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        		"San Francisco considera prohibir los robots de entrega en la acera."
    		]
	}
