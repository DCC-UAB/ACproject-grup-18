[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/USx538Ll)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17282122&assignment_repo_type=AssignmentRepo)


# Objectius primera sessió:
1. Descarregar DATASET
2. STARTING POINT:
    - Analitzar dataset, columnes, files...
    - Filtrar Dataset:
        - Encarregar-se de columnes problemàtiques o confuses
        - Valors NULL o 0
        - Considerar Normalitzar valors.

3. Analitzar i processar diferents divisions del dataset en conjunts de test, train i validació
4. Si hi ha temps, començar a entrenar diferents models amb el dataset.

    ## Dubtes:
    1. Com carreguem el dataset, amb kaggle i similars o el posem al directori?
        - No s'ha de penjar al github, no es pot per espai.
    2. Quan carreguem el dataset, quins són els criteris de filtratge?
        - De moment, borrem aquelles usuaris que hagin fet menys de 50 valoracions i aquells items que tinguin menys de 5 valoracions.
    3. Es pot fer Content-Based?

# Objectius segona i tercera (dia 6 desembre festiu) sessió:
1. Models a entrenar:
   - User-to-User
   - Item-to-Item
   - SVD
2. Distàncies a comparar amb els models User-User i Item-Item
   -  Correlació de Pearson
   -  Distància cosinus

3. Quantitat dataset: (Les proves es poden fer per aquests diferents tamanys de dataset)
   - 500 files
   - 1000 files
   - 1500 files

    ## Dubtes:
    1. Podem importar els models de llibreries o s'ha de programar?
    2. Hem d'agafar un subset? Masses cel·les. Hem de treballar amb tot el dataset? 
    3. És necessari fer Cross Validation?
    4. Quins són les millors mesures de similaritat?
    5. Quins són els millors recomanadors?
    6. Entenc que amb el dataset que tenim, no podem fer CB?
    7. Quins mètodes són més representatius per Evaluar els models?
    8. Com podem comprovar que les recomanacions que fa el nostre sistema avaluador són correctes?

# Objectius quarta sessió:
1. Començar a preparar la presentació.
2. Acabar les coses pendents:
   - svd gràfiques --> Rmse mae
   - Fer precisio recall. 

## Contingut presentació:
Breu explicació estudi previ DATASET
Menció dels tres models que explicarem
User-User i item item grafica pearson cosinus --> Ens quedem amb la millor (serà la distància que utilitzarem per les altres gràfiques)
    son el mateix decidim quedar-nos amb cosinus.
User-user vs Item-item --> Comparem entre ells i expliquem beneficis i contres de cada un.
SVD --> cross validation. (Como no podemos ver la evolucion del model en función de k (vecinos), miramos con varios datasets).
UvsIvsS --> comparem entre els tres. Principalment SVD contra les altres dues, ja que és la millor.
Analitzem ratings --> expliquem perquè fallen més els ratings <= 3 {
    Estaria guay explicar perquè 4 dona menys vegades error que no el 5
}

# Millores
1. Mirar factors latents per el model SVD. 
2. Fer proves d'analisi per comparar els models
3. Analitzar els temps d'execució.




