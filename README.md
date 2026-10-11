# Docker RAG Lab

A hands-on project for learning how to build, containerize, and evolve Python-based AI applications.

## Overview

Docker RAG Lab is a learning project focused on building the foundations of Retrieval-Augmented Generation (RAG) systems.

The project currently provides a lightweight REST API built with FastAPI and runs inside a Docker container. It will gradually evolve into a document-based question-answering system.

## Tech Stack

- **Python 3.12**
- **FastAPI** — REST API development
- **Uvicorn** — ASGI server
- **Docker** — Application containerization

## Current Features

- FastAPI application
- Root endpoint (`GET /`)
- Health check endpoint (`GET /health`)
- Docker image build and container execution
- Git version control and GitHub repository

## Getting Started

### Prerequisites

- Docker Desktop or Docker Engine
- Git

### Build the Docker Image

```bash
docker buildx build --load -t rag-lab:v2 .
```

### Run the Container

```bash
docker run -d --name rag-api -p 8000:8000 rag-lab:v2
```

### Test the API

Root endpoint:

```http
GET /
```

Example response:

```json
{
  "message": "Hello from RAG Lab API"
}
```

Health check:

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Interactive API Documentation

Once the container is running, open:

http://localhost:8000/docs

## Planned Development

- Accept JSON requests through POST endpoints
- Document ingestion and text extraction
- Text chunking and embedding generation
- Vector search with Qdrant
- Retrieval-Augmented Generation (RAG) pipeline
- Docker Compose for multi-service deployment
- Configuration and deployment for local or internal environments

## Project Status

**In progress.** This repository is being developed incrementally as a practical learning and engineering project.

## License

To be defined.
