from odoo import models, fields , api


class EventAttendee(models.Model):
    _name = 'event.attendee'
    _description = 'Attendee'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    user_id = fields.Many2one('res.users', string="User", readonly=True, ondelete='cascade')
    event_ids = fields.Many2many('event.event', through='event.registration', string="Events")

    @api.model #here i have added function to create user ids automatically
    def create(self, vals):
        user_vals = {
            'name': vals.get('name'),
            'login': vals.get('email'),
            'email': vals.get('email')
        }
        user = self.env['res.users'].create(user_vals)
        vals['user_id'] = user.id
        return super(EventAttendee, self).create(vals)
