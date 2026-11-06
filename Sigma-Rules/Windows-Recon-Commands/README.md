# Windows Reconnaissance Commands Detection

## 1. Overview

This project demonstrates the development and validation of a Sigma detection rule designed to identify Windows reconnaissance activity.

The detection focuses on commonly used Windows commands that can help an attacker enumerate user accounts, gather system information and discover network configurations.

The rule is written in vendor-neutral Sigma YAML and converted into Splunk SPL using the Splunk Common Information Model (CIM) pipeline.

## 2. Detection Objective

Identify execution of the following Windows commands:

| Command          | Purpose                                           |
| ---------------- | ------------------------------------------------- |
| `whoami.exe`     | Identify the current user and security context    |
| `ipconfig.exe`   | Discover network configuration                    |
| `nltest.exe`     | Enumerate domain and Active Directory information |
| `systeminfo.exe` | Gather operating system and system details        |
| `net.exe`        | Enumerate users, groups and local groups          |

These commands are legitimate administrative tools. However, their execution can also form part of attacker reconnaissance following initial access.

## 3. MITRE ATT&CK Mapping

| Technique | Name                                   | Relevant Activity                      |
| --------- | -------------------------------------- | -------------------------------------- |
| T1087     | Account Discovery                      | User and group enumeration             |
| T1082     | System Information Discovery           | Gathering operating system information |
| T1016     | System Network Configuration Discovery | Discovering network configuration      |

Reference: [MITRE ATT&CK](https://attack.mitre.org/)

## 4. Detection Logic

The Sigma rule uses Windows process creation telemetry.

It identifies:

* Execution of selected reconnaissance binaries.
* Execution of `net.exe` with command-line arguments associated with user and group enumeration.

The detection uses the following Sigma condition:

`1 of selection_*`

This means an event matching any of the defined selection blocks will trigger the rule.

## 5. Splunk Implementation

The Sigma rule was converted into Splunk SPL using the `splunk_cim` processing pipeline.

**Output fields:**

* `Processes.process_path`
* `Processes.process`

These fields correspond to the CIM process data model.

The converted query is available in:

`splunk-output.txt`

**Conversion command:**

```bash
sigma convert -t splunk -p splunk_cim Sigma-Rules/Windows-Recon-Commands/windows-recon-commands.yml
```

The query assumes that relevant endpoint process telemetry is available and correctly mapped to the Splunk CIM data model.

## 6. Microsoft Sentinel Implementation

A Microsoft Sentinel equivalent was developed using Kusto Query Language (KQL).

**Data source:**
- Table: `SecurityEvent`
- Event ID: `4688` – Process Creation

**Detection logic:**

The query identifies execution of the same reconnaissance commands as the Sigma rule, including user and group enumeration through `net.exe`.

**Fields analysed:**
- `NewProcessName`
- `CommandLine`
- `SubjectUserName`
- `Computer`
- `TimeGenerated`

**Query file:**

`windows-recon-commands.kql`

**Telemetry requirements:**

Windows process creation auditing must be enabled. The policy **Include command line in process creation events** must also be enabled to capture command-line arguments.

The workspace must ingest the relevant Windows Security Events into the `SecurityEvent` table.

**Validation status:** KQL query written but not yet tested against live Sentinel telemetry.## 6. Validation

The Sigma rule was validated locally using pySigma.

## 7. Elastic Security Implementation

An Elastic Security equivalent was developed using Kibana Query Language (KQL).

**Platform:**
- Elastic Security
- Kibana Query Language (KQL)
- Elastic Common Schema (ECS)

**Detection logic:**

The query identifies execution of the same reconnaissance commands covered by the Sigma rule, including user and group enumeration through `net.exe`.

**Fields analysed:**
- `event.category`
- `event.type`
- `process.name`
- `process.args`

**Query file:**

`elastic-recon-detection.kql`

**Implementation requirements:**

The Elastic environment must collect process creation telemetry and populate the relevant ECS fields.

The query is designed for use as a KQL filter within an Elastic Security detection rule.

**Validation status:** Query written but not yet tested against live Elastic telemetry.

## 8. Validation

Validation covered:

* YAML parsing.
* Sigma rule parsing.
* Available registered pySigma validators.

**Result:** Passed with no validation findings.

The Splunk conversion also completed successfully.

Note: Successful parsing and conversion do not establish detection effectiveness. Further testing against representative endpoint telemetry is required.

## 9. Potential False Positives

Legitimate activity may trigger this detection, including:

* IT administrator troubleshooting.
* Helpdesk support activity.
* System inventory tools.
* Automated asset discovery.
* Configuration management scripts.

Additional investigation should consider the user account, parent process, command-line arguments, host role and surrounding activity.

## 10. Limitations and Future Improvements

Current limitations:

* The rule detects command execution rather than malicious intent.
* Legitimate administrative activity may generate alerts.
* Detection depends on suitable Windows process creation telemetry.
* The Splunk implementation depends on CIM field mappings and data model availability.
* No production detection effectiveness has yet been established.

Potential improvements:

* Add parent-process and user-context analysis.
* Develop additional correlation logic for sequences of reconnaissance commands.
* Test against representative Windows event telemetry.
* Develop a Microsoft Sentinel KQL equivalent.
* Tune detection logic based on observed false positives.

## 11. Development and Attribution

This project builds on practical detection engineering training and hands-on exercises.

The rule has been independently documented, validated and converted into a Splunk CIM-oriented implementation for this portfolio.

Training source: TryHackMe.

## 12. Disclaimer

This detection is experimental and intended for educational and professional development purposes.

It should be tested and tuned against the target environment before being considered for production deployment.
