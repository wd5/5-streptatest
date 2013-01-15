# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Lab.phone'
        db.add_column('places_lab', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'Drugstore.phone'
        db.add_column('places_drugstore', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'Clinic.phone'
        db.add_column('places_clinic', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Lab.phone'
        db.delete_column('places_lab', 'phone')

        # Deleting field 'Drugstore.phone'
        db.delete_column('places_drugstore', 'phone')

        # Deleting field 'Clinic.phone'
        db.delete_column('places_clinic', 'phone')


    models = {
        'places.branch': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Branch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.City']"}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'places.city': {
            'Meta': {'ordering': "['id']", 'object_name': 'City'},
            'coordinates_center': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {})
        },
        'places.clinic': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Clinic'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.City']"}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'places.drugstore': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Drugstore'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.City']"}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'places.lab': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Lab'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.City']"}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['places']