# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    education_ids = fields.One2many('employee.education', 'employee_id', string='Education')


# Your Python code (e.g., in a controller or model)

class EmployeeEducation(models.Model):
    _name = 'employee.education'
    _description = 'Employee Education'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    country = fields.Many2one('res.country', string="Country", tracking=True)
    degree_id = fields.Many2one('employee.degree', string="Degree")
    University = fields.Char(string='University')
    faculty = fields.Char(string='faculty')
    major = fields.Char(string='Major')
    education_start_date = fields.Date(string='Start Date')
    education_end_date = fields.Date(string='End Date')
    batch_no = fields.Integer(string='Batch No')
    education_remarks = fields.Char(string='Remarks')







