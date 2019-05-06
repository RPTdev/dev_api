from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Golang', 'Rust', 'Ruby']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

