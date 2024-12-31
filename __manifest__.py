# -*- coding: utf-8 -*-
{
    'name': "todoApp",

    'summary': "Test Addons to learn",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','hr_timesheet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # katdefinie chkon li radi accidi ldata mn lawal bach t3tini l'autorisation
        'data/sequence.xml',
        'views/List_tasks.xml',
        'views/todo_app_task_history_view.xml',
        'views/to_do_menu.xml',
        'wizard/change_state_wizard_view.xml',
        'reports/task_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

