from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# array
topiks = [{"id": 1, "horario": "09:00", "motorista": "Junior", "destino": "Cedro"}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar-topiks')
def listar_topiks():
    return render_template('listar_topiks.html', topiks=topiks)

@app.route('/adicionar-topik', methods=['GET', 'POST'])
def adicionar_topik():
    if request.method == 'POST':
        horario = request.form['horario']
        motorista = request.form['motorista']
        destino = request.form['destino']
        topik_id = len(topiks) + 1
        topik = {"id": topik_id, "horario": horario, "motorista": motorista, "destino": destino}
        topiks.append(topik)
        return redirect('/listar-topiks')
    return render_template('adicionar_topik.html')

@app.route('/editar-topik/<int:id>', methods=['GET', 'POST'])
def editar_topik(id):
    topik = next((topik for topik in topiks if topik['id'] == id), None)
    if request.method == 'POST':
        topik['horario'] = request.form['horario']
        topik['motorista'] = request.form['motorista']
        topik['destino'] = request.form['destino']
        return redirect('/listar-topiks')
    return render_template('editar_topik.html', topik=topik)

@app.route('/excluir-topik/<int:id>', methods=['POST'])
def excluir_topik(id):
    topiks[:] = [topik for topik in topiks if topik['id'] != id]
    return redirect('/listar-topiks')

if __name__ == '__main__':
    app.run(debug=True)
