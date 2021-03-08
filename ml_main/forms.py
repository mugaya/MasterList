from django import forms
from .functions import get_list, get_county_list

keph_levels = (('', 'Select Level'), (2, 'Level 2'),
               (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5'))

approval_status_list = get_list('regulation_status_id', 'Please Select')
facility_type_list = ()
owner_type_list = ()
service_category_list = ()
county_list = get_county_list()
yesno_ids = get_list('yes_no_id')


class MasterListForm(forms.Form):
    """Master Listing details form."""

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Name',
                   'id': 'name'}))

    official_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Official Name',
                   'id': 'official_name'}))

    keph_level = forms.ChoiceField(
        choices=keph_levels,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'keph_level'}))

    reg_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Reg. Number',
                   'id': 'reg_number'}))

    approval_status = forms.ChoiceField(
        choices=approval_status_list,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'approval_status'}))

    facility_type = forms.ChoiceField(
        choices=facility_type_list,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'facility_type'}))

    owner_type = forms.ChoiceField(
        choices=owner_type_list,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'owner_type'}))

    is_operational = forms.ChoiceField(
        choices=yesno_ids,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'is_operational'}))

    approved = forms.ChoiceField(
        choices=yesno_ids,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'approved'}))

    county = forms.ChoiceField(
        choices=county_list,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'county'}))

    sub_county = forms.ChoiceField(
        choices=(),
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'sub_county'}))

    constituency = forms.ChoiceField(
        choices=(),
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'constituency'}))

    ward = forms.ChoiceField(
        choices=(),
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'ward'}))

    category = forms.ChoiceField(
        choices=service_category_list,
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'category'}))

    service = forms.ChoiceField(
        choices=(),
        initial='',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'service'}))


class SearchForm(forms.Form):
    """Master Listing search form."""

    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Name',
                   'id': 'name'}))

    approval_status = forms.ChoiceField(
        choices=approval_status_list,
        initial='',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'approval_status'}))
