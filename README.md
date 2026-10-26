# Technical Journal

Portale editoriale per pubblicare note di progettazione, analisi e decisioni tecniche. Evoluzione del vecchio esercizio Django: bozze private, pubblicazione programmata, ricerca, filtro per argomento, paginazione e feed RSS. La redazione avviene tramite Django Admin con autenticazione e protezione CSRF; i lettori non hanno endpoint di scrittura.

## Avvio locale

Python 3.12+, Django 5.2 LTS. Non contiene database o account precompilati.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
export DJANGO_SECRET_KEY="$(.venv/bin/python -c 'import secrets; print(secrets.token_urlsafe(64))')"
.venv/bin/python manage.py migrate
.venv/bin/python manage.py createsuperuser
.venv/bin/python manage.py runserver 127.0.0.1:8000
```

Aprire `/admin/` per creare note. Una nota è pubblica solo se lo stato è `published` e la data di pubblicazione è già trascorsa. Le bozze e le note future sono escluse da ricerca, dettaglio e RSS. Il corpo è testo semplice con escaping HTML: nessuno script o HTML editoriale viene interpretato.

## Verifica

Con la chiave d'ambiente impostata: `.venv/bin/python manage.py test` e `.venv/bin/python manage.py check`.

SQLite è adatto a un piccolo sito editoriale. Per una distribuzione Internet occorre un server WSGI, un proxy HTTPS, statici serviti correttamente, `DJANGO_ALLOWED_HOSTS`, `DJANGO_SECURE_COOKIES=1`, backup, monitoraggio e limitazione dei tentativi di accesso a livello di proxy. `runserver` serve solo per lo sviluppo. Nessun CMS di terze parti o caricamento di file utente incluso. I dati del vecchio schema non sono migrati automaticamente.

## Pulizia del repository

Il nuovo albero non contiene il vecchio SQLite, bytecode o chiavi hardcoded. La cronologia precedente contiene una chiave Django di sviluppo e un database: non considerare quella chiave riutilizzabile e non assumere che la rimozione dal branch corrente cancelli la cronologia. La bonifica storica/creazione di un repository pulito è un passaggio distinto dalla revisione del codice.
