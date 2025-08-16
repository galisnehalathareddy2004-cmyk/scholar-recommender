from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Test route
@app.get("/")
def home():
    return {"message": "Scholarship Recommender Backend is running 🚀"}
