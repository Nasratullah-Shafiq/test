# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeStep(models.Model):
    _name = 'employee.step'
    _description = 'Employee Step'

    name = fields.Char(string='Step Or Rank')





