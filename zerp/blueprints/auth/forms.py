from flask.ext.wtf import Form, TextField, PasswordField, Required


class LoginForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
