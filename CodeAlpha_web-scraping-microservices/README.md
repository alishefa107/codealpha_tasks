
# Web Scraping Microservices Architecture

## Project Overview
This project demonstrates a **microservices-based web scraping system**
built using Python (Flask), React, Docker, and message queues.

## Services
- **API Gateway** – Entry point for clients
- **Scheduler Service** – Manages jobs using Celery & Redis
- **Scraper Service** – Scrapes web pages
- **Parser Service** – Cleans & structures data
- **Storage Service** – Stores data in PostgreSQL

## Tech Stack
- Frontend: React + TailwindCSS
- Backend: Python, Flask
- Queue: Celery, Redis
- Database: PostgreSQL
- Deployment: Docker & Docker Compose

## How to Run
```bash
docker-compose up --build
```

## API Usage
- POST `/api/scrape`
- GET `/api/datasets/{id}`

## Author
Ali Shefa
CS Student
