                                                   import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ApolloBot:
    def __init__(self):
        self.datos = None

    def cargar_datos(self, archivo):
        """
        Cargar los datos para su análisis y visualización.
        """
        self.datos = pd.read_csv(archivo)
        print("Datos cargados exitosamente.")
    
    def visualizar_distribucion(self, columna):
        """
        Visualiza la distribución de una columna específica de los datos.
        """
        plt.figure(figsize=(10,6))
        sns.histplot(self.datos[columna], kde=True, color="skyblue")
        plt.title(f"Distribución de {columna}")
        plt.show()

    def generar_tablero_control(self):
        """
        Crear un tablero de control básico con las principales métricas.
        """
        resumen = self.datos.describe().transpose()
        print("Tablero de Control:")
        print(resumen)

    def correlacion_datos(self):
        """
        Visualiza la matriz de correlación entre las variables.
        """
        plt.figure(figsize=(12,8))
        sns.heatmap(self.datos.corr(), annot=True, cmap="coolwarm")
        plt.title("Matriz de Correlación")
        plt.show()

# Ejemplo de uso
apollo = ApolloBot()
apollo.cargar_datos('datos_financieros.csv')
apollo.visualizar_distribucion('Precio')
apollo.generar_tablero_control()
apollo.correlacion_datos()
