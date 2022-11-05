import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)

from auth.access import group_required

blueprint_tickets = Blueprint('blueprint_tickets', __name__, template_folder='templates')


@blueprint_tickets.route('/')
@group_required
def tickets():
	return render_template('tickets.html')



