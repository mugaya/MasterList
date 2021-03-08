import csv
import time
from django.http import HttpResponse


def dump_to_csv(modeladmin, request, qs):
    """
    These takes in a Django queryset and spits out a CSV file.

    Generic method for any queryset
    """
    model = qs.model
    file_id = 'ML_%s_%d' % (model.__name__, int(time.time()))
    file_name = 'attachment; filename=%s.csv' % (file_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = file_name
    writer = csv.writer(response, csv.excel)

    headers = []
    for field in model._meta.fields:
        if field.name != 'password':
            headers.append(field.name)
    writer.writerow(headers)

    for obj in qs:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == bytes:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)
    return response


dump_to_csv.short_description = u"Dump to CSV"
