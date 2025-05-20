from app.database import db

class Asistencia(db.Model):
    __tablename__ = 'asistencias'

    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, default=False)
