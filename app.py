from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#index
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return redirect("https://resume.io/r/jav1DVI6t")


@app.route('/github')
def github():
    return redirect("https://github.com/FatemeZamanian")


@app.route('/insta')
def insta():
    return redirect("https://instagram.com/python.with.fateme?igshid=YmMyMTA2M2Y=")

@app.route('/linkedin')
def linkedin():
    return redirect("https://www.linkedin.com/in/fatemezamanian")

@app.route('/youtube')
def youtube():
    return redirect("https://youtube.com/channel/UCfI5V_TExc9ntvGSdUNjJ4Q")

