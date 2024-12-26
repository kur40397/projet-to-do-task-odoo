from odoo import fields, models, api


class Timesheet(models.Model):
    _name = 'todo_app.timesheet'


    task_ids=fields.Many2one('todo_app.task')
