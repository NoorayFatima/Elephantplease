# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'your-css-class', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'your-css-class', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'your-css-class', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'your-css-class', 'placeholder': 'Email Address'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'your-css-class', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'your-css-class', 'placeholder': 'Confirm Password'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match")


#class SignInForm(AuthenticationForm):
#    username = forms.CharField(widget=forms.TextInput())
#    password = forms.CharField(widget=forms.PasswordInput())

#class ForgetPasswordForm(PasswordResetForm):
#    email = forms.EmailField()

#class ResetPasswordForm(SetPasswordForm):
#    new_password1 = forms.CharField(widget=forms.PasswordInput())
#    new_password2 = forms.CharField(widget=forms.PasswordInput())

#class ChangePasswordForm(PasswordChangeForm):
#    old_password = forms.CharField(widget=forms.PasswordInput())
#    new_password1 = forms.CharField(widget=forms.PasswordInput())
#    new_password2 = forms.CharField(widget=forms.PasswordInput())
