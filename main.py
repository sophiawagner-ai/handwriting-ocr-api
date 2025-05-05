from fastapi import FastAPI, File, UploadFile, HTTPException
from ocr_service import recognize_text_from_image
from llm_service import correct_text_with_llm

app = FastAPI()


# ------------------------------------------------------------------------------
@app.post("/recognize-handwriting")
async def recognize_handwriting(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = recognize_text_from_image(image_bytes)
        if not result:
            return {"message": "Kein Text erkannt"}

        original_text = "\n".join(result)
        corrected_text = correct_text_with_llm(original_text)

        return {
            "Erkannter Text": corrected_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
