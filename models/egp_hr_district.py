# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeDistrict(models.Model):
    _name = 'employee.district'
    _description = 'Employee district'

    district_name = fields.Char(string='District')





