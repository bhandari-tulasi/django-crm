from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from djagno import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label='',max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Requried. 50 Characters or fewer. Letters, Digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text='<ul class="form-text text-muted"><li>Must be combination of letter, numbers and special characters</li></ul>

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text='<ul class="form-text text-muted"><li>Must be combination of letter, numbers and special characters</li></ul>