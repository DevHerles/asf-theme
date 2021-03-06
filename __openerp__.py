# -*- coding: utf-8 -*-
# Copyright 2016 Openworx, LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Bootstrap Backend Theme",
    "summary": "Odoo 10.0 community backend theme",
    "version": "10.0.1.0.18",
    "category": "Themes/Backend",
    "website": "http://www.arandasf.com",
	"description": """
		Backend theme for Odoo 10.0 community edition.
		The app dashboard is based on the module web_responsive from LasLabs Inc and the theme on Bootstrap United.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "ArandaSF",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'sale',
        'base'
    ],
    "data": [
        'views/assets.xml',
        'views/web.xml',
    ],
    "qweb":[
        # 'views/qweb.xml',
    ]
}

