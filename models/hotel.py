# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservationHotel(models.Model):
    _name = 'gestion_reservations.hotel'
    _description = 'hotel'
    _rec_name = "name_hotel"

    id_hotel = fields.Integer(required=True, string="Numéro de l'hôtel", unique=True)
    name_hotel = fields.Char(string="Nom de l'hôtel")
    description = fields.Char(string="Description de l'hôtel")
    tel_hotel = fields.Char(string="Téléphone de l'hôtel")
    adresse_hotel = fields.Char(string="Adresse de l'hôtel")
    ville = fields.Char(string="Ville de l'hôtel")
    image = fields.Image(string="Logo")
    id_room = fields.One2many('gestion_reservations.room', 'id_hotel', string='Chambre')
  
