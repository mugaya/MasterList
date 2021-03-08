from rest_framework import serializers
from ml_main.models import MasterList
from ml_setup.models import ListGeneral


class SearchSerializer(serializers.ModelSerializer):
    """Search serializer."""

    class Meta:
        model = MasterList
        fields = ('code', 'name')
        read_only_fields = ['code']


class SettingsSerializer(serializers.HyperlinkedModelSerializer):
    """Settings serializer."""

    class Meta:
        """Overrride parameters."""

        model = ListGeneral
        fields = ('item_id', 'item_description', 'the_order')


class FacilitySerializer(serializers.ModelSerializer):
    """Search serializer."""

    class Meta:
        model = MasterList
        fields = ('code', 'name', 'official_name', 'reg_number', 'keph_level',
                  'beds', 'cots', 'is_operational', 'facility_type',
                  'owner_type', 'approved')
        read_only_fields = ['code']
