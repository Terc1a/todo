from todo.routes import app, db





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, host='192.168.0.17', port='5555')