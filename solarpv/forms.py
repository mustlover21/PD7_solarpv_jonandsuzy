from django import forms
from django.forms import ModelForm
from .models import Profile, Product, Certificate, Service, Location, Client, PerformanceData, TestSequence, TestStandard
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


non_allowed_usernames = ['abc'] #list of usernames we don't want to allow
# check for unique email and username

   

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']


        # validate username
    def clean_username(self): 
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames: # checks against nonallowed usernames list
            raise forms.ValidationError("This is an invalid username. Please pick another.")
        if qs.exists():
            raise forms.ValidationError("This is an invalid username. Please pick another.")
        # we don't want users to know other peoples usernames from a secrutiy standpoint!
        return username

    # validate email
    def clean_email(self): # validate email
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        # we don't want users to know other peoples usernames from a security standpoint!
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('prefix', 'company', 'job_title', 'office_phone', 'cell_phone', 'image')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        # fields = "__all__"   # if you want all the fields 
        fields = ('model_number', 'product_name', 'length', 'width', 'weight', 'cell_technology', 'cell_manufacturer', 'number_of_cells', 'number_of_cells_in_series', 'number_of_series_strings', 'number_of_bypass_diodes', 'superstrate_type', 'superstrate_manufacturer', 'substrate_type', 'substrate_manufacturer', 'frame_type', 'frame_adhesive', 'encapsulant_type', 'encapsulant_manufacturer', 'junction_box_type', 'junction_box_manufacturer')
        
        labels = {
            'model_number': '',
            'product_name':  '',
            'length': 'Length (inches)',
            'width': 'Width (inches)',
            'weight': 'Weight (kg)',
            'cell_technology': '',
            'cell_manufacturer': '',
            'number_of_cells': 'Number of Cells',
            'number_of_cells_in_series': 'Number of cells in a series',
            'number_of_series_strings': 'Number of series strings',
            'number_of_bypass_diodes': 'Number of bypass diodes',
            'superstrate_type': '',
            'superstrate_manufacturer': '',
            'substrate_type': '',
            'substrate_manufacturer': '',
            'frame_type': '',
            'frame_adhesive': '',
            'encapsulant_type': '',
            'encapsulant_manufacturer': '',
            'junction_box_type': '',
            'junction_box_manufacturer': '',
        }

        widgets = {
            'model_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Model Number'}),
            'product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}),
            'length': forms.NumberInput(attrs={'class':'form-select'}),
            'width': forms.NumberInput(attrs={'class':'form-select'}),
            'weight': forms.NumberInput(attrs={'class':'form-select'}),
            'cell_technology': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cell Technology'}),
            'cell_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cell Manufacturer'}),
            'number_of_cells': forms.NumberInput(attrs={'class':'form-select'}),
            'number_of_cells_in_series': forms.NumberInput(attrs={'class':'form-select'}),
            'number_of_series_strings': forms.NumberInput(attrs={'class':'form-select'}),
            'number_of_bypass_diodes': forms.NumberInput(attrs={'class':'form-select'}),
            'superstrate_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Superstrate Type'}),
            'superstrate_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Superstrate Manufacturer'}),
            'substrate_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Substrate Type'}),
            'substrate_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Substrate Manufacturer'}),
            'frame_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frame Type'}),
            'frame_adhesive': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frame Adhesive'}),
            'encapsulant_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Encapsulant Type'}),
            'encapsulant_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Encapsulant Manufacturer'}),
            'junction_box_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Junction Box Type'}),
            'junction_box_manufacturer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Junction Box Manufacturer'}),
        }

class CertificateForm(ModelForm):
    class Meta:
        model = Certificate

        # fields = "__all__"   # if you want all the fields 
        fields = ('certificate_number', 'model_number', 'user', 'report_number', 'issue_date', 'standard_id', 'location_id') 
        
        labels = {
            'certificate_number': '',
            'user': '',
            'report_number': '',
            'issue_date': '',
            'standard_id': 'Standard ID',
            'location_id': 'Location ID',
            'model_number': '',
        }

        widgets = {
            'certificate_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Certificate Number'}),
            'user': forms.TextInput(attrs={'class':'form-control', 'placeholder':'User'}),
            'report_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Report Number'}),
            'issue_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Issue'}),
            'standard_id': forms.Select(attrs={'class':'form-select'}),
            'location_id': forms.Select(attrs={'class':'form-select'}),
            'model_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Model Number'}),
        }

class ServiceForm(ModelForm):
    class Meta:
        model = Service

        # fields = "__all__"   # if you want all the fields 
        fields = ('service_name', 'description', 'is_fi_required', 'fi_frequency', 'standard_id') 
        
        labels = {
            'service_name': '',
            'description': '',
            'is_fi_required': '',
            'fi_frequency': '',
            'standard_id': 'Standard ID',
        }

        widgets = {
            'service_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Certificate Number'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'User'}),
            'is_fi_required': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Report Number'}),
            'fi_frequency': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of Issue'}),
            'standard_id': forms.Select(attrs={'class':'form-select'}),
        }

class LocationForm(ModelForm):
    class Meta:
        model = Location
        
        # fields = "__all__"   # if you want all the fields 
        fields = ('client_id', 'address1', 'address2', 'city', 'state', 'postal_code', 'country', 'phone_number', 'fax_number') 
        
        labels = {
            'client_id': 'Client ID',
            'address1': '',
            'address2': '',
            'city': '',
            'state': 'State',
            'postal_code': '',
            'country': 'Country',
            'phone_number': '',
            'fax_number': '',
        }

        widgets = {
            'client_id': forms.Select(attrs={'class':'form-select'}),
            'address1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),
            'address2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postal Code'}),
            'country': forms.Select(attrs={'class':'form-select'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'fax_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fax Number'}),
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client

        # fields = "__all__"   # if you want all the fields 
        fields = ('client_name', 'client_type') 
        
        labels = {
            'client_name': '',
            'client_type': '',
        }

        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Name'}),
            'client_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Type'}),
        }

class PerformanceDataForm(ModelForm):
    class Meta:
        model = PerformanceData

        # fields = "__all__"   # if you want all the fields 
        fields = ('model_number', 'sequence_id', 'max_system_voltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff') 
        
        labels = {
            'model_number': 'Model Number',
            'sequence_id': 'Sequence ID',
            'max_system_voltage': 'Max System Voltage (Volts)',
            'voc': 'Voc (Volts)',
            'isc': 'Isc (Amps)',
            'vmp': 'Vmp (Volts)',
            'imp': 'Imp (Amps)',
            'pmp': 'Pmp (Watts)',
            'ff': 'FF (%)',
        }

        widgets = {
            'model_number': forms.Select(attrs={'class':'form-select'}),
            'sequence_id':  forms.Select(attrs={'class':'form-select'}),
            'max_system_voltage': forms.NumberInput(attrs={'class':'form-select'}),
            'voc': forms.NumberInput(attrs={'class':'form-select'}),
            'isc': forms.NumberInput(attrs={'class':'form-select'}),
            'vmp': forms.NumberInput(attrs={'class':'form-select'}),
            'imp': forms.NumberInput(attrs={'class':'form-select'}),
            'pmp': forms.NumberInput(attrs={'class':'form-select'}),
            'ff': forms.NumberInput(attrs={'class':'form-select'}),
        }

class TestSequenceForm(ModelForm):
    class Meta:
        model = TestSequence

        # fields = "__all__"   # if you want all the fields 
        fields = ('sequence_name',) 
        
        labels = {
            'sequence_name': '',
        }

        widgets = {
            'sequence_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sequence Name'}),
        }

class TestStandardForm(ModelForm):
    class Meta:
        model = TestStandard

        # fields = "__all__"   # if you want all the fields 
        fields = ('standard_name', 'description', 'published_date') 
        
        labels = {
            'standard_name': '',
            'description': '',
            'published_date': '',    
        }

        widgets = {
            'servicstandard_namee_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Standard Name'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'User'}),
            'published_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Published Date'}),
        }