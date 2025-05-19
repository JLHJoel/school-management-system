from flask import Flask, render_template
from app.routes.auth_routes import auth_routes
from app.routes.teacher_routes import teacher_routes
from app.routes.student_routes import student_routes
import os

def create_app():
    app = Flask(__name__, template_folder=os.path.join('app', 'templates'), static_folder=os.path.join('app', 'static'))

    # Registrar Blueprints
    app.register_blueprint(auth_routes)
    app.register_blueprint(teacher_routes)
    app.register_blueprint(student_routes)

    @app.route('/')
    def index():
        return render_template('index.html') 

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
