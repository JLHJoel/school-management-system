from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from app.models.teacher import Maestro
from app.models.student import Estudiante
from app.database import db


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    user_type = request.form.get('user_type')
    password = request.form.get('password')

    if user_type == 'maestro':
        correo = request.form.get('correo')
        user = Maestro.query.filter_by(email=correo).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Bienvenido maestro', 'success')
            return redirect(url_for('teacher.panel_maestro'))
        else:
            flash('Credenciales incorrectas', 'danger')

    elif user_type == 'estudiante':
        matricula = request.form.get('matricula')
        user = Estudiante.query.filter_by(matricula=matricula).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Bienvenido estudiante', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales incorrectas', 'danger')

    return redirect(url_for('main.index'))

@auth.route('/registro-maestro', methods=['GET', 'POST'])
def register_maestro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validación simple
        if Maestro.query.filter_by(email=email).first():
            flash('Este correo ya está registrado.', 'warning')
            return redirect(url_for('auth.register_maestro'))

        nuevo_maestro = Maestro(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(nuevo_maestro)
        db.session.commit()

        flash('Registro exitoso. Ya puedes iniciar sesión.', 'success')
        return redirect(url_for('main.index'))

    return render_template('register.html')

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('main.index'))

