"""
Definition of models.
"""

from django.db import models
# Create your models here.

class COGS(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    OrgDetail = models.CharField(max_length=256, blank=True, verbose_name='Org Detail')
    FinanceOwner = models.CharField(max_length=256, blank=True)
    QTDAct = models.IntegerField(blank=True)
    QTDFcst = models.IntegerField(blank=True)
    QTDVTF = models.IntegerField(blank=True)
    YTDAct = models.IntegerField(blank=True)
    YTDBud = models.IntegerField(blank=True)
    YTDVTB = models.IntegerField(blank=True)
    CurrentQtrOutlook = models.IntegerField(blank=True)
    ExecCommentary = models.TextField(blank=True)
    CloseCommentary = models.TextField(blank=True)
    ROCommentary = models.TextField(blank=True)
    def __str__(self):
        return self.OrgDetail

class OPEX(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    OrgDetail = models.CharField(max_length=256, blank=True)
    FinanceOwner = models.CharField(max_length=256, blank=True)
    QTDAct = models.IntegerField(blank=True)
    QTDFcst = models.IntegerField(blank=True)
    QTDVTF = models.IntegerField(blank=True)
    YTDAct = models.IntegerField(blank=True)
    YTDBud = models.IntegerField(blank=True)
    YTDVTB = models.IntegerField(blank=True)
    CurrentQtrOutlook = models.IntegerField(blank=True)
    ExecCommentary = models.TextField(blank=True)
    CloseCommentary = models.TextField(blank=True)
    ROCommentary = models.TextField(blank=True)
    def __str__(self):
        return self.OrgDetail