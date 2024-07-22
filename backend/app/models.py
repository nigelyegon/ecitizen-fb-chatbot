from . import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.String(128), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    response_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Message {self.id}>'
