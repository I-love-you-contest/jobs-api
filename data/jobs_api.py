"""Полный код для теста на https://github.com/I-love-you-contest/jobs-api"""
from flask import jsonify, Blueprint

from . import db_session
from .jobs import Job

blueprint = Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_all():
    sess = db_session.create_session()
    jobs = sess.query(Job).all()
    return jsonify({x.id: x.name for x in jobs})
