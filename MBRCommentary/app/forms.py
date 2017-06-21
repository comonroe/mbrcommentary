"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import * 

class COGSForm(forms.ModelForm):
    class Meta:
        model = COGS
        fields = ('CurrentQtrOutlook', 'ExecCommentary', 'CloseCommentary', 'ROCommentary')

class OPEXForm(forms.ModelForm):
    class Meta:
        model = COGS
        fields = ('CurrentQtrOutlook', 'ExecCommentary', 'CloseCommentary', 'ROCommentary')


