from app.database import db

class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    # Relaciones
    id_docente = db.Column(db.Integer, db.ForeignKey('docente.id'), nullable=True)
    registros = db.relationship('Registro', backref='materia', lazy=True)


class Registro(db.Model):
    __tablename__ = 'registro'
    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Numeric(5, 2), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    asistencias = db.Column(db.Integer, nullable=False)

    # Relaciones
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materia.id'), nullable=False)

