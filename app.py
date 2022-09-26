from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import config
from datetime import date

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':

    return '123'


class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message_text = db.Column(db.String(300), nullable=False)
    date_message = db.Column(db.Date, default=date.today)
    is_deleted = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {'id': self.id, 'message_text': self.message_text}


if __name__ == '__main__':
    app.run()
