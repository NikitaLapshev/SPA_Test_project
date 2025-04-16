# SPA Application: Comments

A simple Single Page Application (SPA) that allows users to leave comments on an image. All comments are saved in a relational database along with identifying user information.

## Features

- Leave comments under an image.
- Store all comments in a relational database.
- Collect and save basic user identification data.

## Tech Stack

- Frontend: HTML, CSS, JS
- Backend: Django
- Database: PostgreSQL
- Containerization: Docker, Docker Compose

## Getting Started

copy all variables from .env.example to .env

```
cp .env.example .env
```

Run application using

```
docker build .
docker-compose up
```
