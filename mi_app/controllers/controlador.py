from flask import Flask, render_template, request, redirect, session
from mi_app import app
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def contador():
    if 'numero' in session:
        session['numero'] += 1
    else:
        session['numero'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/contador2')
def contador2():
    session['numero'] += 1
    return redirect('/')

