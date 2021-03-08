from ml_main.models import MasterList


def get_report(request, date_from, date_to):
    """Method to get report."""
    try:
        results = MasterList.objects.filter(is_void=False)
        if date_from:
            results = results.filter(timestamp_created__gte=date_from)
        if date_to:
            results = results.filter(timestamp_created__lte=date_to)
    except Exception as e:
        raise e
    else:
        return results
