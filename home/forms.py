from django import forms

class RegistrationForms(forms.Form):
    first_name = forms.CharField(label="Enter first name", label_suffix=' ', initial='Jhon Doe', )
    last_name = forms.CharField(label="Enter last name", label_suffix=' ')
    email = forms.CharField(label='Enter email', label_suffix=' ', initial="example@gmail.com", disabled=True)
    password = forms.CharField(label='Enter password', label_suffix=' ', widget=forms.PasswordInput)
    textarea = forms.CharField(label="Comment" , widget=forms.Textarea)
    file = forms.CharField(label="Comment" , widget=forms.FileInput)
    checkbox = forms.CharField(label="Checkbox" , widget=forms.CheckboxInput)
   