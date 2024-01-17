from odoo import fields, models


class OpenSPPServicePoint(models.Model):
    _inherit = "spp.service.point"
    
    weekday_time_start = fields.Float(string='Start Time')
    weekday_time_end = fields.Float(string='End Time')

    weekend_time_start = fields.Float(string='Start Time')
    weekend_time_end = fields.Float(string='End Time')
