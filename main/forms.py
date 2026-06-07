# main/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Resume

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    company = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Company Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '+1 (555) 000-0000'})
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'What is this about?'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell me more about your inquiry...'})
    )
    job_type = forms.ChoiceField(choices=[
        ('fulltime', 'Full-Time Role'),
        ('internship', 'Internship'),
        ('freelance', 'Freelance Project'),
        ('other', 'Other'),
    ])


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf',
            })
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > 5 * 1024 * 1024:  # 5MB limit
                raise ValidationError("File size must be less than 5MB")
            if not file.name.endswith('.pdf'):
                raise ValidationError("Only PDF files are allowed")
        return file