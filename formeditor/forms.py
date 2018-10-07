from django import forms
from .models import Post
from ckeditor.fields import RichTextFormField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CkEditorForm(forms.Form):
    content = RichTextFormField()