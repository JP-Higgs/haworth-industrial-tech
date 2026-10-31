# Legacy Site Content & Asset Audit
**Source:** `http://www.haworthindustrialtechnologies.com`  
**Host Platform:** Weebly  
**Audit Date:** October 30, 2026  
**Auditor:** PAM (AutomationOS)

---

## 1. Executive Summary & Value Proposition
* **Brand Name:** Haworth Industrial Technologies (HIT)
* **Tagline:** Industrial Design and Manufacture
* **Headquarters:** Southern California
* **Target Industries:** Medical Device, Automotive, Heavy Equipment, Oil and Gas, Consumer Products, Agriculture, Chemical Processing.
* **Core Value Statement:**
  > "Haworth Industrial Technologies is a Design and Manufacturing team headquartered in Southern California. Our clients include Medical Device, Automotive, Heavy Equipment, Oil and Gas, Consumer Products, Agriculture, and Chemical Processing companies. We employ Design, Industrial, Quality, and Facilities Engineers with extensive experience in optimizing design and manufacturing processes. We offer a flexible contracting model that fits into our client’s unique needs for short and long-term resource planning."

---

## 2. Core Service Offerings

### A. Mechanical Design
* Full mechanical design for new products, tooling, and assemblies.
* CAD modeling using the latest design software (SolidWorks).
* Production of detailed 3D part and assembly models, manufacturing drawings, and prototype specs.

### B. Industrial Engineering
* **Process and Productivity Improvement**
* **Planning and Logistics Strategy Development**
* **Supplier Management & Sourcing Development:** Local Southern California network and global fabrication sourcing.

### C. Rapid Prototyping & Production Sourcing
* 3D printed prototype development for fit, form, and function testing.
* Design for Manufacturability (DFM) verification.
* Sourcing local machining, sheet metal fabrication, and overseas manufacturing partners.

---

## 3. Case Studies & Client Portfolio

1. **Southland Sensing Ltd. (Analytical Instrumentation)**
   * **Website:** http://www.sso2.com/
   * **Scope:** Custom sensor packaging, sampling systems, mechanical design consulting.
   * **Testimonial:**
     > *“Haworth Industrial Technologies has provided our company their highly professional CAD design consulting services for many years. Their service is not only cost effective, but it is provided with flexible scheduling and a high degree of accessibility. Haworth Industrial Technologies has proven to dramatically reduce the mechanical design process due to the high level of expertise and efficiency that they bring to the table.”*  
     > — **Ben Barker, President, Southland Sensing Ltd.**

2. **Hyon USA (CUETÉ RDA System)**
   * **Scope:** Rebuildable Drip Atomizer engineered from 303 Stainless Steel (25mm diameter), two-post arrangement, 3D printed prototypes, and mass production recommendations.

3. **500 Stones (Bare Back Rack for Jeep Wrangler)**
   * **Scope:** 2007–2017 Jeep Wrangler cargo rack consisting of 58” steel crossbars. 8-part assembly with 3-minute install. Handled design validation, prototype development, and local fabrication vendor sourcing.

4. **Streamline Brakes / Trinity Racing (Off-Road Racing Vehicle Equipment)**
   * **Scope:** Antenna mounts, radio clamps, vehicle brackets distributed with PCI Radios and SDR Motorsports.

5. **CBD / Chemical Processing Equipment**
   * **Scope:** Engineering equipment for harvesting and chemical processing extraction.

6. **Coolit Baskit (Consumer Product)**
   * **Scope:** Converted rough sketches into 3D SolidWorks model, 3D printed functional prototypes, finished production drawings, and affordable manufacturing sourcing.

---

## 4. Brand Assets & Media Catalog
All legacy media assets have been extracted and archived locally in `/home/jp/clients/Haworth Industrial Technologies/assets/legacy/`:
* **Logo:** `1475433710.png` (Haworth Industrial Technologies wordmark / logo)
* **Stock & Hero Images:**
  * `adobestock-9985252_orig.jpeg` (Industrial engineering / machining)
  * `adobestock-39308475_orig.jpeg` (CAD blueprint / drafting)
  * `adobestock-4472107-1_orig.jpeg` (Manufacturing / metal fabrication)
  * `science-in-hd-kph2ikrhpfa-unsplash_orig.jpg` (Technical precision background)

---

## 5. URL Structure & 301 Redirect Mapping

| Legacy Weebly URL | New Modern URL | Redirect Type | Target Content |
| :--- | :--- | :---: | :--- |
| `/` or `/index.html` | `/` | 200 | Modern Hero, Value Prop, Highlights, Lead Form |
| `/services.html` (and `/services1.html`) | `/services` | 301 Permanent | Detailed Mechanical Design & Industrial Engineering |
| `/project-gallery.html` (and `project-gallery1.html`) | `/case-studies` | 301 Permanent | Interactive Portfolio & Case Studies |
| `/request-a-quote.html` | `/quote` | 301 Permanent | CAD File Upload Form (20MB+), Scope Selector |
| `/contact.html` (and `/contact1.html`) | `/contact` | 301 Permanent | Contact Information, Direct Call, Gmail Routing |

---

## 6. Gaps & Modernization Opportunities for the Rebuild
1. **Mobile Optimization & Modern UI:** Legacy site was built on an outdated Weebly template with generic typography and no modern interactive components.
2. **Generative Engine Optimization (GEO):** Currently zero schema markup (`schema.org/EngineeringService`). Adding JSON-LD will immediately allow ChatGPT Search, Perplexity, and Google SGE to recommend Haworth for SolidWorks CAD and engineering consulting.
3. **Speed & Security:** The legacy Weebly site is HTTP-first without strict TLS/HSTS. Moving to Cloudflare Pages guarantees sub-second edge loading, free SSL, and DDoS protection.
4. **Secure CAD Uploads:** The new quote form should allow clean, secure drag-and-drop CAD file uploads (`.sldprt`, `.sldasm`, `.step`, `.iges`) that notify Chris via his connected Google Workspace Gmail.
