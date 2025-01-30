from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label=_("Title"),
        widget=forms.TextInput(attrs={
            "id": "title-field",
            'placeholder': _('What is the title of the story you want?'),
        }),
    )
    content = forms.CharField(
        label=_("Content"),
        widget=forms.Textarea(attrs={
            "id": "content-field",
            'placeholder': _('Can You Tell me your story in here'),
            'rows': 5,
        }),
    )

    class Meta:
        model = Post
        fields = ['title', 'content']
