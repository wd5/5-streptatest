# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailingAddress'
        db.create_table('messages_mailingaddress', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('messages', ['MailingAddress'])

        # Adding model 'Order'
        db.create_table('messages_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('product_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('allow_mailings', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('payment_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cash_pay_sum', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='new', max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('messages', ['Order'])

        # Adding model 'PartnershipOffer'
        db.create_table('messages_partnershipoffer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('offer_author_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('allow_mailings', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('state', self.gf('django.db.models.fields.CharField')(default='new', max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('messages', ['PartnershipOffer'])

        # Adding model 'EntryInSchool'
        db.create_table('messages_entryinschool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('allow_mailings', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('state', self.gf('django.db.models.fields.CharField')(default='new', max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('messages', ['EntryInSchool'])

        # Adding model 'Question'
        db.create_table('messages_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('allow_mailings', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('send_answer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('state', self.gf('django.db.models.fields.CharField')(default='new', max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 18, 0, 0))),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('messages', ['Question'])


    def backwards(self, orm):
        # Deleting model 'MailingAddress'
        db.delete_table('messages_mailingaddress')

        # Deleting model 'Order'
        db.delete_table('messages_order')

        # Deleting model 'PartnershipOffer'
        db.delete_table('messages_partnershipoffer')

        # Deleting model 'EntryInSchool'
        db.delete_table('messages_entryinschool')

        # Deleting model 'Question'
        db.delete_table('messages_question')


    models = {
        'messages.entryinschool': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'EntryInSchool'},
            'allow_mailings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'messages.mailingaddress': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'MailingAddress'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'messages.order': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Order'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'allow_mailings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cash_pay_sum': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'product_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'messages.partnershipoffer': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'PartnershipOffer'},
            'allow_mailings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'offer_author_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'messages.question': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Question'},
            'allow_mailings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'send_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'products.product': {
            'Meta': {'ordering': "['-created_at', '-id']", 'object_name': 'Product'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'test_items_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 18, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['messages']