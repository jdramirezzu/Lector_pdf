# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:17:52 2021

@author: analista4operaciones
"""


from pdf2docx import Converter 
from docx2pdf import convert
import PyPDF2


def pdf_word(doc_pdf, doc_word):
    pdf_file ='cartas.pdf' 
    docx_file ='cartas.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
 
# convertir word a pdf   
def word_pdf(doc_word, doc_pdf):
    convert("cartas.docx")
    convert("cartas.docx", "cartas.pdf")
    
    
def extract_page(doc_name, page_num):
    pdf_reader = PyPDF2.PdfFileReader(open('cartas.pdf', 'rb')) #Se crea objeto para leer pdf
    pdf_writer = PyPDF2.PdfFileWriter() #Se crea objeto para escribir pdf
    pdf_writer.addPage(pdf_reader.getPage(page_num)) #Se crea nuevo pdf
    informacion = pdf_reader.getPage(page_num) #Obtener pagina del archivo
    texto = informacion.extractText() #leer el texto de la pagina
    texto_2 = texto.split() #hacer una lista con el texto encontrado
    texto_3 = texto.splitlines()
    #print(texto_2)
    #print(texto_3)
    
    #Condicional para obtener cedula
    if 'Asociado:' in texto_2:
        indice = texto_2.index('Asociado:')
        cedula = texto_2[indice+1]
    else:
        indice = texto_2.index('Estimado')
        cedula = texto_2[indice-1]
    
    if 'Asociado(a)' in texto_3:
        indice_titular_1 = texto_3.index('Asociado(a)')
        nombre_titular = texto_3[indice_titular_1+2]
    
    if 'Asociado(a)' in texto_2:
        indice_titular_1 = texto_2.index('Asociado(a)')
        primer_nombre_titular = texto_2[indice_titular_1+1]
    
    if 'Asociado(a)' in texto_2:
        indice_titular_2 = texto_2.index('Asociado(a)')
        segundo_nombre_titular = texto_2[indice_titular_2+2]
    
    if 'Asociado(a)' in texto_2:
        indice_titular_3 = texto_2.index('Asociado(a)')
        apellido_titular = texto_2[indice_titular_3+3]
        
    
    if 'Asociado(a)' in texto_2:
        indice_titular_2 = texto_2.index('Asociado(a)')
        segundo_nombre_titular = texto_2[indice_titular_2+2]
    
    if 'Asociado(a)' in texto_2:
        indice_titular_3 = texto_2.index('Asociado(a)')
        apellido_titular = texto_2[indice_titular_3+3]
    
    #condicionales para obtener numero del prestamo y nombre
    if 'No.' in texto_2:
        indice_2 = texto_2.index('No.')
        no_prestamo = texto_2[indice_2+1]
    elif 'adquirido' in texto_2:
        indice_2 = texto_2.index('adquirido')
        no_prestamo = texto_2[indice_2+1]
    else:
        indice_2 = texto_2.index('en')
        no_prestamo = texto_2[indice_2+1]
    
    if 'Señor(a)' in texto_3:
        indice_3 = texto_3.index('Señor(a)')
        nombre_codeudor = texto_3[indice_3 + 2]
    
    if 'Señor(a)' in texto_2:
        indice_3 = texto_2.index('Señor(a)')
        primer_nombre = texto_2[indice_3 + 1]
    
    if 'Señor(a)' in texto_2:
        indice_4 = texto_2.index('Señor(a)')
        segundo_nombre = texto_2[indice_4 + 2]
    
    if 'Señor(a)' in texto_2:
        indice_5 = texto_2.index('Señor(a)')
        apellido = texto_2[indice_5 + 3]
        
    #Condicional para determinar si el documento se nombra como titular o codeudor
    
    if "codeudor:" in texto_2:
        try:
            with open(f'C_{nombre_codeudor}_{cedula}_{no_prestamo}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
                pdf_writer.write(doc_file)
            
            nombre_archivo = f'C_{nombre_codeudor}_{cedula}_{no_prestamo}.pdf'
            nombre_cliente = f'{nombre_codeudor}'
        except:
            with open(f'C_{primer_nombre}_{segundo_nombre}_{apellido}_{cedula}_{no_prestamo}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
                pdf_writer.write(doc_file)
            
            nombre_archivo = f'C_{primer_nombre}_{segundo_nombre}_{apellido}_{cedula}_{no_prestamo}.pdf'
            nombre_cliente = f'{primer_nombre} {segundo_nombre} {apellido}'
    else:
        try:
            with open(f'T_{nombre_titular}_{cedula}_{no_prestamo}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
                pdf_writer.write(doc_file)
            nombre_archivo = f'T_{nombre_titular}_{cedula}_{no_prestamo}.pdf'
            nombre_cliente = f'{nombre_titular}'
        except:
            with open(f'T_{primer_nombre_titular}_{segundo_nombre_titular}__{apellido_titular}_{cedula}_{no_prestamo}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
                pdf_writer.write(doc_file)
                nombre_archivo = f'T_{primer_nombre_titular}_{segundo_nombre_titular}__{apellido_titular}_{cedula}_{no_prestamo}.pdf'
    
    cedulas.append((nombre_cliente, cedula, no_prestamo,nombre_archivo))
    

if __name__ == '__main__':
    #pdf_word('cartas.pdf', 'cartas.docx')
    #word_pdf('cartas.docx', 'cartas.pdf')
    pdf_reader = PyPDF2.PdfFileReader(open('cartas.pdf', 'rb')) #Nuevamente objeto para leer pdf por que el de la función es en ese scoop
    x = list(range(pdf_reader.numPages)) #Se crea lista con el numero de paginas
    cedulas = []
    #consulta_sql()
    #numeros = []
    
    for pagina in x:
        extract_page('cartas.pdf',pagina)
   
    #archivo_plano()
