import flask
import flask_wtf, wtforms

class LoginForm(flask_wtf.FlaskForm):
    login = wtforms.StringField("Login", validators=[wtforms.validators.InputRequired()])
    password = wtforms.PasswordField("Password", validators=[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField("Log In")