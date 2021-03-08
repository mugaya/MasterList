import uuid
from django.db import models
from django.contrib.gis.db import models as gmodels
from django.utils import timezone

from .utils import unique_fid_generator

from ml_setup.models import (
    Listing, FacilityType, OwnerType, Service,
    ListGeoCounty, ListGeoConstituency, ListGeoWard)


class MasterList(models.Model):
    """Model for Master list main table."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=11, null=True, blank=True)
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
    approval_status = models.CharField(max_length=4, null=True)
    public_visible = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    list_type = models.ForeignKey(Listing, on_delete=models.CASCADE, default=1)
    facility_type = models.ForeignKey(FacilityType, on_delete=models.CASCADE)
    owner_type = models.ForeignKey(OwnerType, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    validated = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    def _get_approved(self):
        if self.approved:
            _approved = MasterList.objects.filter(
                code__isnull=False, approved=True).count()
            return _approved
        else:
            return 0

    def make_code(self):
        """Inline call public method."""
        try:
            ftid = self.facility_type.facility_type_code
            fid = self._get_approved() + 1
            final_code = unique_fid_generator(ftid, fid)
            self.code = final_code
            super(MasterList, self).save()
        except Exception:
            pass

    def save(self, *args, **kwargs):
        # This is to save the Unique code.
        if self.pk is None and not self.code and self.approved:
            self.code = self.code
        elif self.pk and not self.code:
            ftid = self.facility_type.facility_type_code
            fid = self._get_approved() + 1
            final_code = unique_fid_generator(ftid, fid)
            self.code = final_code

        # Call the original save method
        super(MasterList, self).save(*args, **kwargs)

    class Meta:
        """Override table details."""

        db_table = 'master_list'
        verbose_name = 'Master List'
        verbose_name_plural = 'Master Lists'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.name)


class MasterListService(models.Model):
    """Model for Master list services table."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    master_list = models.ForeignKey(MasterList, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'master_list_service'
        verbose_name = 'Master List Service'
        verbose_name_plural = 'Master List Services'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.service)


class MasterListContact(models.Model):
    """Model for Master list services table."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    master_list = models.ForeignKey(MasterList, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=4)
    contact_detail = models.CharField(max_length=4)
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'master_list_contact'
        verbose_name = 'Master List Contact'
        verbose_name_plural = 'Master List Contacts'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.contact_type)


class MasterListGeo(gmodels.Model):
    """ Models to save the Geo Locations."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    master_list = models.OneToOneField(MasterList, on_delete=models.CASCADE)
    county = models.ForeignKey(ListGeoCounty, on_delete=models.CASCADE)
    constituency = models.ForeignKey(
        ListGeoConstituency, on_delete=models.CASCADE)
    sub_county = models.CharField(max_length=100)
    ward = models.ForeignKey(ListGeoWard, on_delete=models.CASCADE)
    lon_lat = gmodels.PointField()
    timestamp_created = models.DateTimeField(default=timezone.now)
    timestamp_updated = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'master_list_geo'
        verbose_name = 'Master List Geo'
        verbose_name_plural = 'Master List Geos'

    def __str__(self):
        """To be returned by admin actions."""
        return 'Geo : %s' % (self.master_list)
