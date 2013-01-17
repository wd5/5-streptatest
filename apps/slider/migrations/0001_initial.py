# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table('slider_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('apps.slider.models.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('slider', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table('slider_photo')


    models = {
        'slider.photo': {
            'Meta': {'ordering': "['-order']", 'object_name': 'Photo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('apps.slider.models.ImageField', [], {'max_length': '100'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['slider']