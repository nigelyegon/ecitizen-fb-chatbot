from extensions import db, bcrypt


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.String(128), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    response_text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Message {self.id}>"


class User(db.Model):
    """User model"""

    # customize the table name
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Save user
    def save(self):
        """Save user to database"""
        db.session.add(self)
        db.session.commit()

    # Rollback transaction
    @staticmethod
    def undo():
        """Rollback the transaction"""
        db.session.rollback()

    @classmethod
    def find_user_by_email(cls, email):
        """FInd user in the table by email"""
        return cls.query.filter_by(email=email).first()

    @staticmethod
    def generate_hash(password):
        """Generate hashed password"""
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def verify_hash(_hash, password):
        """Verify hashed password"""
        return bcrypt.check_password_hash(_hash, password)


class RevokedToken(db.Model):
    """Revoked token model"""

    __tablename__ = "revoked_tokens"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(128), nullable=False)

    # Save token
    def save(self):
        """Save token to database"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_token_blacklisted(cls, jti):
        """Check if the available token is blacklisted"""
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
