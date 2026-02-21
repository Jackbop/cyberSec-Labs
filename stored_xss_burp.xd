# Stored XSS - Bypass dei Filtri Client-Side

**Vulnerabilità:** Stored Cross-Site Scripting (XSS)
**Strumenti usati:** Burp Suite (Proxy & Repeater)
**Obiettivo:** Iniettare un payload XSS persistente nei commenti di un blog.

## Descrizione dell'attacco
Il frontend del sito bloccava l'inserimento di payload nei campi `comment` e `website` imponendo regole sul formato (es. `type="url"`).
Invece di interagire col browser, ho intercettato la richiesta HTTP POST originale usando **Burp Suite Proxy** e l'ho inviata al **Repeater**.

Lì ho modificato direttamente il body della richiesta, inserendo il payload:
`comment=<img src=x onerror=alert(document.cookie)>`

Il server ha risposto con un `302 Found`, accettando il payload senza sanitizzazione lato server. Al ricaricamento della pagina, il payload è stato eseguito con successo, dimostrando la vulnerabilità.
