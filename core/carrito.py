class Carrito:
        def __init__(self, request):
            self.request = request
            self.session = request.session
            carrito = self.session.get("carrito")
            if not carrito:
                carrito = self.session["carrito"] = {}
            self.carrito = carrito
            
        def añadir(self, producto):
            if str(producto.id) not in self.carrito.keys():
                  self.carrito[producto.id] = {
                       "producto_id": producto.id,
                       "nombre": producto.nombre,
                       "cantidad": 1,
                       "precio": str(producto.precio)
                  }
            else:
                 for key, value in self.carrito.items():
                      if key == str(producto.id):
                           value["cantidad"] = value["cantidad"] + 1
                           break
            self.guardar()



        def guardar(self):
            self.session["carrito"] = self.carrito
            self.session.modified = True


        def eliminar(self, producto):
            producto_id = str(producto.id)
            if producto_id in self.carrito:
                del self.carrito[producto_id]
                self.guardar()

        
        def quitar(self, producto):
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] - 1
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    self.guardar()
                    break
                else:
                    print("El producto no existe en el carrito")

        def limpiar(self):
            self.session["carrito"] = {}
            self.session.modified = True
             

     