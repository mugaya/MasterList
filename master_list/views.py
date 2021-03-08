from django.shortcuts import render


def handler_400(request, exception):
    """Some default page for Bad request error page."""
    try:
        return render(request, 'error.html', {'status': 400})
    except Exception as e:
        raise e


def handler_404(request, exception):
    """Some default page for the Page not Found."""
    try:
        return render(request, 'error.html', {'status': 404})
    except Exception as e:
        raise e


def handler_500(request):
    """Some default page for Server Errors."""
    try:
        return render(request, 'error.html', {'status': 500})
    except Exception as e:
        raise e


def csrf_failure(request, reason):
    """Some default page for CSRF error."""
    try:
        return render(request, 'error.html', {'status': 500, 'reason': reason})
    except Exception as e:
        raise e
