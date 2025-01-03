[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/USx538Ll)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17282122&assignment_repo_type=AssignmentRepo)

# **Instruccions del Repositori**

El repositori està organitzat de manera estructurada per facilitar l’accés al codi, resultats, documentació i presentacions relacionades amb el projecte del sistema de recomanació. A continuació, es descriu cada carpeta i arxiu:

## **1. Carpeta `Entrega_Final`**
Aquesta carpeta conté els documents definitius del projecte. Només aquests arxius són vàlids i representen la versió final del treball:

- **`Presentació_final.pdf`**: Arxiu PDF amb la presentació del projecte.
- **`README_Informe.pdf`**: Informe detallat del projecte, que documenta els passos seguits, l’anàlisi del dataset, els models implementats i les conclusions. En aquest document es troben totes les explicacions detallades de tot el que s'ha fet en aquest projecte.
- **`RecommenderSystem_Code.html`**: Exportació en format HTML del notebook principal, per facilitar-ne la consulta sense necessitat d’executar el codi.
- **`RecommenderSystem_Code.ipynb`**: Notebook principal que inclou la implementació de tot el codi que s'ha fet servir en el projecte. Aquest arxiu es pot executar i permet fer totes les proves que hem fet nosaltres.

## **2. Carpeta `Proves_de_Codi`**
Aquesta carpeta conté scripts de proves que es van fer durant les fases inicials del projecte. **Els scripts d’aquesta carpeta han estat descartats i no són vàlids per a la versió final del treball.** Malgrat això, s’inclouen com a referència històrica:

- **`item-to-item.py`**: Script que implementava un model de recomanació basat en la similitud entre ítems (Item-to-Item).
- **`load_csv.py`**: Script per carregar i processar el dataset. Incloïa funcions de neteja inicial segons els criteris definits.

## **3. Altres arxius i carpetes**
- **`.gitignore`**: Arxiu que defineix les rutes i extensions d’arxius que no s’han d’incloure en el control de versions (per exemple, el dataset descarregat localment).
- **`README.md`**: Arxiu principal del repositori que inclou informació bàsica sobre el projecte, instruccions per executar el codi, i una breu descripció dels objectius i resultats obtinguts.

---

## **Instruccions per Executar el Projecte**

### **1. Descarregar el Dataset**
- El dataset s’ha de descarregar manualment des de Kaggle a través del següent enllaç: https://www.kaggle.com/datasets/saurav9786/amazon-product-reviews . Aquest arxiu no s’inclou al repositori per limitacions de mida.
- Guarda el dataset en una carpeta local que sigui accessible des dels scripts.

### **2. Execució del Notebook**
- Obre l’arxiu `RecommenderSystem_Code.ipynb` amb Jupyter Notebook o una eina compatible.
- Executa les cel·les en ordre per analitzar el dataset, entrenar els models i generar els resultats.

### **3. Consulta de l’Informe i Presentació**
- Els documents definitius es troben a la carpeta `Entrega_Final` i inclouen un resum complet del projecte. Aquests documents són ideals per entendre l'anàlisi fet i revisar els resultats obtinguts.

---


# **Seguiment:**
# Objectius per la sessió 2:

**Objectius generals:** Establir una base sòlida i robusta per al treball, definint de forma clara el problema i que esperem d'aquest estudi.
1. Definició del problema:
1. Descarregar dataset
2. Analitzar dataset, columnes, files...
3. Filtrar dataset, comprovar si hi ha columnes o valors problemàtics en el dataset.
4. Reduir el tamany del dataset

Començar a entrenar diferents models de recomanació.
    - Separar el dataset en conjunts de test, train

## Models a entrenar:
- User-to-User
- Item-to-Item
- SVD
- Content-Based: Degut a la falta d'etiquetes en el dataset no és possible fer un recomanador basat en contingut.

## Distàncies amb les que treballarem:
- Correlació de Pearson
- Distància cosinus

## Treballarem amb diferents tamanys del dataset per observar les diferències:
- 1/3 d'usuaris o items
- 2/3 usuaris o items
- La totalitat d'usuaris o items.

## Documentació pendent a redactar:
- Introducció explicant primer contacte amb el dataset.
- Explicar com hem netejat el dataset per poder treballar amb ell. (Eliminació de valors conflictius, filtratge d'elements per reduir la complexitat...)


    ## Dubtes:
    1. **Com carreguem el dataset?**  
    - El dataset es pot obtenir des de Kaggle o altres fonts similars. No s'ha de penjar al GitHub, ja que no és possible per limitacions d'espai.

    2. **Cal filtrar el dataset després de carregar-lo?**  
    - Sí, és necessari fer un filtratge de les dades del dataset. El motiu del filtratge és que estem treballant amb un dataset format originalment per 4201696 usuaris i 476002. Si no fem cap filtratge del dataset, alhora de fer recomanacions es tindran en compte usuaris que han valorat molt pocs ítems i ítems que han sigut valorats per molt pocs usuaris. Això pot conduïr a prediccions errònies ja que estariem fent servir usuaris i ítems molt poc significatius. Aplicar un filtre ens permet treballar només amb aquelles dades que son considerades "rellevants".

    3. **Es pot fer Content-Based?**  
    - S'ha explorat la posibilitat de fer un recomanador basat en contingut però degut a la falta d'etiquetes al dataset i a la simplicitat de les dades s'ha determinat que no és possible aplicar un recomanador *content-based* fent servir el dataset amb el que estem treballant.

    4. **Quin tipus de dades conté el dataset?**
    - Quina és la seva mida inicial? El dataset està format per 7824482 files i 4 columnes.
    - Com és el nostre dataset i què descriu? El dataset amb el que estem treballant descriu les valoracions que els usuaris han fet als items. Cada columna del dataset representa una de les següents entitats: Usuaris (userId), items (productId), valoracions (rating) i marca temporal (timestamp). Cadascuna de les files es correspon amb la valoració que un usuari ha fet d'un ítem

    5. **Hi ha valors nulls o erronis?**  
    - S'ha fet l'anàlisi inicial del dataset i s'ha vist que no hi ha valors nulls ni erronis en el dataset.

    6. **Hi ha files redundants?**  
    - Al fer l'anàlisi també s'ha comprovat que no hi ha cap fila repetida en el dataset.

    7. **Quins són els criteris de filtratge del dataset?**  
    - Eliminem aquells usuaris que hagin fet menys de 50 valoracions i aquells ítems que tinguin menys de 5 valoracions. Aquesta proposta s'ha extret dels starting point del dataset disponibles a Kaggle.

    8. **Quina distribució tenen les nostres dades?**  
    - En l'anàlisi inicial del dataset s'ha observat què només una petita fracció dels usuaris concentra una gran part de les valoracions fetes als productes. Passa el mateix amb els ítems, on una part d'aquests conté la gran majoria de les valoracions rebudes.
     Si analitzem la distribució de les valoracions fetes pels usuaris podem veure una tendència clara a les valoracions altes (5.0 i 4.0), en especial a la màxima valoracio (5.0). Hi ha poques valoracions baixes (1.0, 2.0 i 3.0)

    9. **Cal pujar el dataset al GitHub?**  
    - No, ja que és massa gran per pujar-lo al repositori. Cada membre de l'equip l'ha descarregat localment per poder treballar.

    10. **Quins models recomanadors podem aplicar?**  
        - Explorarem diversos models recomanadors, incloent User-User, Item-Item, i mètodes basats en factorització matricial com SVD. Com s'ha s'ha comentat anteriorment, un model basat en contingut no té sentit amb aquest dataset.



## OBJECTIUS PER LES SESSIONS 3 I 4

1. **Determinar els paràmetres ideals per a cada model recomanador:**  
   - Distància (Pearson o Cosinus): S'ha de ver un anàlisi comparant els errorrs RMSE i MAE per determinar quina de les dues distàncies proporciona els millors resultats en els models User-User i Item-Item. En cas de no veure difernències significatives es compararan també l'evulució de la precisió i el recall.
   - Nombre de veïns òptim: En els mdoels User-User i Item-Item cal determinar quin és el nombre òtim de veïns que seleccionarem per minimitzar l'error mantenint l'eficiència computacional. Es mirarà l'evolució del RMSE i MAE en funció de k i es seleccionarà el valor òptim mitjançant el mètode del colze.
   - Factors latents per a SVD(post-presentació): Durant la presentació els professors ens van fer saber que a SVD s'hauria de mirar el nombre de factors latents en que es descomposa la matriu per obtenir resultats millors.

2. **Analitzar els resultats obtinguts per cada model:**  
   - Aplicar els models amb els paràmetres seleccionats al nostre dataset. Fer un anàlisi dels errors RMSE i MAE.

3. **Comparar els diferents models recomanadors:**  
   - Trobar i utilitzar mètriques adequades per avaluar el rendiment de cada model. Comparar la Precisió i el Recall. Fer la Precision-Recall curve per veure quin dels models està funcionant millor.

4. **Comprovar l'escalabilitat del nostre sistema:**  
   - Avaluar el cost computacional i el rendiment amb diferents mides del dataset. *(Si hi ha temps)*  

5. **Preparar material per a la presentació i informe:**  
   - Crear visualitzacions i definir el guió de la presentació.
      - Gràfiques per comparar RMSE i MAE
      - Gràfiques per comparar Precisió i Recall
      - Graficar la Precision-Recall curve
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


## Contingut de la Presentació

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

### 5. **Anàlisi dels Errors**  
   - Exposar les conclusions

# Millores posteriors a la presentació
1. Mirar factors latents per el model SVD. 
2. Fer proves d'analisi per comparar els models amb diferents tamanys.
3. Analitzar els temps d'execució dels diferents models.
4. Analitzar la quantitat d'ítems recomanats que coincideixen per un usuari en els 3 models recomanadors.
5. Mirar quins són els ítems més recomanats.