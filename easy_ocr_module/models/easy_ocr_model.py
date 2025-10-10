from odoo import models, fields

class EasyOcrModel(models.Model):
    _name = 'easy.ocr.model'
    _description = 'Easy OCR Model'

    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')