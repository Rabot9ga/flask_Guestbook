from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from models import GuestBookItem
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guest_book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['WTF_CSRF_ENABLED']=False
db = SQLAlchemy(app)


@app.route('/')
def index():
    all_items=GuestBookItem.query.all()
    return '123'


if __name__ == '__main__':
    # db.create_all()
    #
    # # Deleting all records:
    # GuestBookItem.query.delete()
    # # # Creating new ones:
    # ivan = GuestBookItem(message_text='Ivan')
    # sveta = GuestBookItem(message_text='Sveta')
    # semen = GuestBookItem(message_text='Semen')
    # kolya = GuestBookItem(message_text='Kolya')
    #
    # db.session.add(ivan)
    # db.session.add(sveta)
    # db.session.add(kolya)
    # db.session.add(semen)
    #
    # db.session.commit()


    app.run(debug=True)
