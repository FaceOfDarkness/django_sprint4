from django import forms
from .models import Category, Comment, Post, User, Location


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтруем только опубликованные категории
        self.fields['category'].queryset = Category.objects.filter(
            is_published=True
        )
        # Фильтруем только опубликованные локации
        self.fields['location'].queryset = Location.objects.filter(
            is_published=True
        )
        self.fields['location'].required = False
        self.fields['category'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')