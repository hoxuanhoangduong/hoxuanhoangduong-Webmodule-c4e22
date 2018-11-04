from flask import *
import mlab
from river import River

app = Flask(__name__)
mlab.connect()

@app.route("/rivers")
def rivers():
  rivers_list = River.objects(continent="Africa")
  # for p in rivers_list:
  #   print(p.name)
  #   print(p.continent)
  #   print(p.length)
  #   print("****")
  return render_template("rivers.html", rivers=rivers_list)


if __name__ == '__main__':
  app.run(debug=True)