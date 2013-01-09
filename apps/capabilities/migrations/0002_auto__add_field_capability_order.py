# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Capability.order'
        db.add_column('capabilities_capability', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Capability.order'
        db.delete_column('capabilities_capability', 'order')


    models = {
        'capabilities.capability': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Capability'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 9, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('apps.capabilities.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'show_on_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 9, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['capabilities']