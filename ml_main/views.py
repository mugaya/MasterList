from django.shortcuts import render


def home(request):
    """Home view."""
    try:
        return render(request, 'home.html')
    except Exception as e:
        raise e
    else:
        pass


def listings(request):
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
        return render(request, 'search.html')
    except Exception as e:
        raise e
    else:
        pass
