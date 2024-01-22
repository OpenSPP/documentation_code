from odoo import api, fields, models


class G2PEntitlementCustom(models.Model):
    _inherit = "g2p.entitlement"

    day_duration = fields.Integer("Valid Duration (Days)", compute="_compute_day_duration")
    
    @api.depends("valid_from", "valid_until")
    def _compute_day_duration(self):
        for rec in self:
            valid_from = rec.valid_from or fields.Date.today()
            delta = rec.valid_until - valid_from
            rec.day_duration = delta.days
