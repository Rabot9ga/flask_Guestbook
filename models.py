from datetime import date
from app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message_text = db.Column(db.String(300), nullable=False)
    date_message = db.Column(db.Date, default=date.today)
    is_deleted = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {'id': self.id, 'message_text': self.message_text}



