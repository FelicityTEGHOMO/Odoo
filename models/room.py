# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReservationRoom(models.Model):
    _name = 'gestion_reservations.room'
    _description = 'room'
    _rec_name = 'room_number'

    id_room = fields.Integer(required=True, string='Identifiant de chambre', unique=True)
    room_number = fields.Char(required=True, string='Numéro de chambre')
    room_amount = fields.Integer(required=True, string='Prix de la chambre')
    room_tel = fields.Char(required=True, string='Téléphone de la chambre')
    capacity = fields.Integer(required=True, string='Capacité')
    image = fields.Image(string="Images")
    types = fields.Selection([
        ('Double Classique', 'Double Classique'),
        ('First Deluxe', 'First Deluxe'),
        ('Double Deluxe', 'Double Deluxe'),
        ('Chambre standard', 'Chambre standard'),
        ('Double Conofort', 'Double Conofort'),
        ('Lits Jumeaux Classique', 'Lits Jumeaux Classique'),
        ('Suite Senior', 'Suite Senior'),
        ('Suite Junior', 'Suite Junior'),
        ('First Deluxe Twin', 'First Deluxe Twin')
    ], string='Type')
    state = fields.Selection([('Disponible', 'Disponible'),
                                 ('occupied', 'Occupée')], 
                                 string='Statut'
                        )
    id_hotel = fields.Many2one('gestion_reservations.hotel', required=True, string='Hôtel')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Réservation') # j'ai remplacé many2one par One2many
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')


    """ @api.onchange('id_hotel')
    def _check_room(self):
        if self.id_hotel:
            self.state='occupied' """

    # def set_room_state(self, id_room, state):
    #     room = self.browse(id_room)
        #  la méthode browse est utilisée pour récupérer l'enregistrement d'une chambre correspondant à un identifiant
        # if room:
        #     room.state = state


