# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields


class HrUnion(models.Model):
    _name = 'hr.union'
    _description = 'HR Union'

    name = fields.Char(string='Name')
    cost = fields.Monetary(string='Cost')
    currency_id = fields.Many2one(
        'res.currency', 'Currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True)
