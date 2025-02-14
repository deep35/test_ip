from fastapi import FastAPI, Request
import uvicorn
app = FastAPI()

@app.get("/get-user-ip")
async def get_user_ip(request: Request):
    user_ip = request.client.host  # Get the user's real IP
    return {"user_ip": user_ip}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,reload= True)