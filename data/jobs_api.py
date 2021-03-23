"""Полный код для теста на https://github.com/I-love-you-contest/jobs-api"""
from flask import jsonify, Blueprint, request

from . import db_session
from .jobs import Job

blueprint = Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_all():
    sess = db_session.create_session()
    jobs = sess.query(Job).all()
    return jsonify({x.id: x.name for x in jobs})


@blueprint.route('/api/jobs/<int:job_id>')
def get_one(job_id):
    sess = db_session.create_session()
    job = sess.query(Job).get(job_id)
    if not job:
        return jsonify({'ERROR': 'Job not found'}), 404
    return jsonify({job.id: job.name})


@blueprint.route('/api/jobs', methods=['POST'])
def create():
    args = request.json
    if not args:
        return jsonify({"ERROR": "EMPTY REQUEST"}), 400
    elif 'name' not in args:
        return jsonify({"ERROR": "BAD REQUEST. NAME IS MISSING"}), 400
    elif set(args.keys()) > {'name', 'id'}:
        return jsonify({"ERROR": "BAD REQUEST. UNKNOWN ARGUMENTS"}), 400
    sess = db_session.create_session()
    job = Job(**args)
    sess.add(job)
    sess.commit()
    return jsonify({'success': {'id': job.id}})

