# Jan-Workflow für das MiroFish-Companion-Repo

## Rollen

### Jan

Jan kuratiert Ziele, Materialien und Entscheidungen. Jan entscheidet, welche Daten genutzt werden dürfen, welche Ergebnisse relevant sind und welche nächsten Schritte tatsächlich umgesetzt werden.

### Aurora

Aurora ist die Strategie-, Erklär- und Prompt-Ebene. Aurora hilft dabei, MiroFish-Ergebnisse einzuordnen, Annahmen sichtbar zu machen, Risiken zu benennen und nächste Aufgaben verständlich zu formulieren.

### Codex

Codex ist die technische Umsetzungsebene. Codex erstellt Dokumentation, Vorlagen, Seed-Strukturen, Prüfskripte oder Repository-Änderungen. Codex soll keine produktiven Änderungen an einem MiroFish-System vornehmen, solange Jan diese nicht freigegeben hat.

### GitHub

GitHub dient als versionierter Arbeitsraum. Änderungen werden nachvollziehbar dokumentiert, geprüft und erst nach Review übernommen.

### OpenAI/API

OpenAI- oder andere LLM-APIs können Analyse-, Assistenz- oder Automatisierungsfunktionen bereitstellen. Jede externe API-Nutzung muss klar markiert werden, besonders wenn Daten übertragen werden könnten.

### MiroFish

MiroFish wird als qualitative Analyseebene genutzt. Es kann Muster, Beziehungen, Risiken, Chancen und Szenarien aus kuratierten Daten ableiten. Die Ergebnisse bleiben Hypothesen und müssen geprüft werden.

## Praktischer Ablauf

### 1. Daten kuratieren

Jan sammelt nur Materialien, die für den Testzweck wirklich nötig sind. Geeignet sind öffentliche Dokumente, synthetische Beispiele, eigene Notizen ohne private Details oder bereits freigegebene Projekttexte.

Nicht geeignet sind private Roh-Chats, API-Keys, geheime Projektdaten, personenbezogene Daten Dritter oder Inhalte ohne Nutzungsfreigabe.

### 2. Daten anonymisieren

Vor der Nutzung werden personenbezogene und sensible Informationen entfernt oder ersetzt. Namen, IDs, Orte, Zeitpunkte, interne Links, Tokens und vertrauliche Details werden pseudonymisiert oder ausgelassen.

### 3. Seed-Pack bauen

Aus den kuratierten und anonymisierten Daten entsteht ein kleines Seed-Pack. Das Seed-Pack sollte klar beschreiben:

- Zweck des Tests,
- Datenbasis,
- bekannte Lücken,
- gewünschte Analysefragen,
- Sicherheitsgrenzen,
- Hinweis, dass Ergebnisse Hypothesen sind.

### 4. Kleinen Testlauf durchführen

Ein Testlauf soll klein bleiben. Ziel ist nicht, eine große Simulation zu starten, sondern den Workflow sicher zu prüfen: Erkennt MiroFish sinnvolle Muster, benennt es Unsicherheiten, und sind die Ausgaben nachvollziehbar?

Dieses Companion-Repo enthält keine erfundenen Startbefehle. Ein echter Testlauf darf erst beschrieben werden, wenn das echte MiroFish-Projekt geprüft wurde.

### 5. Report prüfen

Der Report wird mit dem 9-Punkte-Prüfschema aus `templates/mirofish_report_review_schema_de.md` geprüft. Dabei werden Fakten, Interpretationen, Szenarien und offene Prüfungen getrennt.

### 6. Aurora-Auswertung

Aurora fasst die wichtigsten Muster, Risiken, Chancen und offenen Annahmen in verständlicher Sprache zusammen. Aurora achtet darauf, Spekulation nicht als Fakt auszugeben.

### 7. Nächste Codex-Aufgabe formulieren

Aus der Auswertung entsteht eine kleine, sichere Codex-Aufgabe. Sie sollte klar abgegrenzt, testbar und reversibel sein.

Beispiele:

- eine zusätzliche Review-Vorlage erstellen,
- Seed-Daten strukturieren,
- Datenschutz-Checkliste erweitern,
- Upstream-Repo separat statisch prüfen,
- Installationshinweise erst nach echter Codeprüfung dokumentieren.

## Arbeitsprinzipien

- Klein anfangen.
- Nur anonymisierte Daten verwenden.
- Keine produktiven Änderungen ohne Review.
- Keine Startbefehle erfinden.
- Keine Upstream-Funktionen behaupten, die nicht geprüft wurden.
- Alle MiroFish-Ergebnisse als Hypothesen oder Szenarien markieren.
