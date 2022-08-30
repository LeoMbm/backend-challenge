from django import forms


class NameForm(forms.Form):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=255)



