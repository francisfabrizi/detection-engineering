# Detection Engineering Portfolio

A practical cybersecurity portfolio focused on detection engineering, threat hunting and security monitoring.

Written and maintained by **Francis Fabrizi**, a SOC analyst working with Splunk, Microsoft Sentinel and Microsoft Defender. Each project documents how a detection is developed, validated and implemented across platforms, including the parts that haven't been proven yet.

## Areas of Focus

- **Sigma Rules:** Vendor-neutral detection logic for behaviour seen in endpoint and network telemetry.
- **SIEM Detection:** Converting Sigma rules into platform-specific queries for Splunk, Microsoft Sentinel and Elastic.
- **Detection Validation:** Checking rule structure, documenting false positives and stating the limits of each detection.
- **MITRE ATT&CK:** Mapping detection logic to adversary tactics and techniques.
- **Threat Hunting:** Hypothesis-driven hunts and the investigation work behind them.

## Repository Structure

| Directory | Description |
|---|---|
| `Sigma-Rules/` | Sigma detection rules, each with its platform queries and documentation |

## Current Projects

### Windows Reconnaissance Commands Detection

A Sigma detection designed to identify Windows reconnaissance activity involving:

- `whoami`
- `ipconfig`
- `nltest`
- `systeminfo`
- `net user`
- `net group`
- `net localgroup`

**MITRE ATT&CK techniques:**

- T1033 – System Owner/User Discovery
- T1016 – System Network Configuration Discovery
- T1082 – System Information Discovery
- T1087 – Account Discovery
- T1069 – Permission Groups Discovery
- T1482 – Domain Trust Discovery
- T1018 – Remote System Discovery

**Implementations:**

- Sigma YAML – vendor-neutral detection rule.
- Splunk CIM query expression – converted using the `splunk_cim` processing pipeline.
- Microsoft Sentinel KQL – using the `SecurityEvent` table and Event ID 4688.
- Elastic Security KQL – using Kibana Query Language and ECS fields such as `process.name` and `process.args`.

**Validation:** The Sigma rule parses and validates cleanly with pySigma, and the Splunk conversion completes successfully. The Sentinel and Elastic queries are written and documented but have not yet been tested against live telemetry. Detection effectiveness remains unproven until that testing is completed.

Full documentation, including telemetry requirements and false positive analysis, is available in `Sigma-Rules/Windows-Recon-Commands/`.

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
