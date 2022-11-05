import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)

from auth.access import group_required
from database.operations import select
from database.sql_provider import SQLProvider

blueprint_report = Blueprint('blueprint_report', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))



@blueprint_report.route('/create')
@group_required
def report_create():
	return render_template('report_create.html')



@blueprint_report.route('/view')
@group_required
def report_view():
	return render_template('report_view.html')