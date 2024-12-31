from odoo import fields , models

class changeState(models.TransientModel):
    _name = 'todo_app.change_state_wizard'
    task_id=fields.Many2one('todo_app.task')
    state=fields.Selection([
        ('new', 'New'),
        ('inProgress', 'In Progress'),
        ('completed', 'Completed'),
    ],default='new')
    reason=fields.Char()

    def action_confirm(self):
        self.task_id.status=self.state
        self.task_id.create_history_record('closed',self.state,self.reason)


