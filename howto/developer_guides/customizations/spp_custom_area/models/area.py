from odoo import fields, models


class SPPArea(models.Model):
    _inherit = "spp.area"

    population = fields.Integer()
