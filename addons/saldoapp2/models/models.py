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

    name = fields.Char("Concepto", size= 25,index = True, required=True)

    
    #monto = fields.Char("Monto")

    monto_total = fields.Float("Monto")
    tipo = fields.Selection(selection=[('I','Ingreso'),('E','Egreso')])
    fecha = fields.Date(string='Fecha de Operación' )
    moneda = fields.Selection(string='Moneda', selection=[('PEN','Soles'),('USD','Dolares')])

class Categoria(models.Model):
    _name ="sa.categoria"
    _description = "Categoria"
    _rec_name = "nombre"
    
    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(selection=[('I','Ingreso'),('E','Egreso')])
    active =fields.Boolean(string="Activo",default=True)
   