import pandas as pd
import charts


def run():
  df = pd.read_csv('data.csv') 
  country=input('Escribe el pais => ').capitalize
  result = df[df['Country/Territory']==country].iloc[:,5:13]
  if len(result)>0:
    labels = result.columns
    values = result.values[0]
    charts.generate_bar_chart(country,labels,values)
  else:
    print('No es un pais válido')

  entry=input('Desea filtrar por continente? (Y/N): ').upper()

  if entry=='Y':
    continent=input('Escriba el continente: ').capitalize
    df = df[df['Continent'] == continent]
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(continent,countries,percentages)
  elif entry=='N':
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart('World',countries,percentages)  
  else:  
    print('No es una opción válida')

  


#sirve para controlar la ejecución si es llamado desde la terminal como un script
if __name__ == '__main__':
  run()