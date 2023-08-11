from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Tutor, Pet, TutorSchema, PetSchema


class GetAllResource(Resource):
    def get(self):
        tutors = Tutor.query.all()
        tutors_data = []

        for tutor in tutors:
            tutor_data = {
                "id": tutor.id,
                "nome": tutor.nome,
                "pets": [{"id": pet.id, "nome": pet.nome} for pet in tutor.pets],
            }
            tutors_data.append(tutor_data)

        return jsonify(tutors_data)


class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutors = Tutor.query.all()
            tutors_data = []

        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {"message": "Tutor not found"}, 404

        tutor_data = {
            "id": tutor.id,
            "nome": tutor.nome,
            "pets": [{"id": pet.id, "nome": pet.nome} for pet in tutor.pets],
        }

        return jsonify(tutor_data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nome_tutor", type=str, required=True)
        args = parser.parse_args()
        tutor = Tutor(nome=args["nome_tutor"])
        db.session.add(tutor)
        db.session.commit()
        tutor_schema = TutorSchema()
        tutor_data = tutor_schema.dump(tutor)
        return jsonify(tutor_data)

    def put(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
           return jsonify({"message": "Tutor not found"})

        parser = reqparse.RequestParser()
        parser.add_argument("nome_tutor", type=str, required=True)
        args = parser.parse_args()

        tutor.nome = args["nome_tutor"]
        db.session.commit()

        return jsonify({"message": "Tutor updated successfully", "tutor": tutor.nome})

    def delete(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return jsonify({"message": "Tutor not found"})

        if tutor.pets:
            return jsonify({"message": "Tutor has associated pets"})

        db.session.delete(tutor)
        db.session.commit()
        return jsonify({"message": "Tutor deleted successfully"})


class PetResource(Resource):
    def get(self, pet_id=None, tutor_id=None):
        if pet_id is not None:
            pet = Pet.query.get(pet_id)
            if not pet:
                return {"message": "Pet not found"}, 404
            pet_schema = PetSchema()
            pet_data = pet_schema.dump(pet)
            return jsonify(pet_data)

        if tutor_id is not None:
            pets = Pet.query.filter_by(tutor_id=tutor_id).all()
            pet_schema = PetSchema(many=True)
            pets_data = pet_schema.dump(pets)
            return jsonify(pets_data)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nome_pet", type=str, required=True)
        parser.add_argument("tutor_id", type=int, required=True)
        args = parser.parse_args()

        tutor = Tutor.query.get(args["tutor_id"])
        if not tutor:
            return jsonify({"message": "Tutor not found"})

        pet = Pet(nome=args["nome_pet"], tutor=tutor)
        db.session.add(pet)
        db.session.commit()
        pet_schema = PetSchema()
        pet_data = pet_schema.dump(pet)
        return jsonify(pet_data)

    def put(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return jsonify({"message": "Pet not found"})

        parser = reqparse.RequestParser()
        parser.add_argument("nome_pet", type=str, required=True)
        args = parser.parse_args()

        pet.nome = args["nome_pet"]
        db.session.commit()
        pet_schema = PetSchema()
        pet_data = pet_schema.dump(pet)
        return jsonify({"message": "Pet updated successfully", "pet": pet.nome})
    def delete(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return jsonify({"message": "Pet not found"})

        db.session.delete(pet)
        db.session.commit()
        return jsonify({"message": "Pet deleted successfully"})
