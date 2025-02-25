import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== Graficador de Funciones ===")
    # Solicitar al usuario la función matemática
    funcion = input("Ingrese la función: ")
    
    # Solicitar la variable independiente
    variable = input("Ingrese la variable independiente: ")
    
    # Solicitar el intervalo de graficación
    try:
        min_val = float(input(f"Ingrese el límite inferior del intervalo para {variable}: "))
        max_val = float(input(f"Ingrese el límite superior del intervalo para {variable}: "))
    except ValueError:
        print("Error: Los límites deben ser números. Intente de nuevo.")
        return
    
    if min_val >= max_val:
        print("Error: El límite inferior debe ser menor que el límite superior.")
        return
    
    # Generar los valores para la variable independiente
    x = np.linspace(min_val, max_val, 500)
    
    # Evaluar la función
    try:
        y = eval(funcion)
    except Exception as e:
        print(f"Error al evaluar la función: {e}")
        return
    
    # Graficar la función
    plt.plot(x, y, label=f"f({variable}) = {funcion}")
    plt.title("Graficador de Funciones Matemáticas")
    plt.xlabel(variable)
    plt.ylabel(f"f({variable})")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

