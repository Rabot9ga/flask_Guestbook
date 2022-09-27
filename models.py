from datetime import date
from app import db


class Guestbook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50))
    message_text = db.Column(db.String(300), nullable=False)
    date_message = db.Column(db.Date, default=date.today)
    is_deleted = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {'id': self.id, 'author': self.author, 'message_text': self.message_text, 'date_message': self.date_message, 'is_deleted': self.is_deleted}


    def message(self):
        return self.message_text
