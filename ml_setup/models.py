from django.db import models
from django.utils import timezone


class Listing(models.Model):
    """Model for Listing types details."""

    listing_code = models.CharField(max_length=2)
    listing_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_listing_type'
        verbose_name = '00-Listing Type'
        verbose_name_plural = '00-Listing Types'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.listing_name)


class ServiceCategory(models.Model):
    """Model for Listing types details."""

    category_abbr = models.CharField(max_length=8, null=True)
    category_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_service_category'
        verbose_name = '06-Service Category'
        verbose_name_plural = '06-Service Categories'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.category_name)


class Service(models.Model):
    """Model for Listing types details."""

    service_code = models.IntegerField()
    service_name = models.CharField(max_length=100)
    service_abbr = models.CharField(max_length=8, null=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_service'
        verbose_name = '07-Service List'
        verbose_name_plural = '07-Service Lists'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s : %s' % (self.category, self.service_name)


class TypeCategory(models.Model):
    """Model for Listing types details."""

    type_category_abbr = models.CharField(max_length=8, null=True)
    type_category_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_type_category'
        verbose_name = '01-Type Category'
        verbose_name_plural = '01-Type Categories'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.type_category_name)


class FacilityType(models.Model):
    """Model for Listing types details."""

    facility_type_code = models.IntegerField()
    facility_type_name = models.CharField(max_length=100)
    facility_type_abbr = models.CharField(max_length=8, null=True)
    facility_type = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_facility_type'
        verbose_name = '02-Facility Type'
        verbose_name_plural = '02-Facility Types'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s : %s' % (self.facility_type, self.facility_type_name)


class OwnerCategory(models.Model):
    """Model for Listing types details."""

    owner_category_abbr = models.CharField(max_length=8, null=True)
    owner_category_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_owner_category'
        verbose_name = '03-Owner Category'
        verbose_name_plural = '03-Owner Categories'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.owner_category_name)


class OwnerType(models.Model):
    """Model for Listing types details."""

    owner_type_code = models.IntegerField()
    owner_type_name = models.CharField(max_length=100)
    owner_type_abbr = models.CharField(max_length=8, null=True)
    owner_type = models.ForeignKey(OwnerCategory, on_delete=models.CASCADE)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_owner_type'
        verbose_name = '04-Owner Type'
        verbose_name_plural = '04-Owner Types'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s : %s' % (self.owner_type, self.owner_type_name)


class Regulator(models.Model):
    """Model for Regulator details."""

    regulator_abbr = models.CharField(max_length=8, null=True)
    regulator_name = models.CharField(max_length=100)
    regulation_verb = models.CharField(max_length=10, null=True)
    regulator_code = models.IntegerField()
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_regulator_type'
        verbose_name = '05-Regulator Type'
        verbose_name_plural = '05-Regulator Types'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.regulator_name)


class ListGeneral(models.Model):
    """List used for drop downs and other selections."""

    item_id = models.CharField(max_length=5)
    item_description = models.CharField(max_length=255)
    item_category = models.CharField(max_length=50, null=True, blank=True)
    item_sub_category = models.CharField(max_length=50, null=True, blank=True)
    the_order = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    field_name = models.CharField(max_length=100, null=True, blank=True)
    timestamp_created = models.DateTimeField(default=timezone.now)

    class Meta:
        """Override some params."""

        db_table = 'list_general'
        verbose_name = 'General Settings List'
        verbose_name_plural = 'General Settings Lists'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s - %s' % (self.item_id, self.item_description)


class ListGeoCounty(models.Model):
    """Model for Listing types details."""

    county_code = models.CharField(max_length=3)
    county_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_geo_county'
        verbose_name = 'List Geo - County'
        verbose_name_plural = 'List Geo - Counties'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.county_name)


class ListGeoConstituency(models.Model):
    """Model for Listing types details."""

    constituency_code = models.CharField(max_length=3)
    constituency_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_geo_constituency'
        verbose_name = 'List Geo - Constituency'
        verbose_name_plural = 'List Geo - Constituencies'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s' % (self.constituency_name)


class ListGeoWard(models.Model):
    """Model for Listing types details."""

    county_code = models.IntegerField()
    county_name = models.CharField(max_length=100)
    constituency_code = models.IntegerField()
    constituency_name = models.CharField(max_length=100)
    sub_county_name = models.CharField(max_length=100)
    ward_code = models.IntegerField()
    ward_name = models.CharField(max_length=100)
    timestamp_created = models.DateTimeField(default=timezone.now)
    is_void = models.BooleanField(default=False)

    class Meta:
        """Override table details."""

        db_table = 'list_geo_ward'
        verbose_name = 'List Geo - ward'
        verbose_name_plural = 'List Geo - wards'

    def __str__(self):
        """To be returned by admin actions."""
        return '%s - %s' % (self.ward_code, self.ward_name)
