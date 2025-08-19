from flask import render_template, request, Flask

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return render_template("index.html",
        Texto="Soma de um número",
        texto_sub="Subtração de um número",
        texto_idade="Verificador de idade"
    )

@app.route("/processar", methods=["POST"])
def processar_soma():
    primeiro_numero = float(request.form["primeiro_numero"])
    segundo_numero = float(request.form["segundo_numero"])
    resultado_soma = primeiro_numero + segundo_numero
    resultado = f"{primeiro_numero} + {segundo_numero} = {resultado_soma}"

    return render_template("index.html",
        Texto="Soma de um número",
        texto_sub="Subtração de um número",
        texto_idade="Verificador de idade",
        resultadoForm=resultado)

@app.route("/sub", methods=["POST"])
def processar_subtracao():
    terceiro_numero = float(request.form["terceiro_numero"])
    quarto_numero = float(request.form["quarto_numero"])
    resultado_sub = f"{terceiro_numero} - {quarto_numero} = {terceiro_numero - quarto_numero}"

    return render_template("index.html",
        Texto="Soma de um número",
        texto_sub="Subtração de um número",
        texto_idade="Verificador de idade",
        resultadoForm2=resultado_sub)

@app.route("/verificador_idade", methods=["POST"])
def verificador_idade():
    idade = int(request.form["idade"])
    if idade >= 18:
        a = "Maior de idade :)"
    else:
        a = "Menor de idade :)"

    return render_template("index.html",
        Texto="Soma de um número",
        texto_sub="Subtração de um número",
        texto_idade="Verificador de idade",
        resultadoForm3=a)
@app.route("/laco", methods=["POST"])
def laco():
    for i in range (1,101,2):
        print(i)
        x = []
        x.append(i)
    return render_template("index.html",
        Texto="Soma de um número",
        texto_sub="Subtração de um número",
        texto_idade="Verificador de idade",
        resultadoForm4=i)
if __name__ == '__main__':
    app.run(debug=True)
