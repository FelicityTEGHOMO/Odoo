from odoo import http
from odoo.http import request

class WebsiteController(http.Controller):

    @http.route('/hotel', auth='public', website=True)
    def my_website(self, **kwargs):
        return request.render('hotel.hotel')

    def get_menu(self):
        menus = request.env['gestion_reservations.hotel'].search([])
        parent_menu = menus.filtered(lambda r: r.name == 'Main menu')
        if parent_menu:
            return parent_menu.child_ids.filtered(lambda r: r.name == 'Hotels')
        else:
            return None

    @http.route('/hotels', auth='public', website=True, menu=get_menu)
    def hotel_list(self, **kwargs):
        hotels = request.env['gestion_reservations.hotel'].sudo().search([])
        return request.render('hotel.hotel_list', {'hotels': hotels})
