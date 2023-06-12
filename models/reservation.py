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
    stay_duration = fields.Integer(string="Durée du séjour", compute="_get_stay_duration")
    amount_total = fields.Float(string="Montant total", compute='_compute_amount_total', store=True)



# condition sur la disponibilité d'une chambre

    @api.constrains('id_room')
    def check_chamber(self):
        rooms= self.env['gestion_reservations.room'].search([('id','=',self.id_room.id)])
        if rooms.state=='Disponible':
            rooms.state='occupied'
        else:
            raise UserError('La chambre est déja réservée')

# à push

# condition sur les dates  

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        for reservation in self:
            if reservation.start_date > reservation.end_date:
                raise ValidationError("La date d'arrivée ne peut pas être supérieure à la date de départ.")

# Méthode pour calculer le nombre de jours de séjour
    @api.depends('id_room')
    def _get_stay_duration(self):
        # rooms= self.env['gestion_reservations.room'].search([('id','=',self.id_room.id)])
        for record in self:
            if reservation.start_date and reservation.end_date:
                delta = record.end_date - record.start_date
                record.stay_duration = delta.days
    reservation.amount_total = record.id_room.room_amount * stay_duration


# Méthode qui calcule le prix à payer en fonction du prix de la chambre et du nombre de jours
#     @api.depends('stay_duration', 'id_room')
#     def _compute_price_to_pay(self):
#         for res in self:
#             if res.stay_duration and res.id_room:
#                 res.price_to_pay = res.id_room.rate * res.stay_duration

# @api.depends('checkin', 'checkout', 'price')
# def _compute_amount_total(self):
#     for reservation in self:
#         if reservation.checkin and reservation.checkout and reservation.price:
#             duration = (reservation.checkout - reservation.checkin).days
#             reservation.amount_total = reservation.price * duration
