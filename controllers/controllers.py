# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from datetime import datetime
from odoo.exceptions import ValidationError

# controller hotel

class HotelController(http.Controller):
    @http.route('/hotels', auth='public', website=True)
    def hotel_list(self, **kw):
        hotels = http.request.env['gestion_reservations.hotel'].sudo().search([])
        return http.request.render('gestion_reservations.template_hotels', {'hotels': hotels})

    # route nouvellement créée et qui ne marche pas
    @http.route('/hotel/<int:id_hotel>/chambres/<int:id_room>', website=True, type='http', auth="public")
    def hotel_chambres(self, id_hotel, id_room, **kwargs):
        hotel = request.env['gestion_reservations.hotel'].sudo().browse(id_hotel)
        chambres = request.env['gestion_reservations.room'].sudo().browse(id_room)
        return http.request.render('gestion_reservations.hotel_chambre_template', {'hotel': hotel, 'chambres': chambres})


# controller chambre
class ChambreController(http.Controller):
    @http.route('/chambres', auth='public', website=True)
    def chambre_list(self, **kw):
        chambres = http.request.env['gestion_reservations.room'].search([])
        return http.request.render('gestion_reservations.template_chambres', {'chambres': chambres})

# controller réserver
class ReserverController(http.Controller):
    @http.route('/reserver', type="http", auth='public', website=True, csrf=False) #Ajout des informations liées à room
    def reserver_webform(self, **kw):
        id = kw['room_reserve']
        print(id)
        chambre = request.env['gestion_reservations.room'].sudo().browse(int(id))
        return http.request.render('gestion_reservations.Reserver', {'chambre': chambre}) #Template

    @http.route('/create/reservation', type="http", auth='public', website=True) #Action de reservation
    def create_reservation(self,**kw):
        print("hey....................................", kw)
        # request.env['gestion_reservations.customer'].sudo().create(kw)
        reservation_val={
            'last_name':kw.get('last_name'),
            'first_name': kw.get('first_name'),
            'country':kw.get('country'),
            'phone':kw.get('phone'),
            'email': kw.get('email'),
            'start_date':kw.get('start_date'),
            'end_date':kw.get('end_date')
        }
        request.env['gestion_reservations.reservation'].sudo().create(reservation_val)
        return request.render('gestion_reservations.reserver_thanks', {})

    
    @http.route('/room/reserver', type='http', auth="user")
    def book_now(self, **post):
        # Logique pour charger la route
        # ...
        return request.redirect('/gestion_reservations/reserver')
#     @http.route('/gestion_reservation/gestion_reservation/objects/<model("gestion_reservation.gestion_reservation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_reservation.object', {
#             'object': obj
#         })

