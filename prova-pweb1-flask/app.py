# cad pets
from flask import Flask, render_template, request, redirect

# run flask
app = Flask(__name__)

# array
pets = [
    {"id": 1, "tutor": "Junior", "pet": "Miguel", "species": "cat", "birthdate": "15/06/2023"},
]

# for start on 2 (id)
next_id = 2

# home
@app.route('/')
def index():
    return render_template('index.html')

# list all pets
@app.route('/list-pets')
def listPet():
    return render_template('list_pets.html', pets=pets)

# add pets
@app.route('/add-pets', methods=['GET', 'POST'])
def addPet():
    global next_id  # adicionar a declaração para usar a variável globalmente

    if request.method == 'POST':
        tutor = request.form['tutor']
        pet = request.form['pet']
        species = request.form['species']
        birthdate = request.form['birthdate'] 
        
        if not tutor or not pet or not species or not birthdate: 
            error_message = "all fieldsf are required."
            return render_template('add_pets.html', error_message=error_message)

        pets.append({"id": next_id, "tutor": tutor, "pet": pet, "species": species, "birthdate": birthdate})
        next_id += 1
        return redirect('/list-pets')

    return render_template('add_pets.html')


# edit pets
@app.route('/edit-pets/<int:id>', methods=['GET', 'POST'])
def editPet(id):
    for pet in pets:
        if pet['id'] == id:
            if request.method == 'POST':
                pet['tutor'] = request.form['tutor']
                pet['pet'] = request.form['pet']
                return redirect('/list-pets')
            else:
                return render_template('edit_pets.html', pet=pet, id=id)
    return "Pet not found."

# delete pets
@app.route('/delete-pets/<int:id>', methods=['POST'])
def deletePet(id):
    global pets
    pets = [pet for pet in pets if pet['id'] != id]
    return redirect('/list-pets')

# search pets
@app.route('/search-pets', methods=['GET', 'POST'])
def searchPets():
    if request.method == 'POST':
        search_query = request.form['search']
        search_results = []
        for pet in pets:
            if search_query.lower() in pet['tutor'].lower() or search_query.lower() in pet['pet'].lower():
                search_results.append(pet)
    return render_template('search_pets.html')
# start
if __name__ == '__main__':
    app.run(debug=True)
