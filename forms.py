from flask_wtf import Form
from wtforms import SubmitField,  FloatField


class predictForm(Form):

    bathrooms = FloatField('bathrooms')
    bedrooms = FloatField('bedrooms')
    pools = FloatField('pools')
    garages = FloatField('garages')
    lotsize = FloatField('lotsize')
    finishedsquarefeet = FloatField('finishedsquarefeet')

    submit = SubmitField('Predict')