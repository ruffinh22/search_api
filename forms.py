# ;§>

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class GoogleSearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    sector = SelectField('Sector', choices=[('Agence immobiliere', 'Agence immobiliere'), ('Sante', 'Sante')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Search')

class FacebookSearchForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    sector = SelectField('Sector', choices=[('Agence immobiliere', 'Agence immobiliere'), ('Sante', 'Sante'), ('', '')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Search')
# ;§<