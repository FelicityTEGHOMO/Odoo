# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservationClient(models.Model):
    _name = 'gestion_reservations.customer'
    _description = 'customer'
    _rec_name = "email"

    id_customer = fields.Char(string="Numéro du client")
    last_name = fields.Char(required=True, string="Nom du client")
    first_name = fields.Char(required=True, string="Prénom du client")
    country = fields.Char(required=True, string="Pays du client")
    phone = fields.Char(required=True, string="Téléphone du client")
    email = fields.Char(required=True,string="Email du client")    
    start_date = fields.Date(string='Date d\'arrivée')
    end_date = fields.Date(string='Date de départ')
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Reservation')