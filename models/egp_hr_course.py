# -*- coding: utf-8 -*-
from odoo import fields, models, api

class EmployeeCourse(models.Model):
    _name = 'employee.course'
    _description = 'Employee Course'

    name = fields.Char(string='Course')













