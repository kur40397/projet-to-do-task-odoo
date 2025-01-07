# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api
from odoo.addons.test_convert.tests.test_env import field
from odoo.api import readonly


class Task(models.Model):
    _name = 'todo_app.task'
    _description = 'this a todo app' # humain readable model name
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'name' # le field li radi afficha comme un nom du record
    ref= fields.Char(readonly=True )
    name= fields.Char(required=True, tracking=True)
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
    taskHistory_ids=fields.One2many('todo_app.task_history','task_id')



    def button_in_progress(self):
        self.create_history_record(self.status,'inProgress','1')
        self.write({'status': "inProgress"})

    def button_completed(self):
        self.create_history_record(self.status,'completed')
        self.write({'status':'completed'})

    def action_closed(self):
        self.create_history_record(self.status,'closed')
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
        print(self.env['todo_app.task'].search(['|',('name','=','badr'),('description','=','this is badr')]))

    @api.model
    def create(self,vals):
        res=super(Task,self).create(vals)

        res.ref=self.env['ir.sequence'].next_by_code('todo_app_task_seq_TS')

        return res


    def create_history_record(self, old_state, new_state,reason=None):
         print(self.id)
         self.env['todo_app.task_history'].create({
                'user_id': self.env.user.id,
                'task_id': self.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or "aucune reason",
            })

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('todo_app.action_change_state_wizard_window')
        # _for_xml_id katrecupiri l'action par son id li howa module.record_id bach to open pop up
        action['context'] = {'default_task_id': self.id}
        # action['context']: permettre d'ajouter des données supplémentaires

        return action
    def action_related_assignTo(self):
        action=self.env['ir.actions.actions']._for_xml_id('base.action_partner_form')
        view_id=self.env.ref('base.view_partner_form').id
        action['res_id']=self.assignTo.id
        #res_id za3ma l'id dial record of the model li action katpointi 3lih
        action['views']=[[view_id,'form']]
        return action
