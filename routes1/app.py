from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/exp")
def experiencia():
    return render_template('exp.html')

@app.route("/formacao")
def formacao():
    return render_template('formacao.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)