# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields
import string


class HrPlanRetirement(models.Model):
    _name = 'hr.plan_retirement'
    _description = 'HR Plan Retirement'

    code = fields.Char(string='Code')
    name = fields.Char(string='Name')
    onp = fields.Integer(string="Onp")
    fund = fields.Integer(string="Fund")
    commission = fields.Float(string="Comminssion")
    insurance = fields.Float(string="Insurance")
