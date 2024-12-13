from flask_sqlalchemy import SQLAlchemy

# Variables para la configuración
DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_NAME = 'gestion_estudiantes'

# Configuración de la base de datos
DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy()

