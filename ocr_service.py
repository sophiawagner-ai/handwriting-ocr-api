from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import time
import io
import os

load_dotenv()

ocr_api_key = os.getenv("AZURE_OCR_API_KEY")
ocr_endpoint = os.getenv("AZURE_OCR_ENDPOINT")


# ------------------------------------------------------------------------------
def initialize_client():
    if ocr_api_key and ocr_endpoint:
        return ComputerVisionClient(ocr_endpoint, CognitiveServicesCredentials(ocr_api_key))


# ------------------------------------------------------------------------------
def recognize_text_from_image(image_bytes):
    client = initialize_client()
    image_stream = io.BytesIO(image_bytes)
    result = client.read_in_stream(image_stream, language="de", raw=True)

    operation_id = result.headers["Operation-Location"].split("/")[-1]

    while client.get_read_result(operation_id).status in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
        time.sleep(1)

    result = client.get_read_result(operation_id)
    return [line.text for line in result.analyze_result.read_results[0].lines] if result.status == OperationStatusCodes.succeeded else []
