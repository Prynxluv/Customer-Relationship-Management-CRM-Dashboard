from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField


# Create your models here.

# ----- OPTION CHOICES -----

GENDER = {
    "Male" : "Male",
    "Female" : "Female",
}


SELECT = {
    "Yes" : "Yes",
    "No" : "No",
}


SCHELDULE = {
    "9am to 10am" : "9am to 10am",
    "10am to 11am" : "10am to 11am",
    "11am to 12pm" : "11am to 12pm",
    "12pm to 1pm" : "12pm to 1pm",
    "1pm to 2pm" : "1pm to 2pm",
    "2pm to 3pm" : "2pm to 3pm",
    "3pm to 4pm" : "3pm to 4pm",
    "4pm to 5pm" : "4pm to 5pm",
    "5pm to 6pm" : "5pm to 6pm",
}


DAY = {
    "Monday" : "Monday",
    "Tuesday" : "Tuesday",
    "Wednesday" : "Wednesday",
    "Thursday" : "Thursday",
    "Friday" : "Friday",
    "Saturday" : "Saturday",
    "Sunday" : "Sunday",
}



class Customer(models.Model):

    full_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.PositiveIntegerField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='full_name', always_update=True, null=True, unique=True)
    
    
    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):

        return f"{self.full_name}"
    

    # def save(self, *args, **kwargs):
    #     # if not self.slug:
    #     self.slug = slugify(f'{self.full_name}-{str(self.phone)}')
    #     return super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(f'{self.full_name}-{str(self.phone)}')
    #     return super().save(*args, **kwargs)



class Information(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name='customers_name')
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    age = models.PositiveIntegerField(null=True)
    address_1 = models.CharField(max_length=300, null=True)
    address_2 = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    postcode = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='full_name', always_update=True, null=True, unique=True)
    # slug = models.CharField(max_length=1000, null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.customer.full_name} Informations"
    

    @property
    def full_name(self):
        return self.customer.full_name
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(f'{self.customer.full_name}-{str(self.customer.phone)}')
    #     return super().save(*args, **kwargs)



class SkinCareInquiry(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    hair_coloring = models.CharField(max_length=10, choices=SELECT, null=True)
    hair_coloring_details = models.TextField(max_length=1000, null=True)

    scalp_issues = models.CharField(max_length=10, choices=SELECT, null=True)
    scalp_issues_details = models.TextField(max_length=1000, null=True)

    skin_allergy = models.CharField(max_length=10, choices=SELECT, null=True)
    skin_allergy_details = models.TextField(max_length=1000, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Skin Care Inquiries'

    def __str__(self):

        return f"{self.customer.full_name} Skin Care Inquiry"



# connect the report below to the ID of the skin inquiry above or give them both a number or give the above a slug with and and date created



class SkinCareReport(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    allergic_reaction = models.CharField(max_length=10, choices=SELECT, null=True)
    proceed_service = models.CharField(max_length=10, choices=SELECT, null=True)
    observation = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.customer.full_name}'s Skin Care Report"



class TreatmentList(models.Model):

    treatment_name = models.CharField(max_length=200, null=True)
    extra_note = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.treatment_name}"



class Treatment(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    treatment_list = models.ForeignKey(TreatmentList, on_delete=models.CASCADE, null=True)
    treatment_note = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.customer.full_name} {self.treatment_list.treatment_name}"
    


##### Schedule and Automate appointment
class ScheduleAppointment(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    treatment_name = models.ForeignKey(TreatmentList, on_delete=models.CASCADE, null=True)
    schedule = models.CharField(max_length=20, choices=SCHELDULE, null=True)
    day = models.CharField(max_length=20, choices=DAY, null=True)
    appointment_note = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):

        return f"{self.customer.full_name} Scheduled Appointment"



class BookAppointment(models.Model):

    full_name = models.CharField(max_length=100, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    treatment_name = models.ForeignKey(TreatmentList, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100, null=True)
    schedule = models.CharField(max_length=20, choices=SCHELDULE, null=True)
    day = models.CharField(max_length=20, choices=DAY, null=True)
    message = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.full_name} Booked Appointment"



class Report(models.Model):

    full_name = models.CharField(max_length=100, null=True)
    phone = models.PositiveIntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=1000, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    

    
