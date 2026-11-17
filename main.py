from flask import Flask, render_template, request  # Importa las herramientas de Flask que utilizaremos.

app = Flask(__name__)  # Crea la aplicacion web utilizando Flask.

@app.route('/')  # Define la ruta principal de la aplicacion.
def index():  # Crea la funcion que responde a la ruta principal.
    return render_template('index.html')  # Carga la pagina principal desde templates.

@app.route('/ejercicio1', methods=['GET', 'POST'])  # Define la ruta del ejercicio 1 y permite GET y POST.
def ejercicio1():  # Crea la funcion del primer ejercicio.
    if request.method == 'POST':  # Comprueba si el formulario envio datos mediante POST.
        nota1 = int(request.form['nota1'])  # Recibe la primera nota como numero entero.
        nota2 = int(request.form['nota2'])  # Recibe la segunda nota como numero entero.
        nota3 = int(request.form['nota3'])  # Recibe la tercera nota como numero entero.
        asistencia = int(request.form['asistencia'])  # Recibe el porcentaje de asistencia.
        promedio = (nota1 + nota2 + nota3) / 3  # Suma las tres notas y divide el resultado entre tres.
        if promedio >= 40 and asistencia >= 75:  # Comprueba si el promedio y la asistencia cumplen los requisitos.
            estado = "APROBADO"  # Guarda el estado cuando ambas condiciones se cumplen.
        else:  # Se ejecuta cuando alguna condicion no se cumple.
            estado = "REPROBADO"  # Guarda el estado cuando el estudiante no cumple los requisitos.
        return render_template('ejercicio1.html', promedio=promedio,estado=estado)  # Envia el promedio y el estado al formulario HTML.

    return render_template('ejercicio1.html')  # Muestra el formulario cuando se accede mediante GET.

@app.route('/ejercicio2', methods=['GET', 'POST'])  # Define la ruta del ejercicio 2 y permite GET y POST.
def ejercicio2():  # Crea la funcion que responde a la ruta del segundo ejercicio.
    if request.method == 'POST':  # Comprueba si el formulario envio los nombres mediante POST.
        nombre1 = request.form['nombre1']  # Recibe el primer nombre del formulario.
        nombre2 = request.form['nombre2']  # Recibe el segundo nombre del formulario.
        nombre3 = request.form['nombre3']  # Recibe el tercer nombre del formulario.
        if nombre1 == nombre2 or nombre1 == nombre3 or nombre2 == nombre3:  # Comprueba si existen nombres repetidos.
            return render_template('ejercicio2.html', error="Los tres nombres deben ser diferentes.")  # Devuelve el formulario con un aviso.
        largo1 = len(nombre1)  # Cuenta los caracteres del primer nombre.
        largo2 = len(nombre2)  # Cuenta los caracteres del segundo nombre.
        largo3 = len(nombre3)  # Cuenta los caracteres del tercer nombre.
        if largo1 >= largo2 and largo1 >= largo3:  # Comprueba si el primer nombre es el mas largo.
            nombre_mayor = nombre1  # Guarda el primer nombre.
            cantidad = largo1  # Guarda su cantidad de caracteres.
        elif largo2 >= largo1 and largo2 >= largo3:  # Comprueba si el segundo nombre es el mas largo.
            nombre_mayor = nombre2  # Guarda el segundo nombre.
            cantidad = largo2  # Guarda su cantidad de caracteres.
        else:  # Se ejecuta cuando el tercer nombre es el mas largo.
            nombre_mayor = nombre3  # Guarda el tercer nombre.
            cantidad = largo3  # Guarda su cantidad de caracteres.
        return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad=cantidad)  # Envia el nombre mas largo y su cantidad de caracteres al HTML.

    return render_template('ejercicio2.html')  # Muestra el formulario cuando se accede mediante GET.

if __name__ == '__main__':  # Comprueba si el archivo se ejecuta directamente.
    app.run()  # Inicia el servidor de Flask.