# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReservationRoom(models.Model):
    _name = 'gestion_reservations.room'
    _description = 'room'
    _rec_name = 'room_number'

    # name = fields.Char(help='chambre', required=True)
    id_room = fields.Integer(required=True, string='Identifiant de chambre')
    room_number = fields.Integer(required=True, string='Numéro de chambre')
    room_amount = fields.Integer(required=True, string='Prix de la chambre')
    room_tel = fields.Char(required=True, string='Téléphone de la chambre')
    disponible = fields.Boolean(default=True,string='Disponibilité')
    capacity = fields.Integer(required=True, string='Capacité')
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
    id_hotel = fields.Many2one('gestion_reservations.hotel', required=True, string='Hôtel')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Réservation')
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')

    def action_reserve(self):
        self.available = False




#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
