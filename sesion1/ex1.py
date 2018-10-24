from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def BMI():
  return render_template("show_bmi.html")

@app.route("/bmi/<int:x>/<int:y>")
def show_bmi(x,y):
  z = x*10000/(y*y)
  if z < 16:
    return render_template("Severely_underweight.html",z=str(z))
  elif 16 <= z < 18.5:
    return render_template("Underweight.html",z=str(z) )
  elif 18.5 <= z < 25:
    return render_template("Normal.html",z=str(z))
  elif 25 <= z < 30:
    return render_template("Overweight.html",z=str(z))
  else:
    return render_template("Obese.html",z=str(z))

if __name__ == '__main__':
  app.run(debug=True)