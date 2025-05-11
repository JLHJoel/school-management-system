from flask import Flask, render_template
from app.routes import auth_routes, teacher_routes, student_routes
import os

def create_app():
    # 🔧 Se indica la carpeta de templates dentro de /app
    app = Flask(__name__, template_folder=os.path.join('app', 'templates'), static_folder=os.path.join('app', 'static'))

    # Registrar Blueprints
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(teacher_routes.bp)
    app.register_blueprint(student_routes.bp)

    @app.route('/')
    def index():
        return render_template('index.html') 

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
