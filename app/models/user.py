from app.database import db

class Administrador(db.Model):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)


class Docente(db.Model):
    __tablename__ = 'docente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)

    # Relaciones
    materias = db.relationship('Materia', backref='docente', lazy=True)
    estudiantes = db.relationship('Estudiante', backref='docente', lazy=True)
""
