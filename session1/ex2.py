from flask import Flask ,render_template
app = Flask(__name__)

Users = {
    "huy": {
        "name":"Nguyễn Quang Huy",
        "gender":"male",
        "age":29,
    },
    "quan": {
        "name":"Huynh Tuan Anh",
        "gender":"male",
        "age":22,
    },
    "anh":{
        "name":"Tuan Anh",
        "gender":"male",
        "age":21,
    },
    "duong":{
        "name":"Hồ Xuân HOàng DƯơng",
        "gender":"male",
        "age":24
    }
}

@app.route("/")
def homepage():
    return render_template("checkname.html")

@app.route("/user/<username>")
def profile(username):
    if username in Users.keys():
        return render_template("username.html", user = Users [username])
    else: 
        return "User not found" 

if __name__ == '__main__':
  app.run(debug=True)