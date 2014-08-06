# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ModLog.conment'
        db.add_column(u'assets_modlog', 'conment',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ModLog.conment'
        db.delete_column(u'assets_modlog', 'conment')


    models = {
        u'assets.modlog': {
            'Meta': {'ordering': "['asset']", 'object_name': 'ModLog'},
            'asset': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'conment': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moduser': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'mtime': ('django.db.models.fields.DateTimeField', [], {}),
            'newvalue': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'oldvalue': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'typename': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'assets.servers': {
            'Meta': {'ordering': "['asset']", 'object_name': 'Servers'},
            'account_cost': ('django.db.models.fields.FloatField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'accounting_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'accounting_info': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'administrator': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'asset': ('django.db.models.fields.CharField', [], {'max_length': '60', 'primary_key': 'True'}),
            'asset_old': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'business': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'changeInfo': ('django.db.models.fields.TextField', [], {'max_length': '4000', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'consignee': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'harddisk': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'order_list': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'ownername': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'purchase_cost': ('django.db.models.fields.FloatField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'receivedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'scrapDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'serialno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['assets.Status']"}),
            'subtype': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'vendor_contacts': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'warehousedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'warrantyexpirationdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'assets.status': {
            'Meta': {'object_name': 'Status'},
            'exclusive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60', 'primary_key': 'True'})
        }
    }

    complete_apps = ['assets']