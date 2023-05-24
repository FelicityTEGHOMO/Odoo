# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservationHotel(models.Model):
    _name = 'gestion_reservations.hotel'
    _description = 'hotel'
    _rec_name = "id_hotel"

    id_hotel = fields.Char(required=True, string="Numéro de l'hôtel")
    name_hotel = fields.Char(required=True, string="Nom de l'hôtel")
    tel_hotel = fields.Char(required=True, string="Téléphone de l'hôtel")
    adresse_hotel = fields.Char(required=True, string="Adresse de l'hôtel")
    ville = fields.Char(required=True, string="Ville de l'hôtel")
    # id_customer = fields.Many2many('gestion_reservations.customer', 'id_hotel', string='Customer')
    id_room = fields.One2many('gestion_reservations.room', 'id_hotel', string='Chambre')
    # room_amount = fields.Integer(required=True, string='Prix de la chambre')
    # start_date = fields.Date(required=True, string='Date d\'arrivée')
    # end_date = fields.Date(required=True, string='Date de départ')


# Cette méthode retourne le nombre de chambres pour chaque hotel

    def get_hotel_room_count(self):
        rooms_data = self.env['gestion_reservations.room'].read_group([('id_hotel', 'in', self.ids)], ['id_hotel'], ['id_hotel'])
        result = dict((data['id_hotel'][0], data['id_hotel_count']) for data in rooms_data)
        for record in self:
            record.hotel_room_count = result.get(record.id, 0)

    hotel_room_count = fields.Integer(compute='get_hotel_room_count', string='Nombre de chambres')
