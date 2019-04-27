from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/can")
def canvas():
    return render_template('can.html')

app.run(debug = True , port = 3000)