import os
import json
from flask import Flask, render_template, redirect, abort, request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
# APP CONTEXT
app= Flask(__name__)


app.config['SECRET_KEY'] = os.urandom(32)
app.config['CSRF_ENABLED'] = True
login_manager = LoginManager()
login_manager.init_app(app)


users = {'andrej@gmail.com':{'password': 'halabala'}, 'filip@gmail.com': {'password': 'halabala2'}}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    user = User()
    user.id = email
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
        <form action='login' method='POST'>
        <input type='text' name='email' id='email' placeholder='email'>
        <input type='password' name='password' id='password' placeholder='password'>
        <input type='submit' name='submit'>
        </form>
        '''
    email = request.form['email']
    if email in users and request.form['password'] == users[email]['password']:
        user=User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))
    return 'BAD LOGIN'

@app.route('/protected')
@login_required
def protected():
    return 'logged in as' + current_user.id

@app.route('/logout')
def logout():
    logout_user()
    return 'LOGGED OUT'



# ROUTES
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/setsession')
def setsession():
    session['USERNAME'] = 'Anonymous'
    flash('USERNAME JE NASTAVENE')
    app.logger.debug('USERNAME JE NASTAVENE')
    return redirect('/index')

@app.route('/getsession')
def getsession():
    if 'USERNAME' in session:
        username = session['USERNAME']
        msg = f'SESSION FOR USER : {username} WAS ACCESED'
        flash(msg)
        app.logger.info(msg)
        return redirect('/index')
    else:
        return 'WELCOME GUEST'

@app.route('/delsession')
def delsession():
    session.pop('USERNAME', None)
    flash('SESSION BOLA VYMAZANA')
    app.logger.debug('SESSION BOLA VYMAZANA')
    return redirect('/index')


@app.route('/info', methods=['GET', 'POST'])
def info():
    form = MojFormular()
    app.logger.debug('FORMULAR BOL VYTVORENY')
    if request.method == 'POST':
        csrf.generate_csrf()
        app.logger.debug('SPRAVA PRISLA')
        #if request.form.get('info') != '':
        if form.validate():
            print(request.form.get('info'))
            session['info'] = request.form.get('info')
            # FIRST
            #with open(file='session_info.json', mode='a', encoding='utf8') as f:
            #    json.dump(fp=f, obj=session, indent=4)
            add_record(session['info'])
            app.logger.info('INFO ULOZENA DO SESSION')
            return redirect(f'/submit')
        else:
            app.logger.info('INFORMACIA NEBOLA ULOZENA')

    return render_template('info.html', form=form)

@app.route('/submit', methods=['GET'])
def submit():
    return render_template('submit.html')

@app.route('/view', methods=['GET'])
def infolist():
    try:
        entry = str(session['info'])
        app.logger('SPRAVA')
        flash('Info je v poriadku')
    except KeyError:
        entry=None
        flash('Nemam info')
    finally:
        return render_template('view.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)