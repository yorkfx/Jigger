import pyautogui
import time
import random

# Configuraciones de seguridad
pyautogui.FAILSAFE = True  # Si lo llevas a una esquina, se detiene
pyautogui.PAUSE = 0.1

def jiggler_visible():
    print("👀 Mouse Jiggler VISIBLE iniciado.")
    print("El cursor se moverá de forma errática pero visible.")
    print("Presiona Ctrl+C para detener.")

    # Obtener el tamaño de la pantalla para no salirse de los bordes
    width, height = pyautogui.size()

    try:
        while True:
            # 1. Obtener posición actual
            x_act, y_act = pyautogui.position()

            # 2. Calcular un destino aleatorio no muy lejos (ej. 100-200 píxeles)
            # Asegurándonos de no salirnos de los límites de tu monitor
            offset_x = random.randint(100, 200) * random.choice([-1, 1])
            offset_y = random.randint(100, 200) * random.choice([-1, 1])
            
            nuevo_x = max(10, min(width - 10, x_act + offset_x))
            nuevo_y = max(10, min(height - 10, y_act + offset_y))

            # 3. MOVER EL MOUSE (Visible)
            # 'duration' controla la velocidad: 1.5 segundos lo hace muy visible
            # 'tween' hace que empiece lento, acelere y frene suavemente
            print(f"Moviendo a: ({nuevo_x}, {nuevo_y})")
            pyautogui.moveTo(nuevo_x, nuevo_y, duration=1.2, tween=pyautogui.easeInOutQuad)

            # 4. Espera antes del siguiente movimiento
            # Un tiempo más corto (10 a 20 seg) para que veas acción frecuente
            espera = random.randint(10, 20)
            print(f"Próximo movimiento en {espera} segundos...")
            time.sleep(espera)

    except KeyboardInterrupt:
        print("\n🛑 Detenido por el usuario.")
    except pyautogui.FailSafeException:
        print("\n⚠️ Detención de emergencia (esquina detectada).")

if __name__ == "__main__":
    jiggler_visible()