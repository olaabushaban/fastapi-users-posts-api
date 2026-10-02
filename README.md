# Users & Posts API

A simple REST API built with **FastAPI** and **PostgreSQL** to practice the basics of backend development.
It lets you manage users and the posts they write (create, read, update, delete).

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Pydantic (data schemas)

## Project Structure

```
PostgreAndPy/
├── app/
│   ├── routers/
│   │   ├── users.py      # user endpoints
│   │   └── posts.py      # post endpoints
│   ├── database.py       # database connection
│   ├── models.py         # database tables
│   ├── schemas.py        # request/response shapes
│   └── main.py           # app entry point
├── .env.example          # example of required environment variables
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository and go into the project folder.

2. Install the requirements:

   ```
   pip install -r requirements.txt
   ```

3. Create a PostgreSQL database named `blog_db`.

4. Copy `.env.example` to `.env` and put your own database username and password inside it.

5. Run the server from inside the `app` folder:

   ```
   cd app
   uvicorn main:app --reload
   ```

6. Open the interactive docs in your browser: http://127.0.0.1:8000/docs

The tables are created automatically the first time the app starts.

## Endpoints

### Users

| Method | Path | Description |
|--------|------|-------------|
| POST | `/users/` | Create a user |
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get one user |
| PUT | `/users/{user_id}` | Update a user |
| DELETE | `/users/{user_id}` | Delete a user |

### Posts

| Method | Path | Description |
|--------|------|-------------|
| POST | `/users/{user_id}/posts/` | Create a post for a user |
| GET | `/posts/` | Get all posts |
| PUT | `/posts/{post_id}` | Update a post |
| DELETE | `/posts/{post_id}` | Delete a post |

## Roadmap

- [ ] Data validation and proper error handling
- [ ] Authentication