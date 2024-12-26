from odoo import fields, models, api


class HistoryTask(models.Model):
    _name = 'todo_app.task_history'
    _description = 'Task history'

    user_id=fields.Many2one('res.users')
    task_id=fields.Many2one('todo_app.task')
    old_state=fields.Char()
    new_state=fields.Char()