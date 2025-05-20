from app.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Estudiante(db.Model, UserMixin):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    asistencia_total = db.Column(db.Integer, default=0)
    promedio = db.Column(db.Numeric(5, 2), default=0.00)

    id_maestro = db.Column(db.Integer, db.ForeignKey('maestros.id'), nullable=False)
    maestro = db.relationship('Maestro', back_populates='estudiantes')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)