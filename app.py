from flask import Flask
from cfg import app, db
import controller.main_controller



with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
