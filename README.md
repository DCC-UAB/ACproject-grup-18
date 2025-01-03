[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/USx538Ll)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17282122&assignment_repo_type=AssignmentRepo)


# OBJECTIUS PER LA SESSIÓ 2:

1. Descarregar dataset
2. Analitzar dataset, columnes, files...
3. Filtrar dataset, comprovar si hi ha columnes o valors problemàtics en el dataset.
4. Reduir el tamany del dataset

(Si hi ha temps) Començar a entrenar diferents models de recomanació.
    -Separar el dataset en conjunts de test, train i validació

## Models a entrenar:
- User-to-User
- Item-to-Item
- SVD

## Distàncies:
- Correlació de Pearson
- Distància cosinus

## Quantitat de dades dataset:
- 1/3 d'usuaris o items
- 2/3 usuaris o items
- La totalitat d'usuaris o items.

## Documentació pendent a redactar:
- Introducció explicant primer contacte amb el dataset.
- Explicar com hem netejat el dataset per poder treballar amb ell. (Eliminació de valors conflictius, filtratge d'elements per reduir la complexitat...)


    ## Dubtes:
    1. **Com carreguem el dataset?**  
    - El dataset es pot obtenir des de Kaggle o altres fonts similars. No s'ha de penjar al GitHub, ja que no és possible per limitacions d'espai.

    2. **Quins són els criteris de filtratge del dataset?**  
    - Eliminem aquells usuaris que hagin fet menys de 50 valoracions i aquells ítems que tinguin menys de 5 valoracions.

    3. **Es pot fer Content-Based?**  
    - Aquesta és una opció a explorar.

    4. **Quin tipus de dades conté el dataset?**  
    - Com és el nostre dataset i què descriu? Quina és la seva mida inicial?

    5. **Hi ha valors nulls o erronis?**  
    - No hi ha valors nulls ni erronis en el dataset.

    6. **Hi ha columnes redundants?**  
    - Això s'ha de comprovar durant l'exploració de dades.

    7. **Quina distribució tenen les nostres dades?**  
    - Podem veure tendències o patrons que siguin significatius?

    8. **Cal filtrar el dataset després de carregar-lo?**  
    - Sí, seguint els criteris indicats anteriorment.

    9. **Cal pujar el dataset al GitHub?**  
    - No, ja que és massa gran per pujar-lo al repositori. Cada membre de l'equip ha de descarregar-lo localment.

    10. **Quins models recomanadors podem aplicar?**  
        - Explorarem diversos models recomanadors, incloent User-User, Item-Item, i mètodes basats en factorització matricial com SVD.



## OBJECTIUS PER LES SESSIONS 3 I 4

1. **Determinar els paràmetres ideals per a cada model recomanador:**  
   - Distància (Pearson o Cosinus)  
   - Nombre de veïns  
   - Factors latents (per a SVD)  

2. **Analitzar els resultats obtinguts per cada model:**  
   - Aplicar els models amb els paràmetres seleccionats al nostre dataset.  

3. **Comparar els diferents models recomanadors:**  
   - Trobar i utilitzar mètriques adequades per avaluar el rendiment de cada model.  

4. **Comprovar l'escalabilitat del nostre sistema:**  
   - Avaluar el cost computacional i el rendiment amb diferents mides del dataset. *(Si hi ha temps)*  

5. **Preparar material per a la presentació i informe:**  
   - Crear visualitzacions i definir el guió de la presentació.  
   - Redactar un informe explicatiu amb les conclusions i els passos seguits.

    ## Dubtes:
    1. **Podem importar els models de llibreries o s'ha de programar?**  
    - Aquesta és una consideració inicial clau.

    2. **Hem d'agafar un subset del dataset o treballar amb totes les dades?**  
    - Si el dataset és massa gran, caldrà considerar l'ús d'un subset.

    3. **És necessari fer Cross Validation?**  
    - Ens assegura millors resultats

    4. **Quines són les millors mesures de similaritat?**  
    - Comparar mètodes com el coeficient de Pearson i el cosinus.

    5. **Quins són els millors recomanadors?**  
    - Identificar els models més adequats per al dataset.

    6. **Com dividir les dades?**  
    - Decidir entre entrenament/test, validació, etc.

    7. **Quines són els millors paràmetres pel model User-to-User i per l'Item-to-Item?**  
    - Ajustar els paràmetres per maximitzar el rendiment.

    8. **Quina diferència hi ha entre la distància de Pearson i Cosinus?**  
    - Analitzar els avantatges i inconvenients de cada mètrica.

    9. **Quin és l'equivalent al nombre de veïns per SVD?**  
    - Identificar el paràmetre equivalent en models de factorització matricial.

    10. **Com podem comparar els diferents models? Quines mètriques utilitzem?**  
        - Proposar mètriques com RMSE, MAE, precisió, i record.

    11. **És l'error igual per totes les valoracions?**  
        - Identificar si els models fallen més en algunes condicions.

    12. **Hi ha diferències en els temps d'execució dels models?**  
        - Comparar la complexitat computacional entre els models.

    13. **Què passa quan treballem amb menys dades?**  
        - Analitzar l'impacte de reduir la mida del dataset en el rendiment.

    14. **Hi ha ítems o usuaris que coincideixen en les recomanacions?**  
        - Identificar quins ítems són més recomanats per cada model.

    15. **Aplicar la tècnica de Cross-Validation canvia els resultats?**  
        - Avaluar l'efecte de la validació creuada en els resultats finals.


## CONTINGUT DE LA PRESENTACIÓ

### 1. **Estudi Previ del Dataset**  
   - Breu explicació de l'anàlisi inicial del dataset, incloent-hi el filtratge posterior basat en criteris seleccionats.  

### 2. **Explicació dels Models Recomanadors**  
   - **User-to-User:** Descripció del model i com funciona.  
   - **Item-to-Item:** Principis bàsics i aplicació.  
   - **SVD:** Explicació del model de factorització matricial.  

### 3. **Tria d'Hiperparàmetres**  
   - **Distància:** Determinar quina és la millor (Pearson o Cosinus) per als models User-to-User i Item-to-Item.  
   - **Nombre de Veïns:** Explicació i justificació de l'elecció.  
   - **Factors Latents (per SVD):** Selecció i impacte sobre el rendiment.  

### 4. **Comparació dels Models**  
   - Comparació dels models User-to-User, Item-to-Item i SVD.  
   - Resultats obtinguts i anàlisi de quin model és més efectiu.  
   - Incloure resultats d'anàlisis amb **Cross-Validation**.  

### 5. **Anàlisi dels Errors**  
   - Error per tipus de valoració (per exemple, error en valoracions 1.0 vs altres).  
   - Observacions i conclusions sobre els casos en què els models fallen més.

# Millores
1. Mirar factors latents per el model SVD. 
2. Fer proves d'analisi per comparar els models
3. Analitzar els temps d'execució.




