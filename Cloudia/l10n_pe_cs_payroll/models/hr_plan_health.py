# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields


class HrPlanHealth(models.Model):
    _name = 'hr.plan_health'
    _description = 'HR Plan Health'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    price = fields.Monetary(string='Price')
    currency_id = fields.Many2one(
        'res.currency', 'Currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True)
