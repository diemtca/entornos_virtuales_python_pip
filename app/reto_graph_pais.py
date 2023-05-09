import read_csv
import charts
import re

def main():

  labels=[]
  values=[]
  country= input('Escribe el pais: ')
  data=read_csv.read_csv('./app/data.csv')
  country_data=list(filter(lambda pais:pais['Country/Territory']==country.title(),data))

  print(country_data)
  if len(country_data)>0:
    for key,value in country_data[0].items():
      #uso de expresiones regulares
      if re.match('[0-9]{4} Population',key):
        labels.append(key.replace('Population',''))
        values.append(int(value))
  
    charts.generate_bar_chart(labels,values)
  else:
    input('No es un pais válido')
    exit()

if __name__=='__main__':
  main()