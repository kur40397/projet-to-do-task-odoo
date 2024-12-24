from odoo import fields, models


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    task_ids = fields.Many2one('todo_app.task','Task')
