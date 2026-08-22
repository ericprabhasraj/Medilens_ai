from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="MediLens AI",
    description="Multimodal Medical Understanding & Patient Education Assistant",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "MediLens AI",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File received successfully"
    }
