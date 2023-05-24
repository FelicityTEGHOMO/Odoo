# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReservationRoom(models.Model):
    _name = 'gestion_reservations.room'
    _description = 'room'
    _rec_name = 'id_room'

    # name = fields.Char(help='chambre', required=True)
    id_room = fields.Integer(required=True, string='Numero de chambre')
    room_amount = fields.Integer(required=True, string='Prix de la chambre')
    room_tel = fields.Integer(required=True, string='Téléphone de la chambre')
    Disponible = fields.Boolean(default=True)
    types = fields.Selection([
        ('dc', 'Double Classique'),
        ('fd', 'First Deluxe'),
        ('dd', 'Double Deluxe'),
        ('cs', 'Chambre standard'),
        ('dc', 'Double Conofort'),
        ('ljc', 'Lits Jumeaux Classique'),
        ('ss', 'Suite Senior'),
        ('sj', 'Suite Junior'),
        ('fdt', 'First Deluxe Twin')
    ])
    id_hotel = fields.Many2one('gestion_reservations.hotel', required=True, string='Hotel')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Reservation')
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')

    def action_reserve(self):
        self.available = False




#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
