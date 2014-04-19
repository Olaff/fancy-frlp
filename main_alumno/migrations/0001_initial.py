# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carrera'
        db.create_table(u'main_alumno_carrera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tit_intermedio', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('planestudio', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank='True')),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from=('nombre',), overwrite=False)),
        ))
        db.send_create_signal(u'main_alumno', ['Carrera'])

        # Adding model 'Comision'
        db.create_table(u'main_alumno_comision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('turno', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_alumno.Carrera'])),
            ('catedra', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catedras', to=orm['main_alumno.Catedra'])),
        ))
        db.send_create_signal(u'main_alumno', ['Comision'])

        # Adding model 'Catedra'
        db.create_table(u'main_alumno_catedra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('jefe_catedra', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jtp', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from=('nombre',), overwrite=False)),
            ('electiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['main_alumno.Carrera'])),
            ('sylabus', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'main_alumno', ['Catedra'])

        # Adding model 'Alumno'
        db.create_table(u'main_alumno_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('domicilio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('localidad', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('legajo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from=('apellido',), overwrite=False)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_alumno.Carrera'])),
        ))
        db.send_create_signal(u'main_alumno', ['Alumno'])

        # Adding model 'Cursada'
        db.create_table(u'main_alumno_cursada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'main_alumno', ['Cursada'])


    def backwards(self, orm):
        # Deleting model 'Carrera'
        db.delete_table(u'main_alumno_carrera')

        # Deleting model 'Comision'
        db.delete_table(u'main_alumno_comision')

        # Deleting model 'Catedra'
        db.delete_table(u'main_alumno_catedra')

        # Deleting model 'Alumno'
        db.delete_table(u'main_alumno_alumno')

        # Deleting model 'Cursada'
        db.delete_table(u'main_alumno_cursada')


    models = {
        u'main_alumno.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main_alumno.Carrera']"}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'domicilio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legajo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'localidad': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('apellido',)", 'overwrite': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main_alumno.carrera': {
            'Meta': {'object_name': 'Carrera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'planestudio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': "'True'"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('nombre',)", 'overwrite': 'False'}),
            'tit_intermedio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'main_alumno.catedra': {
            'Meta': {'ordering': "['-nombre']", 'object_name': 'Catedra'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['main_alumno.Carrera']"}),
            'electiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe_catedra': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jtp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('nombre',)", 'overwrite': 'False'}),
            'sylabus': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'main_alumno.comision': {
            'Meta': {'object_name': 'Comision'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main_alumno.Carrera']"}),
            'catedra': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catedras'", 'to': u"orm['main_alumno.Catedra']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'turno': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'main_alumno.cursada': {
            'Meta': {'object_name': 'Cursada'},
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main_alumno']