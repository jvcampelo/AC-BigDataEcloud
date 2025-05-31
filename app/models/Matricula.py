import random
import string
from datetime import datetime
from app import db

def generate_unique_matricula():
    # Gera um identificador alfanumérico aleatório de 9 dígitos
    # Nota: Em um ambiente de produção, você precisaria garantir a unicidade
    # consultando o banco de dados antes de atribuir a matricula.
    digits = string.digits
    matricula = ''.join(random.choice(digits) for i in range(9))
    return matricula

class Matricula(db.Model):
    matricula = db.Column(db.String(9), primary_key=True, default=generate_unique_matricula)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    curso = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'matricula': self.matricula,
            'nome': self.nome,
            'email': self.email,
            'curso': self.curso,
            'created_at': self.created_at.isoformat()
        }

    def __repr__(self):
        return f'<Matricula {self.matricula}>' 