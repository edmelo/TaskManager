from todo_project import app, db

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)