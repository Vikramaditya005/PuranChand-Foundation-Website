# foundation_app/forms.py

from django import forms
from .models import ContactMessage, Volunteer, Campaign # ADDED: Import the Volunteer model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        # You can add widgets for custom HTML attributes like placeholders or custom classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Inquiry about partnership', 'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here...', 'rows': 5, 'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200'}),
        }

# NEW CLASS: Form for the volunteer submission on the dashboard
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'email', 'phone', 'availability', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                'placeholder': 'Your Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                'placeholder': 'Your Phone Number'
            }),
            'availability': forms.TextInput(attrs={
                'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                'placeholder': 'Your Availability (e.g. weekends, evenings)'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Why do you want to volunteer?',
                'rows': 5,
                'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200'
            }),
        }



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                'placeholder': 'Your Username'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
            'placeholder': '********'
        })
    )

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
            'placeholder': 'Your Email'
        })
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
            'placeholder': 'Your First Name'
        })
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
            'placeholder': 'Your Last Name'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'w-full px-5 py-3 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 text-lg transition-colors duration-200',
                    'placeholder': self.fields[field_name].label
                })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        if commit:
            user.save()
        return user


class CampaignForm(forms.ModelForm):
    class Meta:
        # Link this form to the Campaign model.
        model = Campaign
        
        # Specify the fields that will be included in the form.
        fields = ['title', 'goal_amount', 'description']
        
        # Add custom styling and placeholders using widgets.
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 sm:text-lg',
                'placeholder': 'e.g., Support Our Clean Water Initiative'
            }),
            'goal_amount': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 sm:text-lg',
                'placeholder': 'e.g., 500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-orange-500 focus:border-orange-500 sm:text-lg',
                'placeholder': 'Tell your story and explain why this cause is important to you.',
                'rows': 6
            }),
        }
from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title', 'goal_amount', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:outline-none',
                'placeholder': 'e.g., Support Our Clean Water Initiative'
            }),
            'goal_amount': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:outline-none',
                'placeholder': 'e.g., 500'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-orange-500 focus:outline-none',
                'placeholder': 'Tell your story and explain why this cause is important to you.'
            }),
        }
