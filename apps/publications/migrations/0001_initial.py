# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table('publications_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('where_published', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('publications', ['Publication'])

        # Adding model 'NewsCategory'
        db.create_table('publications_newscategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('publications', ['NewsCategory'])

        # Adding model 'News'
        db.create_table('publications_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publications.NewsCategory'], null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('publications', ['News'])

        # Adding model 'Article'
        db.create_table('publications_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0), auto_now=True, blank=True)),
        ))
        db.send_create_signal('publications', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table('publications_publication')

        # Deleting model 'NewsCategory'
        db.delete_table('publications_newscategory')

        # Deleting model 'News'
        db.delete_table('publications_news')

        # Deleting model 'Article'
        db.delete_table('publications_article')


    models = {
        'publications.article': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Article'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'publications.news': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'News'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.NewsCategory']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'publications.newscategory': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'NewsCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        'publications.publication': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Publication'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'where_published': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['publications']