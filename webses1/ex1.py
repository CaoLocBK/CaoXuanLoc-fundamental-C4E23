from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about-me")
def home(aboutme):
    return "Cao Xuan Loc, 1993, ky su dien, thich am nhac, xem phim, doc sach"

@app.route("/school")
def school(school):
    return render_template("web.html",title =t, content=c)"