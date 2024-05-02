# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeOrganization(models.Model):
    _name = 'employee.organization'
    _description = 'Employee Organization'

    name = fields.Char(string='Organization')













