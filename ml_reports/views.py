from django.shortcuts import render
from .forms import ReportForm
from .functions import get_report


def home(request):
    """Home view."""
    try:
        results = {}
        form = ReportForm()
        if request.method == 'POST':
            form = ReportForm(data=request.POST)
            date_from = request.POST.get('date_from')
            date_to = request.POST.get('date_to')
            results = get_report(request, date_from, date_to)
        return render(request, 'reports.html',
                      {'form': form, 'results': results})
    except Exception as e:
        raise e
    else:
        pass


def facilities(request):
    """Home view."""
    try:
        form = ReportForm()
        return render(request, 'reports.html', {'form': form})
    except Exception as e:
        raise e
    else:
        pass
