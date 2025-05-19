from flask import Blueprint, request
from marshmallow import ValidationError
from infrastructure.validators import LoanApplicationSchema
from infrastructure.middleware import standard_response
from usecases.evaluate_loan import evaluate_loan
from domain.entities import LoanApplication

bp = Blueprint('routes', __name__)

@bp.route('/evaluate-loan', methods=['POST'])
@standard_response
def evaluate_loan_route():
    json_data = request.get_json()
    if not json_data:
        return {"error": "No input data provided"}, 400
    
    schema = LoanApplicationSchema()
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    application = LoanApplication(
        tax_id=data['taxId'],
        business_name=data['businessName'],
        requested_amount=data['requestedAmount']
    )

    decision = evaluate_loan(application)

    return {"loanDecision": decision}
