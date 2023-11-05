from odoo import fields, models,api


class SaleOrder(models.Model):
    _inherit = "sale.order"


    account_payment_ids = fields.One2many('account.payment', 'sale_id', string="Pay sale ", readonly=True)

    # compute fields
    total_payment = fields.Float(compute='_compute_total_payment', compute_sudo=True)

    remaining_amount = fields.Float(compute='_compute_remaining_amount')


    #  recalculate the ramaining amount

    def _compute_remaining_amount(self):
        for amount in self:
            amount.remaining_amount = amount.amount_total - amount.total_payment

    # recalculate the total payment amount

    def _compute_total_payment(self):
        for parent in self:
            parent.total_payment = sum(parent.account_payment_ids.mapped('amount'))












