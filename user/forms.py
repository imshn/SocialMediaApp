from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic', 'username', 'first_name', 'last_name', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'profile_pic':
                field.widget.attrs.update({
                    'class': 'form-control'
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control'
                })

        self.fields['bio'].widget.attrs.update({
            'rows': 3
        })
        self.fields['profile_pic'].widget.attrs.update({
            'class': 'd-none',
            'id': 'id_profile_pic'
        })
        self.fields['username'].disabled = True
        self.fields['username'].widget.attrs.update({
            'class': 'form-control disabled cursor-not-allowed'
        })

