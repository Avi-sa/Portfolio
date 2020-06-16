from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label=' ',required=True,widget=forms.TextInput(attrs={'style': 'width:330px'}))
    subject = forms.CharField(max_length=30,label=' ',required=True,widget=forms.TextInput(attrs={'style': 'width:330px'}))
    message = forms.CharField(label='    ',widget=forms.Textarea, required=True)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
