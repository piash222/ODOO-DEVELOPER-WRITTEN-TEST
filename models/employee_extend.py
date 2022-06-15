from odoo import fields, models


class EmployeeExtend(models.Model):
    _inherit = 'hr.employee'

    emergency_contact_ids = fields.One2many('emergency.contact', 'employee_id', string='Emergency Contact')
    multiple_education_ids = fields.One2many('multiple.education', 'employee_id', string='Education')
