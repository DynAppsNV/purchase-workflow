# Copyright 2021 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        if self.env.context.get("search_purchase_no_grouping", False):
            return self.browse()
        return super().search(domain, offset=offset, limit=limit, order=order)
