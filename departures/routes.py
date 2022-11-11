import os

from flask import (
	Blueprint, render_template,
	request, current_app,
	session, redirect, url_for
)

from database.operations import select
from database.sql_provider import SQLProvider

blueprint_departures = Blueprint('blueprint_departures', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_departures.route('/')
def get_departures():
	sql = provider.get('departures.sql')
	items = select(current_app.config['db_config'], sql)
	return render_template('departures.html', items=items)


@blueprint_departures.route('/buy', methods=['GET', 'POST'])
def ticket_buy():
	flightNumber = request.args.get('flightNumber')
	baseCost = request.args.get('baseCost')
	return render_template('ticketbuy.html', flightNumber=flightNumber, baseCost=baseCost)


@blueprint_departures.route('/check', methods=['GET', 'POST'])
def ticket_check():
	return render_template('ticket_check.html')