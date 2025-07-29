# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    check_number = fields.Char(
        copy=False,
        index=True,
    )

    def _prepare_move_line_default_vals(self, counterpart_account_id=None):
        line_vals_list = super()._prepare_move_line_default_vals(counterpart_account_id)
        for vals in line_vals_list:
            vals.update({"check_number": self.check_number})
        return line_vals_list
