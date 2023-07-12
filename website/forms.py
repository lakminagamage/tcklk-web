from django import forms
from .models import ContactFormModel,PortfolioItems,TestimonialItems,ClientlogoItems


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'contact_number', 'subject', 'message' ]


class PortfolioAdd(forms.ModelForm):
    class Meta:
        model = PortfolioItems
        fields = ['name', 'type', 'image', 'sort_by', 'keyword']

class ClientlogoAdd(forms.ModelForm):
    class Meta:
        model = ClientlogoItems
        fields = ['business_name', 'image', 'keyword']

class TestimonialAdd(forms.ModelForm):
    class Meta:
        model = TestimonialItems
        fields = ['name' , 'business_name', 'contact_number', 'email', 'image', 'message', 'keyword']

