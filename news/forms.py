from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from django import forms
from .models import Post, User


# Создаём модельную форму
class PostForm(ModelForm):
    # check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = [
          'author',
          'category_type',
          'title',
          'text'
          ]

        widgets = {
          'authorType' : forms.TextInput(attrs={'class': 'form-control pure-input-1-2'}),
          'category' : forms.Select(attrs={'class': 'form-control pure-input-1-2'}),
          'title' : forms.TextInput(attrs={'class': 'form-control pure-input-1-2',   'placeholder': 'Post Title'}),
          'text': forms.Textarea(attrs={'class': 'form-control pure-input-1-2'})
        }
        labels = {
                    "author": "Author",
                    "category_ype": "Category",
                    "title": "Title",
                    "text": "Text",
                }


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            # 'password',

        ]