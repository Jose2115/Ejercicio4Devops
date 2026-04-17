import csv

def procesar_datos():
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            estados = list(reader)
        
        # Ejemplo de procesamiento: Calcular temperatura promedio
        temps = [float(e['Temperatura']) for e in estados]
        promedio = sum(temps) / len(temps)
        total_registros = len(estados)

        with open('resultado.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(f"Resumen de Procesamiento\n")
            f_out.write(f"------------------------\n")
            f_out.write(f"Total de estados analizados: {total_registros}\n")
            f_out.write(f"Temperatura promedio: {promedio:.2f}°C\n")
            f_out.write(f"Estado con más calor: {max(estados, key=lambda x: float(x['Temperatura']))['Estado']}\n")
            
        print("Archivo resultado.txt generado con éxito.")
    except Exception as e:
        print(f"Error procesando datos: {e}")

if __name__ == "__main__":
    procesar_datos()