import matplotlib.pyplot as plt

def generate_bar_chart(name_country,labels,values):
 
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'imgs/countrys/bar{name_country}.png')
  plt.close


def generate_pie_chart(name_continent,labels,values):
  fig, ax = plt.subplots()
  ax.pie(values,labels=labels)
  #ubicar la grafica en el centro
  ax.axis('equal')
  plt.savefig(f'imgs/continents/pie_{name_continent}.png')
  plt.close


if __name__=='__main__':
  labels=['a','b','c']
  values=[100,200,800]
  #generate_bar_chart(labels,values)
  generate_pie_chart(labels,values)

