from odoo import api, fields, models


class RecruitmentExtend(models.Model):
    _inherit = 'hr.applicant'

    emergency_contact_ids = fields.One2many('emergency.contact', 'applicant_id', string='Emergency Contact')
    multiple_education_ids = fields.One2many('multiple.education', 'applicant_id', string='Education')
    manager_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Manager',
        required=False)

    def create_employee_from_applicant(self):
        dict_act_window = super(RecruitmentExtend, self).create_employee_from_applicant()
        employee_id = self.env['hr.employee'].search([('id', '=', dict_act_window['res_id'])])
        employee_id.parent_id = self.manager_id
        for rec in self.emergency_contact_ids:
            rec.employee_id = employee_id.id
        for rec in self.multiple_education_ids:
            rec.employee_id = employee_id.id

        # self.emergency_contact_ids.employee_id = employee_id
        # self.multiple_education_ids.employee_id = employee_id



        leave_type = self.env['hr.leave.type'].search([], limit=1, order='id')
        leave_allocation = self.env['hr.leave.allocation'].create({
            'name': f"Leave Allocation For {employee_id.name}",
            'holiday_status_id': leave_type.id,
            'holiday_type': 'employee',
            'employee_id': employee_id.id,
            'allocation_type': 'regular',
            'number_of_days': 20.00,
        })
        leave_allocation.action_approve()
        leave_allocation.action_validate()
        return dict_act_window


class EmergencyContact(models.Model):
    _name = 'emergency.contact'
    _description = 'Recruiter Emergency Contact Details'

    seq = fields.Char()
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    applicant_id = fields.Many2one('hr.applicant', string="Applicant")
    employee_id = fields.Many2one('hr.employee', string="Employee")


class MultipleEducation(models.Model):
    _name = 'multiple.education'
    _description = 'Applicant Education Details'

    seq = fields.Char()
    institute = fields.Char(string='Institute')
    degree = fields.Char(string='Degree')
    passing_year = fields.Char(string='Passing Year')
    applicant_id = fields.Many2one('hr.applicant', string="Applicant")
    employee_id = fields.Many2one('hr.employee', string="Employee")
