## OSINT module list

```

- High priority (core capabilities)

- Passive DNS / Historical DNS lookup  
  Purpose: Retrieve historical/current DNS records (A, AAAA, CNAME, MX, NS).  
  Inputs: domain, IP.  
  Options: source (VirusTotal/Shodan/DNSDumpster/DNSDB), timeframe.  
  Outputs: records list, timestamps.  
  Deps: APIs (VirusTotal, SecurityTrails), dnspython.  

- Whois lookup + parsing  : DONE
  Purpose: Domain registration/registrant, creation/expiry, name servers.  
  Inputs: domain, IP.  
  Options: raw/whois-parsed, redact GDPR fields.  
  Outputs: structured contact fields, raw WHOIS.  
  Deps: python-whois, RDAP clients.  

- Subdomain enumeration (passive only)      
  Purpose: Find subdomains from passive sources.  
  Inputs: domain.  
  Options: passive-only.  
  Outputs: list with source.  
  Deps: APIs (CertSpotter, VirusTotal).  

- Certificate Transparency / Cert search  
  Purpose: Discover domains/subdomains via CT logs (certificates).  
  Inputs: domain, CN/SAN patterns.  
  Options: time range, include expired.  
  Outputs: cert chains, issuance dates, SAN list.  
  Deps: CertSpotter API, requests.  

- IP Ownership / ASN lookup  
  Purpose: Map IP → owner, ASN, netblocks, geolocation.  
  Inputs: IP or ASN.  
  Options: include RIPE/ARIN whois, reverse DNS.  
  Outputs: ASN, prefixes, owner, country.  
  Deps: ipwhois, Team Cymru, MaxMind lite.  

- Identity & people search

- Email harvest (passive only)  
  Purpose: Collect emails (from search engines, breach APIs).  
  Inputs: domain, person name, pattern.  
  Options: check hunter.io/HaveIBeenPwned.  
  Outputs: emails + source.  
  Deps: Hunter API, HaveIBeenPwned.  

- Social media aggregator  
  Purpose: Search usernames across platforms, gather public profiles.  
  Inputs: username, name, profile URL.  
  Options: platform list, depth (profile only / posts).  
  Outputs: profile metadata, profile links, last activity.  
  Deps: platform APIs (Twitter/X, Instagram via scraping or APIs).  

- People search / PII enrichment  
  Purpose: Combine public records, social, and people-search sources to build profiles.  
  Inputs: name, location, phone, email.  
  Options: strict/loose matching, include relatives.  
  Outputs: aggregated profile, confidence score.  
  Deps: Pipl-like services (commercial), open sources.  

- Phone number lookup  
  Purpose: Carrier, region, public listings, WhatsApp/Telegram presence.  
  Inputs: phone number.  
  Options: international format, carrier lookup.  
  Outputs: carrier, type, associated accounts (where available).  
  Deps: Numverify, social lookup.  

- Social media & content analysis

- Post / tweet search & archive (social media)  
  Purpose: Search posts by keywords, user, timeframe.  
  Inputs: keyword, handle, date range.  
  Options: include replies, media-only.  
  Outputs: posts, metadata, engagement metrics.  
  Deps: platform APIs (X, Reddit, Mastodon, YouTube).  

- Image reverse search & metadata extraction  
  Purpose: Reverse-image search, EXIF extraction, find duplicates.  
  Inputs: image file or URL.  
  Options: search engines (Google, Bing, Yandex), include perceptual hashing.  
  Outputs: matches, EXIF, thumbnails, similarity score.  
  Deps: exifread, TinEye/Google Vision APIs (or scraping).  

- Video/YouTube metadata & comments scraper  
  Purpose: Fetch video metadata, comments, channel info, captions.  
  Inputs: video URL or channel.  
  Options: download captions, comment depth.  
  Outputs: transcripts, upload dates, subscribers.  
  Deps: pytube, YouTube Data API.  

- Infrastructure & metadata

- Technology fingerprinting (passive headers only)  
  Purpose: Detect CMS, frameworks, server software from public data.  
  Inputs: URL.  
  Options: include header analysis, JS fingerprinting (if cached).  
  Outputs: detected tech, confidence.  
  Deps: Wappalyzer patterns or own signatures.  

- Reverse WHOIS / domain owner clustering  
  Purpose: Find domains registered by same registrant/email.  
  Inputs: email, registrant name.  
  Options: timeframe, include variations.  
  Outputs: domain cluster, registration dates.  
  Deps: Domain DB APIs (SecurityTrails, WhoisXML).  

- Search & discovery engines

- Google dork / search engine harness  
  Purpose: Run targeted dorks across search engines and aggregate results.  
  Inputs: query/dork, engine.  
  Options: pagination, safe-search toggle, site:, filetype:.  
  Outputs: result URLs, snippets, cache links.  
  Deps: serpapi or scraping with rate limiting.  

- Shodan/Censys/ZoomEye integration  
  Purpose: Query internet-scanning engines for exposed services, cameras, IoT.  
  Inputs: query, IP, domain.  
  Options: include vulnerability tags, pagination.  
  Outputs: matched hosts with banners and ports.  
  Deps: Shodan/Censys APIs.  

- Paste & leak scanner  
  Purpose: Search pastebins and leaks for target mentions or data.  
  Inputs: domain, email, keyword.  
  Options: timeframe, show snippet.  
  Outputs: paste entries, leak metadata.  
  Deps: Paste APIs, HaveIBeenPwned, GitHub (for accidental commits).  

- Geolocation & mapping

- Geolocation from metadata & IPs  
  Purpose: Map IPs/images/metadata to coordinates.  
  Inputs: IPs, image EXIF, text with location hints.  
  Options: confidence threshold, map output.  
  Outputs: lat/long + source.  
  Deps: MaxMind, exif extraction libraries.  

- OSINT mapping / graph builder (visual)  
  Purpose: Build link graphs between domains, people, IPs for visualization.  
  Inputs: aggregated dataset.  
  Options: graph depth, include confidence weights.  
  Outputs: Graph file (GraphML, JSON), interactive HTML (pyvis).  
  Deps: networkx, pyvis.  

- Content & language analysis

- Language detection & translation  
  Purpose: Detect language of text and optionally translate.  
  Inputs: text.  
  Options: target language.  
  Outputs: language code, translated text.  
  Deps: langdetect, translation APIs.  

- NLP entity extraction (names, orgs, locations)  
  Purpose: Extract named entities from text (NER).  
  Inputs: text, files (PDF/HTML).  
  Options: model (spaCy/en_core_web_sm).  
  Outputs: entities with types and confidence.  
  Deps: spaCy, transformers (optional).  

- Sentiment & trend analysis  
  Purpose: Sentiment scores on posts, trending keywords over time.  
  Inputs: collection of posts or texts.  
  Options: window size, granularity.  
  Outputs: sentiment aggregation, trending list.  
  Deps: transformers or lighter sentiment libs.  

- Document & artifact processing

- PDF/Document extractor & metadata reader  
  Purpose: Extract text, metadata, embedded links, author.  
  Inputs: PDF/DOCX path or URL.  
  Options: OCR for scanned PDFs.  
  Outputs: text, metadata, found emails/URLs.  
  Deps: pdfminer.six, pytesseract for OCR.  

- GitHub / code search scanner  
  Purpose: Find leaked secrets, credentials, or references in code.  
  Inputs: org/user/repo, keyword.  
  Options: search in commits, Gist, historical.  
  Outputs: matches with file/line/context.  
  Deps: GitHub API, pygit2.  

- Automation & enrichment

- API aggregator / enrichment module  
  Purpose: Given an entity (domain/email/IP), call multiple enrichment APIs and merge results.  
  Inputs: entity.  
  Options: selected sources, concurrency.  
  Outputs: unified JSON profile.  
  Deps: many APIs — design with adapter pattern.  

- Scheduled scanning / cron-like tasks  
  Purpose: Periodically run selected modules and record diffs/changes.  
  Inputs: schedule config, modules list.  
  Options: alerting (email/webhook), diff thresholds.  
  Outputs: time-series results, alerts.  
  Deps: APScheduler, DB.  

- Utility & hygiene

- Results exporter (JSON/CSV/HTML)  
  Purpose: Export collected data in standard formats and templates.  
  Inputs: query/filter, format.  
  Options: include attachments, zip.  
  Outputs: files for download.  
  Deps: builtin JSON/CSV, Jinja2 for HTML reports.  

- API key manager (secure)  
  Purpose: Store/validate API keys used by other modules (encrypted).  
  Inputs: service, key.  
  Options: keyring or file-based AES.  
  Outputs: key status, TTL.  
  Deps: keyring, cryptography.  

- Rate-limit & proxy manager  
  Purpose: Throttle modules, rotate proxies to avoid IP bans.  
  Inputs: rate config, proxy list.  
  Options: per-module limits, global.  
  Outputs: effective request logs.  
  Deps: proxy providers, requests sessions.  

- Nice-to-have / advanced

- OCR & handwriting transcription  
  Purpose: Extract text from images/photos (e.g., screenshots, documents).  
  Inputs: image or PDF.  
  Options: language, image preprocess.  
  Outputs: extracted text.  
  Deps: pytesseract, OpenCV.  

- Timeline builder  
  Purpose: Build chronological timeline of events for an entity.  
  Inputs: aggregated events (from posts, WHOIS, certs).  
  Options: granularity.  
  Outputs: interactive timeline HTML/JSON.  
  Deps: plotly, matplotlib.  

- False-positive matcher / deduper  
  Purpose: Deduplicate results and score likely false positives.  
  Inputs: result set.  
  Options: similarity threshold, manual whitelist.  
  Outputs: deduped dataset, clusters.  

- Legal & ethical module

- Compliance / legality checker  
  Purpose: Flag actions that may violate TOS, local law, or privacy concerns (e.g., active exploitation, scraping sensitive data).  
  Inputs: planned actions, region.  
  Outputs: warnings, recommended mitigations.  


```


## Python OSINT Library list
```

* Threat Intelligence / Malware & File Analysis Libraries

  * virustotal-python – Query VirusTotal for files, hashes, URLs, domains, IPs.
  * python-magic – Detect file types (useful in enrichment).
  * pefile – Parse PE files for static analysis.

* Threat Intelligence / Malware & File Analysis APIs

  * VirusTotal API – file, URL, domain, IP reputation, pivoting.
  * Hybrid Analysis – malware analysis reports and file intelligence.
  * MalShare / MalwareBazaar – downloadable malware samples and metadata.
  * Abuse.ch Feeds – malware domains, ransomware, and botnet trackers.
  * Any.Run API – sandbox analysis (if needed, mainly OSINT: network connections, URLs).

* Network / IP / Domain Recon Libraries

  * dnspython – DNS queries, reverse lookups, zone transfers.
  * python-whois – Fetch WHOIS info for domains.
  * ipwhois – ASN and IP ownership info.

* Network / IP / Domain Recon APIs

  * PassiveTotal / RiskIQ – passive DNS, domain history, subdomains.
  * SecurityTrails – DNS history, WHOIS, domain/IP relationships.
  * Shodan – internet-connected hosts, banners, open ports.
  * Censys – host and certificate scans, IP metadata.
  * Farsight DNSDB – passive DNS historical data.

* URL & Phishing Intelligence Libraries

  * urlscan – Query URLScan.io programmatically.
  * googlesearch-python – Search Google programmatically.

* URL & Phishing Intelligence APIs

  * URLScan.io API – URL scanning, domain connections, screenshots.
  * PhishTank – phishing URL reports.
  * Google Safe Browsing – URL threat classification.
  * APIVoid – URL, domain, IP, and email reputation services.

* Social Media / OSINT Profiling Libraries

  * Tweepy – Twitter/X API access.
  * praw – Reddit API access.
  * instaloader – Download public Instagram profiles/posts.
  * linkedin-api – Access LinkedIn public data (non-official).

* Social Media / OSINT Profiling APIs

  * Twitter / X API – profile data, tweets, mentions.
  * Facebook Graph API – public pages, posts, connections (limited).
  * LinkedIn API / Scraping (public) – company/employee info.
  * Reddit API – posts, comments, subreddits.
  * Instagram Graph API – public profiles/posts.

* Certificates / SSL / Infrastructure APIs

  * Censys API – certificates, SSL/TLS details.
  * crt.sh API – certificate transparency search.
  * CertSpotter / Facebook Certificate Transparency – track domains via certificates.

* OSINT Search Engines & Aggregators APIs

  * Google Custom Search / Programmable Search – web footprinting.
  * Bing Search API / Microsoft Cognitive Services – web search and entity extraction.
  * IntelTechniques OSINT Tools – people, domain, and email recon.
  * Spyse – domain/IP/host enumeration and metadata.

* Social Engineering / Email OSINT Libraries

  * haveibeenpwned – Check email breaches.
  * emailrep – Email reputation and threat scoring.
  * dehashed-python – Search email/username breaches.

* Social Engineering / Email OSINT APIs

  * HaveIBeenPwned API – breached email accounts.
  * Hunter.io – email format discovery, domain email patterns.
  * EmailRep.io – email reputation and threat scoring.
  * Dehashed – breached emails, usernames, passwords.

* Geolocation & Mapping Libraries

  * geopy – Geocoding addresses and coordinates.
  * folium – Map visualization for IPs/domains.
  * maxminddb – IP geolocation database access.

* Geolocation & Mapping APIs

  * Google Maps / Places API – geolocation, addresses, POIs.
  * OpenStreetMap / Nominatim – geocoding and location OSINT.
  * MaxMind GeoIP / IP2Location – IP geolocation.

* Other Enrichment / Graph / Relationships Libraries

  * networkx – Build and analyze graphs of relationships (files, domains, IPs).
  * pyvis – Visualize network graphs interactively in browser.
  * igraph – Advanced graph analysis for OSINT clusters.

* Other Enrichment / Graph / Relationships APIs

  * MISP – threat intelligence sharing, indicator enrichment.
  * OpenCTI – threat actor, malware, and campaign relationships.
  * SpiderFoot HX API – automated OSINT for domains, IPs, emails, names.
  * CIRCL Passive DNS – historical DNS infrastructure.


```

## APIs for OSINT

```

* Threat Intelligence / Malware & File Analysis

  * VirusTotal API – file, URL, domain, IP reputation, pivoting.
  * Hybrid Analysis – malware analysis reports and file intelligence.
  * MalShare / MalwareBazaar – downloadable malware samples and metadata.
  * Abuse.ch Feeds – malware domains, ransomware, and botnet trackers.
  * Any.Run API – sandbox analysis (if needed, but mainly OSINT: network connections, URLs).

* Domain & DNS Intelligence

  * PassiveTotal / RiskIQ – passive DNS, domain history, subdomains.
  * SecurityTrails – DNS history, WHOIS, domain/IP relationships.
  * WhoisXML API – WHOIS, domain owner, registrar info.
  * Shodan – internet-connected hosts, banners, open ports.
  * Censys – host and certificate scans, IP metadata.
  * Farsight DNSDB – passive DNS historical data.

* IP / Network Intelligence

  * IPinfo.io – ASN, geolocation, hosting provider.
  * AbuseIPDB – IP reputation, reports, malicious activity.
  * GreyNoise – background internet noise, scanning infrastructure.
  * Shodan / Censys – network scanning data, host vulnerabilities.

* URL & Phishing Intelligence

  * URLScan.io API – URL scanning, domain connections, screenshots.
  * PhishTank – phishing URL reports.
  * Google Safe Browsing – URL threat classification.
  * APIVoid – URL, domain, IP, and email reputation services.

* Social Media / OSINT Profiling

  * Twitter / X API – profile data, tweets, mentions.
  * Facebook Graph API – public pages, posts, connections (limited).
  * LinkedIn API / Scraping (public) – company/employee info.
  * Reddit API – posts, comments, subreddits.
  * Instagram Graph API – public profiles/posts.

* Certificates / SSL / Infrastructure

  * Censys API – certificates, SSL/TLS details.
  * crt.sh API – certificate transparency search.
  * CertSpotter / Facebook Certificate Transparency – track domains via certificates.

* OSINT Search Engines & Aggregators

  * Google Custom Search / Programmable Search – web footprinting.
  * Bing Search API / Microsoft Cognitive Services – web search and entity extraction.
  * IntelTechniques OSINT Tools – people, domain, and email recon.
  * Spyse – domain/IP/host enumeration and metadata.

* Social Engineering / Email OSINT

  * HaveIBeenPwned API – breached email accounts.
  * Hunter.io – email format discovery, domain email patterns.
  * EmailRep.io – email reputation and threat scoring.
  * Dehashed – breached emails, usernames, passwords.

* Geolocation & Mapping

  * Google Maps / Places API – geolocation, addresses, POIs.
  * OpenStreetMap / Nominatim – geocoding and location OSINT.
  * MaxMind GeoIP / IP2Location – IP geolocation.

* Other Enrichment / Graph / Relationships

  * MISP – threat intelligence sharing, indicator enrichment.
  * OpenCTI – threat actor, malware, and campaign relationships.
  * SpiderFoot HX API – automated OSINT for domains, IPs, emails, names.
  * CIRCL Passive DNS – historical DNS infrastructure.



```