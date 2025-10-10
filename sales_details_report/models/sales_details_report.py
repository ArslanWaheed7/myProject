from odoo import models, fields

class SalesDetailsReport(models.Model):
    _name = 'sales.details.report'
    _description = 'Sales Details Report'

    customer_id = fields.Many2one('res.partner', string='Customer')
    product_id = fields.Many2one('product.product', string='Product')
    product_category_id = fields.Many2one('product.category', string='Product Category')
    order_line_id = fields.Many2one('sale.order.line', string='Order Line')