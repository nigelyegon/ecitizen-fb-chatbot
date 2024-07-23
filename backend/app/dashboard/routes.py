from flask import render_template
from .dashboard import dashboard_bp
from ..models import Message


@dashboard_bp.route('/')
def index():
    messages = Message.query.all()
    return render_template('dashboard/index.html', messages=messages)
