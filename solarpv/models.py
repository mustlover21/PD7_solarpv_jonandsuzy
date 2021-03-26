from django.db import models
from django.conf import settings # import user settings
from django_countries.fields import CountryField # for location
from localflavor.us.models import USStateField # for location
from localflavor.us.us_states import STATE_CHOICES # for location
from django.contrib.auth.models import User
from PIL import Image

User = settings.AUTH_USER_MODEL

# models used as a FK must be created before models using it as FK.

class Client(models.Model):
    #id = models.AutoField()
    client_name = models.CharField(max_length=100, default='')
    client_type = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.client_name # displays information when called

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    prefix = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100)
    office_phone = models.CharField(max_length=15)
    cell_phone = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    client_id = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path) # resizes image

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Location(models.Model):
    # id = models.AutoField()
    client_id = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    # FK SET_NULL deletes only the FK not everything associated with it.
    # FK CASCADE deletes FK and everything associated with it.
    address1 = models.CharField(max_length=100, default='')
    address2 = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='')
    state = USStateField(choices = STATE_CHOICES)
    postal_code = models.CharField(max_length=10, default='')
    country = CountryField(default='')
    phone_number = models.CharField(max_length=100, default='')
    fax_number = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.client_id.client_name


class TestStandard(models.Model):
    #id = models.AutoField()
    standard_name = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.standard_name


class TestSequence(models.Model):
    # id = models.AutoField()
    sequence_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.sequence_name


class Product(models.Model):
    #id = models.AutoField()
    model_number = models.CharField(max_length=100, default='')
    product_name = models.CharField(max_length=100, default='')
    length = models.IntegerField(default=0)  
    width = models.IntegerField(default=0)  
    weight = models.IntegerField(default=0)  
    cell_technology = models.CharField(max_length=100, default='')
    cell_manufacturer = models.CharField(max_length=100, default='')
    number_of_cells = models.IntegerField(default=0)    
    number_of_cells_in_series = models.IntegerField(default=0)  
    number_of_series_strings = models.IntegerField(default=0)
    number_of_bypass_diodes = models.IntegerField(default=0)  
    superstrate_type = models.CharField(max_length=100, default='')
    superstrate_manufacturer = models.CharField(max_length=100, default='')
    substrate_type = models.CharField(max_length=100, default='')
    substrate_manufacturer = models.CharField(max_length=100, default='')
    frame_type = models.CharField(max_length=100, default='')
    frame_adhesive = models.CharField(max_length=100, default='')
    encapsulant_type = models.CharField(max_length=100, default='')
    encapsulant_manufacturer = models.CharField(max_length=100, default='')
    junction_box_type = models.CharField(max_length=100, default='')
    junction_box_manufacturer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.product_name 


class Certificate(models.Model):
    #id = models.AutoField()
    certificate_number = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    report_number = models.CharField(max_length=100, default='')
    issue_date = models.DateField(auto_now=False, auto_now_add=False)
    standard_id = models.ForeignKey(TestStandard, blank=True,  null=True, on_delete=models.SET_NULL)
    location_id = models.ForeignKey(Location, blank=True,  null=True, on_delete=models.SET_NULL)
    model_number = models.ForeignKey(Product, blank=True,  null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.certificate_number


class Service(models.Model):
    #id = models.AutoField()
    service_name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    is_fi_required = models.BooleanField(default=False)
    fi_frequency = models.CharField(max_length=100, default='')
    standard_id = models.ForeignKey(TestStandard, blank=True,  null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.service_name


class PerformanceData(models.Model):
    #id = models.AutoField()
    model_number = models.ForeignKey(Product, blank=True,  null=True, on_delete=models.SET_NULL)
    sequence_id = models.ForeignKey(TestSequence, blank=True,  null=True, on_delete=models.SET_NULL)
    max_system_voltage = models.IntegerField(default=0)
    voc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vmp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    imp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pmp = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ff = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.model_number.model_number




