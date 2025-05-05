# Handwriting OCR API

This project provides a simple, locally executable API for recognizing handwritten text in images. It is built with FastAPI and PyTorch and designed to be modular, extendable, and self-contained.

## Features

- OCR for handwritten text (image input)
- Modular structure with separate OCR and optional LLM service
- Fully local execution – no third-party APIs required
- Docker-ready

## Installation

1. Clone the repository  
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open your browser at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

- `POST /ocr` – Upload an image and receive recognized text  
- `POST /llm` – Optional endpoint using a local language model (if available)

## Docker Usage (Optional)

```bash
docker build -t handwriting-ocr .
docker run -p 8000:8000 handwriting-ocr
```

## File Overview

- `main.py` – FastAPI application
- `ocr_service.py` – OCR model and logic
- `llm_service.py` – Optional language model handler
- `requirements.txt` – Dependencies
- `Dockerfile` – Container setup

## Notes

- Designed as a foundation for more advanced OCR tasks  
- Easily extendable with other models or postprocessing logic  
- Multi-line recognition and spelling correction can be added

---

Built with ❤️ and curiosity. Contributions welcome!
