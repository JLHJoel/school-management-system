from flask import Blueprint, render_template

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/dashboard')
def dashboard():
    return render_template('student_dashboard.html')
