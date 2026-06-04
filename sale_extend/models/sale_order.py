from odoo import fields, models


class SaleOrder(models.Model):
    """Extend sale orders with a custom xyz field."""

    _inherit = "sale.order"

    xyz = fields.Char(
        help="Custom XYZ value for this sale order.",
    )
