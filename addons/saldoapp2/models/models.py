# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class saldoapp2(models.Model):
#     _name = 'saldoapp2.saldoapp2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Movimiento(models.Model):
    _name = "sa.movimiento"  # Nombre de la Base de Dato sa_movimiento (SQL)
    _description = "Movimiento" # Nombre del modelo en Odoo 'Movimiento'

    name = fields.Char("Concepto")
    monto = fields.Char("Monto")