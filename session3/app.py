from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return "Whatever"

@app.route("/new_bike", methods=['GET','POST'])
def new_bike():
  if request.method == "GET":
    return render_template("new_bike.html")
  elif request.method == "POST":
    form = request.form
    model = form["model"]
    fee = form["fee"]
    image = form["image"]
    year = form["year"]
    # print(model,fee)
    return "Submit Successfully"



if __name__ == '__main__':
  app.run(debug=True)