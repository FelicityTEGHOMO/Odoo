# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'gestion_reservations.reservation'
    _description = 'reservation'
    _rec_name = "id_reservation"

    id_reservation = fields.Char(required=True,string="Numéro de la réservation")
    last_name = fields.Char(required=True, string="Nom")
    first_name = fields.Char(required=True, string="Prénom")
    email = fields.Char(required=True, string="Adresse e-mail")
    adresse = fields.Char(required=True, string="Adresse")
    ville = fields.Char(required=True,string="Ville")
    start_date = fields.Date(required=True, string='Date d\'arrivée')
    end_date = fields.Date(required=True, string='Date de départ')
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')