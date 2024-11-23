# Resumidor de textos

Esta aplicación te permite resumir los archivos de texto. 
Podes cargar los archivos o simplemente pegarlo en el campo de texto.

## Como funciona un resumidor de texto?

El texto llega al backend y en esta parte se procesa usando python. Cada oración es separada usando el tokenizer, esta función permite separar las oraciones, se podria usar un split con el punto, pero en ese caso se tendria que analizar que pasa cuando en el texto hay puntos de abreviaciones.

Se usa la libreria de TfidfVectorizer: es una clase de scikit-learn que convierte una colección de documentos de texto en una matriz TF-IDF. El modelo TF-IDF es una técnica para representar los textos en forma numérica y ponderar las palabras según su relevancia dentro del conjunto de documentos.

Lo que se obtiene son unos scores que puntua que tan importante puede llegar a ser esa oración y luego se ordena y se imprime


### Disclaimer

Este proyecto es meramente académico, todo el codigo se puede ir encontrando de a partes en varios sitios.

Estoy usando chatgpt para generar el codigo html de la estrucutra y aplicar lo que vi en clase sobre el resumidor de texto