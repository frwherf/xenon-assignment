from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email, URL


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    Name = StringField("Name", validators=[DataRequired()])
    Email = StringField("Email", validators=[DataRequired(),Email(message="Enter correct Email")])
    Password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class Login(FlaskForm):
    Email = StringField("Email", validators=[DataRequired(),Email(message="Enter correct Email")])
    Password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

