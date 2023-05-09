import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 500, 40]
    # crear la figura y las coordenadas con subplot
    fig, ax = plt.subplots()
    #generar la grafica de torta
    ax.pie(values, labels=labels)
    #guardar la grafica en un archivo
    plt.savefig('pie.png')
    plt.close
