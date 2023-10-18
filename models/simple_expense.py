# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

class SimpleExpense(models.Model):
    _name = "simple.expense"
    _description = "Gasto Simple"
    _order = "date_expense desc"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nombre')
    reference = fields.Char('Referencia')
    state = fields.Selection(selection=[
        ('draft', 'Borrador'),
        ('done', 'Hecho'),
        ('cancel', 'Cancelado')
    ], default='draft', string='Estados', copy=False)
    category_expense = fields.Many2one('simple.expense.category', 'Categoria')
    date_expense = fields.Date('Fecha de gasto', required=True)
    expense_manager_id = fields.Many2one('res.partner', 'Responsable de gasto', required=True)
    supplier_id = fields.Many2one('res.partner', 'Proveedor')
    simple_expense_ids = fields.One2many('simple.expense.line','simple_expense_id','Lineas de gasto')
    total = fields.Float('Total', compute='_compute_total', store = True)

    @api.depends('simple_expense_ids')
    def _compute_total(self):
        for ref in self:
            ref.total = 0
            for line in ref.simple_expense_ids:
                ref.total += line.total
    
    def done_expense(self):
        self.state = 'done'
        
    def cancel_expense(self):
        self.state = 'cancel'
        
    def draft_expense(self):
        self.state = 'draft'

    @api.model
    def create(self, var):
        sequence_obj = self.env['ir.sequence']
        correlative = sequence_obj.next_by_code('expense.sequence')
        var['name'] = correlative
        return super(SimpleExpense, self).create(var)

class SimpleExpenseLine(models.Model):
    _name = "simple.expense.line"
    _description = "Linea Gasto Simple"

    simple_expense_id = fields.Many2one('simple.expense', 'Simple Expense')
    name = fields.Char('Gasto', required=True)
    product = fields.Many2one('product.product', 'Producto')
    qty = fields.Float('Cantidad')
    price = fields.Float('Precio')
    total = fields.Float('Total')

    @api.onchange('price', 'qty')
    def _onchange_total(self):
        self.total = (self.price * self.qty)