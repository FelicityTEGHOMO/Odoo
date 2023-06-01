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
    @http.route('/reserver/<int:id_room>', type="http", auth='public', website=True) #Ajout des informations liées à room
    def reserver_webform(self,id_room, **kw):
        chambre = request.env['gestion_reservations.room'].sudo().browse(id_room)
        return http.request.render('gestion_reservations.Reserver', {'chambre': chambre}) #Template

    @http.route('/create/reservation', type="http", auth='public', website=True) #Action de reservation
    def create_reservation(self,**kw):
        print("hey....................................", kw)
        request.env['gestion_reservations.customer'].sudo().create(kw)
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

# j'ai rajouté la méthode is_available
class MonController(http.Controller):
    @http.route('/reserver/<model("gestion_reservations.room"):chambre>', type='http', auth="public", website=True)

    def is_available(self, start_date, end_date):
        reservations = self.reservations.filtered(lambda r: r.start_date <= end_date and r.end_date >= start_date)
        return len(reservations) == 0
    def action_reserver(self, chambre, **post):
        # Récupération des données du formulaire de réservation:
        last_name = post.get('last_name'),
        first_name = post.get('first_name')
        email = post.get('email')
        ville = post.get('ville')
        start_date = datetime.strptime(post.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(post.get('end_date'), '%Y-%m-%d')

        # Vérifier si la chambre est disponible pour la période souhaitée
        if chambre.is_available(start_date, end_date):
            # créer une ligne de réservation associée à la chambre
            self.env['gestion_reservations.reservation'].create({
                'last_name': last_name,
                'first_name': first_name,
                'email': email,
                'ville': ville,
                'id_room': chambre.id,
                'start_date': start_date,
                'end_date': end_date,
            })
            # # Retourner un message de succès
            return _("Réservation effectuée avec succès pour la chambre %s.") % (chambre.room_number,)
        else:
            # Si la chambre n'est pas disponible, retourner un message d'erreur
            raise ValidationError(_("La chambre %s n'est pas disponible pour les dates demandées.") % (chambre.room_number,))

# contoller qui renvoie les détails sur une chambre
class MyRoomController(http.Controller):

    @http.route('/my-room-details/<int:id_room>', auth='public', website=True)
    def room_details(self, id_room=None, **kwargs):
        room = request.env['gestion_reservations.room'].browse(id_room)
        room_data = {
            'Numéro de la chambre': room.room_number,
            'Prix de la chambre': room.room_amount,
            'Téléphone de la chambre': room.room_tel,
            'Capacité' : room.capacity,
            'Images' : room.image,
            'Type' : room.types,
            'Statut' : room.state
        }

        return request.env.ref('gestion_reservations.room_details_template', {'room': room, 'room_data': room_data})

# Action sur le click
class RoomController(http.Controller):
    
    @http.route('/rooms/<int:room_id>/reservation', auth='public', website=True)
    def room_reservation(self, room_id, **kwargs):
        Room = request.env['gestion_reservations.room'].browse(room_id)
        if not Room:
            return request.redirect('/rooms')
        return http.request.render('gestion_reservations.gestion_reservations.room', {
            'room': Room
        })
    
    @http.route('/rooms', auth='public', website=True)
    def room_list(self, **kwargs):
        Room = request.env['gestion_reservations.room']
        rooms = Room.search([])
        
        return http.request.render('gestion_reservations.room_details_template', {
            'rooms': rooms,
        })






















    # class MyController(http.Controller):
    #     @http.route('/my_route', type='http', auth="public", website=True)
    #     def action_reserver(self, **post):
    #         # do something when button is clicked
    #         return "Button clicked!"


    # @http.route('/gestion_reservation/gestion_reservation/hotels', auth='public')
    # def list(self, **kw):
    #     return http.request.render('gestion_reservation.listing', {
    #         'root': '/gestion_reservation/gestion_reservation',
    #         'objects': http.request.env['gestion_reservations.hotel'].search([]),
    #     })


class MonModeleController(http.Controller):
    
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

