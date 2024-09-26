# French Public Universities API

This is a simple API that provides information about French public universities. The API is built using FastAPI.

## Features

- Get a list of all universities.
- Get university details by ID, region, department, city, academy, or institution type.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/DJOMIDO/university-api.git
   cd university-api

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Run the application:

   ```bash
    uvicorn main:app --reload
   
4. Open your browser and navigate to: http://127.0.0.1:8000

## API Endpoints

- `GET /universities/`: Get a list of all universities.
- `GET /universities/name/{university_name}`: Get university details by name.
- `GET /universities/{id}`: Get university details by ID.
- `GET /universities/region/{region}`: Get university details by region.
- `GET /universities/department/{department}`: Get university details by department.
- `GET /universities/city/{city}`: Get university details by city.
- `GET /universities/academy/{academy}`: Get university details by academy.
- `GET /universities/type/{institution_type}`: Get university details by institution type.

## Documentation

FastAPI automatically generates API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
