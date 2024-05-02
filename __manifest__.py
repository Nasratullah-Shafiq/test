{
    "name": "EGP HR Module",
    "version": "17.0.1.0.0",
    "summary": "EGP Human Resource Module",
    'sequence': -100,
    'category': 'Human Resources',
    "description": "",
    "depends": ['hr','hr_recruitment'],
    'data': [
        'security/egp_hr_security.xml',
        'security/ir.model.access.csv',
        'views/egp_hr_employee.xml',
        'views/egp_hr_applicant.xml',
        'report/egp_hr_employee_report.xml',
        'report/egp_hr_employee_card.xml',
    ],
    "author": "MCIT_EGP_Team",
    "website": "https://mcit.gov.af/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": 'OPL-1',
}

