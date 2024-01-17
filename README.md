# Project Title

A brief description of your FastAPI project.

## Overview

Explain what your project does and its main features.

## Installation

Provide instructions on how to install and set up your project locally.

```bash
pip install -r requirements.txt
Usage
Explain how to use your FastAPI application.

bash
Copy code
uvicorn main:app --reload
Visit http://127.0.0.1:8000/docs in your browser to access the Swagger UI.

API Endpoint
Describe the API endpoint(s) and their functionality.

/largest_rectangle: [Description]
Example Request
Provide an example of how to make a request to your API.

bash
Copy code
curl -X POST "http://127.0.0.1:8000/largest_rectangle" -H "Content-Type: application/json" -d '{"matrix": [[1,1,1],[1,1,1],[1,1,1]]}'
Example Response
Show an example response from your API.

json
Copy code
{
  "number": 1,
  "area": 9
}
