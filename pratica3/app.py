from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'admin':
            return render_template('paginas/inicio.html')
        else:
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('paginas/inicio.html')
@app.route('/lanches')
def lanches():
    return render_template('paginas/lanches.html')
@app.route('/lugares')
def lugares():
    return render_template('paginas/lugares.html')
@app.route('/sobre')
def sobre():
    return render_template('paginas/sobre.html')

if __name__ == '__main__':
    app.run(debug=True)
