from flask import Flask, render_template
from dbman.dbman import dbman
from app import app

app.register_blueprint(dbman, url_prefix='/dbman')


@app.route('/')
def ind():
    return '<h1>TEST</h1>'


if __name__ == '__main__':
    app.run(debug=True)
