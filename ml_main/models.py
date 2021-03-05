from django.db import models
from django.utils import timezone
'''
from ml_setup.models import Listing


class MasterList(models.Model):
    """Model for Master list main table."""

    code = models.CharField(max_length=11, null=True)
    name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255)
    reg_number = models.CharField(max_length=50, null=True)
    keph_level = models.IntegerField(null=True)
    beds = models.IntegerField(default=0)
    cots = models.IntegerField(default=0)
    is_operational = models.BooleanField(default=True)
    open_whole_day = models.BooleanField(default=True)
    open_public_holidays = models.BooleanField(default=True)
    open_weekends = models.BooleanField(default=True)
    open_late_night = models.BooleanField(default=True)
    approved = models.BooleanField(default=True)
    public_visible = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    list_type = models.ForeignKey(Listing, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        """Override table details."""

        db_table = 'master_list'
        verbose_name = 'Master List'
        verbose_name_plural = 'Master Lists'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.name)
'''