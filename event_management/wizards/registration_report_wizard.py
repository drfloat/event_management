from odoo import models, fields, api
import base64
import io
from datetime import datetime
import xlwt

class RegistrationReportWizard(models.TransientModel):
    _name = 'registration.report.wizard'
    _description = 'Registration Report Wizard'

    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    #here i have added a function to print xlsx report for event registerations between given time frame
    def print_report(self):
        registrations = self.env['event.registration'].search([
            ('registration_date', '>=', self.start_date),
            ('registration_date', '<=', self.end_date)
        ])


        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Registrations')


        header_style = xlwt.easyxf('font: bold on; align: horiz center;')
        worksheet.write(0, 0, 'Registration Date', header_style)
        worksheet.write(0, 1, 'Organizer Name', header_style)
        worksheet.write(0, 2, 'Attendee Name', header_style)
        worksheet.write(0, 3, 'Event Name', header_style)
        worksheet.write(0, 4, 'Registration State', header_style)


        row = 1
        for registration in registrations:
            worksheet.write(row, 0, str(registration.registration_date))
            worksheet.write(row, 1, registration.event_id.organizer_id.name if registration.event_id.organizer_id else '')
            worksheet.write(row, 2, registration.attendee_id.name)
            worksheet.write(row, 3, registration.event_id.name)
            worksheet.write(row, 4, registration.state)
            row += 1


        report_file = io.BytesIO()
        workbook.save(report_file)
        report_file.seek(0)

        filename = 'Registration_Report.xls'
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'datas': base64.encodebytes(report_file.getvalue()),
            'res_model': self._name,
            'res_id': self.id
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new',
        }

