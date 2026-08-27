"""
Funciones de procesamiento de datos - Taller 2
Módulo con las funciones creadas para limpiar, calcular y clasificar
los registros del dataset de mecatrónica.
"""


def convertir_a_float(valor):
    """Convierte un valor a float. Si no es posible, retorna None."""
    try:
        return float(valor)
    except (ValueError, TypeError):
        return None


def calcular_potencia(voltaje, corriente):
    """Calcula la potencia (P = V * I). Retorna None si hay datos
    inválidos o negativos."""
    if voltaje is None or corriente is None:
        return None
    elif voltaje < 0 or corriente < 0:
        return None
    else:
        return voltaje * corriente


def clasificar_temperatura(temp):
    """Clasifica la temperatura en Normal, Precaución o Alerta."""
    if temp is None:
        return "Dato inválido"
    elif temp < 40:
        return "Normal"
    elif temp < 50:
        return "Precaución"
    else:
        return "Alerta"


def generar_resumen(registros):
    """Genera un resumen estadístico a partir de una lista de registros
    limpios (potencia promedio, temperatura promedio, conteo de estados)."""
    total_registros = len(registros)

    potencias = [
        regis["potencia"] for regis in registros if regis["potencia"] is not None
    ]
    temperaturas = [
        regis["temperatura"]
        for regis in registros
        if regis["temperatura"] is not None
    ]

    potencia_promedio = sum(potencias) / len(potencias) if len(potencias) > 0 else 0
    temperatura_promedio = (
        sum(temperaturas) / len(temperaturas) if len(temperaturas) > 0 else 0
    )

    estados = [regis["estado_temperatura"] for regis in registros]

    resumen = {
        "total_registros": total_registros,
        "registros_validos_potencia": len(potencias),
        "potencia_promedio": potencia_promedio,
        "temperatura_promedio": temperatura_promedio,
        "cantidad_alertas": estados.count("Alerta"),
        "cantidad_precauciones": estados.count("Precaución"),
        "cantidad_normales": estados.count("Normal"),
    }

    return resumen
