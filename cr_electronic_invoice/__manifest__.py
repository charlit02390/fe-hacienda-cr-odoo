# -*- coding: utf-8 -*-

{
	'name': 'Facturación electrónica Costa Rica',
	'version': '1.0.0',
	'author': 'Automatuanis.com',
	'license': 'OPL-1',
	'website': 'https://www.automatuanis.com/',
	'category': 'Invoicing Management',
	'description':
		'''
		Facturación electronica Costa Rica.
		''',
	'depends': ['base', 'account', 'product', 'sale_management', 'sales_team', 'account_invoicing', 'l10n_cr_country_codes', 'account_cancel', 'res_currency_cr_adapter', ],
	'data': ['data/ir_cron_data.xml',
			 'data/account_account_tag_data.xml',
			 'data/account_tax_group_data.xml',
			 'data/account_tax_template_data.xml',
			 'data/account_tax_data.xml',
			 'data/code.type.product.csv',
	         'data/identification.type.csv',
	         'data/payment.methods.csv',
	         'data/reference.code.csv',
	         'data/reference_document_data.xml',
	         'data/sale.conditions.csv',
			 'data/credit.conditions.csv',
	         'data/product.uom.csv',
			 'data/mail_template_data.xml',
			 'data/sequence.xml',
			 'data/economic_activity_data.xml',
			 'data/electronic_invoice_version.xml',
			 'data/electronic_invoice_schema_4_2.xml',
			 'data/electronic_invoice_schema_4_3.xml',

			 'views/account_tax_views.xml',
			 'views/account_invoice.xml',
			 'views/account_journal.xml',
			 'views/electronic_invoice_views.xml',
			 'views/electronic_invoice_version_views.xml',
			 'views/electronic_invoice_schema_views.xml',
			 'views/res_company_views.xml',
			 'views/product_views.xml',
		  	 'views/product_template_views.xml',
			 'views/product_category_views.xml',
			 'views/res_partner.xml',

			 'report/report_invoice.xml',

	         'security/ir.model.access.csv',

	         ],
	'installable': True,
	'application': True,
}
