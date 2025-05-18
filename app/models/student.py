from app.database import db

class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)
    clave_registro = db.Column(db.String(50), nullable=False)
    grado = db.Column(db.String(50), nullable=False)

    # Relaciones
    id_docente = db.Column(db.Integer, db.ForeignKey('docente.id'), nullable=True)
    registros = db.relationship('Registro', backref='estudiante', lazy=True)

