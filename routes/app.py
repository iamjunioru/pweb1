from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/sobre", methods=["GET"])
def sobre():
    return 'Olá, esta é uma página falando sobre mim.' \
           '<br>' \
           'Bom, eu sou o Júnior. :)'

@app.route("/exp", methods=["GET"])
def experiencia():
    return 'Não tenho nenhuma experiência, apenas trabalho na roça.'

@app.route("/formacao", methods=["GET"])
def formacao():
    return 'Eu estudo no IFCE Campus Cedro.'

@app.route("/contato", methods=["GET"])
def contato():
    return '[[Fale comigo aqui]]' \
            '<br>' \
           '<a href="https://wa.me/+5588994953035">-whatsapp</a>'

if __name__ == '__main__':
    app.run(debug=True)