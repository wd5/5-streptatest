# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.email'
        db.add_column('reviews_review', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Review.phone_code'
        db.add_column('reviews_review', 'phone_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Review.phone'
        db.add_column('reviews_review', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Review.email'
        db.delete_column('reviews_review', 'email')

        # Deleting field 'Review.phone_code'
        db.delete_column('reviews_review', 'phone_code')

        # Deleting field 'Review.phone'
        db.delete_column('reviews_review', 'phone')


    models = {
        'reviews.review': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Review'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 25, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('apps.reviews.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'review': ('django.db.models.fields.TextField', [], {}),
            'reviewer_post': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reviewer_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 25, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reviews']