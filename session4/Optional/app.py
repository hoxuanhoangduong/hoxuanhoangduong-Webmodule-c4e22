from flask import Flask, render_template,request
import mlab
from poll import Poll
from random import choice

app = Flask(__name__)
mlab.connect()

@app.route("/polls")
def polls():
  # 1. Read All polls
  poll_list = Poll.objects()

  # for p in poll_list:
  #   print(p.question)

  # 2. Render all polls
  return render_template("polls.html", polls=poll_list)

@app.route("/poll/<poll_code>")
def poll(poll_code):
  # 1. Get Poll

  # objects(yob__gt=1990) >1990
  #

  poll_list = Poll.objects(code=poll_code)
  poll = poll_list[0]
  # print(poll.question)
  # print(poll.options)

  # 2. Render
  return render_template("poll.html", p=poll)

@app.route("/new_bike", methods=['GET','POST'])
def new_bike():
  if request.method == "GET":
    return render_template("new_bike.html")
  elif request.method == "POST":
    form = request.form
    question = form["question"]
    options = []
    for k,v in form.items():
      if k != "question":
        options.append()
    print(question)
    print(options)
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    c = ""  
    for _ in range(6):
      c += choice(alphabet)
    p = Poll(question = question,options = options, code=c)
    p.save()
    return "Ok"

if __name__ == '__main__':
  app.run(debug=True)