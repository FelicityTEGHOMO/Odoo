# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReservationClient(models.Model):
    _name = 'gestion_reservations.customer'
    _description = 'customer'
    _rec_name = "id_customer"

    id_customer = fields.Char(required=True,string="Numéro du client")
    last_name = fields.Char(required=True, string="Nom du client")
    first_name = fields.Char(required=True, string="Prénom du client")
    country = fields.Char(required=True, string="Pays du client")
    phone = fields.Char(required=True, string="Téléphone du client")
    email_customer = fields.Char(required=True,string="Email du client")
    id_room = fields.Many2one('gestion_reservations.room', string='Chambre')
    id_reservaton = fields.Many2one('gestion_reservations.reservation', string='Reservation')