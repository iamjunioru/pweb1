from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Tutor, Pet, TutorSchema, PetSchema

class TutorResource(Resource):
    def get(self, tutor_id=None):
        if tutor_id is None:
            tutors = Tutor.query.all()
            return TutorSchema(many=True).dump(tutors), 200

        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {'message': 'Tutor not found'}, 404

        tutor_data = {
            'id': tutor.id,
            'nome': tutor.nome,
            'pets': [{'id': pet.id, 'nome': pet.nome} for pet in tutor.pets]
        }

        return tutor_data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        tutor = Tutor(nome=args['nome_tutor'])
        db.session.add(tutor)
        db.session.commit()
        tutor_schema = TutorSchema()
        tutor_data = tutor_schema.dump(tutor)
        return tutor_data, 201

    def put(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {'message': 'Tutor not found'}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        
        tutor.nome = args['nome_tutor']
        db.session.commit()

        return {'message': 'Tutor updated successfully'}, 200

    def delete(self, tutor_id):
        tutor = Tutor.query.get(tutor_id)
        if not tutor:
            return {'message': 'Tutor not found'}, 404

        if tutor.pets:
            return {'message': 'Cannot delete tutor with associated pets'}, 400
        
        db.session.delete(tutor)
        db.session.commit()
        return {'message': 'Tutor deleted successfully'}, 204


class PetResource(Resource):
    def get(self, pet_id=None, tutor_id=None):
        if pet_id is not None:
            pet = Pet.query.get(pet_id)
            if not pet:
                return {'message': 'Pet not found'}, 404
            pet_schema = PetSchema()
            pet_data = pet_schema.dump(pet)
            return pet_data, 200

        if tutor_id is not None:
            pets = Pet.query.filter_by(tutor_id=tutor_id).all()
            pet_schema = PetSchema(many=True)
            pets_data = pet_schema.dump(pets)
            return pets_data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        parser.add_argument('tutor_id', type=int, required=True)
        args = parser.parse_args()

        tutor = Tutor.query.get(args['tutor_id'])
        if not tutor:
            return {'message': 'Tutor not found'}, 404
        
        pet = Pet(nome=args['nome_pet'], tutor=tutor)
        db.session.add(pet)
        db.session.commit()
        pet_schema = PetSchema()
        pet_data = pet_schema.dump(pet)
        return pet_data, 201

    def put(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return {'message': 'Pet not found'}, 404
        
        parser = reqparse.RequestParser()
        parser.add_argument('nome_pet', type=str, required=True)
        args = parser.parse_args()
        
        pet.nome = args['nome_pet']
        db.session.commit()
        pet_schema = PetSchema()
        pet_data = pet_schema.dump(pet)
        return pet_data, 200

    def delete(self, pet_id):
        pet = Pet.query.get(pet_id)
        if not pet:
            return {'message': 'Pet not found'}, 404
        
        db.session.delete(pet)
        db.session.commit()
        return {'message': 'Pet deleted'}, 204
