from odoo import models, fields, api

class EventRegistration(models.Model):
    _name = 'event.registration'
    _description = 'Event Registration'

    attendee_id = fields.Many2one('event.attendee', string="Attendee", required=True)
    event_id = fields.Many2one('event.event', string="Event", required=True)
    registration_date = fields.Datetime(string="Registration Date", default=fields.Datetime.now)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], string="State", default='draft')

    def action_confirm(self): #function for confirming invite
        self.write({'state': 'confirmed'})
        self._send_email()

    def action_cancel(self): #function for declining invite
        self.write({'state': 'cancelled'})
        self._send_email()

    def _send_email(self): #function to send email(please ensure you have added valid email id to attendee,organizer,manager)
        template = self.env.ref('event_management.email_template_registration_state')
        for registration in self:
            template.with_context(
                attendee_email=registration.attendee_id.email,
                organizer_email=registration.event_id.organizer_id.email
            ).send_mail(registration.id, force_send=True)

