#importar las opciones del menu
from iu.main_menu import main_menu
#importar las acciones de negocio
from negocio.negocio_usuarios import mostrar_usuarios
from negocio.negocio_ejemplar import mostrar_ejemplar
from negocio.negocio_libros import mostrar_libros



main_menu()

mostrar_usuarios()

mostrar_ejemplar()

mostrar_libros()
