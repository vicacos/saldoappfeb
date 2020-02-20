# -*- coding: utf-8 -*-
from odoo import http

# class Saldoapp2(http.Controller):
#     @http.route('/saldoapp2/saldoapp2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saldoapp2/saldoapp2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saldoapp2.listing', {
#             'root': '/saldoapp2/saldoapp2',
#             'objects': http.request.env['saldoapp2.saldoapp2'].search([]),
#         })

#     @http.route('/saldoapp2/saldoapp2/objects/<model("saldoapp2.saldoapp2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saldoapp2.object', {
#             'object': obj
#         })