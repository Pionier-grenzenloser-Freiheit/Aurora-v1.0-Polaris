# integrity-marker-format.md

## Zweck

| Punkt | Festlegung | Klasse |
|---|---|---|
| Ziel | Dieses Dokument definiert ein minimales Formatkonzept für `integrity_marker`. | derived_from_source |
| Bezug | Der Kontrollvertrag verlangt einen Integritätsmarker für Nachvollziehbarkeit, lässt die konkrete Konstruktion aber offen. | stated_in_source |
| Grenze | Dieses Dokument definiert keine kryptografische Implementierung. | target_assumption |

## Minimales Formatkonzept

| Element | Festlegung | Klasse |
|---|---|---|
| Datentyp | `integrity_marker` bleibt ein String. | stated_in_source |
| Zweck | Der Wert referenziert oder bezeichnet einen Integritätsnachweis für Audit-Nachvollziehbarkeit. | derived_from_source |
| Inhalt | Der Marker soll keine Rohdaten enthalten. | target_assumption |
| Stabilität | Der Marker soll stabil genug sein, um Audit Events später mit einem Integritätsnachweis zu verknüpfen. | target_assumption |

## Baseline-Kompatibilität

| Punkt | Festlegung | Klasse |
|---|---|---|
| Aktueller Schema-Stand | `integrity_marker` bleibt im freigegebenen Schema-Pack ein nicht-leerer String. | stated_in_source |
| Bestehende gültige Werte | Werte wie `integrity-marker-open` bleiben baseline-kompatibel. | derived_from_source |
| Zielformat | Die empfohlene String-Form ist noch kein baseline-verbindliches Pattern. | target_assumption |

## Empfohlene String-Form

```text
integrity:<method-or-profile>:<marker-ref>
```

| Bestandteil | Bedeutung | Klasse |
|---|---|---|
| `integrity` | fester Präfix für Integritätsmarker | target_assumption |
| `<method-or-profile>` | Platzhalter für das später freigegebene Integritätsprofil | open |
| `<marker-ref>` | Referenzwert auf den konkreten Integritätsnachweis | open |

## Migrationshinweis für das bestehende Schema

| Empfehlung | Klasse |
|---|---|
| Kurzfristig keine Änderung am freigegebenen Schema-Pack anwenden; `integrity_marker` bleibt nicht-leerer String. | target_assumption |
| Eine spätere Schema-Version kann optional ein Pattern für `integrity:<method-or-profile>:<marker-ref>` ergänzen; dies ist im aktuellen Baseline-Stand noch nicht anzuwenden. | target_assumption |
| Die konkrete Methode oder Hash-Konstruktion bleibt offen und wird hier nicht erfunden. | open |
