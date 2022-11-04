from django import forms
from django.forms import fields, widgets
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Comment
        fields = ['body',]

class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={"placeholder":"Dweet something...", "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Post
        exclude = ("author",)
    class PostForm1(forms.ModelForm):
        class Meta:
            model = Post
            fields = ("title","content","author","date_posted")