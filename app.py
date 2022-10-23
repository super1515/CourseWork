import json


from flask import Flask, render_template, session


app = Flask(__name__)
app.secret_key = 'SuperKey'


app.config['db_config'] = json.load(open('configs/db.json'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exit')
def exit_session():
    session.clear()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
