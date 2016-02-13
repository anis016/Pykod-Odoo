# -*- coding: utf-8 -*-
{
    'name': "lead_custom",

    'summary': """ This module adds project id and flows the project id from lead to the sales.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Sayed Anisul Hoque",
    'website': "http://www.pykod.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sale', 'sale_crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}