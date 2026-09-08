URL Shortener API
A production-ready URL shortener service built with FastAPI, PostgreSQL, and SQLAlchemy. Shorten long URLs, track click analytics, and manage redirects with ease.

---

## Features

- Shorten long URLs into unique short codes
- Redirect users to the original URL
- Track click counts for each shortened link
- View analytics and statistics
- Interactive API documentation (Swagger UI)
- Modular and scalable architecture
- Environment-based configuration

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Core programming language |
| FastAPI | Web framework for building APIs |
| PostgreSQL | Relational database for storing URLs |
| SQLAlchemy | ORM for database interaction |
| Pydantic | Data validation and serialization |
| Uvicorn | ASGI server for running FastAPI |
| python-dotenv | Environment variable management |

---

## Project Structure

```
url-shortener-api/
├── app/
│   ├── __init__.py      # Package initializer
│   ├── main.py          # API endpoints and server
│   ├── database.py      # Database connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # Database operations
│   └── utils.py         # Helper functions
├── .env                 # Environment variables
├── .gitignore           # Ignored files
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── LICENSE              # MIT License
```

---

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database

Create a database in PostgreSQL:

```sql
CREATE DATABASE url_shortener;
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/url_shortener
```

### 5. Run the Application

```bash
python app/main.py
```

### 6. Access the API

Open your browser and go to:

```
http://localhost:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| POST | `/shorten` | Shorten a long URL |
| GET | `/{short_code}` | Redirect to original URL |
| GET | `/stats/{short_code}` | Get click statistics |

---

## Example Usage

### Shorten a URL

**Request:**

```json
POST /shorten
{
  "original_url": "https://www.google.com"
}
```

**Response:**

```json
{
  "short_code": "abc123",
  "original_url": "https://www.google.com",
  "short_url": "http://localhost:8000/abc123",
  "clicks": 0,
  "created_at": "2024-01-01T12:00:00"
}
```

### Redirect

Visit: `http://localhost:8000/abc123`

### Get Stats

**Request:**

```
GET /stats/abc123
```

**Response:**

```json
{
  "short_code": "abc123",
  "original_url": "https://www.google.com",
  "clicks": 5,
  "created_at": "2024-01-01T12:00:00"
}
```

---

## Database Schema

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| short_code | String | Unique short URL code |
| original_url | Text | Original long URL |
| created_at | Timestamp | Creation time |
| clicks | Integer | Number of redirects |

---

## Dependencies

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
python-dotenv
```

---

## License

This project is licensed under the MIT License.
```

---

## How to Use

1. Go to your repository on GitHub
2. Click on `README.md`
3. Click the pencil icon (Edit)
4. Delete everything
5. Paste the above content
6. Click **"Commit changes"**
