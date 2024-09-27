Preprocesador de texto
Descripción del reto

El objetivo del reto es implementar un preprocesador de texto en español, sin utilizar librerías externas. El preprocesador debe cumplir con los siguientes pasos de limpieza:

    Convertir todo el texto a minúsculas.
    Eliminar saltos de línea y caracteres que no sean letras.
    Eliminar cualquier dígito presente en el texto.
    Tokenizar el texto (convertirlo en una lista de palabras).
    Remover las stopwords más comunes en español.

Funcionalidad esperada

El programa esperará leer un archivo raw-text.txt que será provisto por el mentor. El programa realizará las operaciones de limpieza, escribiendo el texto procesado en otro archivo llamado processed-text.txt.
Ejemplo:

    raw-text.txt: El curso de Python cuesta 100 soles y es excelente. ¡Lo recomiendo!
    processed-text.txt: ['curso', 'python', 'cuesta', 'soles', 'excelente.', 'recomiendo']
