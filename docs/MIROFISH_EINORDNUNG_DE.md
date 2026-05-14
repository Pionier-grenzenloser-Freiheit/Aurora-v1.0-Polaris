# MiroFish – Einordnung für Jan

## Zweck der Einordnung

Dieses Dokument beschreibt, wie MiroFish im Jan-Aurora-Codex-Arbeitsraum verstanden und geprüft werden soll. Es behauptet nicht, dass dieses Repository den MiroFish-Quellcode enthält oder ausführbar ist.

## Was MiroFish wahrscheinlich oder überprüfbar sein kann

Auf Basis der vorgesehenen Nutzung sollte MiroFish als System oder Workflow für qualitative Analyse geprüft werden. Die folgenden Begriffe sind Arbeitsannahmen und müssen am echten Upstream-Projekt verifiziert werden.

### Knowledge Graph / GraphRAG

MiroFish kann wahrscheinlich oder potenziell dabei helfen, Informationen als Beziehungsknoten zu strukturieren. In einem GraphRAG-ähnlichen Workflow würden Dokumente, Begriffe, Personen, Themen und Ereignisse miteinander verknüpft, damit spätere Fragen kontextreicher beantwortet werden können.

Zu prüfen bleibt am echten Projekt:

- ob ein expliziter Knowledge Graph implementiert ist,
- welche Datenbank oder Graphstruktur verwendet wird,
- ob GraphRAG tatsächlich Teil der Architektur ist,
- welche Quellen importiert und indexiert werden können.

### Dokumentenanalyse

MiroFish kann als Werkzeug zur Analyse kuratierter Dokumente genutzt werden. Sinnvolle Dokumenttypen wären zum Beispiel Notizen, Zusammenfassungen, öffentliche Texte, synthetische Seed-Daten oder freigegebene Projektmaterialien.

Zu prüfen bleibt:

- welche Dateiformate unterstützt werden,
- ob Metadaten ausgewertet werden,
- wie Quellen zitiert oder referenziert werden,
- ob sensible Daten lokal bleiben oder an externe Dienste übertragen werden.

### Agentensimulation

MiroFish kann als Umgebung für qualitative Agentensimulation betrachtet werden, sofern das echte Projekt entsprechende Funktionen bietet. Dabei könnten Rollen, Strategien, Perspektiven oder mögliche Interaktionen simuliert werden.

Wichtig: Solche Simulationen sind keine belastbaren Vorhersagen. Sie erzeugen Hypothesen, Muster und Szenarien.

### Report-Workflow

Ein MiroFish-Report sollte nicht als endgültige Wahrheit gelesen werden. Er sollte als Analyseartefakt verstanden werden, das durch Jan und Aurora geprüft wird.

Ein sinnvoller Report-Workflow trennt:

- Datenbasis,
- erkannte Beziehungen,
- Interpretationen,
- Szenarien,
- Risiken,
- Chancen,
- offene Prüfungen,
- nächste sichere Aktionen.

### Deep-Interaction-Workflow

Ein Deep-Interaction-Workflow kann mehrere Analyse- und Reflexionsrunden umfassen. Jan kuratiert Daten, MiroFish erzeugt Musterhypothesen, Aurora erklärt und priorisiert, Codex setzt technische Aufgaben um oder dokumentiert nächste Schritte.

## Klare Trennung der Aussagearten

### Fakten

Fakten sind direkt belegbare Aussagen aus einer Quelle. Sie müssen auf eine konkrete Datenbasis oder ein konkretes Dokument zurückführbar sein.

Beispiel: „Im Seed-Dokument steht, dass Codex als technische Umsetzungsebene beschrieben wird.“

### Interpretation

Interpretationen sind Deutungen auf Basis von Fakten. Sie können hilfreich sein, sind aber nicht automatisch wahr.

Beispiel: „Die wiederholte Nennung von Codex deutet auf einen technischen Automatisierungsfokus hin.“

### Szenarien

Szenarien sind plausible Entwicklungen oder Handlungsoptionen. Sie sind keine Prognosen.

Beispiel: „Ein nächster sinnvoller Schritt könnte ein kleiner, anonymisierter Testlauf sein.“

### Kreative Ableitungen

Kreative Ableitungen verbinden Muster mit neuen Ideen. Sie können strategisch nützlich sein, müssen aber besonders klar als spekulativ markiert werden.

Beispiel: „Aus Harlequin-Aurora könnte eine eigene visuelle Canon-Prüfung entstehen.“

### Offene Prüfungen

Offene Prüfungen sind Punkte, die Jan, Aurora oder Codex noch verifizieren müssen.

Beispiel: „Ist das echte MiroFish-Upstream-Projekt lokal ausführbar, und welche Dienste kontaktiert es?“

## Grundregel

Alle MiroFish-Ergebnisse in diesem Companion-Repo sind Hypothesen, Szenarien oder Interpretationen, bis sie anhand der Quelle, des Codes oder einer unabhängigen Prüfung bestätigt wurden.
