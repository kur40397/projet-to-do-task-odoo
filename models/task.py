# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class Task(models.Model):
    _name = 'todo_app.task'
    _description = 'this a todo app'
    name= fields.Char(required=True,string='Name')
    assignTo=fields.Many2one('res.partner',string='Assign To')
    description=fields.Char(string='Description')
    dueDate=fields.Date(string='Due Date')
    status=fields.Selection(
        [
            ('new','New'),
            ('inProgress','In Progress'),
            ('completed','Completed'),
        ],default='new'
    )

