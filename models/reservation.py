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
    total_price = fields.Float(compute='_compute_total_price', string="Total à payer" ,store=True)
    cancellation_policy = fields.Selection([
        ('non_cancellable', 'Non-Cancellable'),
        ('free_cancellation', 'Annulation gratuite jusqu\'à 24 heures avant l\'enregistrement'),
        ('50_percent_charge', '50% de frais si annulé dans les 24 heures avant l\'enregistrement'),
        ('full_charge', 'Frais de 100% si annulé dans les 24 heures avant l\'enregistrement')
    ], string='Conditions d\'annulation', default='free_cancellation')
    # amount_total = fields.Float(string="Montant total", compute='_compute_amount_total', store=True)



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


    @api.depends('start_date', 'end_date', 'id_room.room_amount')
    def _compute_total_price(self):
        for reservation in self:
            nights = (reservation.end_date - reservation.start_date).days
            reservation.total_price = nights * reservation.id_room.room_amount

# Conditions d'annulation 

    @api.constrains('cancellation_policy')
    def check_cancellation_rules(self):
        if self.cancellation_policy == 'non_cancellable':
            # Ne permet pas l'annulation
            return False
        elif self.cancellation_policy == 'free_cancellation':
            # Permet l'annulation sans frais jusqu'à 24 heures avant le check-in
            return self.start_date - timedelta(days=1) > datetime.today().date()
        elif self.cancellation_policy == 'full_charge':
            # Charge intégrale en cas d'annulation
            return False
        else:
            # Réglez à votre convenance
            return True



#récupération des chambres disponibles dans une période spécifiée

    # @api.multi
    # def get_available_rooms(self, start_date, end_date):
    #     domain = [('start_date', '<=', start_date), ('end_date', '>=', end_date), ('state', 'not in', ['occupied'])]
    #     occupied_rooms = self.search(domain).mapped('id_room')
    #     available_rooms = self.env['gestion_reservations.room'].search([('id', 'not in', occupied_rooms.ids)])
    #     return available_rooms
