import os

from flask import (
    Blueprint, render_template,
    request, current_app,
    session, redirect, url_for
)

from auth.access import group_required, login_required
from database.operations import select
from database.sql_provider import SQLProvider

blueprint_query = Blueprint('blueprint_query', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/')
@group_required
def query():
    return render_template('queries.html')


@blueprint_query.route('/query_1', methods=['GET', 'POST'])
@group_required
def query_1():
    if request.method == 'GET':
        return render_template('query_1.html')
    else:
        number = request.form.get('number')
        sql = provider.get('query_1.sql', number=number)
        items = select(current_app.config['db_config'], sql)
        if not items:
            print(items)
            items = 'None'
        return render_template('query_1.html', items=items)


@blueprint_query.route('/query_2', methods=['GET', 'POST'])
@group_required
def query_2():
    if request.method == 'GET':
        return render_template('query_2.html')
    else:
        date_in = request.form.get('date_start')
        date_out = request.form.get('date_end')
        sql = provider.get('query_2.sql', date_in=date_in, date_out=date_out)
        items = select(current_app.config['db_config'], sql)
        if not items:
            print(items)
            items = 'None'
        return render_template('query_2.html', items=items)


@blueprint_query.route('/query_3.sql', methods=['GET', 'POST'])
@group_required
def query_3():
    if request.method == 'GET':
        return render_template('query_3.html')
    else:
        num = request.form.get('num')
        sql = provider.get('query_3.sql', num=num)
        items = select(current_app.config['db_config'], sql)
        if not items:
            print(items)
            items = 'None'
        return render_template('query_3.html', items=items)


@blueprint_query.route('/query_4.sql', methods=['GET', 'POST'])
@group_required
def query_4():
    if request.method == 'GET':
        return render_template('query_4.html')
    else:
        date_in = request.form.get('date_start')
        date_out = request.form.get('date_end')
        sql = provider.get('query_4.sql', date_in=date_in, date_out=date_out)
        items = select(current_app.config['db_config'], sql)
        if not items:
            print(items)
            items = 'None'
        return render_template('query_4.html', items=items)