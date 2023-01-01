# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields,api


class Contract(models.Model):
    _inherit = 'hr.contract'

    Salary_Freq = [('halfmonth','HalfMonth'),
                    ('fullmonth','FullMonth')]

    plan_health = fields.Many2one('hr.plan_health', string="Health Insurance Plan")
    plan_health_cost = fields.Float(string="Health Insurance Cost")
    plan_retirement = fields.Many2one('hr.plan_retirement',string="Retirement Plan")
    plan_health_contribution = fields.Monetary(string="Health Insurance Employer Additional Contribution")
    plan_union = fields.Many2one('hr.union_plan',string="Union dues")
    salary_frequency_wage = fields.Selection(Salary_Freq, string="Salary payment frequency")
    sctr = fields.Boolean(string="SCTR")
    previous_income = fields.Monetary(string="Previous income")
    previous_income_date = fields.Date(string="Previous income Date")
    unions = fields.Many2one('hr.union',string="Union membership")
    commisions = fields.Boolean(string="Commissions")
    attendance_tracking = fields.Boolean(string="Attendance")

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        if 'commisions' in fields_list and 'attendance_tracking' in fields_list:
            if self.env.user.has_group('hr.group_hr_manager'):
                defaults['commisions'] = False
                defaults['attendance_tracking'] = False
        return defaults
