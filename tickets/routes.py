import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)


blueprint_tickets = Blueprint('blueprint_tickets', __name__, template_folder='templates')


@blueprint_tickets.route('/')
def tickets():
    return render_template('tickets.html')
