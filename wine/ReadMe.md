## Steps to be followed
Install virtualenv in your command line / terminal

```
pip3 install virtualenv
```

Then install below respective libraries 

```
pip3 install flask
pip3 install -U scikit-learn
pip3 install joblib
```

Now you have to create a environment using virtual env

```
python3 -m venv wine-prediction

$env:FLASK_ENV = "development"
flask  run --host=0.0.0.0
```

