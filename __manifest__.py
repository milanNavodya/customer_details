# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Customer Details',
    'version': '1.0',
    'description': """Customer Details""",
    'depends': [
        'base',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_details_views.xml',
    ],

    'installable': True,
    'application': True,

}
