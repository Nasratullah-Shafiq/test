# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeStatus(models.Model):
    _name = 'employee.status'
    _description = 'Employee Status'

    name = fields.Char(string='Status')













