{
    'name': 'Paraguay - Localization ',
    'version': '18.0.1.0.0',
    'category': 'Localization/Account',
    'summary': 'Paraguayan Localization Chart of Accounts',
    'description': """
Paraguayan Localization for Odoo 18.
===================================
This module provides the Chart of Accounts for Paraguay, based on the INCOOP standard.

Key features include:
* Standard Chart of Accounts (Clase 1 to Clase 8)
* Basic Account Types mapping for Odoo's financial reports.
    """,
    'author': 'Savetec LLC',
    'website': 'https://shop.paravida.com.py',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'base',
    ],
    'data': [
        'data/account_chart_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}