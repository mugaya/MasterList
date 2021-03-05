from django.shortcuts import render
from .forms import MasterListForm
from .functions import handle_search


def home(request):
    """Home view."""
    try:
        return render(request, 'home.html')
    except Exception as e:
        raise e
    else:
        pass


def listings(request, lid=0):
    """Home view."""
    try:
        return render(request, 'listings.html')
    except Exception as e:
        raise e
    else:
        pass


def search(request):
    """Home view."""
    try:
        form = MasterListForm()
        results = handle_search(request)
        return render(request, 'search.html',
                      {'form': form, 'results': results})
    except Exception as e:
        raise e
    else:
        pass
