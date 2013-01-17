# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Capability'
        db.create_table('capabilities_capability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('show_on_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('apps.capabilities.models.ImageField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('capabilities', ['Capability'])


    def backwards(self, orm):
        # Deleting model 'Capability'
        db.delete_table('capabilities_capability')


    models = {
        'capabilities.capability': {
            'Meta': {'ordering': "['-order', '-created_at', '-id']", 'object_name': 'Capability'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('apps.capabilities.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'show_on_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['capabilities']