from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from flasgger import swag_from
from infrastructure.validators import LoanApplicationSchema
from infrastructure.middleware import standard_response
from usecases.evaluate_loan import evaluate_loan
from domain.entities import LoanApplication

bp = Blueprint('loan', __name__)

@bp.route('/loan/apply', methods=['POST'])
@standard_response
@swag_from({
    'tags': ['Loans'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'tax_id': {'type': 'string', 'example': '123456789'},
                    'business_name': {'type': 'string', 'example': 'Mi Empresa'},
                    'requested_amount': {'type': 'number', 'example': 40000}
                },
                'required': ['tax_id', 'businessName', 'requestedAmount']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Loan application processed successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'statusCode': {'type': 'integer', 'example': 200},
                    'message': {'type': 'string', 'example': 'Loan application processed'},
                    'details': {'type': 'array', 'items': {'type': 'string'}, 'example': ['Loan Approved']}
                }
            }
        },
        400: {
            'description': 'Validation error or bad request',
            'schema': {
                'type': 'object',
                'properties': {
                    'statusCode': {'type': 'integer', 'example': 400},
                    'message': {'type': 'string', 'example': 'Invalid input'},
                    'details': {'type': 'array', 'items': {'type': 'string'}, 'example': ['taxId is required']}
                }
            }
        }
    }
})
def evaluate_loan_route():
    json_data = request.get_json()
    if not json_data:
        return {
            "statusCode": 400,
            "message": "No input data provided",
            "details": []
        }, 400
    
    schema = LoanApplicationSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        # Flatten error messages para que sea un array de strings
        errors = []
        for field, msgs in err.messages.items():
            for msg in msgs:
                errors.append(f"{field}: {msg}")

        return {
            "statusCode": 400,
            "message": "Invalid input",
            "details": errors
        }, 400

    application = LoanApplication(
        tax_id=data['taxId'],
        business_name=data['businessName'],
        requested_amount=data['requestedAmount']
    )

    decision = evaluate_loan(application)

    return {"loanDecision": decision}
