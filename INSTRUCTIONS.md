# Esercizio per Sviluppatore Junior: Sviluppo di un'Applicazione Web

**Obiettivo**: Sviluppare una semplice applicazione web che gestisca un elenco di attività. Puoi scegliere di utilizzare Laravel (preferito) o PHP puro per il backend e qualsiasi framework frontend (Angular, Vue, React). Inoltre, l'intera applicazione deve essere containerizzata utilizzando Docker e il controllo della versione deve essere gestito con Git.

## Note importanti
- Leggi questo file completamente prima di cominciare
- Puoi inviare l'esercizio anche se non è completamente completato o se hai utilizzato tecnologie diverse.
- Sentiti libero di andare oltre i requisiti e aggiungere funzionalità o miglioramenti che pensi possano mostrare le tue abilità e creatività.

## Requisiti

### Backend (Laravel/PHP/Python)
- Crea un'API RESTful utilizzando Laravel (preferito), PHP puro o Python.
- L'API deve avere i seguenti endpoint:
  - `GET /tasks`: Recupera un elenco di attività.
  - `POST /tasks`: Crea una nuova attività.
  - `PUT /tasks/{id}`: Aggiorna un'attività esistente.
  - `DELETE /tasks/{id}`: Elimina un'attività.
- Usa un semplice storage in memoria (ad es., un array) per memorizzare le attività per semplicità.
- **Includi commenti, dove lo ritieni necessario, che spieghino la logica del codice e le decisioni prese.**

### Frontend (Angular/Vue/React)
- Crea una semplice interfaccia utente utilizzando HTML, CSS e un framework frontend a tua scelta (Angular, Vue o React).
- L'interfaccia utente deve permettere all'utente di:
  - Visualizzare l'elenco delle attività.
  - Aggiungere una nuova attività.
  - Modificare un'attività esistente.
  - Eliminare un'attività.
- Usa Fetch API o Axios per effettuare richieste HTTP al backend.
- **Includi commenti, dove lo ritieni necessario, che spieghino la logica del codice e le decisioni prese.**

### Docker
- Containerizza l'applicazione utilizzando Docker.
- Crea un `Dockerfile` sia per il backend che per il frontend.
- Utilizza Docker Compose per orchestrare i servizi.
- Assicurati che l'applicazione possa essere avviata con un singolo comando (`docker-compose up`).
- **Documenta la configurazione di Docker e le eventuali difficoltà incontrate.**

### Git
- Inizializza un repository Git.
- Fai commit regolari con messaggi significativi.
- Pusha il codice in un repository pubblico su GitHub o GitLab.

### npm
- Utilizza npm per gestire le dipendenze del frontend.
- Includi un file `package.json` con le dipendenze e gli script necessari.

## Consegne
- L'URL di un repository pubblico Git contenente il progetto.
- Un file `README.md` con le istruzioni su come configurare ed eseguire l'applicazione.
- Un file Docker Compose per orchestrare i servizi backend e frontend.
- **Commenti e spiegazioni del codice.**

## Criteri di Valutazione
- Qualità e organizzazione del codice.
- Implementazione corretta delle funzionalità API e frontend.
- Uso appropriato di Docker per la containerizzazione.
- Uso efficace di Git per il controllo della versione.
- Documentazione chiara e completa.
- **Chiarezza e profondità delle spiegazioni del codice.**
- **Innovazione e funzionalità aggiuntive (se presenti).**

## Follow-up
- Preparati per una sessione di code review per spiegare la tua implementazione.
- Potresti ricevere un compito aggiuntivo da completare in un breve lasso di tempo dopo la consegna.

## Istruzioni
- Effettua il fork del repository fornito nel tuo account GitHub.
- Completa l'esercizio seguendo i requisiti sopra descritti.
- Una volta completato, invia l'URL del repository insieme a eventuali note o commenti aggiuntivi sulla tua implementazione.
- Preparati per una sessione di code review e per un possibile compito di follow-up.
