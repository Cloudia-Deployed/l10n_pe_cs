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
                              'hr_payroll',
                            ],

  'demo'                 :  [
                              'data/hr_payroll_demo.xml',
                            ],

  'data'                 :  [
                              'data/hr_payroll_account_journal.xml',
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
