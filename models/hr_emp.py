# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrApplicantInherit(models.Model):
    _inherit = 'hr.applicant'
    _description = "Human Resource"

    # father_name = fields.Char(string='Father Name')