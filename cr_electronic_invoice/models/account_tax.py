# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class InvoiceTaxElectronic(models.Model):
	_inherit = "account.tax"

	tax_code = fields.Char(string="Código de impuesto", required=False, )