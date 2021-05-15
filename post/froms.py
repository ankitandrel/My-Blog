from django import forms
from django.db import models
from django.forms import ModelForm
from . models import Post
from ckeditor.widgets import CKEditorWidget
class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']
        help_texts = {
            'heading_image': "Url of Image",
        }