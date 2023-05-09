import utils
import read_csv
import charts


def run():
  data=read_csv.read_csv('data.csv')
  country=input('Escribe el pais => ')
  result=utils.population_by_country(data,country)
  
  if len(result)>0:
    country=result[0]
    labels,values=utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)

  else:
    print('No es un pais válido')
  
  entry=input('Desea filtrar por continente? (Y/N): ').upper()
  if entry=='Y':
    continent=input('Escriba el continente: ')
    continent = "South America"
    data=list(filter(lambda item : item['Continent'] == continent,data))
    '''countries=list(map(lambda item:item['Country/Territory'],data))
    percentages=list(map(lambda item:item['World Population Percentage'],data))
    '''
    countries=[item['Country/Territory'] for item in data]
    percentages=[item['World Population Percentage'] for item in data]
    charts.generate_pie_chart(continent,countries,percentages)
  elif entry=='N':
    #countries=[item['Country/Territory'] for item in data]
    #percentages=[item['World Population Percentage'] for item in data]
    world_dict={item['Country/Territory']:item['World Population Percentage'] for item in data}
    charts.generate_pie_chart('World',world_dict.keys(),world_dict.values())
    
    #charts.generate_pie_chart(countries,percentages)
  else:  
    print('No es una opción válida')

  


#sirve para controlar la ejecución si es llamado desde la terminal como un script
if __name__ == '__main__':
  run()