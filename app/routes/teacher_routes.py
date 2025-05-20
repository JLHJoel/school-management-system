from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.student import Estudiante
from app.database import db
from werkzeug.security import generate_password_hash

teacher_bp = Blueprint('teacher', __name__, url_prefix='/maestro')

@teacher_bp.route('/panel')
@login_required
def panel_maestro():
    estudiantes = Estudiante.query.filter_by(id_maestro=current_user.id).all()
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

    nuevo_estudiante = Estudiante(
    nombre=nombre,
    apellido=apellido,
    matricula=matricula,
    password=hashed_password,
    id_maestro=current_user.id  # Asignar maestro actual
    )

    nuevo_estudiante.set_password(password)

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

    #valores de asistencia_total y promedio
    estudiante.asistencia_total = request.form.get('asistencia_total')
    estudiante.promedio = request.form.get('promedio')

    if estudiante.asistencia_total is not None:
        try:
            estudiante.asistencia_total = int(estudiante.asistencia_total)
        except ValueError:
            flash('Asistencia total debe ser un número entero.', 'danger')
            return redirect(url_for('teacher.panel_maestro'))

    if estudiante.promedio is not None:
        try:
            prom_float = float(estudiante.promedio)
            if 0 <= prom_float <= 100:
                estudiante.promedio = prom_float
            else:
                flash('Promedio debe estar entre 0 y 100.', 'danger')
                return redirect(url_for('teacher.panel_maestro'))
        except ValueError:
            flash('Promedio debe ser un número válido.', 'danger')
            return redirect(url_for('teacher.panel_maestro'))

    db.session.commit()
    flash('Datos del estudiante actualizados.', 'success')
    return redirect(url_for('teacher.panel_maestro'))

