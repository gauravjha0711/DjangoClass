# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # author set in view, not by user
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'rows': 8, 'class': 'form-control'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if not content or not content.strip():
            raise forms.ValidationError("Content cannot be empty or only whitespace.")
        return content
