# -*- coding: utf-8 -*-

from odoo import models, fields


class ReservationRoom(models.Model):
    _name = 'gestion_reservations.room'
    _description = 'room'
    _rec_name = 'room_number'

    # name = fields.Char(help='chambre', required=True)
    id_room = fields.Integer(required=True, string='Identifiant de chambre')
    room_number = fields.Char(required=True, string='Numéro de chambre')
    room_amount = fields.Integer(required=True, string='Prix de la chambre')
    room_tel = fields.Char(required=True, string='Téléphone de la chambre')
    capacity = fields.Integer(required=True, string='Capacité')
    image = fields.Image(string="Images")
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
    state = fields.Selection([('disponible', 'Disponible'),
                                 ('occupied', 'Occupée')], 
                                 string='Statut'
                        )
    id_hotel = fields.Many2one('gestion_reservations.hotel', required=True, string='Hôtel')
    id_reservation = fields.Many2one('gestion_reservations.reservation', string='Réservation') # j'ai remplacé many2one par One2many
    id_customer = fields.Many2one('gestion_reservations.customer', string='Client')


    def set_room_state(self, id_room, state):
        room = self.browse(id_room)
        #  la méthode browse est utilisée pour récupérer l'enregistrement d'une chambre correspondant à un identifiant
        if room:
            room.state = state




    # def action_confirm(self):
    #     self.write({'state': 'confirm'})
    #     self.sale_order_id.write({'invoice_status': 'to invoice', 'state': 'sale'})

    # def action_cancel(self):
    #     self.state = 'cancel'
    #     for rec in self.reservation_line_ids:
    #         rec.room_id.write({'status': 'available'})

     


#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
