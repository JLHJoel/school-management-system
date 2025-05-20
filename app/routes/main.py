from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Creamos el blueprint llamado 'main'
main = Blueprint('main', __name__)

# Ruta para la página principal
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/teacher_dashboard')
@login_required
def panel_maestro():
    return render_template('teacher_dashboard.html', maestro=current_user)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

