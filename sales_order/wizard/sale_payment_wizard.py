# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import api, fields, models


class SalePaymentWizard(models.TransientModel):
    _name = 'sale.payment.wizard'
    _description = 'Sale Payment'

    # == Business fields ==
    payment_date = fields.Date(string="Payment Date", default=fields.Date.context_today,required=True)
    currency_id = fields.Many2one('res.currency', string='Journal Currency' ,
                                  default=lambda self: self.env.ref('base.EUR'))
    amount = fields.Monetary(currency_field='currency_id')

    journal_id = fields.Many2one('account.journal', string="Payment Journal", required=True)


    # make_payment to create payment values
    # check the valid enter amount if it is less than or equal to the total_amount of the sale
    def make_payment(self):
        sale_ids = self.env.context.get('active_ids', [])
        if sale_ids:
            sale_id = self.env['sale.order'].browse(sale_ids[0])
            if sale_id.total_payment + self.amount > sale_id.amount_total:
                raise ValidationError("Entered amount cannot be greater than the total amount.")

            payment_vals = {
                'payment_type': 'inbound',
                'partner_id': sale_id.partner_id.id,
                'partner_type': 'customer',
                'journal_id': self.journal_id.id,
                'currency_id': sale_id.currency_id.id,
                'date': self.payment_date,
                'amount': self.amount,
                'sale_id': sale_id.id,
                'name': "Payment" + " - " + sale_id.name,
                'state':"draft"
            }
            self.env['account.payment'].create(payment_vals)
        return {
            'type': 'ir.actions.act_window_close',
        }



