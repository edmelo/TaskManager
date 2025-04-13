from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Correção para SameSite
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Adicionando cabeçalhos de segurança
@app.after_request
def set_headers(response):
    # Anti-clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Proteção contra MIME sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Política de Segurança de Conteúdo (CSP)
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self';"
    # Permissions Policy
    response.headers['Permissions-Policy'] = "geolocation=(), microphone=()"
    # Medidas contra Spectre
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    # Remover ou mascarar cabeçalho Server
    response.headers['Server'] = 'Custom-Server'
    return response

@app.after_request
def remove_server_header(response):
    response.headers['Server'] = 'Custom-Server'
    return response

# Always put Routes at end
from todo_project import routes