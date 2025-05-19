from collections import deque

class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.aplicacion}: {self.mensaje}"

def eliminar_notificaciones_facebook(cola_notificaciones):
    """
    Elimina todas las notificaciones de Facebook de una cola.

    Args:
        cola_notificaciones (deque): Una cola de objetos Notificacion.
    """
    cola_auxiliar = deque()
    while cola_notificaciones:
        notificacion = cola_notificaciones.popleft()
        if notificacion.aplicacion.lower() != 'facebook':
            cola_auxiliar.append(notificacion)
    while cola_auxiliar:
        cola_notificaciones.append(cola_auxiliar.popleft())

def mostrar_notificaciones_twitter_con_python(cola_notificaciones):
    """
    Muestra las notificaciones de Twitter cuyo mensaje contiene la palabra 'Python'
    sin perder datos en la cola.

    Args:
        cola_notificaciones (deque): Una cola de objetos Notificacion.
    """
    cola_auxiliar = deque()
    print("Notificaciones de Twitter con 'Python':")
    while cola_notificaciones:
        notificacion = cola_notificaciones.popleft()
        cola_auxiliar.append(notificacion)
        if notificacion.aplicacion.lower() == 'twitter' and 'python' in notificacion.mensaje.lower():
            print(notificacion)
    while cola_auxiliar:
        cola_notificaciones.append(cola_auxiliar.popleft())

def contar_notificaciones_en_rango_horario(cola_notificaciones):
    """
    Utiliza una pila para almacenar temporalmente las notificaciones producidas
    entre las 11:43 y las 15:57 y determina cuántas son.

    Args:
        cola_notificaciones (deque): Una cola de objetos Notificacion.

    Returns:
        int: La cantidad de notificaciones en el rango horario especificado.
    """
    pila_temporal = []
    cola_auxiliar = deque()
    contador = 0
    hora_inicio = "11:43"
    hora_fin = "15:57"

    while cola_notificaciones:
        notificacion = cola_notificaciones.popleft()
        cola_auxiliar.append(notificacion)
        if hora_inicio <= notificacion.hora <= hora_fin:
            pila_temporal.append(notificacion)
            contador += 1

    while pila_temporal:
        pila_temporal.pop()
    while cola_auxiliar:
        cola_notificaciones.append(cola_auxiliar.popleft())

    return contador

# Ejemplo de uso:
if __name__ == "__main__":
    notificaciones = deque([
        Notificacion("10:30", "Facebook", "Nueva publicación de un amigo."),
        Notificacion("11:45", "Twitter", "¡Mira este tweet sobre Python!"),
        Notificacion("12:00", "Instagram", "Alguien ha comentado tu foto."),
        Notificacion("14:20", "Twitter", "Aprendiendo mucho sobre Python hoy."),
        Notificacion("15:30", "Facebook", "Te han etiquetado en una foto."),
        Notificacion("16:00", "WhatsApp", "Tienes un nuevo mensaje."),
        Notificacion("11:40", "Twitter", "Otro día programando."),
        Notificacion("15:55", "Facebook", "Recordatorio de evento."),
        Notificacion("13:00", "LinkedIn", "Nueva conexión profesional.")
    ])

    print("Cola de notificaciones original:")
    for notif in list(notificaciones):
        print(notif)
    print("-" * 30)

    eliminar_notificaciones_facebook(notificaciones)
    print("Cola después de eliminar notificaciones de Facebook:")
    for notif in list(notificaciones):
        print(notif)
    print("-" * 30)

    mostrar_notificaciones_twitter_con_python(notificaciones)
    print("-" * 30)
    print("Cola después de mostrar notificaciones de Twitter (sin modificaciones):")
    for notif in list(notificaciones):
        print(notif)
    print("-" * 30)

    cantidad_en_rango = contar_notificaciones_en_rango_horario(notificaciones)
    print(f"Cantidad de notificaciones entre las 11:43 y las 15:57: {cantidad_en_rango}")
    print("-" * 30)
    print("Cola después de contar notificaciones en rango horario (sin modificaciones):")
    for notif in list(notificaciones):
        print(notif)