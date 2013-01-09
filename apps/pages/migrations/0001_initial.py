# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table('pages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_add', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, on_delete=models.SET_NULL, to=orm['pages.Page'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_at_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_at_footer_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('template', self.gf('django.db.models.fields.CharField')(default=u'default.html', max_length=100)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('pages', ['Page'])

        # Adding model 'PageDoc'
        db.create_table('pages_pagedoc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Page'])),
        ))
        db.send_create_signal('pages', ['PageDoc'])

        # Adding model 'PagePic'
        db.create_table('pages_pagepic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=10)),
            ('file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.Page'])),
        ))
        db.send_create_signal('pages', ['PagePic'])

        # Adding model 'MetaData'
        db.create_table('pages_metadata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('pages', ['MetaData'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table('pages_page')

        # Deleting model 'PageDoc'
        db.delete_table('pages_pagedoc')

        # Deleting model 'PagePic'
        db.delete_table('pages_pagepic')

        # Deleting model 'MetaData'
        db.delete_table('pages_metadata')


    models = {
        'pages.metadata': {
            'Meta': {'object_name': 'MetaData'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date_add': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_at_footer_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_at_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['pages.Page']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u'default.html'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'pages.pagedoc': {
            'Meta': {'object_name': 'PageDoc'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'pages.pagepic': {
            'Meta': {'object_name': 'PagePic'},
            'file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['pages']