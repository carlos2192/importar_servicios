import sys
import numpy as geek
import pandas as pd 
from io import StringIO
import sys
import os
import pyodbc
import csv
import  numpy as  np
import pandas as pd


#Funcion Encargada de Realizar la consulta a la base de datos devolviendo un valor si existe y otro valor si no
def consultacliente(documento,tipodocumento):

    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("select ClientID from Clients where AccountID = '"+ documento + "' and AccountIDType ='"+ tipodocumento + "'") # Se genera el cursor con el criterio
  
    existeconsulta = (cursor.rowcount)
    if existeconsulta == -1:
         
        for fila in cursor.fetchall():
            fila = fila[0]
            resultado = 1
          
    else:
        resultado = 0
        fila=""
        

    
    return (resultado,fila)
      

def consultaprestador(nitprestador):

    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("select ProviderID from Providers where nits = '"+ nitprestador + "'") # Se genera el cursor con el criterio
  
   
    
    for fila in cursor.fetchall():
        fila = fila[0]
    
    return (fila)



def consultapagador(ClientID,documento,pagador):

    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    print("select InsuranceIndexID from insurances where Insurance = '"+ pagador + "'and ClientID ='" + ClientID + "' and 'PlanID = '" + documento + "');") # Se genera el cursor con el criterio
    cursor.execute("select InsuranceIndexID from insurances where Insurance = '"+ pagador + "'and ClientID ='" + ClientID + "' and  PlanID = '" + documento + "';") # Se genera el cursor con el criterio
  
   
    
    for fila in cursor.fetchall():
        fila = fila[0]
    
    return (fila)


#Funcion Encargada de instertar un Cliente si no existe
def insertacliente(documento,tipodocumento,nombreafiliado,fechanacimiento,sexo,estatura,apellidos,municipio,telefono,direccion):
    
    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    Name1 = (nombreafiliado + apellidos)
    cursor.execute(" INSERT INTO Clients (Name1,FirstName,Birthday, sex, Height,AccountIDType,AccountID,LastName,City,MobilePhone,PhysicalAddress) VALUES ('"+  Name1 + "','" + nombreafiliado + "','" + fechanacimiento + "','" + sexo + "','" + estatura + "','" + tipodocumento + "','" + documento + "','" + apellidos + "','" + municipio + "','" + telefono + "','" + direccion + "');")
    cursor.commit()
    cursor.execute("SELECT SCOPE_IDENTITY();")
    for fila in cursor.fetchall():
       
       ClientID = fila[0]
              
   
   
    return (ClientID)

#encargado de crear un servicio
def insertaservicio(ClientID,prestadorid,tiposervicio,diacita,horatraslado,acompanante,documentoacompanante,parentezco,movilidad):
    
    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO services (ClientID, ProviderID,ServicesType,ServiceDays,AppointmentTime,Escort,escortCedula,EscortRelationship,MobilityAids1) VALUES ('"  + ClientID + "','" + prestadorid + "','" + tiposervicio + "','" + diacita + "','" + horatraslado + "','" + acompanante + "','" + documentoacompanante + "','" + parentezco + "','" + movilidad + "');")
    cursor.commit()
    cursor.execute("SELECT SCOPE_IDENTITY();")
    for fila in cursor.fetchall():
       
       ClientID = fila[0]
              
   
   
    return (ClientID)

#encartadodeinsertar la autorizacion
def insertaautorization(ClientID,serviceid,insurenceindexID,diagnostico,fechatraslado,numeroautorizacion):
    
    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Authorizations (ClientID, ServiceID,InsuranceID,Dx1,PADate,PAExpire,PreauthorizationNumber) VALUES ('" + ClientID + "','" + serviceid + "','" + insurenceindexID + "','" + diagnostico + "','" + fechatraslado + "','" + fechatraslado + "','"  + numeroautorizacion + "');")
    cursor.commit()
    
    cursor.execute("SELECT SCOPE_IDENTITY();")
    for fila in cursor.fetchall():
       
       PreAuthID = fila[0]
              
   
   
    return (PreAuthID)

#encargado de insertar en la tabla dates
def insertadates(serviceid,numeroautorizacion,fechatraslado,status,horatraslado):
    
    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Dates (ServiceID,PreauthorizationNumber,AppointmentDate,Status,TripType,Hour) VALUES ('" + serviceid + "','" + numeroautorizacion + "','" + fechatraslado + "','" + status + "','" + trytipe + "','"+ horatraslado + "');")
    cursor.commit()
    
    cursor.execute("SELECT SCOPE_IDENTITY();")
    for fila in cursor.fetchall():
       
       dateid = fila[0]
              
   
   
    return (dateid)



#encargado de insertar pagador si el cliente no existe
def insertapagador(ClientID,documento,pagador):
    
    direccion_servidor = 'DESKTOP-2OV4773'
    nombre_bd = 'TRANSCODB'
    nombre_usuario = 'carlos'
    password = '1234'
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
       
       
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)
        
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO Insurances (ClientID,PlanID,Insurance) VALUES ('" + ClientID + "','" + documento  + "','"+ pagador + "');")
    cursor.commit()
    
    cursor.execute("SELECT SCOPE_IDENTITY();")
    for fila in cursor.fetchall():
       
       pagador = fila[0]
              
   
   
    return (pagador)





#main
#Codigo encargado de cargar el csv y meterlo dentro de una matriz
c = open("C:\\users\\CY/prueba5.csv")
vector_v = geek.genfromtxt(c, delimiter =';',  dtype=None)
c.close()
cantidadfilas= int (vector_v.shape[0])


#Codigo encargado de recorer la matriz y buscando en guardando los datos de cada fila para ir a la funcion consultar
for  i in range(1,cantidadfilas):
    #para cliente
   documento =( vector_v[i][9])
   documento = documento.decode('UTF-8')
   tipodocumento =( vector_v[i][8])
   tipodocumento = tipodocumento.decode('UTF-8')
   nombreafiliado = ( vector_v[i][10])
   nombreafiliado = nombreafiliado.decode('UTF-8')
   fechanacimiento = ( vector_v[i][3])
   fechanacimiento = fechanacimiento.decode('UTF-8')
   sexo = ( vector_v[i][4])
   sexo = sexo.decode('UTF-8')
   estatura= ( vector_v[i][6])
   estatura = estatura.decode('UTF-8')
   apellidos= ( vector_v[i][11])
   apellidos = apellidos.decode('UTF-8')
   municipio= ( vector_v[i][12])
   municipio = municipio.decode('UTF-8')
   telefono= ( vector_v[i][13])
   telefono = telefono.decode('UTF-8')
   direccion= ( vector_v[i][14])
   direccion = direccion.decode('UTF-8')
   
   #para servicio
   diacita = ( vector_v[i][7])
   diacita = diacita.decode('UTF-8')
   tiposervicio = ( vector_v[i][16])
   tiposervicio = tiposervicio.decode('UTF-8')
   horatraslado = ( vector_v[i][21])
   horatraslado = horatraslado.decode('UTF-8')
   acompanante = ( vector_v[i][22])
   acompanante = acompanante.decode('UTF-8')
   if acompanante.upper() == "SI":
       acompanante = "1"
   else:
       acompanante = "0"
   documentoacompanante = ( vector_v[i][24])
   documentoacompanante = documentoacompanante.decode('UTF-8')
   parentezco = ( vector_v[i][25])
   parentezco = parentezco.decode('UTF-8')
   movilidad = ( vector_v[i][28])
   movilidad = movilidad.decode('UTF-8')
   nitprestador = ( vector_v[i][17])
   nitprestador = nitprestador.decode('UTF-8')
   prestadorid = consultaprestador(nitprestador)
   prestadorid = str(prestadorid)
   
   
   
   
   
   #para autorizathions
   pagador = ( vector_v[i][29])
   pagador = pagador.decode('UTF-8')
   fechatraslado = ( vector_v[i][20])
   fechatraslado = fechatraslado.decode('UTF-8')
   diagnostico = ( vector_v[i][27])
   diagnostico = diagnostico.decode('UTF-8')
   numeroautorizacion = ( vector_v[i][29])
   numeroautorizacion = numeroautorizacion.decode('UTF-8')
   
   status = "Pending for Trip"
   trytipe = "Round Trip"
   

   
   
   resultadoconsulta =  consultacliente(documento,tipodocumento)
   ClientID= (resultadoconsulta[1])
   ClientID = str(ClientID)
  
   
 
#Codigo Encargado de verificar si el resultado de la funcion consulta es O es por que el cliente no existe asi que lo crea de lo contrario no hace nada
   if resultadoconsulta[0] == 0:
       
       ClientID = insertacliente(documento,tipodocumento,nombreafiliado,fechanacimiento,sexo,estatura,apellidos,municipio,telefono,direccion)
       ClientID = str(ClientID)
       insurenceindexID=str(insertapagador(ClientID,documento,pagador))
       
   else:
       insurenceindexID = str(consultapagador(ClientID,documento,pagador))

       
   serviceid = str(insertaservicio(ClientID, prestadorid, tiposervicio, diacita, horatraslado, acompanante, documentoacompanante, parentezco, movilidad))
   numeroautorizacion = (numeroautorizacion +"-"+ serviceid )
   PreAuthID = str(insertaautorization(ClientID,serviceid,insurenceindexID,diagnostico,fechatraslado,numeroautorizacion))
   dateid = str(insertadates(serviceid,numeroautorizacion,fechatraslado,status,horatraslado))
   
   
   
   
  

   
   
   


   
   
   
   
   
       
       
    






