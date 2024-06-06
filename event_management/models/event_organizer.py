from odoo import models, fields,api


class EventOrganizer(models.Model):
    _name = 'event.organizer'
    _description = 'Organizer'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    user_id = fields.Many2one('res.users', string="User", readonly=True, ondelete='cascade')
    event_ids = fields.One2many('event.event', 'organizer_id', string="Events")

    @api.model
    def create(self, vals):
        user_vals = {
            'name': vals.get('name'),
            'login': vals.get('email'),
            'email': vals.get('email')
        }
        user = self.env['res.users'].create(user_vals)
        vals['user_id'] = user.id
        return super(EventOrganizer, self).create(vals)
