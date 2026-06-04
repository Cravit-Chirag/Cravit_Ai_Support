from odoo import fields, models


class SaleOrder(models.Model):
   """Extend sale.order with shipping address display and custom fields."""

    _inherit = "sale.order"

    xyz = fields.Char(
        help="Custom XYZ value for this sale order.",
    shipping_address_display = fields.Char(
        string="Shipping Address",
        related="partner_shipping_id.contact_address",
        readonly=True,
        help="Formatted delivery address of the customer for this order.",
    )
    abc = fields.Char(
        string="ABC",
        help="Custom ABC value for this sale order.",
    )
