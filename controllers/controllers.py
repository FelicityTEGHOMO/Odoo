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
    


class HotelController(http.Controller):
    @http.route('/hotels', auth='public', website=True)
    def hotel_list(self, **kw):
        hotels = http.request.env['gestion_reservations.hotel'].search([])
        return http.request.render('gestion_reservations.template_hotels', {'hotels': hotels})


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
