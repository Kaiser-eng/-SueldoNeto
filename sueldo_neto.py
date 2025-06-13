TSS_PORCENTAJE = 0.0591
ISR_PORCENTAJE_UNICO = 0.15
BONO_PORCENTAJE = 0.10

def obtener_entrada():
    try:
        sueldo = float(input("Digite el sueldo bruto mensual: RD$ "))
        if sueldo <= 0:
            print("Error: El sueldo debe ser mayor a cero.")
            return None
        otros = float(input("Digite otros descuentos (0 si no aplica): RD$ "))
        bonificacion = input("¿Aplica bonificación? (si/no): ").strip().lower()
        recibe_bono = bonificacion == "si"
        return sueldo, otros, recibe_bono
    except ValueError:
        print("Entrada inválida.")
        return None

def calcular_descuentos(sueldo, otros, bonificacion_activa):
    descuento_tss = sueldo * TSS_PORCENTAJE

    if sueldo > 34685:
        descuento_isr = sueldo * ISR_PORCENTAJE_UNICO
    else:
        descuento_isr = 0

    bono = sueldo * BONO_PORCENTAJE if bonificacion_activa else 0

    sueldo_neto = sueldo - descuento_tss - descuento_isr - otros + bono

    return descuento_tss, descuento_isr, bono, sueldo_neto

def mostrar_resultado(sueldo, otros, tss, isr, bono, neto):
    print("\n------ DESGLOSE DE CÁLCULO ------")
    print(f"Sueldo Bruto: RD$ {sueldo:.2f}")
    print(f"Descuento Seguridad Social (5.91%): RD$ {tss:.2f}")
    print(f"Retención ISR (15% si > RD$34,685): RD$ {isr:.2f}")
    print(f"Otros Descuentos: RD$ {otros:.2f}")
    print(f"Bonificación: RD$ {bono:.2f}" if bono > 0 else "Bonificación: No aplica")
    print(f"Sueldo Neto: RD$ {neto:.2f}")

def main():
    datos = obtener_entrada()
    if datos:
        sueldo, otros_descuentos, aplica_bono = datos
        tss, isr, bono, neto = calcular_descuentos(sueldo, otros_descuentos, aplica_bono)
        mostrar_resultado(sueldo, otros_descuentos, tss, isr, bono, neto)

if __name__ == "__main__":
    main()