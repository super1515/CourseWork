import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)


blueprint_auth = Blueprint('blueprint_auth', __name__, template_folder='templates')


@blueprint_auth.route('/')
def auth():
	return render_template('auth.html')
