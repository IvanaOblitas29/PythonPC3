try:
    from modulo import dividir
except ImportError:
    print("No se puedo importar el módulo.")
else:
    print(os.getcwd())
finally:
    print("Proceso terminado.")