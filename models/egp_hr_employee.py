# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    father_name = fields.Char(string='Father Name')
    grand_father_name = fields.Char(string='Grand Father Name')

    job_step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')],
                                string='Step')

    recruitment_date = fields.Date(string='Recruitment Date')

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    identification_type = fields.Selection([('paper_id_card', 'Paper ID card'),
                                            ('electronic_id_card', 'Electronic ID Card')],
                                string='ID Card')
    identification_print_date = fields.Date(string='Print Date')
    identification_expiry_date = fields.Date(string='Expire Date')
    identification_chapter = fields.Integer(string='Chapter')
    identification_page_no = fields.Integer(string='Page No')

    permanent_province = fields.Many2one('res.country.state', string="Permanent Province", tracking=True, ondelete='cascade')
    temporary_province = fields.Many2one('res.country.state', string="Temporary Province", tracking=True, ondelete='cascade')
    permanent_district = fields.Many2one('employee.district', string="Permanent District", tracking=True,
                                         ondelete='cascade')
    temporary_district = fields.Many2one('employee.district', string="Temporary District", tracking=True,
                                         ondelete='cascade')
    permanent_village = fields.Char(string='Permanent Village')
    temporary_village = fields.Char(string='Temporary Village')
    home_number = fields.Integer(string='Home Number')
    permanent_street = fields.Char(string='Permanent Street')
    private_streets = fields.Char(string='Private Street')
    passport_print_date = fields.Date(string='Print Date')
    passport_end_date = fields.Date(string='Expiry Date')

    education_location = fields.Char(string='Education Location')
    university = fields.Char(string='University')

    skill = fields.Char(string='Skills')
    major = fields.Char(string='Major')
    remarks = fields.Char(string='Remarks')

    course = fields.Char(string='Course')
    training_type = fields.Char(string='Training Type')
    training_location = fields.Char(string='Training Location')
    training_start_date = fields.Date(string='Start Date')
    training_end_date = fields.Date(string='End Date')
