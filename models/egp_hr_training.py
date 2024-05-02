# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    training_ids = fields.One2many('employee.training', 'employee_id', string='Training')

    course_id = fields.Many2one('employee.course', string="Course")
    training_type = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                              ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Training Type")
    training_location = fields.Char(string='Training Location')
    training_start_date = fields.Date(string='Start Date')
    training_end_date = fields.Date(string='End Date')


# Your Python code (e.g., in a controller or model)

class EmployeeTraining(models.Model):
    _name = 'employee.training'
    _description = 'Employee Training'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    course_id = fields.Many2one('employee.course', string="Course", ondelete='cascade')
    training_type = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                                      ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Training Type")
    training_location = fields.Char(string='Training Location')
    training_start_date = fields.Date(string='Start Date')
    training_end_date = fields.Date(string='End Date')














