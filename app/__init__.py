from flask import Flask
from flask_login import LoginManager
from app.database import db

# Importa los modelos para que se registren al hacer db.create_all()
from .models.teacher import Maestro
from .models.student import Estudiante
from .models.subject import Materia
from .models.grade import Calificacion
from .models.attendance import Asistencia
from .models.teacher import Maestro
from .models.student import Estudiante
from flask_login import login_user, logout_user, login_required, current_user

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    # Como tienes dos tipos de usuario, debes decidir cómo cargarlos.
    # Aquí un ejemplo simple (mejorar luego):
    user = Maestro.query.get(int(user_id))
    if user:
        return user
    user = Estudiante.query.get(int(user_id))
    return user




def create_app():
    app = Flask(__name__)
    
    # Configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/gestion_escolar'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'clave_secreta_segura'  # Necesario para sesiones/login

    # Inicializar extensión SQLAlchemy
    db.init_app(app)

    # Crear tablas (solo si no existen)
    with app.app_context():
        db.create_all()

    login_manager.init_app(app)
    login_manager.login_view = 'main.index'  # o 'auth.login' si tienes ruta GET de login

    # Registrar blueprints
    from .routes.main import main
    app.register_blueprint(main)
    from .routes.auth import auth
    app.register_blueprint(auth)
    from .routes.teacher_routes import teacher_bp
    app.register_blueprint(teacher_bp)



    return app



