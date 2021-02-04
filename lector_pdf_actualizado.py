# -*- coding: utf-8 -*-
"""
    Este programa lee un lote de cartas en formato pdf 
    para dividirlas y nombrarlas con el número de cedula del asociado 
    y el número de prestamo. 
    
    creado por: @jdramirezzu & @valvarezrestrepo
"""

import PyPDF2 #Se importan los modulos que permiten leer y escribir pdf
from pdf2docx import Converter 
from docx2pdf import convert
import pandas as pd
import sqlalchemy
import requests

#Conectar con base de datos, hacer consulta y crear csv con los datos
def consulta_sql():
    engine = sqlalchemy.create_engine("mysql://mysql:reportserver@34.74.68.92:3306/BIServer")
    sql_data = pd.read_sql_query("select `cliente`.`cu_customermaster_id` AS `cliente_id`,coalesce(`cbl2`.`name`,'') AS `Agencia`,coalesce(`cbl`.`name`,'') AS `Sucursal`,coalesce(`tipo_id`.`name`,'') AS `Tipo_Identificacion`,coalesce(`cliente`.`identification`,'')AS `Nro_Identificacion`,coalesce(`cliente`.`razonsocial`,'') AS `Nombre_Completo`,cast(coalesce(`telefono`.`addressline`,'') as char(100) charset utf8) AS `Celular`from ((((((((((((((((((((((((((((((((((((((((((((((((`cu_customermaster` `cliente` join `ad_identificationtype` `tipo_id` on((`cliente`.`identificationtype` = `tipo_id`.`ad_identificationtype_id`))) left join `c_bpartner_location` `cbl` on((`cliente`.`branch` = `cbl`.`c_bpartner_location_id`))) left join `c_bpartner_location` `cbl2` on((`cbl`.`ad_org_location_id` = `cbl2`.`c_bpartner_location_id`))) left join `cu_address` `telefono` on(((`telefono`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`) and (`telefono`.`addressclass` = 'TM') and (`telefono`.`is_mainaddress` = 'Y')))) left join `cu_address` `email` on(((`email`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`) and (`email`.`addressclass` = 'CE') and (`email`.`is_mainaddress` = 'Y')))) left join `adm_coddesc` `genero` on(((`cliente`.`sex` = `genero`.`adm_coddesc_id`) and (`genero`.`adm_codtitle_id` = 100007)))) left join `cu_personal` `persona` on((`cliente`.`cu_customermaster_id` = `persona`.`cu_customermaster_id`))) left join `c_nation` `nacion` on((`persona`.`citizenship` = `nacion`.`c_nation_id`))) left join `cu_coddesc` `dependencia` on((`persona`.`dependents` = `dependencia`.`cu_coddesc_id`))) left join `adm_coddesc` `marital` on((`persona`.`maritalstatus` = `marital`.`adm_coddesc_id`))) left join `cu_coddesc` `estudio` on((`persona`.`academiclevel` = `estudio`.`cu_coddesc_id`))) left join `cu_coddesc` `profe` on((`persona`.`profession_id` = `profe`.`cu_coddesc_id`))) left join `cu_employment` `empresa` on(((`empresa`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`) and (`empresa`.`is_mainemploy` = 'Y')))) left join `cu_finantial` `financiero` on((`cliente`.`cu_customermaster_id` = `financiero`.`cu_customermaster_id`))) left join `adm_tipo_contrato` `tipo_contrato` on((`empresa`.`contracttype` = `tipo_contrato`.`adm_tipo_contrato_id`))) left join `cu_coddesc` `economia` on((`empresa`.`economicactivity` = `economia`.`cu_coddesc_id`))) left join `cu_coddesc` `cargo` on((`empresa`.`position` = `cargo`.`cu_coddesc_id`))) left join `adm_coddesc` `ocupacion` on((`persona`.`occupation` = `ocupacion`.`adm_coddesc_id`))) left join `vw_rs_datos_personales_parte01_beneficiarios` `beneficiarios` on((`cliente`.`cu_customermaster_id` = `beneficiarios`.`cu_customermaster_id`))) left join `vw_rs_datos_personales_parte02_tipo_vinculo` `cliente_vinculo` on((`cliente`.`cu_customermaster_id` = `cliente_vinculo`.`cu_customermaster_id`))) left join `cu_coddesc` `empleo_estado` on((`empresa`.`employmentlink` = `empleo_estado`.`cu_coddesc_id`))) left join `cu_address` `direccion_comercial` on(((`direccion_comercial`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`) and (`direccion_comercial`.`addressclass` = 'DF') and (`direccion_comercial`.`addresstype` = 1001709)))) left join `c_city` `ciudad_comercial` on((`direccion_comercial`.`c_city_id` = `ciudad_comercial`.`c_city_id`))) left join `vw_rs_datos_personales_parte03_vinculo` `vinculo` on(((`vinculo`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`) and (`vinculo`.`cu_codtitle_id` = 10049)))) left join `cu_customerinfo` on((`cliente`.`cu_customermaster_id` = `cu_customerinfo`.`cu_customermaster_id`))) left join `vw_rs_datos_personales_parte09_pagaduria` `pagaduria` on((`pagaduria`.`acuerdo` = `cliente`.`cu_customermaster_id`))) left join `vw_rs_datos_personales_parte08_vinculado` `vinculado` on((`vinculado`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`))) left join `vw_rs_datos_personales_parte06_usuario_retiro` `usuario_retiro` on((`usuario_retiro`.`cu_customermaster_id` = `cliente`.`cu_customermaster_id`))) left join `vs_rs_datos_personales_parte11_asociado_retiro` `retiro` on((`cliente`.`cu_customermaster_id` = `retiro`.`cu_customermaster_id`))) left join `cu_coddesc` `motivo_ret` on(((`retiro`.`motivo_retiro` = `motivo_ret`.`cu_coddesc_id`) and (`motivo_ret`.`cu_codtitle_id` = 10044) and (`motivo_ret`.`isactive` = 'Y')))) left join `ad_user` `usuario` on((`cliente`.`updatedby` = `usuario`.`ad_user_id`))) left join `cu_multipleselection` `usoDatos` on(((`cliente`.`cu_customermaster_id` = `usoDatos`.`cu_customermaster_id`) and (`usoDatos`.`value` = 'LEY-1581-2012')))) left join `cu_coddesc` `vivienda` on((`persona`.`housingtype` = `vivienda`.`cu_coddesc_id`))) left join `c_city` `ciunac` on((`persona`.`c_city_id` = `ciunac`.`c_city_id`))) left join `c_region` `regnac` on((`persona`.`c_region_id` = `regnac`.`c_region_id`))) left join `c_country` `ccy` on((`persona`.`c_country_id` = `ccy`.`c_country_id`))) left join `cu_employment` `cue` on(((`cliente`.`cu_customermaster_id` = `cue`.`cu_customermaster_id`) and (`cue`.`is_mainemploy` = 'Y')))) left join `cu_legalrep` `curep` on((`cliente`.`cu_customermaster_id` = `curep`.`cu_customermaster_id`))) left join `c_region` `ccrep` on((`curep`.`c_region_id` = `ccrep`.`c_region_id`))) left join `c_city` `cctrep` on((`curep`.`c_city_id` = `cctrep`.`c_city_id`))) left join `cu_customeraccounts` `cccus` on((`cliente`.`cu_customermaster_id` = `cccus`.`cu_customermaster_id`))) left join `cu_company` `cucom` on((`cliente`.`cu_customermaster_id` = `cucom`.`cu_customermaster_id`))) left join `cu_coddesc` `cucod` on(((`cucom`.`sectorcompany` = `cucod`.`cu_coddesc_id`) and (`cucod`.`cu_codtitle_id` = 10023)))) left join `cu_coddesc` `cucae` on(((`cucom`.`economicactivity` = `cucae`.`cu_coddesc_id`) and (`cucae`.`cu_codtitle_id` = 100006)))) left join `c_region` `ccrcuen` on((`cccus`.`c_region_id` = `ccrcuen`.`c_region_id`))) left join `c_city` `cctcuen` on((`cccus`.`c_city_id` = `cctcuen`.`c_city_id`))) left join `c_country` `cc` on((`financiero`.`country_foreign` = `cc`.`c_country_id`))) left join `c_currency` `ccr` on((`financiero`.`currency_foreign` = `ccr`.`c_currency_id`)))",engine)
    sql_data.to_csv(r'C:\Users\analista4operaciones\Desktop\Lector\datos_personales.csv', index=False, header = True)


def enviar_mensaje():
    for numero_celular in numeros:
        url = "http://107.20.199.106/sms/1/text/single"
        payload="{\r\n  \"to\":\"57"+ numero_celular + "\",\r\n                \"from\": \"Cofincafe\",\r\n                \"text\": \"Este es un mensaje de prueba de la aplicación de las cartas\"\r\n\r\n}"
        headers = {
          'Authorization': 'Basic Q29maW5jYWZlMjYwNjpDMEYxTkM0RjM=',
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.status_code)
    

#Extraer los numeros de celular de la lista de datos personales para cada cedula de las cartas
def lista_celulares():
    df = pd.read_csv(r'C:\Users\analista4operaciones\Desktop\Prueba_base_datos\f1.csv')
    df_2 = pd.read_csv(r'C:\Users\analista4operaciones\Desktop\Prueba_base_datos\datos_personales.csv')
    iterable = df_2['Nro_Identificacion']
    iterable_2 = df_2['Celular']
    iterable_3 = df['identificacion'] 
    identificaciones = [x for x in iterable]
    celulares = [x for x in iterable_2]
    identificaciones_2 = [x for x in iterable_3]
    relacion_cedula_celular = dict(zip(identificaciones, celulares))
    celulares_2 = [] 
    
    for a in identificaciones_2:
        try:
            celulares_2.append(relacion_cedula_celular[str(a)])
        except:
            celulares_2.append(None)
    
    cartas_cedula_telefono = dict(zip(identificaciones_2, celulares_2))
    relacion = pd.DataFrame([[key, cartas_cedula_telefono[key]] for key in cartas_cedula_telefono.keys()], columns=['cedula', 'celular'])
    relacion.to_csv(r'C:\Users\analista4operaciones\Desktop\Lector\relacion.csv')
        
    
    
#Crear archivo plano con identificacion y numero de prestamo
def archivo_plano():
    f =open('f1.csv','w')
    for a,b in cedulas:
        f.write(a+','+b+'\n')
    f.close()
    

   
# convertir pdf a docx
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
    
    
#función para extraer pagina y nombrarla
def extract_page(doc_name, page_num):
    pdf_reader = PyPDF2.PdfFileReader(open('cartas.pdf', 'rb')) #Se crea objeto para leer pdf
    pdf_writer = PyPDF2.PdfFileWriter() #Se crea objeto para escribir pdf
    pdf_writer.addPage(pdf_reader.getPage(page_num)) #Se crea nuevo pdf
    informacion = pdf_reader.getPage(page_num) #Obtener pagina del archivo
    texto = informacion.extractText() #leer el texto de la pagina
    texto_2 = texto.split() #hacer una lista con el texto encontrado
    
    #Condicional para obtener cedula
    if 'Asociado:' in texto_2:
        indice = texto_2.index('Asociado:')
        nombre = texto_2[indice+1]
    else:
        indice = texto_2.index('Estimado')
        nombre = texto_2[indice-1]
    
    #Condicional para obtener numero del prestamo
    if 'No.' in texto_2:
        indice_2 = texto_2.index('No.')
        nombre_2 = texto_2[indice_2+1]
    elif 'adquirido' in texto_2:
        indice_2 = texto_2.index('adquirido')
        nombre_2 = texto_2[indice_2+1]
    else:
        indice_2 = texto_2.index('en')
        nombre_2 = texto_2[indice_2+1]
    
    #Condicional para determinar si el documento se nombra como titular o codeudor
    if "codeudor:" in texto_2:
        with open(f'C_{nombre}_{nombre_2}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
            pdf_writer.write(doc_file)
    else:
        with open(f'T_{nombre}_{nombre_2}.pdf', 'wb') as doc_file: #Se incluye el contenido de la pagina seleccionada en el pdf
            pdf_writer.write(doc_file)
    
    cedulas.append((nombre, nombre_2))


#funcion inicializadora
if __name__ == '__main__':
    pdf_word('cartas.pdf', 'cartas.docx')
    word_pdf('cartas.docx', 'cartas.pdf')
    pdf_reader = PyPDF2.PdfFileReader(open('cartas.pdf', 'rb')) #Nuevamente objeto para leer pdf por que el de la función es en ese scoop
    x = list(range(pdf_reader.numPages)) #Se crea lista con el numero de paginas
    cedulas = []
    consulta_sql()
    numeros = []
    
    for pagina in x:
        extract_page('cartas.pdf',pagina)
   
    archivo_plano()
    lista_celulares()