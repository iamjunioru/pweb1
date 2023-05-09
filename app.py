from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'admin':
            return render_template('paginas/index.html')
        else:
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('paginas/index.html')

if __name__ == '__main__':
    app.run(debug=True)
