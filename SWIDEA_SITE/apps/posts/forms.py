from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'interest', 'devtool']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '아이디어 제목'}),
            'content': forms.Textarea(attrs={'placeholder': '아이디어 내용'}),
            'interest': forms.NumberInput(attrs={'min': 0}),
            'devtool': forms.Select(),  # 생략해도 자동 적용
        }
