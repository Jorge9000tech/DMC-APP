import streamlit as st
import pandas as pd

def main():
    # Título del proyecto y definición del menú principal desplegable con todas las opciones como lista
    st.title("Proyecto Módulo 1 – Especialización Python 2026")
    menu_principal = ["Home","Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
    menu_seleccion = st.sidebar.selectbox("Menu principal", menu_principal)

    # Condicional principal para navegar entre cada menú de la página
    if menu_seleccion == "Home":
        # Menú inicial Home - Contiene descripción del proyecto
        st.subheader("Home")
        st.write("""
        - **Título del proyecto:** Proyecto Aplicativo en Streamlit de Python Fundamentals 
        - **Nombre completo del estudiante:** Jorge Ruiz Santillán
        - **Nombre del curso o módulo:** Especialización en Python for Analytics - Módulo 1
        - **Año:** 2026
        - **Descripción del objetivo:** Aplicación desarrollada en Streamlit que integra conceptos fundamentales de programación como variables, condicionales, estructuras de datos, funciones, programación funcional y POO.
        - **Lista de tecnologías utilizadas:** Python, Streamlit y Pandas
        """)

    elif menu_seleccion == "Ejercicio 1":
        # Menú del ejercicio 1
        st.subheader("Ejercicio 1 - Verificador de Presupuesto")
        st.write("Este es un pequeño verificador para indicar si un gasto monetario se encuentra dentro de un determinado presupuesto o si lo excede.")
        # Creación del formulario del ejercicio 1 con la clave "formulario_1"
        with st.form(key="formulario_1"):
            # Inputs numéricos float para el presupuesto y el gasto, en valores monetarios
            presupuesto = st.number_input("Ingrese su presupuesto")
            gasto = st.number_input("Ingrese el gasto que quiere realizar")
            # Variable del botón de envio del formulario 1
            envio = st.form_submit_button("Enviar Datos")
            # Verifica si se han enviado los datos mediante el botón, de haberse mandado ejecuta el siguiente código
            if envio:
                # Se define la variable diferencia para el paso de verificar si el gasto está dentro del presupuesto o no
                diferencia = presupuesto - gasto
                # Condicional que verifica que la diferencia sea válida, si el resultado es negativo (menor que 0) se avisa que se excede el presupuesto
                # Si es positivo entonces se indica que está dentro del presupuesto.
                if diferencia < 0:
                    st.warning("Error, el gasto excede el presupuesto.")
                else:
                    st.success("El gasto está dentro del presupuesto.")
                # Se muestra la diferencia anteriormente calculada al usuario
                st.write(f"### Diferencia entre el presupuesto y el gasto: {diferencia}")

    elif menu_seleccion == "Ejercicio 2":
        # Menú del ejercicio 2
        st.subheader("Ejercicio 2 - Registro de Actividades")
        st.write("Aquí puede registrar actividades con una serie de valores, visualizar las actividades y revisar una lista donde se le indica si las actividades cumplen o no con el presupuesto que se les asignó de acuerdo al gasto.")
        # Se crea la variable "actividades" la cual será la lista vacía donde se agregaran las actividades que registremos en el formulario
        # Se usa st.session_state para que se guarden los datos de cada actividades registradas
        # Caso contrario no se puede registrar más de una actividad, y necesitaremos que esta lista registre datos para este ejercicio y los demás
        if "actividades" not in st.session_state:
            st.session_state["actividades"] = []
        tipos=["Hogar","Comida","Entretenimiento","Médico", "Otros"]
        # Creación del formulario del ejercicio 2 con la clave "formulario_2"
        with st.form(key="formulario_2"):
            # Uso de inputs de texto y numéricos para registrar los valores de cada actividad
            nombre = st.text_input("Ingrese el nombre de la actividad")
            tipo = st.selectbox("Ingrese el tipo de actividad", tipos)
            presupuesto = st.number_input("Ingrese el presupuesto para esta actividad")
            gasto_real = st.number_input("Ingrese el gasto real de esta actividad")
            # Variable del botón de envio del formulario 2
            envio = st.form_submit_button("Agregar")

            # Verifica si se han enviado los datos mediante el botón, de haberse mandado ejecuta el siguiente código
            if envio:
                # Agrega una nueva actividad en forma de diccionario con claves y valores a la lista "actividades"
                st.session_state["actividades"].append({"Nombre":nombre, "Tipo":tipo, "Presupuesto":presupuesto, "GastoReal":gasto_real})
                st.success("Actividad ingresada con éxito.")
        # Condicional para mostrar la tabla de las actividades registradas cuando se registre al menos una actividad para evitar errores
        # len mayor a 0 indica que hay al menos un elemento en la lista
        if len(st.session_state["actividades"]) > 0:
            # Uso de Pandas para convertir la lista a un Dataframe
            df=pd.DataFrame(st.session_state["actividades"])
            # Conversión del dataframe de Pandas a un dataframe de Streamlit para su visualización en la pantalla
            st.dataframe(df)
            st.divider()
            st.subheader("Estado Financiero de las Actividades")
            # Bucle for para iterar a través de cada fila de la tabla "actividades"
            for item in st.session_state["actividades"]:
                # Uso de [clave] para extraer el valor de la columna respectiva de cada fila
                presupuesto_calculo = item['Presupuesto']
                gasto_real_calculo = item['GastoReal']
                # Variable diferencia para calcular la diferencia entre el presupuesto y el gasto
                diferencia = presupuesto_calculo - gasto_real_calculo
                # Condicional para verificar que el gasto entra dentro del presupuesto o no
                if diferencia < 0:
                    st.write(f"- La actividad {item['Nombre']} no cumple con el presupuesto.")
                else:
                    st.write(f"- La actividad {item['Nombre']} cumple con el presupuesto.")

    elif menu_seleccion == "Ejercicio 3":
        # Menú del ejercicio 3
        st.subheader("Ejercicio 3 - Calcular retorno de actividades")
        st.write("Este es un calculador del retorno (presupuesto x tasa x meses) de las actividades registradas.")
        lista_retorno=[]
        # Al utilizarse las actividades registradas, solo se muestra y ejecuta el código principal si el condicional verifica que hay al menos una actividad registrada
        if "actividades" in st.session_state:
            actividades= st.session_state["actividades"]
            # Se crea la función calcular_retorno que recibe los valores de actividad, tasa y los meses
            def calcular_retorno(actividad, tasa, meses):
                return actividad*tasa*meses
            # Creación del formulario del ejercicio 3 con la clave "formulario_3"
            with st.form(key="formulario_3"):
                # Uso del slider indicando el porcentaje del 1 al 100% de tasa, más input numérico en valores enteros de mínimo 1 mes
                tasa=st.slider("Ingrese la tasa (en porcentaje)", min_value=1, max_value=100, step=1)
                meses=st.number_input("Ingrese el número de meses", min_value=1, step=1)
                # Variable del botón de envio del formulario 3
                envio = st.form_submit_button("Agregar")

                # Verifica si se han enviado los datos mediante el botón, de haberse mandado ejecuta el siguiente código
                if envio:
                    # Para obtener la lista de retornos por cada actividad, se crea la variable lista_retorno
                    # Esta variable empieza con un map, donde se debe ingresar la función a realizar más la lista de datos a la que se le aplicará cada función
                    # En el campo de función, se crea una función lambda con el valor "item", el cual representa cada valor de la lista
                    # La función lambda ejecuta la función calcular_retorno para cada item de la lista actividades
                    # Aquí se le asigna a cada iteración de la función el valor del presupuesto de la actividad junto a la tasa y a los meses
                    # Este map calcula el retorno de cada actividad al recorrer toda la lista, más el lambda que ejecuta la función con cada actividad de la lista
                    lista_retorno = map(lambda item: calcular_retorno(item["Presupuesto"], 1+tasa*0.01, meses), actividades)
                    st.success("Retorno calculado con éxito.")
            # Muestra los datos en el espacio correspondiente una vez se obtiene la lista de retornos
            if lista_retorno:
                st.subheader("Retorno de cada actividad")
                # Para mostrar los datos con un st.write, es necesario hacer un bucle for iterando un zip() que junta la lista de actividades y la de retornos
                # La variable actividad recorre cada actividad y resultado recorre cada retorno
                # Se obtiene el nombre al extraerlo de la clave "Nombre" de cada actividad
                # Al final se usa el st.write para mostrar el retorno de cada actividad en una misma fila
                for actividad, resultado in zip(actividades, lista_retorno):
                    nombre=actividad["Nombre"]
                    st.write(f"- {nombre}: {resultado}")
        else:
            # Si no se han registrado actividades aún, solo se muestra este texto
            st.write(" #### No se ha registrado ninguna actividad, ingrese alguna actividad en el menú anterior.")

    elif menu_seleccion == "Ejercicio 4":
        # Menú del Ejercicio 4
        st.subheader("Ejercicio 4 - Clase Actividad")
        st.write("Aquí se implementa una Clase (POO) asignada como Actividad para convertir cada actividad de la lista de actividades a un objeto con métodos y atributos propios, incluyendo visualización de datos y si el gasto de una actividad cumple con el presupuesto asignado.")
        # Creación de la clase Actividad mediante "class"
        class Actividad:
            # Se definen los atributos de la clase Actividad
            def __init__(self, nombre,tipo, presupuesto, gasto_real):
                self.nombre = nombre
                self.tipo = tipo
                self.presupuesto = presupuesto
                self.gasto_real = gasto_real
            # Se crea la función para comprobar si el gasto de la actividad está en el presupuesto con una llamada self a los propios atributos
            # La función retorna un True o un False de acuerdo a la evaluación realizada
            def esta_en_presupuesto(self):
                if self.presupuesto >= self.gasto_real:
                    return True
                else:
                    return False
            # Se crea la función para mostrar la info con una llamada self a los propios atributos y su escritura en pantalla mediante st.write
            def mostrar_info(self):
                st.write(f"Nombre: {self.nombre} - Tipo: {self.tipo} - Presupuesto: {self.presupuesto} - Gasto Real: {self.gasto_real}")
        # Al utilizarse las actividades registradas, solo se muestra y ejecuta el código principal si el condicional verifica que hay al menos una actividad registrada
        if "actividades" in st.session_state:
            # Se crea la variable actividades para trabajar con la lista de actividades creadas en el menú del ejercicio 2
            actividades = st.session_state["actividades"]
            # Bucle for que recorre cada actividad registrada dentro de la lista
            for i in actividades:
                # Para crear un objeto Actividad y usarlo, se crea una variable utilizando Actividad(variables)
                # Las variables se obtienen colocando i que representa el diccionario y colocando las 4 variables de la clase usando las claves del diccionario
                actividad = Actividad(i["Nombre"],i["Tipo"],i["Presupuesto"],i["GastoReal"])
                st.divider()
                st.write(f"#### Actividad {i["Nombre"]} info:")
                # Uso del metodo mostrar_info de la clase Actividad para mostrar los datos de cada una de estas
                actividad.mostrar_info()
                # Condicional para aplicar el metodo esta_en_presupuesto para mostrar el mensaje correspondiente
                if actividad.esta_en_presupuesto():
                    st.success(f"Actividad: {i['Nombre']} cumple con su presupuesto.")
                else:
                    st.warning(f"Actividad {i["Nombre"]} excede el presupuesto.")
        else:
            # Si no se han registrado actividades aún, solo se muestra este texto
            st.write(" #### No se ha registrado ninguna actividad, ingrese alguna actividad en el menú Ejercicio 2.")

# Ejecución de la función main para correr la aplicación
if __name__ == "__main__":
    main()