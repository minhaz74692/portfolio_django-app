from django import forms
from django.core import validators
class RegistrationForms(forms.Form):
    first_name = forms.CharField(label="Enter first name", label_suffix=' ', initial='Jhon Doe', )
    last_name = forms.CharField(label="Enter last name", label_suffix=' ')
    email = forms.EmailField(label='Enter email', label_suffix=' ', initial="example@gmail.com", disabled=True)
    password = forms.CharField(label='Enter password', label_suffix=' ', widget=forms.PasswordInput)
    repassword = forms.CharField(label='Re-Enter password', label_suffix=' ', widget=forms.PasswordInput)
    textarea = forms.CharField(label="Comment" , widget=forms.Textarea)
    file = forms.CharField(label="Comment" , widget=forms.FileInput)
    checkbox = forms.CharField(label="Checkbox" , widget=forms.CheckboxInput)

    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']

        if rightpass != wrongpass:
            print("Password doesn't match")
            raise forms.ValidationError('Password does not match')

   