from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME


def admin_login(request, extra_context=None):
    """Redirect to default login view which enforces auth policy."""
    next_page = request.get_full_path()
    next_url = next_page.split('=')[1] if '=' in next_page else next_page
    q = REDIRECT_FIELD_NAME + '=' + next_url
    return HttpResponseRedirect(reverse('login') + '?' + q)


admin.site.login = admin_login


def admin_logout(request, extra_context=None):
    """Redirect to default login page and not /admin area."""
    return HttpResponseRedirect(reverse('login'))


admin.site.logout = admin_logout
