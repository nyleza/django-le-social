from django import forms
from django.utils.translation import gettext_lazy as _


class OpenIDForm(forms.Form):
    openid_url = forms.URLField(label=_('OpenID URL'))
