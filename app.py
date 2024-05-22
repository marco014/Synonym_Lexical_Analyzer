from flask import Flask, render_template, request
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Diccionario de sinónimos
synonyms_dict = {
    "rápido": "veloz",
    "lento": "pausado",
    "inteligente": "listo",
    "feliz": "contento",
    "triste": "afligido",
    "grande": "enorme",
    "pequeño": "diminuto",
    "fuerte": "robusto",
    "débil": "frágil",
    "bonito": "hermoso",
    "feo": "horrible",
    "amable": "cortés",
    "grosero": "rudo",
    "amigo": "compañero",
    "enemigo": "adversario",
    "trabajo": "empleo",
    "dinero": "plata",
    "casa": "hogar",
    "coche": "automóvil",
    "bicicleta": "bici",
    "mujer": "dama",
    "hombre": "caballero",
    "niño": "chico",
    "niña": "chica",
    "perro": "can",
    "gato": "felino",
    "cielo": "firmamento",
    "tierra": "suelo",
    "mar": "océano",
    "lago": "laguna",
    "rio": "arroyo",
    "montaña": "cerro",
    "valle": "depresión",
    "bosque": "selva",
    "desierto": "arenal",
    "ciudad": "metrópolis",
    "pueblo": "aldea",
    "camino": "sendero",
    "carretera": "autopista",
    "edificio": "estructura",
    "puente": "viaducto",
    "ciencia": "sabiduría",
    "arte": "creación",
    "música": "melodía",
    "libro": "volumen",
    "película": "filme",
    "juego": "diversión",
    "computadora": "ordenador",
    "teléfono": "móvil",
    "reloj": "cronómetro"
}

def lexical_analyzer(text, synonyms_dict):
    pattern = re.compile(r'\b\w+\b|\d+|[^\w\s]')
    results = []
    lines = text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        for match in pattern.finditer(line):
            word = match.group().lower()  # Convertir a minúsculas para comparar
            if word in synonyms_dict:
                results.append((match.group(), synonyms_dict[word], "X", "", "", line_number, ""))
            elif word.isdigit():
                results.append((match.group(), "", "", "", "X", line_number, ""))
            elif not word.isalnum():
                results.append((match.group(), "", "", "X", "", line_number, ""))
            else:
                results.append((match.group(), match.group(), "", "", "", line_number, "X"))

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        analysis_result = lexical_analyzer(input_text, synonyms_dict)

        return render_template('index.html', analysis_result=analysis_result, input_text=input_text)

    return render_template('index.html', analysis_result=[], input_text='')

if __name__ == '__main__':
    app.run(debug=True)
