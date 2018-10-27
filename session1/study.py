from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template("homepage.html")

@app.route("/about-me")
def aboutme():
  return render_template("about-me.html")

@app.route("/school")
def school():
  return redirect("http://techkids.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)