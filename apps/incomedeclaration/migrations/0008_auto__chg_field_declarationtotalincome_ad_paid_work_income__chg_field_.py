# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DeclarationTotalIncome.ad_paid_work_income'
        db.alter_column('incomedeclaration_declarationtotalincome', 'ad_paid_work_income', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'DeclarationTotalIncome.ad_entrepreneurial_income'
        db.alter_column('incomedeclaration_declarationtotalincome', 'ad_entrepreneurial_income', self.gf('django.db.models.fields.FloatField')(null=True))
    def backwards(self, orm):

        # Changing field 'DeclarationTotalIncome.ad_paid_work_income'
        db.alter_column('incomedeclaration_declarationtotalincome', 'ad_paid_work_income', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'DeclarationTotalIncome.ad_entrepreneurial_income'
        db.alter_column('incomedeclaration_declarationtotalincome', 'ad_entrepreneurial_income', self.gf('django.db.models.fields.IntegerField')(null=True))
    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'incomedeclaration.declarationbiography': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationBiography'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'biographies'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place_dob': ('django.db.models.fields.TextField', [], {}),
            'place_dob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'place_dob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.TextField', [], {}),
            'position_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_contact': ('django.db.models.fields.TextField', [], {}),
            'work_contact_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'work_contact_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcash': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationCash'},
            'amt_currency': ('django.db.models.fields.TextField', [], {}),
            'amt_currency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'amt_currency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cash'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationcontract': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationContract'},
            'date_period_agency': ('django.db.models.fields.TextField', [], {}),
            'date_period_agency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_period_agency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.TextField', [], {}),
            'desc_value_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financial_result': ('django.db.models.fields.TextField', [], {}),
            'financial_result_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'financial_result_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationdeposit': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationDeposit'},
            'balance': ('django.db.models.fields.TextField', [], {}),
            'balance_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'balance_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bank': ('django.db.models.fields.TextField', [], {}),
            'bank_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bank_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deposits'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationentrepreneurial': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationEntrepreneurial'},
            'corp_name_addr': ('django.db.models.fields.TextField', [], {}),
            'corp_name_addr_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'corp_name_addr_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entrepreneurials'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.TextField', [], {}),
            'income_rec_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_date': ('django.db.models.fields.TextField', [], {}),
            'particn_date_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_date_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_type': ('django.db.models.fields.TextField', [], {}),
            'particn_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'particn_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_agency': ('django.db.models.fields.TextField', [], {}),
            'register_agency_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'register_agency_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationfamily': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationFamily'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'family'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'dob': ('django.db.models.fields.TextField', [], {}),
            'dob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relation': ('django.db.models.fields.TextField', [], {}),
            'relation_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'relation_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.TextField', [], {}),
            'surname_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'surname_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationgift': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationGift'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gifts'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_value': ('django.db.models.fields.TextField', [], {}),
            'desc_value_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_value_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'giver_rel': ('django.db.models.fields.TextField', [], {}),
            'giver_rel_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'giver_rel_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationotherinclexpense': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationOtherInclExpense'},
            'amount': ('django.db.models.fields.TextField', [], {}),
            'amount_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'amount_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'otherinclexpenses'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recip_issuer': ('django.db.models.fields.TextField', [], {}),
            'recip_issuer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'recip_issuer_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationproperty': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationProperty'},
            'co_owners': ('django.db.models.fields.TextField', [], {}),
            'co_owners_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'properties'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_shares': ('django.db.models.fields.TextField', [], {}),
            'name_shares_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.TextField', [], {}),
            'prop_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationrealestate': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationRealEstate'},
            'co_owners': ('django.db.models.fields.TextField', [], {}),
            'co_owners_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'co_owners_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realestates'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_area': ('django.db.models.fields.TextField', [], {}),
            'loc_area_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'loc_area_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares': ('django.db.models.fields.TextField', [], {}),
            'name_shares_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_shares_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type': ('django.db.models.fields.TextField', [], {}),
            'prop_type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prop_type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationsecurity': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationSecurity'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'securities'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issuer': ('django.db.models.fields.TextField', [], {}),
            'issuer_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'issuer_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.TextField', [], {}),
            'price_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'price_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.TextField', [], {}),
            'quantity_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'quantity_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {}),
            'type_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.declarationtotalincome': {
            'Meta': {'object_name': 'DeclarationTotalIncome'},
            'ad_entrepreneurial_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ad_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ad_paid_work_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'ad_submission_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'declarationtotalincome'", 'null': 'True', 'to': "orm['representative.Representative']"})
        },
        'incomedeclaration.declarationwage': {
            'Meta': {'ordering': "('declaration',)", 'object_name': 'DeclarationWage'},
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wages'", 'to': "orm['incomedeclaration.IncomeDeclaration']"}),
            'desc_job': ('django.db.models.fields.TextField', [], {}),
            'desc_job_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_job_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_workplace': ('django.db.models.fields.TextField', [], {}),
            'desc_workplace_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_workplace_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income_rec': ('django.db.models.fields.TextField', [], {}),
            'income_rec_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'income_rec_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'name_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'incomedeclaration.incomedeclaration': {
            'Meta': {'ordering': "('decl_id',)", 'object_name': 'IncomeDeclaration'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'decl_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'representative': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'incomedeclaration'", 'null': 'True', 'to': "orm['representative.Representative']"}),
            'scrape_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        'incomedeclaration.incomedeclarationpluginconf': {
            'Meta': {'object_name': 'IncomeDeclarationPluginConf', 'db_table': "'cmsplugin_incomedeclarationpluginconf'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "u'Income Declarations'", 'max_length': '32'})
        },
        'popit.organisation': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Organisation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'ended': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '300'}),
            'started': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'summary_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'popit.person': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'date_of_death': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'description_ka': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'representative.party': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Party', '_ormbases': ['popit.Organisation']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'organisation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Organisation']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'representative.representative': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Representative', '_ormbases': ['popit.Person']},
            'answered': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'committee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'committee_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contact_address_phone_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'declaration_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'education_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'elected_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'electoral_district_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'entrepreneurial_salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'expenses': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expenses_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faction_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'family_status_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'is_majoritarian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'main_salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'other_income': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Party']"}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['popit.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pob': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pob_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'property_assets_ka': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['representative.Term']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'representatives'", 'null': 'True', 'to': "orm['representative.Unit']"})
        },
        'representative.term': {
            'Meta': {'object_name': 'Term'},
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'representative.unit': {
            'Meta': {'object_name': 'Unit'},
            'active_term': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'unit_active'", 'null': 'True', 'to': "orm['representative.Term']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive_terms': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'unit_inactive'", 'blank': 'True', 'to': "orm['representative.Term']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_ka': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parties': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'unit'", 'symmetrical': 'False', 'to': "orm['representative.Party']"}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['incomedeclaration']