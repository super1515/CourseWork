import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)


blueprint_departures = Blueprint('blueprint_departures', __name__, template_folder='templates')


@blueprint_departures.route('/')
def departures():
	return render_template('departures.html')

