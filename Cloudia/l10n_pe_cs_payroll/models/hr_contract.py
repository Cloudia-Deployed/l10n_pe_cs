# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models,fields,api


class Contract(models.Model):
    _inherit = 'hr.contract'

    plan_health = fields.Many2one('hr.plan_health', string="Health Insurance Plan")
    plan_retirement = fields.Many2one('hr.plan_retirement',string="Retirement Plan")
    plan_health_contribution = fields.Monetary(string="Employer Contribution")
    plan_life = fields.Many2many('hr.plan_life',string="Life Insurance")
    plan_sctr = fields.Many2one('hr.plan_sctr',string="SCTR")
    plan_union = fields.Many2one('hr.union_plan',string="Union dues")
    previous_income = fields.Monetary(string="Previous income")
    commisions = fields.Boolean(string="Commissions")
    attendance_tracking = fields.Boolean(string="Attendance")
    withholding = fields.Selection([('0', 'No'), ('1', 'Amount'), ('2', 'Percentage')],
        default='0', string="Withholding")
    withholding_amount = fields.Monetary(string="Withholding Amount")
    withholding_percentage = fields.Float(string="Withholding Percentage", digits=(2,1))

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        if 'commisions' in fields_list and 'attendance_tracking' in fields_list:
            if self.env.user.has_group('hr.group_hr_manager'):
                defaults['commisions'] = False
                defaults['attendance_tracking'] = False
        return defaults
