{
    'name': 'Hospitals Management System',
    'version': '1.0',
    'summary': 'Manage hospital patients data',
    'description': 'This module allows managing patient data in hospitals',
    'author': 'Mai Zain-Elabdeen',
    'category': 'Healthcare',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/department.xml',
        'views/doctor.xml',
    ],
    'application': True,
}
