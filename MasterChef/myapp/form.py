from django import forms

class InputForm(forms.Form):
    inputBox=forms.CharField(max_length=200,
        widget=forms.TextInput(attrs={'placeholder':'ask me about food...'})
    )