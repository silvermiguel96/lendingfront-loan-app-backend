from marshmallow import Schema, fields, ValidationError

class LoanApplicationSchema(Schema):
    taxId = fields.String(required=True, data_key="tax_id")
    businessName = fields.String(required=True, data_key="business_name")
    requestedAmount = fields.Float(required=True, data_key="requested_amount")
