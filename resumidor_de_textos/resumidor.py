import nltk
import numpy as np
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import textwrap

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def obtener_score(tfidf_row):
    x = tfidf_row[tfidf_row != 0]
    return x.mean()

def resumir_texto(texto):
    if not texto.strip():
        raise ValueError("El texto proporcionado está vacío o no es válido.")
    
    # Tokeniza las oraciones
    lineas = sent_tokenize(texto)
    
    # Vectorización TF-IDF
    tokenizar = TfidfVectorizer(
        stop_words=stopwords.words('spanish'),
        norm='l1',
    )
    X = tokenizar.fit_transform(lineas)
    
    # Calcular los scores   
    scores = np.zeros(len(lineas))
    for i in range(len(lineas)):
        score = obtener_score(X[i, :])
        scores[i] = score
    
    # Ordenar por scores
    sort_idx = np.argsort(-scores)
    print("Resumen:")
    oraciones = []
    for i in range(min(15, len(sort_idx))):  # Limita el rango a la cantidad de oraciones disponibles
        oraciones.append([sort_idx[i], scores[sort_idx[i]], lineas[sort_idx[i]]])
        print(f"{i}: score {scores[sort_idx[i]]}: {lineas[sort_idx[i]]}")
    
    # Ordenar por índice original y construir el texto resumido
    oraciones_ord = sorted(oraciones, key=lambda x: x[0])
 
    full_text_resumido = [item[2] for item in oraciones]
    print("####### oraciones_ord",oraciones_ord)
    print("####### full_text_resumido",full_text_resumido)

    return ' '.join(full_text_resumido)
