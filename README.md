# FastAPI Data Processing Server

FastAPI server designed for data processing tasks

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/fastapi-data-processing.git
cd fastapi-data-processing
```

2. Install the project dependencies

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

4. Access the API endpoints

## Project Structure

The current project structure

```bash
fastapi-data-processing/
│
├── routers/
│   ├── __init__.py
│   └── image_router.py
├── services/
│   ├── __init__.py
│   └── opencv_service.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Examples


### Face Detection
- `POST /image/face-detection`
<div 
  style="display:flex; justify-content: space-between;">
    <img src="./images/people.jpg" alt="Image 1"
      style="width:48%; box-sizing: border-box" >
    <img src="./images/people2.png" alt="Image 2"
      style="width:48%; box-sizing: border-box">
</div>





