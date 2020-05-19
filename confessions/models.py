from django.db import models

# Create your models here.
class Confession(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    his_her_name = models.CharField(max_length=100, blank=True, default='')
    his_her_branch_year_hostel = models.CharField(max_length=100, blank=True, default='')
    your_name_branch_year_hostel = models.CharField(max_length=100, blank=True, default='')
    your_confession = models.TextField(null=True, blank=True)
    to_moderator = models.TextField(null=True, blank=True)

    
    class Meta:
        ordering = ['-created']
