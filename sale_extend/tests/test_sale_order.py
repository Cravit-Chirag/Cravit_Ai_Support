from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestSaleOrderShippingAddress(TransactionCase):
    """Test shipping address display on sale orders."""
    @classmethod
    def setUpClass(cls):
        """Prepare sale order model and partners for tests."""
        super().setUpClass()
        cls.SaleOrder = cls.env["sale.order"]
        cls.partner = cls.env["res.partner"].create({"name": "Test Customer"})
        cls.delivery_partner = cls.env["res.partner"].create(
            {
                "name": "Delivery Address",
                "type": "delivery",
                "parent_id": cls.partner.id,
                "street": "123 Main Street",
                "city": "Springfield",
            }
        )

    def test_shipping_address_display_from_delivery_partner(self):
        """Shipping address shows formatted delivery partner address."""
        order = self.SaleOrder.create(
            {
                "partner_id": self.partner.id,
                "partner_shipping_id": self.delivery_partner.id,
            }
        )
        self.assertIn("123 Main Street", order.shipping_address_display)
        self.assertIn("Springfield", order.shipping_address_display)

    def test_shipping_address_display_empty_without_address_lines(self):
        """Shipping address is empty when delivery partner has no address."""
        delivery_without_address = self.env["res.partner"].create(
            {
                "name": "Delivery Without Address",
                "type": "delivery",
                "parent_id": self.partner.id,
            }
        )
        order = self.SaleOrder.create(
            {
                "partner_id": self.partner.id,
                "partner_shipping_id": delivery_without_address.id,
            }
        )
        self.assertEqual(
            order.shipping_address_display,
            delivery_without_address.contact_address,
        )


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

    def test_xyz_in_quotation_tree_view(self):
        """xyz is shown on the quotation list view."""
        tree_view = self.env.ref("sale.view_quotation_tree")
        arch = tree_view.get_combined_arch()
        self.assertIn('name="xyz"', arch)

    def test_xyz_in_order_tree_view(self):
        """xyz is shown on the sale order list view."""
        tree_view = self.env.ref("sale.view_order_tree")
        arch = tree_view.get_combined_arch()
        self.assertIn('name="xyz"', arch)

    def test_xyz_in_form_view(self):
        """xyz is shown on the sale order form view after Order Date."""
        form_view = self.env.ref("sale.view_order_form")
        arch = form_view.get_combined_arch()
        self.assertIn('name="xyz"', arch)
        date_order_pos = arch.find('name="date_order"')
        xyz_pos = arch.find('name="xyz"')
        self.assertGreater(xyz_pos, date_order_pos)


@tagged("post_install", "-at_install")
class TestSaleOrderAbc(TransactionCase):
    """Test the abc field on sale orders."""

    @classmethod
    def setUpClass(cls):
        """Prepare sale order model and a partner for tests."""
        super().setUpClass()
        cls.SaleOrder = cls.env["sale.order"]
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})

    def test_abc_field_on_create(self):
        """abc is stored when set on sale order creation."""
        order = self.SaleOrder.create(
            {
                "partner_id": self.partner.id,
                "abc": "sample-abc",
            }
        )
        self.assertEqual(order.abc, "sample-abc")

    def test_abc_field_on_write(self):
        """abc can be updated after sale order creation."""
        order = self.SaleOrder.create({"partner_id": self.partner.id})
        order.write({"abc": "updated-abc"})
        self.assertEqual(order.abc, "updated-abc")
