from flask import *
import mlab
from river import River

app = Flask(__name__)
mlab.connect()

@app.route("/rivers")
def rivers():
  rivers_list = River.objects(continent="S. America", length__lte =1000)
  return render_template("rivers.html", rivers=rivers_list)


if __name__ == '__main__':
  app.run(debug=True)