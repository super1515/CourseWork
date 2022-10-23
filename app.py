import json

from flask import Flask, render_template, session
from departures.routes import blueprint_departures
from tickets.routes import blueprint_tickets
app = Flask(__name__,
            static_url_path='/static')
app.secret_key = 'SuperKey'

app.config['db_config'] = json.load(open('configs/db.json'))
app.register_blueprint(blueprint_departures, url_prefix='/departures')
app.register_blueprint(blueprint_tickets, url_prefix='/tickets')


@app.route('/')
def departures():
    return render_template('departures.html')


@app.route('/exit')
def exit_session():
    session.clear()
    return render_template('departures.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
