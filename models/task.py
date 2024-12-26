# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import field


class Task(models.Model):
    _name = 'todo_app.task'
    _description = 'this a todo app' # humain readable model name
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'description' # le field li radi afficha comme un nom du record
    name= fields.Char(required=True,string='Name', tracking=True)
    assignTo=fields.Many2one('res.partner',string='Assign To' ,tracking=True,ondelete='cascade')
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
    employee_ids=fields.One2many('hr.employee','task_ids')
    is_late=fields.Boolean()
    late_ticket=fields.Boolean()
    #estimatedTime=fields.One2many('hr_timesheet.timesheet','task_ids')

    def button_in_progress(self):
        self.write({'status': "inProgress"})

    def button_completed(self):
        self.write({'status':'completed'})

    def action_closed(self):
        for rec in self:
            self.write({
                'status':'closed'
            })

    def check_expected_date(self):
        print(self)
        # dans les taches automatiser self fait reference au model
        tasks_ids=self.search([])
        for rec in tasks_ids:
            if rec.dueDate  and rec.dueDate < fields.date.today():
                rec.is_late=True
                rec.write({
                    'is_late':True,
                    'status':'closed'
                })

    def check_late_ticket(self):
        tasks_ids=self.search([])
        for rec in tasks_ids:
            if rec.dueDate and rec.dueDate <= fields.date.today():
                rec.write({
                    'late_ticket':True
                })

    def action(self):
        print(self.env['todo_app.task'].create({
            'name':'tob',
            'description':'where is tob',
            'status':'inProgress'
        }))
