{
    "name": "EGP HR Module",
    "version": "17.0.1.0.0",
    "summary": "EGP Human Resource Module",
    'sequence': -100,
    'category': 'Human Resources',
    "description": "",
    "depends": ['hr'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        'view/employee.xml',
        'report/employee_report.xml',
        'report/employee_card.xml',
    ],
    "author": "MCIT_EGP_Team",
    "website": "https://mcit.gov.af/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": 'OPL-1',
}

