import pyautogui
import time
import random
import ctypes  # Para interactuar con el sistema Windows si fuera necesario

# Configuración óptima para Windows
pyautogui.FAILSAFE = True  # Arrastra a una esquina para detener
pyautogui.PAUSE = 0.1

def jiggler_windows():
    # Título de la ventana de consola (solo Windows)
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Python Mouse Jiggler - Activo")
    except:
        pass

    print("🪟 Mouse Jiggler para WINDOWS iniciado.")
    print("------------------------------------------")
    print("Estado: EL MOVIMIENTO ES VISIBLE")
    print("Detener: Mueve el ratón a una esquina o pulsa Ctrl+C")
    print("------------------------------------------")

    width, height = pyautogui.size()

    try:
        while True:
            # 1. Obtener posición inicial
            x_ini, y_ini = pyautogui.position()

            # 2. Calcular un destino aleatorio amplio (para que se note)
            # Entre 150 y 300 píxeles de distancia
            offset_x = random.randint(150, 300) * random.choice([-1, 1])
            offset_y = random.randint(150, 300) * random.choice([-1, 1])

            # Asegurar que no intente salir de la pantalla
            destino_x = max(50, min(width - 50, x_ini + offset_x))
            destino_y = max(50, min(height - 50, y_ini + offset_y))

            # 3. EJECUTAR MOVIMIENTO (Muy visible)
            # Usamos una duración de 1.5s para que veas el trayecto claramente
            print(f"Moving: ({x_ini}, {y_ini}) -> ({destino_x}, {destino_y})")
            
            # easeInOutExpo hace que el movimiento sea muy fluido y "premium"
            pyautogui.moveTo(destino_x, destino_y, duration=1.5, tween=pyautogui.easeInOutExpo)

            # 4. Pausa de espera (puedes ajustar el rango)
            espera = random.randint(15, 30)
            print(f"Esperando {espera} segundos para el próximo movimiento...")
            time.sleep(espera)

    except KeyboardInterrupt:
        print("\n🛑 Script detenido manualmente.")
    except pyautogui.FailSafeException:
        print("\n⚠️ Fail-safe activado. El script se detuvo porque llevaste el mouse a una esquina.")

if __name__ == "__main__":
    jiggler_windows()