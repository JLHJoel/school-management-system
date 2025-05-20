from app.database import db

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)

    id_maestro = db.Column(db.Integer, db.ForeignKey('maestros.id'), nullable=False)

    calificaciones = db.relationship('Calificacion', backref='materia', lazy=True)
    asistencias = db.relationship('Asistencia', backref='materia', lazy=True)
