from flask import Flask, render_template, abort, redirect, request
import datetime

app = Flask(__name__)
BUFFER = list()
#3
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.route('/500')
def error500():
    abort(500)

#1
@app.route('/')
@app.route('/index')
def main():
    return '<h1>Ahoj ja som Dzin z flase</h1>'


@app.route('/mojastranka')
def moja():
    return '<h2>TEST MOJEJ STRANKY</h2><p>Toto je moja skusobna stranka lebo mne sa paci WEB</p>'


@app.route('/cas')
def cas():
    return render_template('main.html', cas=datetime.datetime.now())

@app.route('/welcome')
def welcome():
    return render_template('vitajte.html')

@app.route('/vitajte')
def vitajte():
    return redirect('/vitajte.html')

@app.route('/spravy/<int:index>', methods=['GET'])
def spravy(index):
    spravy = ['sprava1 - zlacnelo mydlo', 'Sprava2 - zajtra bude prsat', 'Sprava3 - Hovovo']
    try:
        return render_template('spravy.html', msg=spravy[index])
    except IndexError:
        abort(404)

@app.route('/kurzkk', methods=['GET'])
def kurz():
    kurz = [12, 34,23,78,45, -3,-76, 15, -34, 10, -67, 89]
    return render_template('kurzkk.html', kurzy=kurz)

@app.route('/form', methods=['GET', 'POST'])
def form():
    print(request)
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        # print(user, pwd)
        BUFFER.append((user, pwd))
        app.logger.info('SUCCESS - vysledok bol ulozeny v BUFFERI ')

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)