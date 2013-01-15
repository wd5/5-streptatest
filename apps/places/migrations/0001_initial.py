# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('places_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('coordinates_center', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('zoom', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('places', ['City'])

        # Adding model 'Clinic'
        db.create_table('places_clinic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.City'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('places', ['Clinic'])

        # Adding model 'Drugstore'
        db.create_table('places_drugstore', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.City'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('places', ['Drugstore'])

        # Adding model 'Lab'
        db.create_table('places_lab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.City'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('places', ['Lab'])

        # Adding model 'Branch'
        db.create_table('places_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.City'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 14, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('places', ['Branch'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('places_city')

        # Deleting model 'Clinic'
        db.delete_table('places_clinic')

        # Deleting model 'Drugstore'
        db.delete_table('places_drugstore')

        # Deleting model 'Lab'
        db.delete_table('places_lab')

        # Deleting model 'Branch'
        db.delete_table('places_branch')


    models = {
        'places.branch': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Branch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.City']"}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['places']