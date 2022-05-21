from keras.models import load_model
from flask import Flask, render_template, request
import joblib
app = Flask("Social-Network-Ads")
model = joblib.load("svm_social_networ.h5")
@app.route("/item")
def home():
   return render_template("myform.html")

@app.route("/output", methods=[ "GET" ] )
def dia():
      x1 = request.args.get("z1")
      x2 = request.args.get("z2")

      output = model.predict([[ int(x1), int(x2)]])
      if str(round(output[0])) == 1:
         data="Eligible to Purchase Item !!"
         return render_template("result.html", data=data)
      else:
          data="Not Eligible to Purchase !"
          return render_template("result.html", data=data)
app.run(host="0.0.0.0", port=6666)