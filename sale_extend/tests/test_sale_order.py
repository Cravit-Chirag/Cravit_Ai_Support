from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestSaleOrderXyz(TransactionCase):
    """Test the xyz field on sale orders."""

    @classmethod
    def setUpClass(cls):
        """Prepare sale order model and a partner for tests."""
        super().setUpClass()
        cls.SaleOrder = cls.env["sale.order"]
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})

    def test_xyz_field_on_create(self):
        """xyz is stored when set on sale order creation."""
        order = self.SaleOrder.create(
            {
                "partner_id": self.partner.id,
                "xyz": "sample-xyz",
            }
        )
        self.assertEqual(order.xyz, "sample-xyz")

    def test_xyz_field_on_write(self):
        """xyz can be updated after sale order creation."""
        order = self.SaleOrder.create({"partner_id": self.partner.id})
        order.write({"xyz": "updated-xyz"})
        self.assertEqual(order.xyz, "updated-xyz")
