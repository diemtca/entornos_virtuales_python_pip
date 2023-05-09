import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    #lector de archivo csv
    reader=csv.reader(csvfile,delimiter=',')
    #obtener el nombre de las columnas
    header=next(reader)
    #print(header)
    #generar un data para guardar los diccionarios 
    data=[]
    for row in reader:
      #zip une en tuplas el header(primera fila con las etiquetas) 
      #con el valor que corresponde
      #print(row)
      iterable = zip(header,row)
      #generar diccionarios con dicts_comprenhesion
      country_dict = { key:value for key,value in iterable}
      #guardar cada diccionario en cada iteración
      data.append(country_dict)
    return data  


if __name__=='__main__':
  data=read_csv('./app/data.csv')
  #consultamos solo el primer diccionario
  #print(data[11])