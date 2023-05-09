
import read_csv
import charts

data=read_csv.read_csv('./app/data.csv')

entry=input('Desea filtrar por continente? (Y/N): ').upper()
if entry=='Y':
  continent=input('Escriba el continente: ')
  data=list(filter(lambda item : item['Continent'] == continent,data))
  '''countries=list(map(lambda item:item['Country/Territory'],data))
  percentages=list(map(lambda item:item['World Population Percentage'],data))
  '''
  countries=[item['Country/Territory'] for item in data]
  percentages=[item['World Population Percentage'] for item in data]
  charts.generate_pie_chart(countries,percentages)
elif entry=='N':
  #countries=[item['Country/Territory'] for item in data]
  #percentages=[item['World Population Percentage'] for item in data]
  world_dict={item['Country/Territory']:item['World Population Percentage'] for item in data}
  charts.generate_pie_chart(world_dict.keys(),world_dict.values())
  
  #charts.generate_pie_chart(countries,percentages)
else:  
  print('No es una opción válida')

