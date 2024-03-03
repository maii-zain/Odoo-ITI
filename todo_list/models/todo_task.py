from odoo import models, fields


class Ticket(models.Model):
    _name = 'ticket'
    _description = 'Ticket'
    name = fields.Char('Name')
    number = fields.Char()
    tag = fields.Char()
    state = fields.Selection([('new', 'New'), ('doing', 'Doing'), ('done', 'Done')], default='new', string='State')
    file = fields.Binary()
    assign_to = fields.Many2one('res.users', string='Assign To')
    description = fields.Text(string='Description')
