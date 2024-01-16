from odoo import api, fields, models


class OpenSPPGroupCustom(models.Model):
    _inherit = "res.partner"

    z_ind_grp_count_below_salary = fields.Integer(
        "Number of members with below 100 salary",
        compute="_compute_count_below_salary",
    )

    @api.depends("group_membership_ids", "group_membership_ids.salary")
    def _compute_count_below_salary(self):
        for rec in self:
            below_salary_count = 0
            for membership in rec.group_membership_ids:
                if membership.salary < 100:
                    below_salary_count += 1

            rec.z_ind_grp_count_below_salary = below_salary_count
