# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

class SimpleExpenseCategory(models.Model):
    _name = "simple.expense.category"
    _description = "Categoria Gasto Simple"

    name = fields.Char('Nombre', required=True)
    code = fields.Char('Codigo', required=True)