from flask import Flask
import test

fields = test.getFields()
print(fields)

app = Flask(__name__)

@app.route("/")
def hello_world():
    text = ""
    for i in fields:
        text += "<p>" + i + "</p>"
    return text