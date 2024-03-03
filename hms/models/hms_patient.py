from odoo import models, fields, api, exceptions
from datetime import datetime

class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = 'Hospital Patient'

    name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ])
    pcr = fields.Boolean()
    image = fields.Binary(attachment=True)
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')
    department_id = fields.Many2one('hms.department', domain="[('isOpened', '=', True)]")
    doctor_id = fields.Many2one('hms.doctor', string='Doctor')
    department_capacity = fields.Integer(string='Department Capacity', related='department_id.Capacity')
    department_name = fields.Char(string='Department Name', related='department_id.Name', store=True)
    doctor_name = fields.Char(string='Doctor Name', related='doctor_id.First_name', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                birth_date_str = record.birth_date.strftime('%Y-%m-%d')
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
                today = datetime.today().date()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

    @api.constrains('department_id')
    def _check_department_opened(self):
        for patient in self:
            if patient.department_id and not patient.department_id.isOpened:
                raise exceptions.ValidationError("You cannot choose a closed department for the patient.")
