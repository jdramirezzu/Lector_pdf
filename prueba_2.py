# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:22:43 2021

@author: analista4operaciones
"""

from pdf2docx import Converter 
from docx2pdf import convert
import PyPDF2


def extract_page(doc_name, page_num):
    pdf_reader = PyPDF2.PdfFileReader(open('cartas.pdf', 'rb')) #Se crea objeto para leer pdf
    pdf_writer = PyPDF2.PdfFileWriter() #Se crea objeto para escribir pdf
    pdf_writer.addPage(pdf_reader.getPage(page_num)) #Se crea nuevo pdf
    informacion = pdf_reader.getPage(page_num) #Obtener pagina del archivo
    texto = informacion.extractText() #leer el texto de la pagina
    texto_2 = texto.split() #hacer una lista con el texto encontrado
    texto_3 = texto.splitlines()