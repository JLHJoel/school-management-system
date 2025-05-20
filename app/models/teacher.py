from app.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Maestro(db.Model, UserMixin):
    __tablename__ = 'maestros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())

    estudiantes = db.relationship('Estudiante', back_populates='maestro', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)