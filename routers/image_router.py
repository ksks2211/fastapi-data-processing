from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
# from services.opencv_service import get_detector, FaceDetector
from services.mtcnn_service import get_detector, FaceDetector

from io import BytesIO

router = APIRouter(
    prefix="/image",
    tags=['image']
)


@router.post("/face-detect")
async def process_image(file: UploadFile = File(...), detector: FaceDetector = Depends(get_detector)):
    print(file.filename)
    image_contents = await file.read()
    image_processed = detector.detect(image_contents)
    return StreamingResponse(BytesIO(image_processed), media_type="image/png")
