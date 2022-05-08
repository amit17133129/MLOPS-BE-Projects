from keras.models import load_model
from flask import Flask, render_template, request
import joblib
app = Flask("LoadPrediction")
model = joblib.load("model_joblib_classifier.h5")
@app.route("/loanprediction")
def home():
   return render_template("myform.html")

@app.route("/output", methods=[ "GET" ] )
def dia():
      x1 = request.args.get("z1")
      x2 = request.args.get("z2")
      x3 = request.args.get("z3")
      x4 = request.args.get("z4")
      x5 = request.args.get("z5")
      x6 = request.args.get("z6")
      x7 = request.args.get("z7")
      x8 = request.args.get("z8")
      x9 = request.args.get("z9")
      x10 = request.args.get("z10")
      x11 = request.args.get("z11")

      output = model.predict([[ int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), float(x7), float(x8), float(x9), float(x10), int(x11)]])
      if str(round(output[0])) == 1:
         data="Person is eligible for load Detected !!"
         return render_template("result.html", data=data)
      else:
          data="Person is not eligible for load !"
          return render_template("result.html", data=data)
app.run(host="0.0.0.0", port=5555)