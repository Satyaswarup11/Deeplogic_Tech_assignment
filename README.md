# Programming Test

The application utilizes the Flask framework to create a simple web service that retrieves and parses content from the Time website.

## Getting Started

Make sure you have [Flask](https://flask.palletsprojects.com/) installed. You can install it using:

```bash
pip install flask
```

## Clone the repository and navigate to the project directory.
```bash
git clone https://github.com/Satyaswarup11/Deeplogic_Tech_assignment.git
cd Deeplogic_Tech_assignment
```

## Usage
 Run the Flask application using the following command:
```bash
python app.py
```

Use the /getTimeStories endpoint to get the latest six stories in JSON format.
Example:
```bash
curl http://<localhost>/getTimeStories
```

## Error Handling

The application includes basic error handling to manage failed requests or unexpected errors during the process.

## Dependencies
- Flask
- Requests
