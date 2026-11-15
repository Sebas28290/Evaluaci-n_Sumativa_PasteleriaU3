Asistente de IA (Gemini): Utilizado como guía de apoyo y consultas durante el desarrollo del proyecto en Django

- Partes del proyecto desarrolladas con apoyo de IA
El diseño de CSS dentro de los htmls (catalogo, detalle, comprobante)

Motivo: Al no manejar en profundidad el diseño de interfaces en HTML y CSS, utilicé la IA como guía para estructurar las plantillas utilizando el formato utilizado en clases (tarjetas del catálogo, barra de filtros, alertas y tabla del comprobantes).

A partir de esa estructura, me ajusté a las etiquetas y comandos de plantillas de Django trabajadas en la asignatura (como los extends, block, for, empty, if, urls y crsf_token) para mostrar correctamente los datos enviados desde las vistas realizadas.

Consultas que fueron puntuales de sintaxis y comandos de Django a utilizar:
El uso para aplicar redirect y como guia de apoyo en la realización de todos los htmls realizados y el uso para aplicar los GET, POST en vistas. 

Desallorados por parte mia:

Configuración del proyecto y entorno virtual, creación del entorno virtual, instalación de dependencias (Django y Pillow), creación de los requerimientos, creación del proyecto y app (config, catalogo) y configuración de settings.py y la creación de rutas.

Modelo de datos: La realización de las clases de "Linea", "Producto y "Encargo", sus relaciones fueron creadas todas por parte mia, la generación de codigos unicos con la importación de uuid, la carpeta de imagenes y las funciones de formatos en pesos chilenos.

Templates: Su organización y el uso de los comandos trabajados en 
clases(como los extends, block, for, empty, if, urls y crsf_token)

Panel de admin: Todo lo realizado en admin.py fue realizado por parte mia el listado, filtrado y busquedas en el admin, la creación de grupos y usuarios con permisos, datos de pruebas y la carga de imagenes.

Vistas: Las funciones de inicio catalogo y detalle producto, el filtrado de la función de inicio, la función de detalle producto el manejo de errores 404, control y descuento de stock y comprobante de encargo.

