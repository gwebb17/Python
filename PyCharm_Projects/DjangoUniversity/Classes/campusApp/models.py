from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(max_length=10, blank=True, null=False)

    #this will format how we display the objects name in the admin browser
    #0.campus name corresponds to the property we want to be displayed (campus_name)
    def __str__(self):
        display_campus = '{0.campus_name}:'
        return display_campus.format(self)
    #this is the nickname the class will be displayed as in browser
    class Meta:
        verbose_name_plural = "University Campus"
