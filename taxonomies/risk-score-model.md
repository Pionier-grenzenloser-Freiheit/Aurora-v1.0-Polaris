# risk-score-model.md

## Zweck

| Punkt | Festlegung | Klasse |
|---|---|---|
| Ziel | Dieses Dokument legt ein minimales Modell für `risk_score` in Audit- und MVP-Events fest. | derived_from_source |
| Bezug | Der Kontrollvertrag erlaubt `risk_score` als Risiko-Score oder Risikoklasse; die genaue Skala ist offen. | stated_in_source |
| Schema-Stand | Das freigegebene Schema-Pack erlaubt aktuell `number` oder `string`. | stated_in_source |

## Modellentscheidung

| Entscheidung | Begründung | Klasse |
|---|---|---|
| `risk_score` bleibt dual modelliert: numerisch oder ordinal. | Das bestehende Schema bildet bereits beide Varianten ab und der Kontrollvertrag lässt die genaue Skala offen. | derived_from_source |
| Numerische Werte werden für berechenbare Risikoausgaben genutzt. | Der Kontrollvertrag nennt Risiko-Score als mögliche Form. | stated_in_source |
| Ordinale Werte werden für klassifizierte Risikoausgaben genutzt. | Der Kontrollvertrag nennt Risikoklasse als mögliche Form. | stated_in_source |
| Bestehende String-Werte wie `open` bleiben baseline-kompatibel. | Das freigegebene Schema erlaubt `string`, und gültige Beispielinstanzen verwenden `open`. | derived_from_source |

## Ordinale Zielwerte

| Wert | Bedeutung | Klasse |
|---|---|---|
| `low` | geringe kontrollierte Risikolage ohne automatische Review-Pflicht | target_assumption |
| `medium` | relevante Risikolage mit expliziter Begründungspflicht | target_assumption |
| `high` | Risikolage mit Review-, Gate- oder Eskalationsbezug | target_assumption |
| `critical` | blockierende oder rollback-nahe Risikolage | target_assumption |
| `open` | Risikolage noch nicht abschließend klassifiziert | derived_from_source |

## Numerisches Zielmodell

| Festlegung | Klasse |
|---|---|
| Numerische Werte sollen als `number` geführt werden. | stated_in_source |
| Eine verbindliche numerische Skala ist noch offen. | open |
| Bis zur finalen Skala darf numerisches `risk_score` nicht automatisch mit Severity gleichgesetzt werden. | target_assumption |

## Migrationshinweis für das bestehende Schema

| Empfehlung | Klasse |
|---|---|
| Kurzfristig keine Änderung am freigegebenen Schema-Pack anwenden; `risk_score` bleibt `number` oder `string`. | target_assumption |
| In einer späteren Schema-Version kann der String-Zweig auf `low`, `medium`, `high`, `critical`, `open` eingeschränkt werden. | target_assumption |
| Eine numerische Mindest-/Höchstskala sollte erst ergänzt werden, wenn die Skala fachlich freigegeben ist. | open |

## Nicht Bestandteil

| Punkt | Klasse |
|---|---|
| Keine Risikoberechnung. | target_assumption |
| Keine branchenspezifische Gewichtung. | open |
| Keine Kopplung an externe Risikofeeds. | stated_in_source |
