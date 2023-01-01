# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields


class HRUnionPlan(models.Model):
    _name = 'hr.union_plan'
    _description = 'Union Plan'

    name = fields.Char(string="Name")
    fees = fields.Integer(string="Fees")
