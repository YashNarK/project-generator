from fastapi import FastAPI
from api.v1.endpoints.api import router as api_router

app=FastAPI()
app.include_router(api_router)

def about():
    return """
    This is a python fastapi based REST API to get project ideas based on user's interests and expertise
"""






if __name__ == "__main__":
    about()
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)