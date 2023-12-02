class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        return f'Nombre: {self.nombre}, Código: {self.codigo}'
    
    def obtener_pais_lote(self):
        partes = self.codigo.split('-')
        pais = partes[0]
        lote = partes [1]
        return pais, lote