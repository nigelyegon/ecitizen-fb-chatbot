"""
The dashboard will display metrics such as:

    Number of responses per day.
    Number of messages received per day.
    Response time.
    Most frequently asked questions.
    User engagement over time.
    
"""
from flask import Blueprint, jsonify
from ..models import Message, db
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/metrics/messages_per_day', methods=['GET'])
def messages_per_day():
    data = db.session.query(
        func.date(Message.timestamp).label('date'),
        func.count(Message.id).label('count')
    ).group_by(func.date(Message.timestamp)).all()
    result = [{'date': str(row.date), 'count': row.count} for row in data]
    return jsonify(result)


@dashboard_bp.route('/metrics/responses_per_day', methods=['GET'])
def responses_per_day():
    data = db.session.query(
        func.date(Message.timestamp).label('date'),
        func.count(Message.response_text).label('count')
    ).filter(Message.response_text != '').group_by(func.date(Message.timestamp)).all()
    result = [{'date': str(row.date), 'count': row.count} for row in data]
    return jsonify(result)


@dashboard_bp.route('/metrics/most_frequent_questions', methods=['GET'])
def most_frequent_questions():
    data = db.session.query(
        Message.message_text,
        func.count(Message.message_text).label('count')
    ).group_by(Message.message_text).order_by(func.count(Message.message_text).desc()).limit(10).all()
    result = [{'question': row.message_text, 'count': row.count} for row in data]
    return jsonify(result)
