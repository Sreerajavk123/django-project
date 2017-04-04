from django import forms

class nameform(forms.Form):
    your_name=forms.charfield(label='your name' ,max_length=100)
    