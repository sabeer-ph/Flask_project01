# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:25:49 2022

@author: husssabe
"""
from attr import validate
from flask import render_template, redirect,url_for, flash, get_flashed_messages
from App import app, db
import forms
from models import *
from datetime import datetime as dt

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)


@app.route('/add',methods=['GET','POST'])
def add():
    form = forms.AddTaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('Hello World')
        print(form.title)
        t = Task(title=form.title.data,date=dt.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the Db')
        return redirect(url_for('index'))
    return render_template('add.html',form=form)