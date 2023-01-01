# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Cloudia Systems S.A.C. | http://cloudia.systems | <info@cloudia.systems>
# Copyright (c) 2021-TODAY Cloudia Systems S.A.C.
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

{
  'name'                 :  'Peru Payroll',
  'version'              :  '15.0.1.0',
  'category'             :  'Payroll',

  'author'               :  'Cloudia',
  'website'              :  'https://cloudia.systems/',

  'depends'              :  [
                              'hr_payroll_account',
                              'hr_holidays',
                              'l10n_pe',
                            ],

  'demo'                 :  [
                              'data/hr_payroll_demo.xml',
                            ],

  'data'                 :  [
                              'data/account_journal_data.xml',
                              #'data/account_account_data.xml',
                              'data/hr_rule_parameter_data.xml',
                              'data/hr_payroll_structure_type_data.xml',
                              'data/hr_salary_rule_category_data.xml',
                              'data/hr_work_entry_type_data.xml',
                              'data/hr_payslip_input_type.xml',
                              'data/hr_payroll_structure.xml',
                              # 'views/hr_contract_view.xml'
                            ],

  'qweb'                 :  [
                            ],

  'assets'               :  {
                              'web.assets_frontend': [
                              ]
                            },

  'images'               :  ['static/description/banner.png'],

  'application'          :  False,
  'installable'          :  True,
  'auto_install'         :  False,
  'sequence'             :  10,

  'license'              :  'OPL-1',
  'price'                :  0.00,
  'currency'             :  'USD',
}
