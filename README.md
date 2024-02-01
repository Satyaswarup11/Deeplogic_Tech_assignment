#Programming Test

The application utilizes the Flask framework to create a simple web service that retrieves and parses content from the Time website.

## Getting Started

Make sure you have [Flask](https://flask.palletsprojects.com/) installed. You can install it using:

```bash
pip install flask

# Clone the repository and navigate to the project directory.
git clone https://github.com/your-username/your-repository.git
cd your-repository

# Usage
# Run the Flask application using the following command:
python app.py

# The application will be accessible at http://127.0.0.1:5000/. 
# Use the /getTimeStories endpoint to get the latest six stories in JSON format.
# Example:
curl http://127.0.0.1:5000/getTimeStories

# Error Handling
The application includes basic error handling to manage failed requests or unexpected errors during the process.

# Dependencies
- Flask
- Requests
