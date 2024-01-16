from odoo import fields, models


class OpenSPPMembershipCustom(models.Model):
    _inherit = "g2p.group.membership"
    
    currency_id = fields.Many2one(
        "res.currency",
        related="individual.ind_currency_id",
    )

    salary = fields.Monetary(
        "Salary",
        currency_field="currency_id",
        related="individual.ind_salary",
    )
