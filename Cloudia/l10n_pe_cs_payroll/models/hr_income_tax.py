# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields


class HrIncomeTax(models.Model):
    _name = 'hr.income_tax'
    _description = 'HR Income Tax'

    sequence = fields.Integer(string="Sequence", change_default="1")
    name = fields.Char(string='Name')
    uit_value = fields.Float(string='UIT Value')
    tax_rate = fields.Float(string="Tax Rate")
