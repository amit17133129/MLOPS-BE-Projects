# from keras.models import load_model
from flask import Flask, render_template, request
import joblib
app = Flask("Wine-Prediction-App")
model = joblib.load("wine_model.h5")
@app.route("/wine")
def home():
   return render_template("myform.html")

@app.route("/output", methods=[ "POST" ] )
def dia():
      x1 = request.form.get("z0")
      x2 = request.form.get("z1")
      x3 = request.form.get("z2")
      x4 = request.form.get("z3")
      x5 = request.form.get("z4")
      x6 = request.form.get("z5")
      x7 = request.form.get("z6")
      x8 = request.form.get("z7")
      x9 = request.form.get("z8")
      x10 = request.form.get("z9")
      x11 = request.form.get("z10")

      output = model.predict([[ float(x1), float(x2),  float(x3), float(x4),  float(x5), float(x6),  float(x7), float(x8),  float(x9), float(x10), float(x11)]])
      #output = model.predict([[ int(x1), int(x2),  int(x3), int(x4),  int(x5), int(x6),  int(x7), int(x8),  int(x9), int(x10), int(x11)]])
      if str(round(output[0])) == "0":
         data="Low"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "1":
         data="High"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "2":
         data="Low"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "3":
         data="Low"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "4":
         data="Average"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "5":
         data="Average"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "6":
         data="Average"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "7":
         data="Average"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "8":
         data="High"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "9":
         data="High"
         return render_template("results.html", data=data)

      if str(round(output[0])) == "10":
         data="High"
         return render_template("result.html", data=data)
app.run(host="0.0.0.0", port=6666)