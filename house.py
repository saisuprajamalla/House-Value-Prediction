from flask import Flask, render_template, request
from flask_script import Manager
from forms import predictForm
import pickle

app = Flask(__name__)
app.secret_key = 's3cr3t'
manager = Manager(app)

@manager.command
def runserver():
    app.run(host='127.0.0.1', port=5000, debug=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = predictForm()
    if request.method == 'POST':

        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        pools = form.pools.data
        garages = form.garages.data
        lotsize = form.lotsize.data
        finishedsquarefeet = form.finishedsquarefeet.data

        sample=[]
        sample.append(lotsize)
        sample.append(finishedsquarefeet)
        sample.append(bedrooms)
        sample.append(bathrooms)
        sample.append(2)
        sample.append(garages)
        sample.append(pools)
        sample.append(9)
        sample.append(0)

        load_model = pickle.load(open('xgboost.sav', 'rb'))
        res = -load_model.predict(sample)
        price1 =(res * (1299963.0-900001.0))+900001.0
        price = price1[0]
        # price = str(res[0])
        return render_template('predict.html', price=price)
    elif request.method == 'GET':
        return render_template('home.html', form=form)


if __name__ == '__main__':
    manager.run()

