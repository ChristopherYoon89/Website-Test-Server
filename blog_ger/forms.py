from django import forms 
from blog.models import (
	ContactRequest,
	NewsletterRequest,
)
from .models import JobApplicationGerman
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django.conf import settings


RECAPTCHA_PRIVATE_KEY = settings.RECAPTCHA_PRIVATE_KEY
RECAPTCHA_PUBLIC_KEY = settings.RECAPTCHA_PUBLIC_KEY


class ContactForm(forms.ModelForm):
    """
    Form that allows user to contact me
    """
    name = forms.TextInput()
    email = forms.EmailField()
    subject = forms.TextInput()
    message = forms.Textarea()
    captcha = ReCaptchaField(
        public_key=RECAPTCHA_PUBLIC_KEY,
        private_key=RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3(
            action='contact'
        ),    
    )

    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'subject', 'message', 'captcha']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Name'
        self.fields['email'].label = 'Email'
        self.fields['subject'].label = 'Betreff'
        self.fields['message'].label = 'Nachricht'



class NewsletterForm(forms.ModelForm):
    '''
    Form that allows user to sign up for the newsletter
    '''
    email = forms.EmailField() 
    captcha = ReCaptchaField(
        public_key=RECAPTCHA_PUBLIC_KEY,
        private_key=RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3(
            action='newsletter'
        ),
    )

    class Meta:
        model = NewsletterRequest
        fields = ['email', 'captcha']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'



class JobApplicationGermanForm(forms.ModelForm):

    captcha = ReCaptchaField(
        public_key=RECAPTCHA_PUBLIC_KEY,
        private_key=RECAPTCHA_PRIVATE_KEY,
        widget=ReCaptchaV3(
            action='jobapplication_de'
        ),
    )

    class Meta:
        model = JobApplicationGerman
        fields = ['name', 'email', 'subject', 'message', 'resume_upload', 'captcha']