# CTI Bookmarks

Welcome — this is a browser bookmark file (`cti-bookmarks.html`) collecting open source cyber threat intelligence resources I've found useful, organised for import into a browser.

For day-to-day hunting, you can also open [`cti-bookmarks-console.html`](cti-bookmarks-console.html) in a browser: same curated set, with folder navigation, search, star list, light/dark theme, and a **Use for** filter aimed at threat hunters (enrich, sandbox, detect, feed, and so on). Not a generic mega-bookmark dump.

## Index ℹ️

This collection is organised into four top-level folders that map onto the different intelligence levels and needs of a CTI analyst: **Operational**, **Tactical**, and **Strategic** intelligence, plus a **Tools** folder for the day-to-day analysis platforms that cut across all three. While all three intelligence levels are essential for effective decision-making, they differ in focus, scope, timeframe, and intended audience — reflecting the hierarchical levels and operational requirements of the organisation.

### Operational 🚨
Operational intelligence covers the medium-term picture — active campaigns, live feeds, and the ongoing situational awareness an analyst needs day to day.

- **National CERTs & Advisories 🏛️** — government and national CERT advisory feeds (NCSC, CISA, ENISA, BSI, ACSC, CCCS, CERT NZ) plus ISAC directories for sector-based sharing
- **Adversary Intelligence 🌐** — actor profile databases, alias cross-referencing, APT mapping projects, and tool matrices tracking who's using what
- **Ransomware Intelligence 🔒** — leak site trackers, victim indexes, decryptor repositories, and countermeasure tracking specific to ransomware crews
- **IoC Feeds & Sharing 🎱** — live indicator feeds (abuse.ch, OTX, Emerging Threats) and open MISP-compatible feed lists
- **Situational Awareness & News 🗺️** — daily security news, incident journalism, and independent CTI analysis blogs
- **Monthly Threat Reports ⏱️** — recurring vendor threat briefings and pulse reports

### Tactical 🐾

Tactical intelligence supports short-term decisions and hands-on technical work — detection engineering, hunting, and understanding specific techniques.

- **Frameworks & Methodology ⚙️** — ATT&CK and its extended family (D3FEND, CAR, CAPEC, Engage), the Diamond Model, Kill Chain, and CTI fundamentals
- **Detection Engineering 🚨** — Sigma/YARA rule repositories, SIEM use-case marketplaces, and detection validation tooling (Atomic Red Team)
- **Threat Hunting 🐾** — hunt playbooks, beaconing detection, and network monitoring tools
- **TTP & Technique References 📖** — living-off-the-land binary/driver/library catalogues (LOLBAS, GTFOBins, LOLDrivers, Hijack Libs) and technique lookup sites
- **Exploitation & Offensive Technique References 💣** — exploit databases, shellcode, payload, and reverse-shell references used to understand attacker tradecraft
- **Datasets & Adversary Emulation Logs 🗃️** — public datasets and replayed emulation logs for testing detections
- **Vendor Threat Research 🔬** — the major vendor threat intel blogs (Talos, Mandiant, Unit42, Securelist, CrowdStrike, and more) plus report libraries

### Strategic 🧭
Strategic intelligence informs long-term planning and executive decision-making — landscape trends, geopolitics, and governance.

- **Annual & Landscape Reports 📊** — the flagship yearly reports (DBIR, ENISA Threat Landscape, M-Trends, X-Force, Digital Defense Report)
- **Geopolitics & Policy 🌍** — think tank research, cyber law toolkits, nation-state operations breakdowns, and sanctions trackers
- **Risk, Governance & Standards 📜** — control frameworks and standards (NIST CSF, CIS Controls, ISO 27001, PCI DSS, Essential Eight, IT-Grundschutz) and CTI capability frameworks (FIRST, CREST, STIX/TAXII)

### Tools 🛠️
The Tools folder holds the day-to-day analysis platforms, grouped by what the tool is used for rather than by the intelligence level.

- **IP, URL & Domain Analysis 🔎** — reputation lookups, sandboxed URL rendering, and IP/ASN enrichment
- **DNS & Infrastructure Pivoting 🕸️** — passive DNS, certificate transparency, and domain permutation/typosquat tools
- **File & Malware Analysis ☣️** — sandboxes, sample repositories, and static/dynamic analysis tooling
- **Phishing & Email Analysis 🎣** — header analysis, SPF/DKIM/DMARC inspection, and phishing kit trackers
- **Vulnerability & Exploit Intelligence 🩹** — CVE/CWE databases, exploitation scoring (EPSS), and 0-day tracking
- **Dark Web & Exposure Monitoring 🕶️** — breach checkers, onion service directories, and darknet OSINT tooling
- **Internet Scanning & Attack Surface 🛰️** — Shodan/Censys-style scanners and secret-leak detection
- **OSINT & Investigation 🔍** — general-purpose OSINT toolkits, enumeration tools, and archiving services
- **Threat Intelligence Platforms (TIPs) 🧩** — MISP, OpenCTI, TheHive/Cortex, and related knowledge-management platforms
- **Reporting & Analytic Tradecraft ✍️** — report templates, analytic standards (ICD 203), and tradecraft training material
- **Technical References 📚** — encyclopedic lookups (HTTP codes, TLDs, file signatures, Windows APIs, syscalls) used while investigating
- **Learning, Labs & Skill-Building 🧠⬆️** — free labs, gamified projects, and certification study resources
- **AI-Assisted CTI & Agent Security 🤖** — emerging tooling for AI-assisted analysis and securing AI agents themselves
- **Curated Resource Lists 📑** — meta-collections and "awesome-list" style repositories covering OPSEC, ICS/OT, mobile threat intel, certifications, forensics, and incident response, for further reading beyond what's bookmarked directly

