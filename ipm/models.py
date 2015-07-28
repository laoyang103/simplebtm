from django.db import models

# Create your models here.
class bus_tags(models.Model):
    group      = models.IntegerField(default=0)
    bus_tag_0  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_1  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_2  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_3  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_4  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_5  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_6  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_7  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_8  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_9  = models.CharField(max_length=100, blank=True, default='')
    bus_tag_10 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_11 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_12 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_13 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_14 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_15 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_16 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_17 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_18 = models.CharField(max_length=100, blank=True, default='')
    bus_tag_19 = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return str(self.group) + '----' + self.bus_tag_0
