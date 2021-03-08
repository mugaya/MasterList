from django.db.models import Q
from django.core.cache import cache
from ml_setup.models import ListGeneral
from .models import MasterList, MasterListService, MasterListGeo
from ml_setup.models import ListGeoCounty


def get_listings(request, lid=None):
    """Method to pick all listings."""
    try:
        if lid:
            listings = MasterList.objects.get(id=lid)
        else:
            listings = MasterList.objects.all()
    except Exception as e:
        raise e
    else:
        return listings


def get_services(request, lid):
    """Method to pick all listings services."""
    try:
        services = MasterListService.objects.filter(master_list_id=lid)
    except Exception as e:
        raise e
    else:
        return services


def get_geos(request, lid):
    """Method to pick all listings services."""
    try:
        geos = MasterListGeo.objects.get(master_list_id=lid)
    except Exception as e:
        raise e
    else:
        return geos


def get_list(field_name=[], default_txt=False, category=False):
    my_list = ()
    try:
        cat_id = '1' if category else '0'
        cache_key = 'set_up_list_%s_%s' % (field_name, cat_id)
        cache_list = cache.get(cache_key)
        if cache_list:
            v_list = cache_list
        else:
            v_list = get_general_list([field_name], category)
            cache.set(cache_key, v_list, 300)
        my_list = v_list.values_list(
            'item_id', 'item_description').order_by('the_order')
        if default_txt:
            initial_list = ('', default_txt)
            final_list = [initial_list] + list(my_list)
            return final_list
    except Exception as e:
        error = 'Error getting list - %s' % (str(e))
        print(error)
        return my_list
    else:
        return my_list


def get_general_list(field_names=[], item_category=False):
    '''
    Get list general filtered by field_name
    '''
    try:
        queryset = ListGeneral.objects.filter(is_active=True).order_by(
            'the_order', 'id')
        if len(field_names) > 1:
            q_filter = Q()
            for field_name in field_names:
                q_filter |= Q(**{"field_name": field_name})
            queryset = queryset.filter(q_filter)
        else:
            queryset = queryset.filter(
                field_name=field_names[0]).order_by('the_order')
        if item_category:
            queryset = queryset.filter(
                item_category=item_category).order_by('the_order')
    except Exception as e:
        error = 'Error getting whole list - %s' % (str(e))
        print(error)
        return None
    else:
        return queryset


def get_counties():
    """Get all Organisational units."""
    try:
        org_units = ListGeoCounty.objects.all().values(
            'id', 'county_name', 'county_code')
    except Exception as e:
        error = "Error getting counties - %s" % (str(e))
        print(error)
        return None
    else:
        return org_units


def get_county_list(initial="Select County"):
    """Get all Organisational units for drop down."""
    try:
        unit_detail = {'': initial} if initial else {}
        org_units = get_counties()
        for unit in org_units:
            unit_code = str(unit['county_code']).zfill(3)
            unit_name = unit['county_name']
            unit_detail[unit['id']] = '%s - %s' % (unit_code, unit_name)
    except Exception as e:
        print("error - %s" % (str(e)))
        return {}
    else:
        return unit_detail.items()
