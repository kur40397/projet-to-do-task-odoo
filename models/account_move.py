from odoo import fields, models, api

#Étendre le modèle : Permet d'ajouter la méthode liée au bouton.

class AccountMove(models.Model):
    _inherit = 'account.move'

    def just_do_something(self):
        print(self,"inside action_do_something method")


