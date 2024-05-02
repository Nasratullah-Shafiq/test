# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeDegree(models.Model):
    _name = 'employee.degree'
    _description = 'Employee Degree'

    name = fields.Char(string='Degree')





