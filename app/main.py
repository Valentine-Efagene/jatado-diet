import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=3000, reload=True)
