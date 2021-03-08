from django.shortcuts import render
from django.forms.models import model_to_dict

from .forms import MasterListForm, SearchForm
from .functions import get_listings, get_services, get_geos


def home(request):
    """Home view."""
    try:
        listings = get_listings(request)
        counts = listings.count() if listings else 0
        return render(request, 'home.html', {'counts': counts})
    except Exception as e:
        raise e
    else:
        pass


def listings(request, lid=0):
    """Listings view."""
    try:
        results = get_listings(request)
        return render(request, 'listings.html',
                      {'results': results})
    except Exception as e:
        raise e
    else:
        pass


def search(request):
    """Search view."""
    try:
        form = SearchForm(data=request.GET)
        return render(request, 'search.html',
                      {'form': form})
    except Exception as e:
        raise e
    else:
        pass


def new_listing(request):
    """New Listing view."""
    try:
        form = MasterListForm()
        return render(request, 'new_listing.html', {'form': form})
    except Exception as e:
        raise e
    else:
        pass


def view_listing(request, lid):
    """View listing view."""
    try:
        record = get_listings(request, lid)
        services = get_services(request, lid)
        geos = get_geos(request, lid)
        return render(request, 'view_listing.html',
                      {'record': record, 'services': services,
                       'geos': geos})
    except Exception as e:
        raise e
    else:
        pass


def edit_listing(request, lid):
    """Edit Listing view."""
    try:
        record = get_listings(request, lid)
        data = model_to_dict(record)
        form = MasterListForm(data)
        return render(request, 'edit_listing.html', {'form': form})
    except Exception as e:
        raise e
    else:
        pass
