# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field comisiones on 'Catedra'
        db.delete_table(db.shorten_name(u'main_alumno_catedra_comisiones'))


    def backwards(self, orm):
        # Adding M2M table for field comisiones on 'Catedra'
        m2m_table_name = db.shorten_name(u'main_alumno_catedra_comisiones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('catedra', models.ForeignKey(orm[u'main_alumno.catedra'], null=False)),
            ('comision', models.ForeignKey(orm[u'main_alumno.comision'], null=False))
        ))
        db.create_unique(m2m_table_name, ['catedra_id', 'comision_id'])


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
            'comisiones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'catedras'", 'symmetrical': 'False', 'through': u"orm['main_alumno.Horario']", 'to': u"orm['main_alumno.Comision']"}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'numero': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'turno': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'main_alumno.cursada': {
            'Meta': {'object_name': 'Cursada'},
            'estado': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main_alumno.horario': {
            'Meta': {'object_name': 'Horario'},
            'ayudantes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'catedra': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main_alumno.Catedra']"}),
            'comision': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main_alumno.Comision']"}),
            'dia_p': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'dia_t': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'hora_fin_p': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hora_fin_t': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'hora_inicio_p': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'hora_inicio_t': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prof_p': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'prof_t': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['main_alumno']