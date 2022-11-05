import json

from flask import Flask, render_template, session, redirect, url_for, g
from departures.routes import blueprint_departures
from tickets.routes import blueprint_tickets
from auth.routes import blueprint_auth
from query.routes import blueprint_query
from report.routes import blueprint_report

app = Flask(__name__,
            static_url_path='/static')
app.secret_key = 'SuperKey'

app.config['db_config'] = json.load(open('configs/db.json'))
app.config['access_config'] = json.load(open('configs/access.json'))
app.register_blueprint(blueprint_departures, url_prefix='/departures')
app.register_blueprint(blueprint_tickets, url_prefix='/tickets')
app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_report, url_prefix='/query')

@app.route('/')
def departures():

    return redirect(url_for('blueprint_departures.get_departures'))


@app.route('/unauth')
def exit_session():
    session.clear()
    return redirect(url_for('blueprint_departures.get_departures'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
