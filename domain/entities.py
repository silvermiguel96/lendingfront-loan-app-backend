from dataclasses import dataclass


@dataclass
class LoanApplication:
    tax_id: str
    business_name: str
    requested_amount: float
