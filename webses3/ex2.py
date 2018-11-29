from flask import Flask, render_template, request
import ex2mlab
from ex2mlab import Newbike

ex2mlab.connect()
app = Flask(__name__)
@app.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        #User request form
        return render_template("ex1.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        m = form["model"]
        dlfee = form["dailyfee"]
        img = form["image"]
        y = form["year"]
        
        nbike = Newbike(model=m, dailyfee=dlfee, image=img, year=y)
        nbike.save()

        return "Gotcha!!!"

if __name__=="__main__":
    app.run(debug=True)