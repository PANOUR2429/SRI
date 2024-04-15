from django.db import models


# Create your models here.
class DomainWeight(models.Model):
    building_type = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    dw_cr1 = models.FloatField()
    dw_cr2 = models.FloatField()
    dw_cr3 = models.FloatField()
    dw_cr4 = models.FloatField()
    dw_cr5 = models.FloatField()
    dw_cr6 = models.FloatField()
    dw_cr7 = models.FloatField()


class ImpactWeight(models.Model):
    building_type = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    imp_cr1 = models.FloatField()
    imp_cr2 = models.FloatField()
    imp_cr3 = models.FloatField()
    imp_cr4 = models.FloatField()
    imp_cr5 = models.FloatField()
    imp_cr6 = models.FloatField()
    imp_cr7 = models.FloatField()


class Levels(models.Model):
    code = models.CharField(max_length=200)
    level_desc = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    score_cr1 = models.FloatField()
    score_cr2 = models.FloatField()
    score_cr3 = models.FloatField()
    score_cr4 = models.FloatField()
    score_cr5 = models.FloatField()
    score_cr6 = models.FloatField()
    score_cr7 = models.FloatField()
    level = models.FloatField()
    mandatory = models.FloatField()
    domain = models.CharField(max_length=200)


class Services(models.Model):
    domain = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    service_group = models.CharField(max_length=200)
    service_desc = models.CharField(max_length=200)
