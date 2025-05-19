from marshmallow import Schema, fields, ValidationError

class LoanApplicationSchema(Schema):
    taxId = fields.String(required=True)
    businessName = fields.String(required=True)
    requestedAmount = fields.Float(required=True)
