# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Reservation(models.Model):
    _name = 'gestion_reservations.reservation'
    _description = 'reservation'
    _rec_name = "email"

    id_reservation = fields.Char(string="Numéro de la réservation", unique=True)
    last_name = fields.Char(string="Nom")
    first_name = fields.Char(string="Prénom")
    email = fields.Char(string="Adresse e-mail")
    country = fields.Char(string="Pays du client")
    phone = fields.Char( string="Téléphone du client")
    start_date = fields.Date(string='Date d\'arrivée')
    end_date = fields.Date(string='Date de départ')
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')
    cool= fields.Boolean()


    """@api.depends('id_room')
    def _change_state_room(self):
        if self.id_room:
            self.id_room.state='occupied'
            self.cool=True
        else:
            self.cool=False """

    

    @api.constrains('id_room')
    def check_chamber(self):
        rooms= self.env['gestion_reservations.room'].search([('id','=',self.id_room.id)])
        if rooms.state=='Disponible':
            rooms.state='occupied'
        else:
            raise UserError('La chambre est déja réservée')


    
