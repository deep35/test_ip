from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User IP Address</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            #ip-address {
                font-size: 1.5em;
                color: #007BFF;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Your IP Address is:</h1>
            <p id="ip-address">Loading...</p>
        </div>
        <script>
            // Fetch the user's IP address from the API
            fetch('/get-user-ip')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('ip-address').textContent = data.user_ip;
                })
                .catch(error => {
                    console.error('Error fetching IP address:', error);
                    document.getElementById('ip-address').textContent = 'Unable to fetch IP address';
                });
        </script>
    </body>
    </html>
    """

# API endpoint to get the user's IP address
@app.get("/get-user-ip")
async def get_user_ip(request: Request):
    user_ip = request.client.host  # Get the user's real IP
    return {"user_ip": user_ip}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
