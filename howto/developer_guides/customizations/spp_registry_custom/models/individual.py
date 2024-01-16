from odoo import fields, models


class OpenSPPIndividualCustom(models.Model):
    _inherit = "res.partner"

    ind_currency_id = fields.Many2one(
        "res.currency",
        "Currency",
        default=lambda self: self.env.user.company_id.currency_id or None,
    )
    ind_salary = fields.Monetary("Salary", currency_field="ind_currency_id", default=0.0)
