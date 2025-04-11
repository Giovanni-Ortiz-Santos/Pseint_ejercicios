class TiendaAbarrotes:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.acumulador = 0
        self.productos = ["Papa", "Chile", "Jitomate", "Cebolla", "Brocoli", "Tortillas", "Vino Tinto", "Cerveza", "Celular del oxxo", "Mango"]
        self.precios_productos = [20.0, 15.0, 40.0, 30.0, 25.0, 23.0, 150.0, 57.0, 1999.9, 50.0]

    def mostrar_opciones(self):
        opciones = "*** TIENDA DE ABARROTES ***\n"
        for i, producto in enumerate(self.productos):
            opciones += f"\t{i + 1}-{producto:<15}---- {self.precios_productos[i]:<5}\n"
        return opciones

    def comprar_producto(self, numero_producto, ventana, cuadro_texto):
        if numero_producto < 1 or numero_producto > len(self.productos):
            raise ValueError("Producto inválido. Selecciona un producto válido.")

        precio_producto = self.precios_productos[numero_producto - 1]

        # Verificar si el producto excede el saldo disponible
        if precio_producto > self.saldo - self.acumulador:
            raise ValueError(f"No puedes comprar '{self.productos[numero_producto - 1]}'. Saldo insuficiente.")
        else:
            self.acumulador += precio_producto
            cuadro_texto.insert("end", f"Producto comprado: {self.productos[numero_producto - 1]} | Precio: {precio_producto} | Saldo disponible: {self.saldo - self.acumulador}\n")

    def finalizar_compra(self):
        return f"Saldo restante: {self.saldo - self.acumulador}\nTotal gastado: {self.acumulador}"
