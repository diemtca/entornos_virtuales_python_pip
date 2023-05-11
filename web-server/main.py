import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app =  FastAPI()

#agregar instancia que se conoce como decorador @app.get('')
# va la ruta por la cual desde la web van a poder ingresar

@app.get('/')

def get_list():
    return [1,2,3,]

@app.get('/contact')

def get_list():
    return {'name': 'Platzi'}


#Para devolver un html y no datos directos
@app.get('/contactHtml', response_class=HTMLResponse)

def get_list():
    #podriamos retornar el renderizado completo 
    # de una pagina web
    return """
        <h1>Hola soy una pagina</h1>
        <p>Yo soy un parrafo</p>
    """




def run():
    store.get_categories()

if __name__=='__main__':
    run()