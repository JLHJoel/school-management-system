from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.student import Estudiante
from app.database import db
from werkzeug.security import generate_password_hash

teacher_bp = Blueprint('teacher', __name__, url_prefix='/maestro')

@teacher_bp.route('/panel')
@login_required
def panel_maestro():
    estudiantes = Estudiante.query.all()
    return render_template('teacher_dashboard.html', maestro=current_user, estudiantes=estudiantes)

@teacher_bp.route('/add-estudiante', methods=['POST'])
@login_required
def add_student():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    matricula = request.form.get('matricula')
    password = request.form.get('password')

    if Estudiante.query.filter_by(matricula=matricula).first():
        flash('Ya existe un estudiante con esa matrícula.', 'danger')
        return redirect(url_for('teacher.panel_maestro'))

    hashed_password = generate_password_hash(password)
    nuevo_estudiante = Estudiante(nombre=nombre, apellido=apellido, matricula=matricula, password=hashed_password)
    db.session.add(nuevo_estudiante)
    db.session.commit()
    flash('Estudiante agregado exitosamente.', 'success')
    return redirect(url_for('teacher.panel_maestro'))

@teacher_bp.route('/edit-estudiante/<int:estudiante_id>', methods=['POST'])
@login_required
def edit_student(estudiante_id):
    estudiante = Estudiante.query.get_or_404(estudiante_id)
    estudiante.nombre = request.form.get('nombre')
    estudiante.apellido = request.form.get('apellido')
    estudiante.matricula = request.form.get('matricula')
    if request.form.get('password'):
        estudiante.password = generate_password_hash(request.form.get('password'))

    db.session.commit()
    flash('Datos del estudiante actualizados.', 'success')
    return redirect(url_for('teacher.panel_maestro'))

