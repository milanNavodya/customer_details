from odoo import api, fields, models, _, tools


class CustomerDetails(models.Model):
    _name = "customer.details"
    _description = "Customer Details"

    name = fields.Char(string="Customer Name")
    dob = fields.Date(string="DOB")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',
                              required=True)
    rep = fields.Many2one(comodel_name="res.partner", string="Customer Rep")
    service_line = fields.One2many(comodel_name="customer.services", inverse_name="customer_details_id",
                                   string="Services")


class CustomerServices(models.Model):
    _name = "customer.services"

    name = fields.Char(string="Service")
    type = fields.Char(string="Type")
    customer_details_id = fields.Many2one(comodel_name="customer.details", string='Customer details id')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_type = fields.Selection([('from_app', 'From App'), ('direct', 'Direct')], string="Sale Type")
