from flask import Flask, request, jsonify
import spacy

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

app = Flask(__name__)

# Carga el modelo de spaCy para NER en español
nlp = spacy.load('es_core_news_sm')

@app.route('/ner', methods=['POST'])
def recognize_entities():
    try:
        # Obtén los datos del JSON de la solicitud
        data = request.json
        oraciones = data.get('oraciones', [])
        resultados = []

        # Procesa cada oración usando spaCy y extrae las entidades nombradas
        for oracion in oraciones:
            doc = nlp(oracion)
            entidades = {}

            for ent in doc.ents:
                entidades[ent.text] = ent.label_

            # Agrega el resultado al formato deseado
            resultados.append({
                'oración': oracion,
                'entidades': entidades
            })

        # Devuelve el resultado como JSON
        return jsonify({'resultado': resultados})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)