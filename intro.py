from typing import Optional
import requests
from fastapi import FastAPI,File, UploadFile
from pydantic import BaseModel
from backend.googlevision import upload_file_to_gs, async_detect_document, import_to_excel
import re
import tempfile
import fitz
import cv2


app = FastAPI()


class Item(BaseModel):
    path: str



def create_black(a):
    output_file = "example-with-barcode.pdf"
    barcode_file = "black.png"

    # define the position (upper-right corner)
    image_rectangle = fitz.Rect(280, 100, 590, 570)

    # retrieve the first page of the PDF
    file_handle = fitz.open(a.read())
    first_page = file_handle[0]

    # add the image
    first_page.insertImage(image_rectangle, filename=barcode_file)

    file_handle.save(output_file)
    return output_file


@app.post("/uploadfile/")
def create_upload_item(pdf: UploadFile = File(...)):
    """
    upload file uses spooled file:Spooling is a system function that saves data in a database file for later processing or printing
    """
    #pdf.filename = create_black(pdf.file)
    # save the file
    input_path = upload_file_to_gs(pdf.file, pdf.filename)
    output_path = 'gs://amul/output/' + pdf.filename

    text = async_detect_document(input_path, output_path)
    # import_to_excel(text)
    return {'input_path': input_path, 'output_path': output_path, 'text': text}



