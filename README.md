# Loan Application API

This is a simple Flask-based backend API for evaluating loan applications. It provides an endpoint for small business owners to apply for loans and get an instant decision based on the requested amount.

## Features

* POST `/api/v1/loan/apply` endpoint to submit loan applications
* Input validation using Marshmallow
* Standardized API responses via middleware
* Swagger UI documentation with Flasgger
* CORS enabled for cross-origin requests
* Environment variables support with `.env` file

## Getting Started

### Prerequisites

* Python 3.8+
* `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file to set environment variables (optional):

   ```
   PORT=5000
   ```

### Running the Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`.

### Swagger UI

Access the API documentation and try the endpoints interactively at:

```
http://localhost:5000/apidocs/
```

## API Usage

### Apply for a Loan

**Endpoint:** `POST /api/v1/loan/apply`

**Request body:**

```json
{
  "tax_id": "123456789",
  "business_name": "My Business",
  "requested_amount": 30000
}
```

**Response example:**

```json
{
  "statusCode": 200,
  "message": "Success",
  "details": [{
    "loanDecision": "Approved"
  }]
}
```

## Project Structure

* `app.py` — Main Flask app initialization
* `interfaces/routes.py` — API route definitions
* `infrastructure/validators.py` — Marshmallow schemas
* `infrastructure/middleware.py` — Middleware for standard responses
* `usecases/evaluate_loan.py` — Loan evaluation logic
* `domain/entities.py` — Data models/entities

## Testing with curl

Example:

```bash
curl -X POST http://localhost:5000/api/v1/loan/apply \
  -H "Content-Type: application/json" \
  -d '{"tax_id":"123456789", "business_name":"My Business", "requested_amount":30000}'
```

## License

MIT License

---

If you want, I can help you tailor it more or add sections like deployment or testing. Just tell me!
