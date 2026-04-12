# aurora-polaris__mvp-architecture.md

## Zweck und Abgrenzung

| Aussage | Klasse |
|---|---|
| Dieses Artefakt beschreibt den Phase-0/1-Zielschnitt des regulierten Aurora-MVP. | derived_from_source |
| Dieses Artefakt enthält nur Architektur, Systemgrenzen, Flüsse, minimale Schnittstellen, Events und Governance-Mechanik für das MVP. | target_assumption |
| Langfristige Zukunftsmodule bleiben out of scope, sofern sie nicht für Phase 0/1 benötigt werden. | target_assumption |

## Phase-0/1-Zielschnitt

| Phase | Ziel | Enthaltene Bausteine | Klasse |
|---|---|---|---|
| Phase 0: Foundation | Basisplattform für Orchestrierung, Wissen, Policies und Audit schaffen | Polaris Core, API Gateway, Agent Registry, Policy Engine, PostgreSQL, FAISS, Audit Store, Observability, RBAC, Vault, erste Betriebsmodi, Template-Bibliothek | stated_in_source |
| Phase 1: Regulated MVP | regulierte Freigabe- und Monitoring-Workflows validieren | Legal Compliance Assessor, Secure-Model-Releaser, Human-in-the-Loop-Router, Audit-/Governance-Dashboard, KI-Freigabe, Prozessmonitoring | stated_in_source |
| MVP-Fokus | zwei regulierte Startfelder operationalisieren | regulatorische KI-Freigabe und Prozessabweichungs-Erkennung | derived_from_source |

## Systemgrenzen

### In Scope

| Bestandteil | Zweck | Klasse |
|---|---|---|
| Polaris Core | zentrale Orchestrierung, Kontextanalyse, Routing und Risikobewertung | stated_in_source |
| Agent Registry | Verwaltung zulässiger Agenten, Fähigkeiten und Statusinformationen | derived_from_source |
| Policy Engine | Policy-Prüfung, Blockierung, Eskalation und Freigabesteuerung | stated_in_source |
| Audit Store | revisionsfähige Ablage von Entscheidungen, Provenance und Prüfpfaden | stated_in_source |
| HITL Router | Eskalation an Human Review bei Schwellenwerten oder Policy-Anforderungen | stated_in_source |
| Legal Compliance Assessor | regulatorische Prüfung, Checklisten und Workflow-Gating | stated_in_source |
| Secure-Model-Releaser | stufenweises, policybasiertes Modell-Release | stated_in_source |
| Monitoring Hub / Outlier Detection | Erkennung von Prozessabweichungen, Anomalien und Trends im MVP-Kontext | derived_from_source |
| Knowledge Layer | Retrieval und Kontextspeicherung über PostgreSQL, FAISS und Ontologien | stated_in_source |
| Governance Dashboard | Audit-, Compliance- und Freigabestatus für Phase 1 sichtbar machen | stated_in_source |

### Out of Scope für Phase 0/1

| Bestandteil | Status | Klasse |
|---|---|---|
| Innovation Forge und Patent-Scoring | später / Deep-Dive Expansion | stated_in_source |
| Quantum Sampler Adapter | später / Deep-Dive Expansion | stated_in_source |
| Third-Party-Agent-Marketplace | später / 2026+ Skalierung | stated_in_source |
| >45 Sprachen | später / 2026+ Skalierung | stated_in_source |
| Neuromorphic-Acceleration-PoCs | später / 2026+ Skalierung | stated_in_source |
| Emotion-Synth und erweiterte empathische Module | später / 2026+ Skalierung | stated_in_source |
| Storytelling/Spielleitung | kein MVP-Architekturgegenstand | derived_from_source |

## Kernmodule des regulierten MVP

| Modul | MVP-Aufgabe | Klasse |
|---|---|---|
| API Gateway | Eingangspunkt für Anfrage, Authentisierung und Policy Pre-Check | stated_in_source |
| Polaris Core | plant Aufgaben, routet an zulässige Agenten und bewertet Risiko/Confidence | stated_in_source |
| Context & Prompt Engine | strukturiert Anfrage, Kontext, Ontologien und Prompt-Pakete | stated_in_source |
| Agent Registry | stellt Fähigkeiten, Verfügbarkeit und zulässige Agentenpfade bereit | derived_from_source |
| Policy Engine | prüft Policies vor Ausführung, Freigabe und Antwort | stated_in_source |
| Legal Compliance Assessor | bewertet regulatorische Anforderungen und erzeugt Compliance-Status | stated_in_source |
| Secure-Model-Releaser | steuert Sandbox, Pilot, Canary und Produktion für Modellfreigaben | stated_in_source |
| HITL Router | leitet Fälle an Doppel-Review oder Eskalation weiter | stated_in_source |
| Audit Store | speichert Entscheidungsprovenienz, Auditpunkte und Integritätsnachweise | stated_in_source |
| Knowledge Layer | liefert Kontext aus PostgreSQL, FAISS und Ontologien | stated_in_source |
| Monitoring Hub | verarbeitet Telemetrie, Abweichungen und Drift-Hinweise für MVP-Use-Cases | derived_from_source |
| Governance Dashboard | zeigt Freigabe-, Audit-, Policy- und Risikostatus an | stated_in_source |

## Daten- und Kontrollflüsse

| Schritt | Fluss | Klasse |
|---:|---|---|
| 1 | User oder System Input erreicht API Gateway mit Authentisierung und Policy Pre-Check. | stated_in_source |
| 2 | Polaris Core analysiert Kontext, Routingbedarf und Risikoklasse. | stated_in_source |
| 3 | Knowledge Layer liefert relevante Informationen aus PostgreSQL, FAISS und Ontologien. | stated_in_source |
| 4 | Agent Registry und Policy Engine bestimmen zulässige Agenten und Ausführungspfade. | derived_from_source |
| 5 | Spezialisierte MVP-Agenten führen Teilaufgaben sequenziell oder parallel aus. | stated_in_source |
| 6 | Evaluation prüft Confidence, Compliance, Ethik, Security und Drift-Hinweise. | stated_in_source |
| 7 | HITL Router eskaliert, wenn Schwellenwerte, Policies oder Risikoklassen dies verlangen. | stated_in_source |
| 8 | Ergebnis wird mit Provenance, Entscheidungspfad und Audit-Eintrag bereitgestellt. | stated_in_source |
| 9 | Feedback- und Monitoring-Events speisen Lern-, Drift- und Release-Prüfungen. | stated_in_source |

## Agent Registry, Policy Engine, Audit Store und HITL Router

| Komponente | Mindestverantwortung im MVP | Klasse |
|---|---|---|
| Agent Registry | Fähigkeiten, Modulversionen, Health-Status und erlaubte Einsatzkontexte verwalten | derived_from_source |
| Policy Engine | Ausführung vorab prüfen, Policy-Verstöße blockieren und Review-Schwellen anwenden | stated_in_source |
| Audit Store | Anfragen, Entscheidungen, genutzte Quellen, Scores, Freigaben und Eskalationen protokollieren | derived_from_source |
| HITL Router | Doppel-Review bei Confidence < 0,83 und Eskalation ethischer Abweichungen auslösen | stated_in_source |
| Secure-Model-Releaser | Release-Gates, Canary-Plan und Rollback-Bedingungen verwalten | stated_in_source |

## Minimale Schnittstellen

| Schnittstelle | Zweck | MVP-Relevanz | Klasse |
|---|---|---|---|
| `/capabilities` | verfügbare Fähigkeiten eines Moduls offenlegen | Agent Registry und Planbarkeit | stated_in_source |
| `/plan` | vorgeschlagenen Ausführungsplan erzeugen | Orchestrierung | stated_in_source |
| `/execute` | freigegebene Teilaufgabe ausführen | kontrollierte Agentenausführung | stated_in_source |
| `/explain` | Begründung, Herkunft und Prüfpfad liefern | Audit und Governance | stated_in_source |
| `/health` | Betriebsstatus bereitstellen | Observability und Routing | stated_in_source |
| `/metrics` | Metriken für SLO, Drift, Kosten und Nachhaltigkeit liefern | Monitoring und Governance | stated_in_source |

## Eventtypen

| Eventtyp | Bedeutung im MVP | Klasse |
|---|---|---|
| `aurora.context.enriched` | Kontext wurde angereichert und klassifiziert. | stated_in_source |
| `aurora.task.planned` | Polaris Core hat einen Ausführungsplan erstellt. | stated_in_source |
| `aurora.agent.result` | Ein Agent hat ein Teilresultat geliefert. | stated_in_source |
| `aurora.policy.blocked` | Policy Engine hat Ausführung oder Antwort blockiert. | stated_in_source |
| `aurora.feedback.received` | Nutzer- oder Systemfeedback wurde erfasst. | stated_in_source |
| `aurora.drift.detected` | Drift oder ungewöhnliche Abweichung wurde erkannt. | stated_in_source |
| `aurora.model.promoted` | Modell wurde in eine höhere Freigabestufe verschoben. | stated_in_source |

## Audit-, Policy- und Freigabelogik

| Bedingung | Systemreaktion | Klasse |
|---|---|---|
| Confidence < 0,83 | Doppel-Review oder Human-in-the-Loop | stated_in_source |
| Ethikabweichung erkannt | Eskalation innerhalb von < 2 h | stated_in_source |
| Drift erkannt | Shadow Mode, Canary oder Auto-Rollback prüfen | stated_in_source |
| CVSS >= 7,3 in CI/CD oder Laufzeitbefund | Auto-Rollback oder Block | stated_in_source |
| Policy-Verstoß | Antwort blockieren, Audit-Eintrag erzeugen, Eskalation auslösen | stated_in_source |
| High-Risk-Release | Freigabe nur über Secure-Model-Releaser | stated_in_source |

## Release Gates

| Stufe | Zweck | Klasse |
|---|---|---|
| Sandbox | interne Tests ohne produktive Nutzung | stated_in_source |
| Guarded Pilot | kontrollierte Nutzergruppe | stated_in_source |
| Canary | limitierter Produktivanteil | stated_in_source |
| Full Production | Produktion nach Compliance-, Bias-, Security- und Drift-Freigabe | stated_in_source |

Pflichtartefakte für Modellfreigaben:

| Artefakt | Klasse |
|---|---|
| Model Card | stated_in_source |
| Eval-Report | stated_in_source |
| Bias-/Robustheitsreport | stated_in_source |
| Datenschutzbewertung | stated_in_source |
| Rollback-Plan | stated_in_source |
| Freigabeprotokoll | stated_in_source |

## Offene technische Entscheidungen

| Entscheidung | Status | Klasse |
|---|---|---|
| Zielbetrieb: Cloud, Hybrid oder On-Prem | offen | open |
| konkrete Datenmodelle für Audit Store, Registry und Policy Packs | offen | open |
| konkrete Compliance Packs je Branche und Land | offen | open |
| Mandantenmodell und Rollenmodell | offen | open |
| konkrete Connector-Freigaben für Jira, Slack, Teams, SAP S/4HANA, Snowflake und DSaaS-Feeds | offen | open |
| verbindliche Model Registry und Model-Card-Struktur | offen | open |
| konkrete Observability- und Dashboard-Implementierung | offen | open |
| produktive Prüfung der in den Quellen genannten Baseline-/Leistungswerte | offen | open |

## Nicht Bestandteil dieses Artefakts

| Nicht enthalten | Begründung | Klasse |
|---|---|---|
| Vision- oder Markenprosa | gehört nicht in den MVP-Zielschnitt | target_assumption |
| Agenten-Systemidentität und Antwortregeln | gehört in `aurora-polaris__system-prompt.md` | target_assumption |
| langfristige Deep-Dive-Module als MVP-Kern | erst nach Phase 1 relevant | stated_in_source |
| Roadmap jenseits Phase 0/1 als Architekturvorgabe | gehört in `aurora-polaris__strategy.md` | target_assumption |
| reale externe Zugriffe oder Live-Datennutzung | nicht freigegeben | stated_in_source |

## Offene Punkte

| Punkt | Klasse |
|---|---|
| Die minimale technische Spezifikation der Schnittstellen ist noch nicht als OpenAPI/gRPC-Vertrag formalisiert. | open |
| Die genaue Audit-Schema-Struktur ist offen. | open |
| Die konkrete Policy-Sprache ist mit OPA/Rego benannt, aber Kontrollkataloge sind nicht ausgearbeitet. | open |
| Die MVP-Use-Case-Priorisierung ist aus den Quellen ableitbar, aber noch nicht final freigegeben. | open |
