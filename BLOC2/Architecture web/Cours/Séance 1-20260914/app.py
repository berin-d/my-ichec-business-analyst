from flask import Flask

# 1. Create the application instance
app = Flask(__name__)

# 2. Define a Route
# When user visits http://localhost:5000/
@app.route("/")
def home():
    # Return HTML directly
    return "<h1>Hello, Master Business Analyst!</h1><p>Welcome to Flask.</p>"

# When user visits http://localhost:5000/api
@app.route("/api")
def api_status():
    # Return JSON (ideal for APIs)
    return {"status": "online", "version": 1.0}

# 3. Run the server
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
