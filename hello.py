#!/usr/bin/evn python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, session, url_for, redirect
from flask_moment import Moment
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = "Hard to guess string"


class NameForm(Form):
    name = StringField("what is your name?", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
