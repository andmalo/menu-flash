# MenuFlash

MenuFlash è una web app semplice per creare, salvare e ristampare menu in pochi secondi.

Non è solo un generatore: permette di salvare il lavoro, modificarlo e riutilizzarlo senza rifare tutto da zero.

## Funzionalità

- Creazione menu con categorie e piatti
- Aggiunta e rimozione dinamica
- Template multipli (Classic, Modern, Elegant)
- Autosave automatico nel browser
- Import menu da file JSON
- Export menu in JSON
- Stampa PDF del menu

## Tecnologie

- Python
- Flask
- HTML
- CSS
- JavaScript

## Avvio locale

1. Clona il progetto

git clone https://github.com/TUO_USERNAME/menu-flash.git  
cd menu-flash  

2. Installa dipendenze

pip install -r requirements.txt  

3. Avvia il server

python app.py  

4. Apri il browser su

http://127.0.0.1:5000  

## Deploy

Build command:

pip install -r requirements.txt  

Start command:

gunicorn app:app  

## Perché esiste

Creare un menu una volta è facile.  
Modificare e aggiornare un menu nel tempo è la parte noiosa.

MenuFlash serve a rendere questo processo veloce, riutilizzabile e senza errori.
