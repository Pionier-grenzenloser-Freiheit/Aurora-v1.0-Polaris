# aurora-polaris__mvp-control-contract.md

## 1. Zweck und Geltungsbereich

| Punkt | Vertrag | Klasse |
|---|---|---|
| Zweck | Dieses Dokument definiert den minimalen Kontrollvertrag für den regulierten Aurora-Polaris-MVP in Phase 0/1. | derived_from_source |
| Bezug | Der Vertrag formalisiert die Kontrollflächen aus `aurora-polaris__mvp-architecture.md`: Modulmanifest, Policy Decision, Audit Event, Release Gates, HITL-Auslöser und MVP-Events. | derived_from_source |
| Geltung | Der Vertrag gilt für MVP-relevante Module, kontrollierte Ausführung, Freigaben, Auditierung und Eskalation. | target_assumption |
| Fail-closed-Regel | Fehlt ein Pflichtfeld, Pflichtartefakt oder eine Policy-Entscheidung, wird Ausführung, Antwort oder Promotion blockiert oder an Human Review eskaliert. | target_assumption |
| Externe Systeme | Externe Connectoren bleiben ohne ausdrückliche Freigabe konzeptionell und dürfen nicht als operativ verfügbar behandelt werden. | stated_in_source |
| Out of scope | Langfristige Deep-Dive-Module, Marketplace, mehrsprachige Skalierung, Neuromorphic-PoCs, Emotion-Synth, reale Live-Datenzugriffe und Deployment-Manifeste sind nicht Bestandteil dieses Vertrags. | derived_from_source |

## 2. Modulmanifest-Minimalschema

Jedes MVP-relevante Modul muss vor Planung, Ausführung oder Freigabe ein Manifest nach folgendem Feldvertrag besitzen.

| Feld | Pflicht | Vertrag | Klasse |
|---|---:|---|---|
| `module_id` | ja | stabiler technischer Modulbezeichner, eindeutig im MVP-Kontext | derived_from_source |
| `module_type` | ja | Rolle des Moduls, z. B. Gateway, Orchestrator, Registry, Policy, Agent, Store, Router, Release Gate, Dashboard | derived_from_source |
| `version` | ja | versionierter Modulstand; SemVer ist als Zielstandard gesetzt | stated_in_source |
| `purpose` | ja | knappe Zweckbeschreibung des Moduls im MVP | derived_from_source |
| `capabilities` | ja | Liste der erlaubten Fähigkeiten des Moduls | stated_in_source |
| `dependencies` | ja | benötigte interne Module, Speicher, Policies oder Kontrollflächen; leere Liste ist zulässig | derived_from_source |
| `allowed_connectors` | ja | erlaubte Connectoren; externe Connectoren nur bei Freigabe, sonst `[]` oder `conceptual_only` | derived_from_source |
| `policy_profile` | ja | zugeordnetes Policy-Profil oder `open`, wenn noch nicht spezifiziert | stated_in_source |
| `review_policy` | ja | Review-Schwellen und Eskalationsregeln, mindestens Confidence- und Policy-Verstoß-Behandlung | derived_from_source |
| `health_signals` | ja | minimale Betriebs- und Kontrollsignale, die über `/health` oder `/metrics` sichtbar werden | derived_from_source |
| `output_contract` | ja | erwarteter Output-Typ, Pflichtfelder und Referenzierbarkeit für Audit | target_assumption |
| `fallback_action` | ja | eine kontrollierte Rückfallaktion: `block`, `human_review`, `safe_response` oder `rollback_candidate` | derived_from_source |

MVP-relevante Modul-IDs:

| `module_id` | `module_type` | Zweck | Klasse |
|---|---|---|---|
| `api-gateway` | Gateway | Eingangspunkt, Authentisierung, Policy Pre-Check | derived_from_source |
| `polaris-core` | Orchestrator | Planung, Routing, Risiko-/Confidence-Bewertung | stated_in_source |
| `context-prompt-engine` | Agent | Kontextstrukturierung und Prompt-Paket-Erzeugung | stated_in_source |
| `agent-registry` | Registry | Fähigkeiten, Versionen, Health-Status und erlaubte Einsatzkontexte | derived_from_source |
| `policy-engine` | Policy | Policy-Prüfung, Blockierung, Eskalation und Freigabesteuerung | stated_in_source |
| `legal-compliance-assessor` | Agent | regulatorische Prüfung, Checklisten, Workflow-Gating | stated_in_source |
| `secure-model-releaser` | Release Gate | stufenweises, policybasiertes Modell-Release | stated_in_source |
| `hitl-router` | Router | Human-in-the-Loop- und Doppel-Review-Eskalation | stated_in_source |
| `audit-store` | Store | Audit-Trail, Provenance und Prüfpfade | stated_in_source |
| `knowledge-layer` | Store | Kontext und Retrieval über PostgreSQL, FAISS und Ontologien | derived_from_source |
| `monitoring-hub` | Monitoring | Telemetrie, Anomalien, Drift- und Prozessabweichungshinweise | derived_from_source |
| `governance-dashboard` | Dashboard | Sichtbarkeit von Audit-, Compliance-, Policy- und Freigabestatus | stated_in_source |

## 3. Policy-Decision-Minimalschema

Jede kontrollierte Ausführung, Blockierung, Eskalation oder Promotion muss eine Policy Decision referenzieren.

| Feld | Pflicht | Vertrag | Klasse |
|---|---:|---|---|
| `decision_id` | ja | eindeutige Kennung der Policy-Entscheidung | target_assumption |
| `subject` | ja | betroffene Anfrage, Aufgabe, Modulaktion, Antwort oder Release-Promotion | derived_from_source |
| `policy_pack` | ja | angewendeter Policy-Katalog oder `open`, wenn noch nicht spezifiziert | stated_in_source |
| `decision` | ja | kontrollierter Entscheidungswert: `allow`, `block`, `require_human_review`, `escalate`, `promote` oder `rollback_candidate` | derived_from_source |
| `severity` | ja | Schweregrad der Entscheidung; finale Taxonomie ist offen | target_assumption |
| `rationale` | ja | kurze Begründung der Entscheidung ohne interne Denkprotokolle | derived_from_source |
| `triggered_rules` | ja | Liste ausgelöster Regeln, Schwellen oder Kontrollpunkte | derived_from_source |
| `requires_human_review` | ja | boolescher Wert; `true` bei HITL-Auslösern oder unvollständiger Evidenz | derived_from_source |
| `timestamp` | ja | Zeitstempel der Entscheidung; genaue Zeitquelle offen | target_assumption |

Mindestregel: `decision = allow` ist nur zulässig, wenn keine offenen Pflichtfelder, keine blockierende Policy-Regel und kein ungeklärter HITL-Auslöser vorliegt.

## 4. Audit-Event-Minimalschema

Jeder relevante Kontrollschritt muss als Audit Event nachvollziehbar sein. Payloads werden über Referenzen geführt; Rohdaten gehören nicht in das Minimalschema.

| Feld | Pflicht | Vertrag | Klasse |
|---|---:|---|---|
| `event_id` | ja | eindeutige Ereigniskennung | target_assumption |
| `event_type` | ja | Eventtyp aus dem MVP-Event-Set | stated_in_source |
| `correlation_id` | ja | Verknüpfung zusammengehöriger Anfrage-, Policy-, Agenten- und Release-Ereignisse | derived_from_source |
| `actor` | ja | auslösender Akteur: Nutzer, System, Modul oder Reviewer | derived_from_source |
| `module_id` | ja | referenziertes MVP-Modul | derived_from_source |
| `input_ref` | ja | Referenz auf Eingabe, Kontext oder Artefakt; keine Rohdatenpflicht | target_assumption |
| `output_ref` | ja | Referenz auf Ergebnis oder Artefakt; `null` bei Blockierung zulässig | target_assumption |
| `decision_ref` | ja | Referenz auf zugehörige Policy Decision | derived_from_source |
| `confidence` | ja | Confidence-Wert oder `null`, wenn für das Ereignis nicht anwendbar | stated_in_source |
| `risk_score` | ja | Risiko-Score oder Risikoklasse; genaue Skala offen | stated_in_source |
| `integrity_marker` | ja | Integritätsmarker für Nachvollziehbarkeit; konkrete Konstruktion offen | stated_in_source |
| `timestamp` | ja | Zeitstempel des Ereignisses; genaue Zeitquelle offen | target_assumption |

Mindestregel: Ein Audit Event ohne `correlation_id`, `event_type`, `module_id`, `decision_ref` oder `timestamp` ist nicht kontrollvertragskonform.

## 5. Release-Gate-Checkliste

| Gate | Eintrittsbedingungen | Prüfkriterien | Pflichtartefakte | Blocker | Eskalationsweg |
|---|---|---|---|---|---|
| Sandbox | Modulmanifest vorhanden; Policy-Profil zugeordnet; interne Testnutzung | Health-Signale vorhanden; Policy Decision referenzierbar; Audit Event erzeugbar | Modulmanifest, Policy Decision, Audit Event; bei Modellartefakten zusätzlich Model Card und Eval-Report | fehlendes Manifest, fehlende Policy-Zuordnung, fehlender Audit-Trace | Secure-Model-Releaser oder HITL Router |
| Guarded Pilot | Sandbox nicht blockiert; Review Policy definiert; Pflichtartefakte referenzierbar | Compliance-, Bias-, Robustheits-, Security- und Datenschutzprüfung begonnen oder als offen markiert | Model Card, Eval-Report, Bias-/Robustheitsreport, Datenschutzbewertung, Rollback-Plan, Freigabeprotokoll | Policy-Verstoß, fehlende Pflichtartefakte, Confidence < 0,83 ohne Review | HITL Router, Legal Compliance Assessor, Ethics & Audit |
| Canary | Guarded Pilot nicht blockiert; Rollback-Bedingungen definiert | Drift-Hinweise, Security-Befunde, Policy-Verstöße und Audit-Abdeckung geprüft | aktualisierte Pflichtartefakte, Canary-Plan, Rollback-Plan, Freigabeprotokoll | Drift ohne Bewertung, CVSS >= 7,3, Policy-Verstoß, fehlender Rollback-Plan | Secure-Model-Releaser, HITL Router, Auto-Rollback-Kandidat |
| Full Production | Canary nicht blockiert; Freigabeentscheidung vorhanden | Compliance-, Bias-, Security- und Drift-Freigabe vorhanden; Audit-Trail vollständig referenzierbar | vollständige Pflichtartefakte, finale Policy Decision, Freigabeprotokoll | fehlende Freigabe, offene High-Risk-Policy, ungeklärte Ethikabweichung, fehlende Audit-Referenzen | Block, Human Review, Secure-Model-Releaser |

## 6. HITL-Auslöser

| Auslöser | Mindestreaktion | Klasse |
|---|---|---|
| Confidence < 0,83 | Doppel-Review oder Human-in-the-Loop | stated_in_source |
| Policy-Verstoß | blockieren, Audit-Eintrag erzeugen, eskalieren | stated_in_source |
| Ethikabweichung | Eskalation innerhalb von < 2 h | stated_in_source |
| Drift-Hinweis | Shadow Mode, Canary-Prüfung oder Auto-Rollback-Kandidat | stated_in_source |
| Security-/CVSS-Befund >= 7,3 | Auto-Rollback oder Block | stated_in_source |
| fehlende Pflichtartefakte | Gate blockieren oder Human Review erzwingen | derived_from_source |
| fehlende Policy Decision | Ausführung, Antwort oder Promotion blockieren | target_assumption |

## 7. Event-Set des MVP

Alle MVP-Events müssen das Audit-Event-Minimalschema erfüllen. Event-spezifische Nutzdaten werden nur referenziert.

| Eventtyp | Verwendungszweck | Minimale Zusatzfelder / Referenzen | Klasse |
|---|---|---|---|
| `aurora.context.enriched` | Kontext wurde angereichert und klassifiziert. | `input_ref`, `output_ref`, `risk_score` | stated_in_source |
| `aurora.task.planned` | Polaris Core hat einen Ausführungsplan erstellt. | `module_id`, `output_ref`, `decision_ref` | stated_in_source |
| `aurora.agent.result` | Ein Agent hat ein Teilresultat geliefert. | `module_id`, `output_ref`, `confidence` | stated_in_source |
| `aurora.policy.blocked` | Policy Engine hat Ausführung, Antwort oder Promotion blockiert. | `decision_ref`, `triggered_rules`, `risk_score` | stated_in_source |
| `aurora.feedback.received` | Nutzer- oder Systemfeedback wurde erfasst. | `actor`, `input_ref`, `correlation_id` | stated_in_source |
| `aurora.drift.detected` | Drift oder ungewöhnliche Abweichung wurde erkannt. | `module_id`, `risk_score`, `decision_ref` | stated_in_source |
| `aurora.model.promoted` | Modell wurde in eine höhere Freigabestufe verschoben. | `module_id`, `decision_ref`, `output_ref` | stated_in_source |

## 8. Offene Punkte

| Punkt | Klasse |
|---|---|
| Finale Serialisierung der Schemata als JSON Schema, OpenAPI oder gRPC-Vertrag ist offen. | open |
| Konkrete Wertelisten für `module_type`, `severity`, `risk_score` und `policy_pack` sind offen. | open |
| Exakte Konstruktion des `integrity_marker` ist offen. | open |
| Verbindliche Zeitquelle für `timestamp` ist offen. | open |
| Konkrete Policy Packs je Branche und Land sind offen. | open |
| Reale Connector-Freigaben für Unternehmenssysteme und DSaaS-Feeds sind offen. | open |
| Aufbewahrungsfristen und Zugriffsklassen für Audit Events sind offen. | open |
