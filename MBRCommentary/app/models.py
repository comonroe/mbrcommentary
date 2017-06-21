"""
Definition of models.
"""

from django.db import models
# Create your models here.

class COGS(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    OrgDetail = models.CharField(max_length=256, blank=True, verbose_name='Org Detail')
    FinanceOwner = models.CharField(max_length=256, blank=True, verbose_name='Finance Owner')
    QTDAct = models.IntegerField(blank=True, verbose_name='QTD Act')
    QTDFcst = models.IntegerField(blank=True, verbose_name='QTD Fcst')
    QTDVTF = models.IntegerField(blank=True, verbose_name='QTD VTF')
    YTDAct = models.IntegerField(blank=True, verbose_name='YTD Act')
    YTDBud = models.IntegerField(blank=True, verbose_name= 'YTD Bud')
    YTDVTB = models.IntegerField(blank=True, verbose_name='YTD VTB')
    CurrentQtrOutlook = models.IntegerField(blank=True, verbose_name='Current Qtr Outlook')
    ExecCommentary = models.TextField(blank=True, verbose_name='Exec Commentary')
    CloseCommentary = models.TextField(blank=True, verbose_name='Close Commentary')
    ROCommentary = models.TextField(blank=True, verbose_name='RO Commentary')
    def __str__(self):
        return self.OrgDetail

class OPEX(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    OrgDetail = models.CharField(max_length=256, blank=True, verbose_name='Org Detail')
    FinanceOwner = models.CharField(max_length=256, blank=True, verbose_name='Finance Owner')
    QTDAct = models.IntegerField(blank=True, verbose_name='QTD Act')
    QTDFcst = models.IntegerField(blank=True, verbose_name='QTD Fcst')
    QTDVTF = models.IntegerField(blank=True, verbose_name='QTD VTF')
    YTDAct = models.IntegerField(blank=True, verbose_name='YTD Act')
    YTDBud = models.IntegerField(blank=True, verbose_name= 'YTD Bud')
    YTDVTB = models.IntegerField(blank=True, verbose_name='YTD VTB')
    CurrentQtrOutlook = models.IntegerField(blank=True, verbose_name='Current Qtr Outlook')
    ExecCommentary = models.TextField(blank=True, verbose_name='Exec Commentary')
    CloseCommentary = models.TextField(blank=True, verbose_name='Close Commentary')
    ROCommentary = models.TextField(blank=True, verbose_name='RO Commentary')
    def __str__(self):
        return self.OrgDetail