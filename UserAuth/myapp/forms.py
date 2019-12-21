from django import forms
from .models import School, Tutor, Coaching


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'location', 'email', 'phone', 'photo', 'video')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'required': True, 'multiple': True, 'accept': 'image/*'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'required': True, 'multiple': True, 'accept': 'video/*'}),
        }


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('name', 'location', 'email', 'phone', 'photo', 'video')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'multiple': True, 'accept': 'image/*'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'multiple': True, 'accept': 'video/*'}),
        }


class CoachingForm(forms.ModelForm):
    class Meta:
        model = Coaching
        fields = ('name', 'location', 'email', 'phone', 'photo', 'video')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'autofocus': ''}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'multiple': True, 'accept': 'image/*'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'multiple': True, 'accept': 'video/*'}),
        }
