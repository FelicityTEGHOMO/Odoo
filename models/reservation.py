# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'gestion_reservations.reservation'
    _description = 'reservation'
    _rec_name = "email"

    id_reservation = fields.Char(string="Numéro de la réservation")
    last_name = fields.Char(string="Nom")
    first_name = fields.Char(string="Prénom")
    email = fields.Char(string="Adresse e-mail")
    country = fields.Char(string="Pays du client")
    phone = fields.Char(required=True, string="Téléphone du client")
    start_date = fields.Date(string='Date d\'arrivée')
    end_date = fields.Date(string='Date de départ')
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')
