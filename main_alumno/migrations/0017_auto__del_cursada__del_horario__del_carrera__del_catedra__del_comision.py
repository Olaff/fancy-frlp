# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Cursada'
        db.delete_table(u'main_alumno_cursada')

        # Deleting model 'Horario'
        db.delete_table(u'main_alumno_horario')

        # Deleting model 'Carrera'
        db.delete_table(u'main_alumno_carrera')

        # Deleting model 'Catedra'
        db.delete_table(u'main_alumno_catedra')

        # Deleting model 'Comision'
        db.delete_table(u'main_alumno_comision')


        # Changing field 'Alumno.carrera'
        db.alter_column(u'main_alumno_alumno', 'carrera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carrera.Carrera']))

    def backwards(self, orm):
        # Adding model 'Cursada'
        db.create_table(u'main_alumno_cursada', (
            ('estado', self.gf('django.db.models.fields.CharField')(default='', max_length=20)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main_alumno', ['Cursada'])

        # Adding model 'Horario'
        db.create_table(u'main_alumno_horario', (
            ('dia_p', self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True)),
            ('dia_t', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True)),
            ('comision', self.gf('django.db.models.fields.related.ForeignKey')(related_name='horarios', to=orm['main_alumno.Comision'])),
            ('catedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_alumno.Catedra'])),
            ('prof_p', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora_fin_p', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('hora_fin_t', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('hora_inicio_t', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('ayudantes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('hora_inicio_p', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('prof_t', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'main_alumno', ['Horario'])

        # Adding model 'Carrera'
        db.create_table(u'main_alumno_carrera', (
            ('planestudio', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank='True')),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from=('nombre',), allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, overwrite=False)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tit_intermedio', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'main_alumno', ['Carrera'])

        # Adding model 'Catedra'
        db.create_table(u'main_alumno_catedra', (
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from=('nombre',), allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, overwrite=False)),
            ('sylabus', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('sitio', self.gf('django.db.models.fields.URLField')(max_length=100)),
            ('jtp', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('electiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['main_alumno.Carrera'])),
            ('jefe_catedra', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main_alumno', ['Catedra'])

        # Adding model 'Comision'
        db.create_table(u'main_alumno_comision', (
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('numero', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('turno', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_alumno.Carrera'])),
        ))
        db.send_create_signal(u'main_alumno', ['Comision'])


        # Changing field 'Alumno.carrera'
        db.alter_column(u'main_alumno_alumno', 'carrera_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main_alumno.Carrera']))

    models = {
        u'carrera.carrera': {
            'Meta': {'object_name': 'Carrera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'planestudio': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': "'True'"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('nombre',)", 'overwrite': 'False'}),
            'tit_intermedio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'main_alumno.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carrera.Carrera']"}),
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
        }
    }

    complete_apps = ['main_alumno']