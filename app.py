import shutil
from pathlib import Path

from flask import Flask, request, abort

app = Flask(__name__)

DEST_DIRECTORY_BASE = '/var/www/files'


def check_user(user, password):
    if not user or not password:
        return False
    with open('users.txt') as users_file:
        for line in users_file:
            _user, _password = [x.rstrip() for x in line.split(':')]
            if _user == user and _password == password:
                return user
        return False


@app.route('/upload', methods=['POST'])
def index():
    app.logger.debug('-------> %s', request.form)
    user = check_user(request.form['user'], request.form['password'])
    if not user:
        abort(403)
    # move to final directory
    dest_directory = Path('%s/%s' % (DEST_DIRECTORY_BASE, user))
    if not dest_directory.exists():
        dest_directory.mkdir()
    dest_file = dest_directory / request.form['file.name']
    shutil.move(request.form['file.path'], str(dest_file))
    return 'OK', 201
