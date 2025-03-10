from Controlador.LogicaNegocio.Controlador import convertir_moneda

def main():
    print("Bienvenido al convertidor de divisas")
    monto = float(input("Ingrese el monto: "))
    moneda_base = input("Moneda base (ej: USD): ").upper()
    moneda_destino = input("Moneda destino (ej: EUR): ").upper()

    resultado = convertir_moneda(monto, moneda_base, moneda_destino)

    if resultado:
        print(f"{monto} {moneda_base} equivale a {resultado.tasa:.2f} {moneda_destino}")
    else:
        print("No se pudo realizar la conversión. Verifique las monedas ingresadas.")

if __name__ == "__main__":
    main()
