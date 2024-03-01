# -*- coding: utf-8 -*-
{
    'name': 'Todo List',
    'version': '17.0.1.0.0',
    'category': 'productivity',
    'summary': 'Manage your daily tasks',
    'description': """ This module allows users to manage their daily tasks in Odoo.  """,
    'author': 'Mai Zain',

    'depends': ['base', 'web'],
    'data': [
    'views/ticket.xml',
    # 'views/ticket_menus.xml',
    'security/ir.model.access.csv',
],

    'application': True,

}
