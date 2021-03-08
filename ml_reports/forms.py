from django import forms


class ReportForm(forms.Form):
    """Reports details form."""

    date_from = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker',
                   'placeholder': 'YYYY-MM-DD',
                   'id': 'date_from'}))

    date_to = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker',
                   'placeholder': 'YYYY-MM-DD',
                   'id': 'date_to'}))
