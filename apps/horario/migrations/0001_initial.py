# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Horario'
        db.create_table(u'horario_horario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catedra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catedra.Catedra'])),
            ('comision', self.gf('django.db.models.fields.related.ForeignKey')(related_name='horarios', to=orm['comision.Comision'])),
            ('prof_t', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('prof_p', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('ayudantes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('dia_t', self.gf('django.db.models.fields.CharField')(default='', max_length=10, null=True)),
            ('dia_p', self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True)),
            ('hora_inicio_t', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('hora_fin_t', self.gf('django.db.models.fields.TimeField')(null=True)),
            ('hora_inicio_p', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('hora_fin_p', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'horario', ['Horario'])


    def backwards(self, orm):
        # Deleting model 'Horario'
        db.delete_table(u'horario_horario')


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
        u'catedra.catedra': {
            'Meta': {'ordering': "['-nombre']", 'object_name': 'Catedra'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': u"orm['carrera.Carrera']"}),
            'comisiones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'catedras'", 'symmetrical': 'False', 'through': u"orm['horario.Horario']", 'to': u"orm['comision.Comision']"}),
            'electiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jefe_catedra': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jtp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sitio': ('django.db.models.fields.URLField', [], {'max_length': '100'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "('nombre',)", 'overwrite': 'False'}),
            'sylabus': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'comision.comision': {
            'Meta': {'object_name': 'Comision'},
            'carrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carrera.Carrera']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'turno': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'horario.horario': {
            'Meta': {'object_name': 'Horario'},
            'ayudantes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'catedra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catedra.Catedra']"}),
            'comision': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'horarios'", 'to': u"orm['comision.Comision']"}),
            'dia_p': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'dia_t': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True'}),
            'hora_fin_p': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hora_fin_t': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'hora_inicio_p': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hora_inicio_t': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prof_p': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'prof_t': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['horario']