# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    relative_ids = fields.One2many('employee.relatives', 'employee_id', string='Relatives')


# Your Python code (e.g., in a controller or model)

class EmployeeRelative(models.Model):
    _name = 'employee.relatives'
    _description = 'Employee Relatives'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    father_name = fields.Char(string='Father Name')
    grand_father_name = fields.Char(string='Grand Father Name')
    job = fields.Char(string='Job')
    nic_no = fields.Integer(string='NIC No')
    permanent_address = fields.Many2one('res.country.state', string="Province", tracking=True)
    permanent_district_id = fields.Many2one('employee.district', string="Permanent District / Village")
    temporary_address = fields.Many2one('res.country.state', string="Province", tracking=True)
    temporary_district_id = fields.Many2one('employee.district', string="Temporary District / Village")
    street_no = fields.Integer(string='Street No')
    home_no = fields.Integer(string='Home No')






