{
    'name': 'Employee Recruitment extend',
    'version': '13.0.0.0.1',
    'summary': 'Module to extend Employee and Recruitment',
    'description': 'Adding Extra Feature on Employee and Recruitment',
    'category': 'Human Resources',
    'author': 'Md. Shihab Uddin',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'hr_recruitment'
    ],
    'data': [
        'security/sequrity.xml',
        'security/ir.model.access.csv',
        'views/applicant_extend.xml',
        'views/employee_extend.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': False
}
