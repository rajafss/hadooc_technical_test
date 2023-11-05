# -*- coding: utf-8 -*-
from odoo import api,fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    sale_id = fields.Many2one('sale.order', string="Sale")

    # print action to print the report pdf
    def action_print(self):
        return self.env.ref('sales_order.sale_payment_report_action').report_action(self)









