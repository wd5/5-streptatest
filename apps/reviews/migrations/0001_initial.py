# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Review'
        db.create_table('reviews_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reviewer_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('reviewer_post', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('review', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('apps.reviews.models.ImageField')(max_length=100, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('reviews', ['Review'])


    def backwards(self, orm):
        # Deleting model 'Review'
        db.delete_table('reviews_review')


    models = {
        'reviews.review': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Review'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('apps.reviews.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'review': ('django.db.models.fields.TextField', [], {}),
            'reviewer_post': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reviewer_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reviews']