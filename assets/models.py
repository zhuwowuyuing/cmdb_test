#coding=utf8

from django.db import models

# Create your models here.

class Device(models.Model):
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号', max_length=60, primary_key=True)
    asset_old       = models.CharField('旧资产编号', max_length=60, blank=True)
    district        = models.CharField('所在地区', max_length=60)
    company         = models.CharField('账上所属公司', max_length=60)
    type            = models.CharField('类别', max_length=60)
    subtype         = models.CharField('子类别', max_length=60)
    manufacturer    = models.CharField('品牌', max_length=60, blank=True)
    model           = models.CharField('型号', max_length=100, blank=True)
    serialno    = models.CharField('序列号', max_length=100, blank=True)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.asset, self.type, self.subtype, self.manufacturer, self.model)

class Server(models.Model):
    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号', max_length=60, primary_key=True)
    size            = models.CharField('尺寸', max_length=60, blank=True)
    cpu             = models.CharField('CPU', max_length=200, blank=True)
    harddisk        = models.CharField('硬盘', max_length=200, blank=True)
    ram             = models.CharField('内存', max_length=200, blank=True)
    os              = models.CharField('操作系统',max_length=200, blank=True)

    def __unicode__(self):
        return u'%s' % (self.asset)

class UsingInfo(models.Model):
    class Meta:
        verbose_name = '使用信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号',max_length=60, primary_key=True)
    status          = models.CharField('使用状态',max_length=60, blank=True)
    building        = models.CharField('机房(所处位置)',max_length=60, blank=True)
    location        = models.CharField('机柜',max_length=60, blank=True)
    consignee       = models.CharField('托管编号',max_length=60, blank=True)
    hostname        = models.CharField('主机名',max_length=60, blank=True)
    dept            = models.CharField('使用部门',max_length=60, blank=True)
    business        = models.CharField('业务系统',max_length=60, blank=True)
    ownername       = models.CharField('领用人',max_length=60, blank=True)
    warehousedate   = models.DateField('入库时间', blank=True)
    receivedate     = models.DateField('领用时间', blank=True)
    warrantyexpirationdate = models.DateField('保修至', blank=True)
    scrapDate       = models.DateField('报废时间', blank=True)
    changeInfo      = models.TextField('变更信息',max_length=4000, blank=True)

    def __unicode__(self):
        return u'%s' % (self.asset)

class Finance(models.Model):
    class Meta:
        verbose_name = '财务信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号',max_length=60, primary_key=True)
    purchase_date   = models.DateField('采购时间', blank=True)
    purchase_cost   = models.FloatField('采购价格',max_length=60, blank=True)
    accounting_date = models.DateField('入账时间', blank=True)
    account_cost    = models.FloatField('入账价格',max_length=60, blank=True)
    vendor          = models.CharField('供应商',max_length=200, blank=True)
    vendor_contacts = models.TextField('供应商联系方式',max_length=2000, blank=True)
    accounting_info = models.TextField('入账情况',max_length=2000, blank=True)

    def __unicode__(self):
        return u'%s' % (self.asset)

class ManInfo(models.Model):
    class Meta:
        verbose_name = '管理信息'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号',max_length=60, unique=True)
    administrator   = models.CharField('实物管理员',max_length=60, blank=True)
    order_list      = models.TextField('相关单据',max_length=2000, blank=True)
    comment         = models.TextField('备注',max_length=2000, blank=True)

    def __unicode__(self):
        return u'%s' % (self.asset)


class Status(models.Model):
    class Meta:
        verbose_name = '使用状态'
        verbose_name_plural = verbose_name

    status          = models.CharField('使用状态',max_length=60)

    def __unicode__(self):
        return u'%s' % (self.status)

class Servers(models.Model):
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = verbose_name
        ordering = ['asset']

    asset           = models.CharField('资产编号', max_length=60, primary_key=True)
    asset_old       = models.CharField('旧资产编号', max_length=60, blank=True)
    district        = models.CharField('所在地区', max_length=60)
    company         = models.CharField('账上所属公司', max_length=60)
    type            = models.CharField('类别', max_length=60)
    subtype         = models.CharField('子类别', max_length=60)
    manufacturer    = models.CharField('品牌', max_length=60, blank=True)
    model           = models.CharField('型号', max_length=100, blank=True)
    serialno    = models.CharField('序列号', max_length=100, blank=True)
    size            = models.CharField('尺寸', max_length=60, blank=True)
    cpu             = models.CharField('CPU', max_length=200, blank=True)
    harddisk        = models.CharField('硬盘', max_length=200, blank=True)
    ram             = models.CharField('内存', max_length=200, blank=True)
    os              = models.CharField('操作系统',max_length=200, blank=True)
    status          = models.ForeignKey(Status)
    building        = models.CharField('机房(所处位置)',max_length=60, blank=True)
    location        = models.CharField('机柜',max_length=60, blank=True)
    consignee       = models.CharField('托管编号',max_length=60, blank=True)
    hostname        = models.CharField('主机名',max_length=60, blank=True)
    dept            = models.CharField('使用部门',max_length=60, blank=True)
    business        = models.CharField('业务系统',max_length=60, blank=True)
    ownername       = models.CharField('领用人',max_length=60, blank=True)
    warehousedate   = models.DateField('入库时间', blank=True)
    receivedate     = models.DateField('领用时间', blank=True)
    warrantyexpirationdate = models.DateField('保修至', blank=True)
    scrapDate       = models.DateField('报废时间', blank=True)
    changeInfo      = models.TextField('变更信息',max_length=4000, blank=True)
    purchase_date   = models.DateField('采购时间', blank=True)
    purchase_cost   = models.FloatField('采购价格',max_length=60, blank=True)
    accounting_date = models.DateField('入账时间', blank=True)
    account_cost    = models.FloatField('入账价格',max_length=60, blank=True)
    vendor          = models.CharField('供应商',max_length=200, blank=True)
    vendor_contacts = models.TextField('供应商联系方式',max_length=2000, blank=True)
    accounting_info = models.TextField('入账情况',max_length=2000, blank=True)
    administrator   = models.CharField('实物管理员',max_length=60, blank=True)
    order_list      = models.TextField('相关单据',max_length=2000, blank=True)
    comment         = models.TextField('备注',max_length=2000, blank=True)

    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.asset, self.type, self.subtype, self.manufacturer, self.model)