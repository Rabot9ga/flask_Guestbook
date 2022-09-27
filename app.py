from flask import Flask, request, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    from models import Guestbook
    all=Guestbook.query.all()
    return all[0].message()

@app.route('/create/', methods=['GET', 'POST'])
def create():
    from models import Guestbook
    from forms import GuestForm
    if request.method == 'POST':
        form=GuestForm(request.form)
        if form.validate():
            book=Guestbook(**form.data)
            db.session.add(book)
            db.session.commit()
            flash('Tuple was added!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))
    return '213'


if __name__ == '__main__':
    from models import *
    db.create_all()
    app.run()
