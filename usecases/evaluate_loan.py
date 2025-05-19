from domain.entities import LoanApplication


def evaluate_loan(application: LoanApplication) -> str:
    if application.requested_amount > 50000:
        return "Declined"
    elif application.requested_amount == 50000:
        return "Undecided"
    else:
        return "Approved"
