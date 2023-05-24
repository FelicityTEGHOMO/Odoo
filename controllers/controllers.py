# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class HotelController(http.Controller):

#     @http.route('/hotels', auth='public', website=True)
    # def hotel_list(self, **kwargs):
#         hotels = request.env['gestion_reservations.hotel'].sudo().search([])
#         return request.render('my_website.hotel_list', {'hotels': hotels})



# class GestionReservation(http.Controller):
#     @http.route('/shop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"
    

# controller hotel

class HotelController(http.Controller):
    @http.route('/hotels', auth='public', website=True)
    def hotel_list(self, **kw):
        hotels = http.request.env['gestion_reservations.hotel'].search([])
        return http.request.render('gestion_reservations.template_hotels', {'hotels': hotels})

# controller chambre
class ChambreController(http.Controller):
    @http.route('/chambres', auth='public', website=True)
    def hotel_list(self, **kw):
        chambres = http.request.env['gestion_reservations.room'].search([])
        return http.request.render('gestion_reservations.template_chambres', {'chambres': chambres})



# controller réserver
class ReserverController(http.Controller):
    @http.route('/reserver', auth='public', website=True)
    def hotel_list(self, **kw):
        reservations = http.request.env['gestion_reservations.reservation'].search([])
        return http.request.render('gestion_reservations.template_reservations', {'reservations': reservations})

    # @http.route('/gestion_reservation/gestion_reservation/hotels', auth='public')
    # def list(self, **kw):
    #     return http.request.render('gestion_reservation.listing', {
    #         'root': '/gestion_reservation/gestion_reservation',
    #         'objects': http.request.env['gestion_reservations.hotel'].search([]),
    #     })

#     @http.route('/gestion_reservation/gestion_reservation/objects/<model("gestion_reservation.gestion_reservation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_reservation.object', {
#             'object': obj
#         })
