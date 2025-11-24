# FastAPI Async Application

A professional FastAPI application with async support, structured for scalability and maintainability.

## Project Structure

```
Backend/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── vehicles.py
│   │       ├── orders.py
│   │       ├── payments.py
│   │       └── invoices.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── vehicle.py
│   │   ├── service_history.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── invoice.py
│   └── schemas/
│       ├── __init__.py
│       ├── user.py
│       ├── vehicle.py
│       ├── order.py
│       ├── payment.py
│       └── invoice.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Features

- ✅ **Async/Await**: Full async support with AsyncIO and async SQLAlchemy
- ✅ **Professional Structure**: Clean separation of concerns (routes, models, schemas, config)
- ✅ **Database Models**: SQLAlchemy models with relationships based on your schema
- ✅ **API Routes**: Separate route files for each resource (users, vehicles, orders, etc.)
- ✅ **Pydantic Schemas**: Request/response validation with Pydantic v2
- ✅ **CRUD Operations**: Complete Create, Read, Update, Delete operations for all resources
- ✅ **Auto Documentation**: Swagger UI at `/docs` and ReDoc at `/redoc`
- ✅ **Health Check**: Health check endpoint at `/health`
- ✅ **CORS Support**: Configured CORS middleware
- ✅ **Environment Config**: Settings management with Pydantic Settings

## Setup Instructions

### 1. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env` and update the values:

```powershell
Copy-Item .env.example .env
```

Edit `.env` with your database credentials:

```
DATABASE_URL=postgresql+asyncpg://your_user:your_password@localhost:5432/your_db_name
```

### 4. Setup PostgreSQL Database

Install PostgreSQL if not already installed, then create a database:

```sql
CREATE DATABASE your_database_name;
```

### 5. Run the Application

```powershell
uvicorn main:app --reload
```

Or simply:

```powershell
python main.py
```

The application will be available at:

- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Database Tables

The application automatically creates the following tables on startup:

- `users` - User management with roles (admin, client, dealer, owner, PartnerApp)
- `vehicles` - Complete vehicle information with 50+ fields
- `service_history` - Vehicle service records
- `orders` - Order management with user and vehicle relationships
- `payments` - Payment tracking for orders
- `invoices` - Invoice generation and management

## API Endpoints

### Users

- `POST /api/v1/users/` - Create user
- `GET /api/v1/users/` - List users (with pagination)
- `GET /api/v1/users/{user_id}` - Get user by ID
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Vehicles

- `POST /api/v1/vehicles/` - Create vehicle
- `GET /api/v1/vehicles/` - List vehicles (with pagination)
- `GET /api/v1/vehicles/{vehicle_id}` - Get vehicle by ID
- `PUT /api/v1/vehicles/{vehicle_id}` - Update vehicle
- `DELETE /api/v1/vehicles/{vehicle_id}` - Delete vehicle

### Orders

- `POST /api/v1/orders/` - Create order
- `GET /api/v1/orders/` - List orders (with pagination)
- `GET /api/v1/orders/{order_id}` - Get order by ID
- `PUT /api/v1/orders/{order_id}` - Update order
- `DELETE /api/v1/orders/{order_id}` - Delete order

### Payments

- `POST /api/v1/payments/` - Create payment
- `GET /api/v1/payments/` - List payments (with pagination)
- `GET /api/v1/payments/{payment_id}` - Get payment by ID
- `PUT /api/v1/payments/{payment_id}` - Update payment
- `DELETE /api/v1/payments/{payment_id}` - Delete payment

### Invoices

- `POST /api/v1/invoices/` - Create invoice
- `GET /api/v1/invoices/` - List invoices (with pagination)
- `GET /api/v1/invoices/{invoice_id}` - Get invoice by ID
- `PUT /api/v1/invoices/{invoice_id}` - Update invoice
- `DELETE /api/v1/invoices/{invoice_id}` - Delete invoice

## Development

### Running Tests

```powershell
pytest
```

### Database Migrations (Optional - using Alembic)

Initialize Alembic:

```powershell
alembic init alembic
```

Create migration:

```powershell
alembic revision --autogenerate -m "Initial migration"
```

Apply migration:

```powershell
alembic upgrade head
```

## Architecture Highlights

- **Async Database Operations**: All database operations use async/await for better performance
- **Dependency Injection**: FastAPI's dependency injection for database sessions
- **Type Safety**: Full type hints throughout the codebase
- **Separation of Concerns**: Clear separation between routes, models, schemas, and business logic
- **Scalable Structure**: Easy to add new routes, models, and features
- **Production Ready**: Configured for production deployment with proper error handling

## Next Steps

Consider adding:

- Authentication & Authorization (JWT tokens)
- Rate limiting
- Caching (Redis)
- Logging configuration
- API versioning strategy
- Background tasks (Celery)
- Testing suite
- Docker containerization
- CI/CD pipeline
