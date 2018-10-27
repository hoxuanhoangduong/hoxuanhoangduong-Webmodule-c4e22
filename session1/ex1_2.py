from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def BMI():
  return render_template("show_bmi.html")

@app.route("/bmi/<int:x>/<int:y>")
def show_bmi(x,y):
  z = x*10000/(y*y)
  if z < 16:
    return ("Here is your BMI : " + str(z) + " You're serverly underweight")
  elif 16 <= z < 18.5:
    return ("Here is your BMI : " + str(z) + " You're Underweight")
  elif 18.5 <= z < 25:
    return ("Here is your BMI : " + str(z) + " You're Normal")
  elif 25 <= z < 30:
    return ("Here is your BMI : " + str(z) + " You're Overweigth")
  else:
    return ("Here is your BMI : " + str(z) + " You're Obese")

if __name__ == '__main__':
  app.run(debug=True)