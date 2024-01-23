from odoo import api, fields, models


class CustomAuditRule(models.Model):
    _inherit = "spp.audit.rule"

    active = fields.Boolean(default=True)
