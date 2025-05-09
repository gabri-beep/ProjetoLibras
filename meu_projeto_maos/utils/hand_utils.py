import math

def calcular_angulo(a, b, c):
    """Calcula o ângulo entre três pontos 2D."""
    angulo = math.degrees(
        math.atan2(c[1] - b[1], c[0] - b[0]) -
        math.atan2(a[1] - b[1], a[0] - b[0])
    )
    angulo = abs(angulo)
    if angulo > 180:
        angulo = 360 - angulo
    return angulo

def contar_dedos(hand_landmarks, img_shape, lado):
    h, w, _ = img_shape
    lm = [(int(p.x * w), int(p.y * h)) for p in hand_landmarks.landmark]

    dedos_estendidos = []

    # --- Dedos indicadores ao mínimo ---
    dedos_indices = [
        (5, 6, 8),    # Indicador
        (9, 10, 12),  # Médio
        (13, 14, 16), # Anelar
        (17, 18, 20)  # Mínimo
    ]

    for mcp, pip, tip in dedos_indices:
        angulo = calcular_angulo(lm[mcp], lm[pip], lm[tip])
        dedos_estendidos.append(1 if angulo > 160 else 0)

    # --- Polegar com ângulo entre CMC (1), MCP (2), TIP (4) ---
    angulo_polegar = calcular_angulo(lm[1], lm[2], lm[4])
    dedos_estendidos.insert(0, 1 if angulo_polegar > 150 else 0)

    return sum(dedos_estendidos)
