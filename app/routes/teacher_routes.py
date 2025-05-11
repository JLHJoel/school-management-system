from flask import Blueprint, render_template

bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/dashboard')
def dashboard():
    return render_template('teacher_dashboard.html')
