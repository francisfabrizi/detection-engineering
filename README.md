# Detection Engineering Portfolio

A practical cybersecurity portfolio focused on detection engineering, threat hunting and security monitoring.

This repository contains hands-on projects developed by **LogikSec**, demonstrating the development, validation and implementation of security detections across SIEM platforms.

## Areas of Focus

* **Sigma Rules:** Developing vendor-neutral detection logic.
* **SIEM Detection:** Converting Sigma rules into Splunk SPL and Microsoft Sentinel KQL.
* **Threat Hunting:** Investigating suspicious activity and developing hypothesis-driven hunts.
* **MITRE ATT&CK:** Mapping detection logic to adversary tactics and techniques.
* **Detection Engineering:** Improving detection coverage, identifying false positives and documenting detection logic.

## Repository Structure

| Directory              | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `Sigma-Rules/`         | Sigma detection rules and SIEM conversions           |
| `Threat-Hunting/`      | Threat hunting queries and investigations            |
| `Detection-Playbooks/` | Detection documentation and investigation procedures |
| `Screenshots/`         | Supporting technical evidence                        |

## Current Projects

### Windows Reconnaissance Commands Detection

A Sigma detection designed to identify Windows reconnaissance activity involving commands such as:

* `whoami`
* `ipconfig`
* `nltest`
* `systeminfo`
* `net user`
* `net group`
* `net localgroup`

**MITRE ATT&CK techniques:**

* T1087 – Account Discovery
* T1082 – System Information Discovery
* T1016 – System Network Configuration Discovery

**Available implementations:**

* Sigma YAML
* Splunk SPL using the Splunk CIM processing pipeline

**Validation:** Successfully parsed and validated locally using pySigma. Splunk conversion completed successfully.

## Development Approach

Projects follow a repeatable detection engineering workflow:

1. Identify suspicious behaviour and relevant attack techniques.
2. Develop detection logic using Sigma.
3. Validate the rule structure.
4. Convert detection logic into SIEM-specific queries.
5. Test against representative security telemetry.
6. Document findings, limitations and potential false positives.

## Disclaimer

This repository is intended for educational and professional development purposes. Detection rules are experimental unless explicitly stated otherwise and should be tested and tuned before deployment in production environments.

Some projects build upon practical training exercises and publicly available security research. Relevant sources are credited within individual project documentation.
