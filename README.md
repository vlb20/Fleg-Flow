# *Fleg-Flow*: Modello di ottimizzazione per il Piano di Evacuazione bradisismico dei Campi Flegrei
<img src="https://github.com/user-attachments/assets/751c98e6-170e-4104-9f91-acc6fd844d9e" width="300" alt="Fleg-Flow Logo">


Modellazione, analisi ed ottimizzazione di un piano di evacuazione della popolazione dalla zona rossa e gialla dei Campi Flegrei, utilizzando un algoritmo di **Quickest Flow** su una rete stradale reale.

**Autori**
- [**Bruno** Vincenzo Luigi](https://github.com/vlb20)
- [**Carleo** Cristina](https://github.com/iris-cmd22)
- [**Castaldo** Giuseppe](https://github.com/Giuleppe09)

---

### Indice
1.  [Obiettivo del Progetto](#obiettivo-del-progetto)
2.  [Riferimenti Accademici](#riferimenti-accademici)
3.  [Struttura del Progetto](#struttura-del-progetto)
4.  [Flusso di Lavoro](#flusso-di-lavoro)
5.  [Dettagli dei Notebook](#dettagli-dei-notebook)
    - [creazione_grafo.ipynb](#1--creazione_grafoipynb)
    - [fleg_flow.ipynb](#2--fleg_flowipynb)
        - Scenari avversi
6.  [Installazione ed Esecuzione](#installazione-ed-esecuzione)

### Obiettivo del Progetto

Lo scopo di **Fleg-Flow** è applicare un modello di ottimizzazione su rete per analizzare il piano di evacuazione previsto per la crisi bradisismica dei Campi Flegrei. Il progetto si propone di:
- **Calcolare il tempo minimo stimato** per evacuare l'intera popolazione della zona rossa e gialla, data la rete stradale e le sue capacità.
- **Identificare i colli di bottiglia** (strade critiche) che limitano la velocità dell'intera operazione.
- **Simulare scenari avversi** (es. blocco di strade o capacità ridotte) per valutare la resilienza del piano.
- **Fornire una visualizzazione** chiara ed interattiva del piano di flusso risultante.

### Riferimenti accademici

La metodologia implementata trae ispirazione principale da:
- **Fleischer, L., & Skutella, M. (2007). *Quickest Flows Over Time*.**
    Questo paper fornisce il **framework teorico fondamentale** per il progetto. Nello specifico, è stato implementato l'**algoritmo di 2-approssimazione** descritto nella Sezione 3, che riduce il complesso problema del flusso più rapido a una serie di problemi di flusso a costo minimo, risolvibili efficientemente. Nella cartella `riassunto_paper` è possibile leggerne i passaggi principali. 

### Struttura del Progetto

La repository è organizzata come segue:
```txt
fleg-flow/
│
├── creazione_grafo.ipynb       # (FASE 1) Prepara i dati e crea il grafo
├── fleg_flow.ipynb             # (FASE 2) Esegue l'ottimizzazione e l'analisi
│
├── campi_flegrei_features.json # Input: dati ufficiali della Protezione Civile
│
├── grafo_flegreo.graphml       # Output Fase 1: Grafo della rete stradale
├── sorgenti_pozzi.json         # Output Fase 1: Dati su sorgenti e pozzi
│
├── 📂 risultati/
│   └── mappa_evacuazione.html      # Output Fase 2: Mappa interattiva del piano
│
├── requirements.txt                # Lista delle dipendenze Python per pip
│
├──📂 riassunto_paper/
│    └──Quickest_Flow_Over_Time_paper_resume.pdf #Riassunto articolo di riferimento
│
└── README.md                       # Questo file
```

### Flusso di lavoro

Il progetto è diviso in 2 fasi computazionali distinte, implementate in 2 notebook separati.

#### **Fase 1: Preparazione dei dati (`creazione_grafo.ipynb`)**
- **Input**: Un file GeoJSON contenente le aree di incontro e i comuni associati. Per il piano ufficiale, il file è scaricabile dal repository della Protezione Civile.
- **Processo**:
  1.  Utilizza **OSMnx** per scaricare la rete stradale reale dell'area flegrea.
  2.  Processa il grafo calcolando attributi personalizzati per ogni strada: tempo di transito (`tau`) e capacità di flusso (`capacity`).
  3.  Legge il file GeoJSON per identificare le coordinate delle aree di incontro (pozzi) e i nomi dei comuni da evacuare (sorgenti).
  4.  Mappa sorgenti e pozzi ai nodi più vicini sulla rete stradale scaricata.
- **Output:**
  - `grafo_flegreo.graphml`: Un file che contiene il grafo della rete stradale completo e processato.
  - `sorgenti_pozzi.json`: Un file che contiene i dizionari con le informazioni su sorgenti (ID del nodo e popolazione) e pozzi (ID del nodo e nome dell'area).

#### **Fase 2: Ottimizzazione e Analisi (`fleg_flow.ipynb`)**
- **Input:** I file `.graphml` e `.json` generati dalla Fase 1.
- **Processo:**
  1.  Carica il grafo e i dati di sorgenti/pozzi.
  2.  Implementa una **ricerca binaria** sul tempo totale di evacuazione `T`.
  3.  Ad ogni iterazione, risolve un problema di **flusso a costo minimo** utilizzando il solutore **Gurobi** per determinare se un piano è fattibile per il tempo `T` dato.
  4.  Una volta trovato il tempo minimo di riferimento $$T^*$$, calcola il piano di flusso ottimale associato.
  5.  Analizza il piano, calcolando la **saturazione** di ogni strada per identificare i colli di bottiglia.
- **Output:**
  - Analisi stampata a console con il tempo di evacuazione stimato e le strade più critiche.
  - `mappa_evacuazione.html`: Una mappa interattiva (creata con **Folium**) che visualizza le rotte di evacuazione, colorandole in base al livello di saturazione.

### Dettagli dei notebook

#### 1. `creazione_grafo.ipynb`
Questo notebook è il motore di preparazione dei dati. La sua esecuzione è necessaria solo una volta o ogni volta che si desidera aggiornare la mappa stradale o i dati di input. Contiene tutte le logiche di interfacciamento con OSMnx e GeoPandas.

Per utilizzare il file ufficiale del Piano Nazionale Campi Flegrei, è possibile scaricarlo da questo link:
-   [**Link al GeoJSON della Protezione Civile**](https://raw.githubusercontent.com/pcm-dpc/DPC-Mappe/master/rischi/Piano%20Nazionale%20Campi%20Flegrei/campi_flegrei_features.json)

#### 2. `fleg_flow.ipynb`
Questo è il notebook principale per l'analisi. Una volta che i file di input sono stati generati, può essere eseguito più volte per testare diversi scenari senza dover riscaricare o riprocessare la mappa.

##### Analisi di Scenari Avversi
Il notebook è strutturato per facilitare l'analisi di scenari avversi. Modificando il grafo caricato prima dell'ottimizzazione, è possibile simulare:
-   **Blocco di strade critiche**
-   **Riduzione della capacità**

Il confronto tra i risultati del caso base e quelli degli scenari avversi permette di valutare la **resilienza** del piano di evacuazione.

### Installazione ed Esecuzione

#### Prerequisiti
-   Python 3.9 o superiore
-   Git
-   Gurobi Optimizer installato e licenza attiva (la licenza accademica è gratuita).

#### Istruzioni
1. **Clonare la repository**
   ```bash
    git clone [https://github.com/vlb20/Fleg-Flow.git](https://github.com/vlb20/Fleg-Flow.git)
    cd fleg-flow
    ```

2. **Creare ed attivare l'ambiente virtuale:**
   ```bash
    # Crea un ambiente virtuale chiamato 'fleg-env'
    python -m venv fleg-env

    # Attiva l'ambiente
    # Su Windows:
    .\fleg-env\Scripts\activate
    # Su macOS/Linux:
    source fleg-env/bin/activate
    ```
3. **Installare le dipendenze:**
   ```bash
   pip install -r requirements.txt
   ```
