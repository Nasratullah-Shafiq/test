# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    father_name = fields.Char(string='Father Name')
    grand_father_name = fields.Char(string='Grand Father Name')

    job_step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')],
                                string='Step')
    # job_step = fields.Char(string='Step')
    recruitment_date = fields.Date(string='Recruitment Date')
    # job_status = fields.Selection([('fire', 'منفک'), ('change', 'تبدیل'), ('recruiter', 'جدیدالتقرر')], string="حالت")

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
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

    rewards_type = fields.Char(string='Reward Type')
    reason_for_sentence = fields.Char(string='Reason of issuing sentence')
    date_of_sentence = fields.Char(string='Date of the Sentence')
    order_no = fields.Char(string='No of Sentence')

    organization = fields.Char(string='Organization')
    job_position = fields.Char(string='Job Position')
    grade = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'),
                              ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], string="Grade")
    step = fields.Selection([('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'),
                             ('5th', '5th')], string="Step")

    job_location = fields.Char(string='Job Location')
    department = fields.Char(string='Department')
    status = fields.Char(string='Status')
    job_start_date = fields.Date(string='Start Date')
    job_end_date = fields.Date(string='End Date')
    # service_duration = fields.Char(string='Service Duration')

    duration_days = fields.Integer('Duration Days (Days)', compute='_compute_duration_days', store=True)

    @api.depends('job_start_date', 'job_end_date')
    def _compute_duration_days(self):
        for record in self:
            if record.job_start_date and record.job_end_date:
                delta = record.job_end_date - record.job_start_date
                record.duration_days = delta.days
                # record.duration_years = delta.days
                # record.duration_months = delta.months
            else:
                record.duration_days = 0
                # record.duration_months = 0

    publication_type = fields.Selection([('Book', 'Book'), ('Magazine', 'Magazine')], string="Publication Type")
    subject = fields.Char(string='Subject')
    publication_date = fields.Date(string='Publication Date')
    no_of_pages = fields.Char(string='No of Pages')
    isbn = fields.Char(string='ISBN')
# Your Python code (e.g., in a controller or model)
    





