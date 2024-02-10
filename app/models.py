from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    gender_choices = [
    {'value': 'Male', 'label': 'Male'},
    {'value': 'Female', 'label': 'Female'},
    {'value': 'Other', 'label': 'Other'},

    ]
    gender = models.CharField(max_length=10, choices=[(choice['value'], choice['label']) for choice in gender_choices])
    pnum = models.CharField(max_length = 15)
    job_role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    #This is the string representation, what to do after querying a contact 
    def __str__(self):
        return f'{self.name}'

    #This will ordered the contact by date created 
    class Meta:
        ordering = ['-created_at']
