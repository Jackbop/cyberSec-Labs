Crypto-Alert-Bot 📈

Ho creato questo script per monitorare il mercato crypto in tempo reale senza dover tenere mille schede del browser aperte. Il bot interroga le API di CoinGecko, analizza i prezzi di Bitcoin, Ethereum e Solana e spara un alert nel terminale se i prezzi superano o scendono sotto le soglie che ho impostato.
🛠️ Come ho configurato l'ambiente (VENV)

Per evitare di "sporcare" il sistema operativo e gestire le librerie in modo isolato, ho creato un ambiente virtuale dedicato. Ecco i passaggi che ho seguito:

    Creazione della cartella: mkdir crypto-tracker && cd crypto-tracker

    Creazione del Venv: Ho usato il modulo di sistema per creare la bolla isolata:
    Bash

    python3 -m venv venv

    Attivazione: Per "entrare" nell'ambiente e usare le sue risorse:
    Bash

    source venv/bin/activate

    Installazione dipendenze: Una volta dentro, ho installato requests (che serve per parlare con il web):
    Bash

    pip install requests

📝 Il Codice Completo

Questo è il file crypto_tracker.py. Gestisce le chiamate HTTP, il parsing del JSON e il loop infinito di monitoraggio.
Python

import requests
import time
from datetime import datetime

# --- CONFIGURAZIONE TARGET ---
# Modifica questi valori per impostare i tuoi alert
TARGET_BTC_UP = 68000  
TARGET_BTC_DOWN = 55000
INTERVALLO = 60 # Secondi tra un controllo e l'altro

def recupera_prezzi():
    # Endpoint API per ottenere i dati in Euro
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=eur"
    try:
        risposta = requests.get(url, timeout=10)
        return risposta.json()
    except Exception as e:
        print(f"!! Errore di connessione: {e}. Riprovo al prossimo ciclo.")
        return None

def avvia_monitor():
    print("=== MONITORING CRYPTO AVVIATO ===")
    print(f"[*] Controllo attivo ogni {INTERVALLO} secondi.")
    
    try:
        while True:
            dati = recupera_prezzi()
            
            if dati:
                btc = dati['bitcoin']['eur']
                eth = dati['ethereum']['eur']
                sol = dati['solana']['eur']
                
                ora = datetime.now().strftime("%H:%M:%S")
                print(f"[{ora}] BTC: {btc}€ | ETH: {eth}€ | SOL: {sol}€")

                # Logica degli Alert
                if btc >= TARGET_BTC_UP:
                    print(f"🚀 ALERT: Bitcoin sopra soglia ({btc}€).")
                elif btc <= TARGET_BTC_DOWN:
                    print(f"📉 ALERT: Bitcoin sotto soglia ({btc}€).")

            time.sleep(INTERVALLO)
            
    except KeyboardInterrupt:
        print("\n[!] Script fermato dall'utente.")

if __name__ == "__main__":
    avvia_monitor()

🧠 Analisi tecnica

    Richieste REST: Lo script usa il metodo GET per ottenere dati strutturati in formato JSON.

    Parsing Dinamico: Python estrae le chiavi specifiche dal dizionario restituito dall'API.

    Controllo del Flusso: Il loop while True garantisce l'esecuzione continua, mentre time.sleep evita il ban dell'IP per troppe richieste (Rate Limiting).

    Robustezza: Il blocco try-except impedisce allo script di crashare se la connessione internet cade temporaneamente.
