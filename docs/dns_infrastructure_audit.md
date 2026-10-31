# DNS & Infrastructure Cutover Audit
**Target Domain:** `haworthindustrialtechnologies.com`  
**Registrar:** Squarespace  
**Authoritative DNS Provider:** Cloudflare (`jake.ns.cloudflare.com`, `surina.ns.cloudflare.com`)  
**Audit Date:** October 30, 2026  
**Auditor:** PAM (AutomationOS)

---

## 1. Current DNS State & Active Records

### A. Authoritative Nameservers
* `jake.ns.cloudflare.com`
* `surina.ns.cloudflare.com`
*(Domain is already managed under the user's Cloudflare account)*

### B. Mail Delivery Records (Google Workspace Gmail) — CRITICAL TO PRESERVE
* **MX Records:**
  * Priority 1: `aspmx.l.google.com`
  * Priority 5: `alt1.aspmx.l.google.com`
  * Priority 5: `alt2.aspmx.l.google.com`
  * Priority 10: `alt3.aspmx.l.google.com`
  * Priority 10: `alt4.aspmx.l.google.com`
* **SPF TXT Record:**
  * `"v=spf1 include:_spf.google.com ~all"`

---

## 2. Cloudflare Pages Deployment Path
Because Cloudflare already controls DNS resolution for `haworthindustrialtechnologies.com`:
1. We do **not** need to wait for 24-48 hour global nameserver propagation.
2. When the new static site build is deployed to Cloudflare Pages:
   * Cloudflare Pages will create a project-specific endpoint (e.g. `haworth-industrial.pages.dev`).
   * We bind custom domains `haworthindustrialtechnologies.com` and `www.haworthindustrialtechnologies.com`.
   * Cloudflare automatically creates proxied CNAME records at the apex and `www` subdomains.
3. The existing Google Workspace MX and SPF records will remain untouched in the DNS zone, ensuring **zero email downtime**.
4. Full HTTPS/TLS encryption with automatic HTTP -> HTTPS redirects will be active immediately.
