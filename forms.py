from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL,Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegistrationForm(FlaskForm):
    email= StringField(validators=[DataRequired(), Email()], render_kw={"placeholder":"email"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "password"})
    name = StringField(validators=[DataRequired()], render_kw={"placeholder": "name"})
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email= StringField(validators=[DataRequired(), Email()], render_kw={"placeholder":"email"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "password"})
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
