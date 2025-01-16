import os

from app import create_app



print("Current working directory:", os.getcwd())  # Print current working directory

# Create an instance of the Flask application
app = create_app()

if __name__ == '__main__':
    print("Flask app is running on http://127.0.0.1:5000/")
    port = int(os.environ.get('PORT', 5000))  # Get the port from environment variable
    app.run(host='0.0.0.0', port=port, debug=True)
