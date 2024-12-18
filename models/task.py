# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class Task(models.Model):
    _name = 'todo_app.task'
    _description = 'this a todo app'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'description'
    name= fields.Char(required=True,string='Name', tracking=True)
    assignTo=fields.Many2one('res.partner',string='Assign To' ,tracking=True)
    description=fields.Char(string='Description' ,tracking=True)
    dueDate=fields.Date(string='Due Date', tracking=True)
    status=fields.Selection(
        [
            ('new','New'),
            ('inProgress','In Progress'),
            ('completed','Completed'),
            ('closed','Closed')
        ],default='new', tracking=True ,readonly=True, copy=False

    )
    active=fields.Boolean(default=True)

    def button_in_progress(self):
        self.write({'status': "inProgress"})

    def button_completed(self):
        self.write({'status':'completed'})

    def action_closed(self):
        for rec in self:
            self.write({
                'status':'closed'
            })

