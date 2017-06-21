import django_tables2 as tables
from django_tables2.utils import A 
from .models import *

class COGSTable(tables.Table):
    ID = tables.Column(visible=False)
    OrgDetail = tables.LinkColumn('edit_cogs', args=[A('OrgDetail')])
    class Meta:
        model = COGS
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class COGSdetailTable(tables.Table):
    ID = tables.Column(visible=False)
    CurrentQtrOutlook = tables.Column(visible=False)
    ExecCommentary = tables.Column(visible=False)
    CloseCommentary = tables.Column(visible=False)
    ROCommentary = tables.Column(visible=False)
    class Meta:
        model = COGS
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class OPEXTable(tables.Table):
    ID = tables.Column(visible=False)
    OrgDetail = tables.LinkColumn('edit_opex', args=[A('OrgDetail')])
    class Meta:
        model = OPEX
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class OPEXdetailTable(tables.Table):
    ID = tables.Column(visible=False)
    CurrentQtrOutlook = tables.Column(visible=False)
    ExecCommentary = tables.Column(visible=False)
    CloseCommentary = tables.Column(visible=False)
    ROCommentary = tables.Column(visible=False)
    class Meta:
        model = COGS
        attrs = {'class': 'table table-bordered table-striped table-hover'}
