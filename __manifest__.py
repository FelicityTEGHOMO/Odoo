# -*- coding: utf-8 -*-
{
    'name': "Réservations",
    'version': '1.0',
    'summary':'Hotel reservation',
    'description': """
        The module helps you to manage rooms.
        End Users can reserve hotel rooms.
    """,
    'author': "Félicité TEGHOMO",
    'website': "https://hotel-finder.fr",
    'category': 'website',
    'depends': ['base','website','calendar'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/hotel_view.xml',
        'views/room_view.xml',
        'views/customer_view.xml',
        'views/reservation_view.xml',
        'views/menu.xml',
        'views/form_view.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True
}
