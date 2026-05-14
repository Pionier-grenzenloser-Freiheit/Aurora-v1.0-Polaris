# Datenschutz und Sicherheit

## Grundsatz

Dieses Repository ist ein sicherer Companion-Arbeitsraum für Jan. Es darf keine geheimen, privaten oder produktiven Daten enthalten. Alle Beispiele müssen anonymisiert, synthetisch oder ausdrücklich freigegeben sein.

## Keine API-Keys committen

API-Keys, Tokens, Zugangsdaten, Session-Cookies, private URLs und sonstige Geheimnisse dürfen niemals in dieses Repository committed werden.

Falls Konfigurationsbeispiele benötigt werden, dürfen nur Platzhalter verwendet werden, zum Beispiel:

```text
OPENAI_API_KEY=your_api_key_here
MIROFISH_API_URL=https://example.invalid
```

Solche Platzhalter sind keine echten Zugangsdaten.

## Keine privaten Roh-Chats verwenden

Private Roh-Chats dürfen nicht als Seed-Daten, Testdaten oder Analysegrundlage committed werden. Das gilt auch dann, wenn sie vermeintlich harmlos wirken.

Stattdessen verwenden:

- synthetische Beispieltexte,
- stark anonymisierte Zusammenfassungen,
- öffentliche Quellen mit Nutzungsfreigabe,
- kurze, absichtlich verfremdete Testnotizen.

## Sensible Daten anonymisieren

Vor jeder Nutzung müssen sensible Informationen entfernt, verallgemeinert oder ersetzt werden.

Zu entfernen oder zu anonymisieren sind insbesondere:

- echte Namen,
- Adressen,
- Telefonnummern,
- E-Mail-Adressen,
- Benutzer-IDs,
- Kundennummern,
- interne Projektnamen,
- private Links,
- genaue Zeitstempel,
- finanzielle Details,
- Gesundheitsinformationen,
- politische oder religiöse Angaben,
- Zugangsdaten und technische Secrets.

## Externe API-, LLM- und Memory-Dienste markieren

Jeder Workflow muss klar benennen, ob externe Dienste beteiligt sind. Dazu gehören zum Beispiel:

- LLM-APIs,
- Embedding-APIs,
- Vektor- oder Graphdatenbanken,
- Cloud-Speicher,
- Memory-Dienste,
- Telemetrie- oder Logging-Systeme.

Wenn Daten das lokale System verlassen könnten, muss dies vorab sichtbar und verständlich dokumentiert werden.

## Ergebnisse kennzeichnen

MiroFish-Ergebnisse sind als Hypothesen, Szenarien oder Interpretationen zu kennzeichnen. Sie dürfen nicht als gesicherte Fakten, präzise Prognosen oder automatisierte Entscheidungsvorlagen behandelt werden.

Empfohlene Kennzeichnung:

```text
Status: Hypothese / Szenario / Interpretation – menschliche Prüfung erforderlich.
```

## Review vor produktiver Nutzung

Bevor Ergebnisse, Daten oder Workflows produktiv genutzt werden, ist eine menschliche Prüfung erforderlich. Dabei muss mindestens geprüft werden:

- Welche Daten wurden verwendet?
- Wurden sensible Daten entfernt?
- Sind externe Dienste beteiligt?
- Sind Aussagen sauber als Fakt, Interpretation oder Szenario getrennt?
- Gibt es Risiken durch Fehlinterpretation?
- Ist der nächste Schritt klein, sicher und reversibel?
