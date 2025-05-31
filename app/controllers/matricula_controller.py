from flask import request
from flask_restx import Resource, fields, Namespace
from app.models.Matricula import Matricula
from app import db, api

ns = Namespace('matriculas', description='Operações relacionadas a matrículas')

# Modelo para documentação do Swagger
matricula_model = ns.model('Matricula', {
    'matricula': fields.String(required=True, description='Número da matrícula'),
    'nome': fields.String(required=True, description='Nome do aluno'),
    'email': fields.String(required=True, description='Email do aluno'),
    'curso': fields.String(required=True, description='Curso do aluno'),
    'created_at': fields.DateTime(readonly=True)
})

@ns.route('/<string:matricula>')
@ns.param('matricula', 'Número da matrícula do aluno')
class AlunoResource(Resource):
    @ns.doc('get_aluno')
    @ns.marshal_with(matricula_model)
    def get(self, matricula):
        """Busca um aluno pelo número da matrícula"""
        try:
            aluno = Matricula.query.get_or_404(matricula)
            return aluno
        except Exception as e:
            return {'error': 'Erro ao buscar aluno', 'message': str(e)}, 500

@ns.route('/')
class AlunoListResource(Resource):
    @ns.doc('create_aluno')
    @ns.expect(matricula_model)
    @ns.marshal_with(matricula_model, code=201)
    def post(self):
        """Cria um novo aluno"""
        try:
            data = request.get_json()
            
            if not data or not data.get('nome') or not data.get('email') or not data.get('curso'):
                return {'error': 'Dados inválidos: nome, email e curso são obrigatórios'}, 400

            # Verifica se o email já existe
            if Matricula.query.filter_by(email=data['email']).first():
                return {'error': 'Email já cadastrado'}, 400

            aluno = Matricula(
                nome=data['nome'],
                email=data['email'],
                curso=data['curso']
            )
            
            db.session.add(aluno)
            db.session.commit()
            
            return aluno, 201
        except Exception as e:
            db.session.rollback()
            return {'error': 'Erro ao criar aluno', 'message': str(e)}, 500

# Registra o namespace na API
api.add_namespace(ns, path='/api/matriculas') 