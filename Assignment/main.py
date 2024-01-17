# Import necessary modules
import logging  # Import the logging module for logging
from fastapi import FastAPI, Request, HTTPException  # Import necessary FastAPI modules
from typing import List  # Import List type from the typing module
import time  # Import the time module for measuring time
import json  # Import the json module for working with JSON data
from pydantic import BaseModel  # Import the BaseModel class from pydantic

# Set up logging
logger = logging.getLogger(__name__)  # Create a logger instance with the __name__ of the current module

# Define Pydantic model for request validation
class MatrixRequest(BaseModel):
    matrix: List[List[int]]  # Define a Pydantic model to validate the request's JSON structure

# Define the function to find the largest rectangle in the matrix
def largest_rectangle(matrix: List[List[int]]) -> tuple:
    try:
        m = len(matrix)  # Get the number of rows in the matrix
        n = len(matrix[0])  # Get the number of columns in the matrix

        heights = [0] * n  # Initialize a list to store the heights of the rectangles
        left = [0] * n  # Initialize a list to store the left boundaries of the rectangles
        right = [n] * n  # Initialize a list to store the right boundaries of the rectangles

        max_area = 0  # Initialize a variable to track the maximum area
        max_number = None  # Initialize a variable to track the number corresponding to the maximum area

        for i in range(m):  # Iterate through each row of the matrix
            current_left = 0  # Initialize a variable to track the current left boundary
            for j in range(n):  # Iterate through each column of the matrix
                try:
                    if matrix[i][j] == 0:
                        heights[j] = 0
                        left[j] = 0
                        right[j] = n
                    else:
                        heights[j] += 1
                        left[j] = max(left[j], current_left)
                except IndexError:
                    print(f"IndexError: matrix[{i}][{j}] is out of range")

            for j in range(n - 1, -1, -1):  # Iterate through each column in reverse
                try:
                    if matrix[i][j] == 0:
                        right[j] = n
                    else:
                        right[j] = min(right[j], n - current_left)
                        current_left += 1
                except IndexError:
                    print(f"IndexError: matrix[{i}][{j}] is out of range")

            for j in range(n):  # Iterate through each column
                area = heights[j] * (right[j] - left[j])  # Calculate the area of the rectangle
                if area > max_area:  # If the area is greater than the current maximum area
                    max_area = area  # Update the maximum area
                    max_number = matrix[i][j]  # Update the number corresponding to the maximum area

        return max_number, max_area  # Return the tuple containing the number and area
    except Exception as e:
        print(f"Exception in largest_rectangle: {e}")  # Print the exception if an error occurs
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Raise an HTTPException for internal server error

# Create a FastAPI application instance
app = FastAPI()  # Create a FastAPI instance

# Define a POST endpoint to find the largest rectangle
@app.post("/largest_rectangle")
async def find_largest_rectangle(request: MatrixRequest):
    try:
        matrix = request.matrix  # Extract the matrix from the request
        start_time = time.time()  # Record the start time for measuring turnaround time
        number, area = largest_rectangle(matrix)  # Call the function to find the largest rectangle
        end_time = time.time()  # Record the end time for measuring turnaround time
        turnaround_time = end_time - start_time  # Calculate the turnaround time

        # Log request, response, and turnaround time to the database (commented, actual implementation not provided)
        # Implement your database logging here

        return {"number": number, "area": area}  # Return the response JSON containing the number and area
    except Exception as e:
        logger.error(f"Error in find_largest_rectangle: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Raise an HTTPException for internal server error
