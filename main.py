from flask import flask

app = Flash(__name__)

app.run(debug=True)