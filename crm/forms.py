from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import Customer, Information, SkinCareInquiry, SkinCareReport, Treatment, TreatmentList, ScheduleAppointment, BookAppointment, Report
from django import forms
from django.forms.widgets import PasswordInput, TextInput


# -- Register/Create a User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        

# -- Login a User

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# -- Create a Customer Form

class CreateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone']
        

# -- Update a Customer Form

class UpdateCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone']


# -- Create a Information Form

class CreateInformationForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = ['customer', 'gender', 'age', 'address_1', 'address_2', 'city', 'county', 'postcode', 'country']


# -- Update a Information Form

class UpdateInformationForm(forms.ModelForm):

    class Meta:
        model = Information
        fields = ['gender', 'age', 'address_1', 'address_2', 'city', 'county', 'postcode', 'country']


# -- Skin Care Inguiry Form

class SkinCareInquiryForm(forms.ModelForm):

    class Meta:
        model = SkinCareInquiry
        fields = ['customer', 'hair_coloring', 'hair_coloring_details', 'scalp_issues', 'scalp_issues_details', 'skin_allergy', 'skin_allergy_details']


# -- Skin Care Report Form

class SkinCareReportForm(forms.ModelForm):

    class Meta:
        model = SkinCareReport
        fields = ['customer', 'allergic_reaction', 'proceed_service', 'observation']


# -- Treatment List Form

class TreatmentListForm(forms.ModelForm):

    class Meta:
        model = TreatmentList
        fields = ['treatment_name', 'extra_note']


# -- Treatment Form

class TreatmentForm(forms.ModelForm):

    class Meta:
        model = Treatment
        fields = ['customer', 'treatment_list', 'treatment_note']


# -- Schedule / Set Appointment Form

class ScheduleAppointmentForm(forms.ModelForm):

    class Meta:
        model = ScheduleAppointment
        fields = ['customer', 'treatment_name', 'schedule', 'day', 'appointment_note']


# -- Schedule / Book Appointment Form

class BookAppointmentForm(forms.ModelForm):

    class Meta:
        model = BookAppointment
        fields = ['full_name', 'phone', 'email', 'treatment_name', 'address', 'schedule', 'day', 'message']


# -- Report Form

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ['full_name', 'phone', 'email', 'message']




