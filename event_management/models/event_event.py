from odoo import models, fields, api

class EventEvent(models.Model):
    _name = 'event.event'
    _description = 'Event'

    name = fields.Char(string="Event Name", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)
    organizer_id = fields.Many2one('event.organizer', string="Organizer")
    attendee_ids = fields.Many2many('event.attendee', through='event.registration', string="Attendees")
    duration = fields.Text(string="Duration", compute="_compute_duration")
    attendee_count = fields.Integer(string="Attendee Count", compute='_compute_attendee_count')

    @api.depends('start_date', 'end_date') #here i have added function to calculate duration of event
    def _compute_duration(self):
        for event in self:
            if event.start_date and event.end_date:
                duration_hours = (event.end_date - event.start_date).total_seconds() / 3600
                event.duration = "{} hours".format(duration_hours)
            else:
                event.duration = "0 hours"

    def _compute_attendee_count(self): #here i have added function to calculate number of registered attendees
        for event in self:
            event.attendee_count = len(event.attendee_ids)

    def action_view_attendees(self):
        return {
            'name': ('_Attendees'),
            'domain': [('event_ids', '=', self.id)],
            'view_type': 'form',
            'res_model': 'event.attendee',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }



