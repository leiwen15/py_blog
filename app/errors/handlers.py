from flask import render_template
from app import app
from app.errors import bp

@bp.app_handler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_handler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
