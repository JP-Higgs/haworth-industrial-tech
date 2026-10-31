# Site Architecture & UI/UX Design Specification
**Client:** Haworth Industrial Technologies  
**Project:** Modern Website & Cloudflare Pages Replatforming  
**Author:** PAM (AutomationOS)  
**Date:** October 30, 2026

---

## 1. Visual Identity & Design System
* **Color Hierarchy:**
  * **Backgrounds:** Deep Midnight Industrial (`#0b132b`), Card Dark Slate (`#111936`), Subsurface Glass (`rgba(255, 255, 255, 0.04)`)
  * **Accents:** Precision Engineering Cyan (`#00f0ff` / `#00b4d8`), Performance Electric Blue (`#3a86ff`)
  * **Text:** Technical White (`#f8fafc`), Slate Gray Secondary (`#94a3b8`), Muted Borders (`#1e293b`)
* **Typography:** Clean, authoritative modern technical sans-serif with monospace accents for engineering specifications.
* **Layout Structure:** Modular, responsive grid with subtle blueprint / isometric grid styling and crisp border radii.

---

## 2. Information Architecture & Key Sections

1. **Header & Navigation:**
   * Logo & Wordmark (Haworth Industrial Technologies)
   * Nav Links: Services, Capabilities, Portfolio, Testimonial, About
   * CTA Button: "Request a CAD Quote" (direct jump to form)

2. **Hero Section:**
   * Headline: "Precision CAD Engineering & Mechanical Design."
   * Subheadline: "Transforming complex concepts into production-ready SolidWorks models, functional prototypes, and cost-effective manufacturing systems. Headquartered in Southern California."
   * CTAs: "Submit CAD for Quote" & "Explore Case Studies"
   * Trust Badges: 15+ Years Industry Experience | SolidWorks Certified | Rapid Prototype Ready | Flexible Contracting

3. **Core Engineering Services (Interactive Grid):**
   * **Mechanical CAD Design:** Part & assembly modeling, GD&T drawings, reverse engineering, tooling design.
   * **Industrial Engineering & DFM:** Design for Manufacturability, assembly line optimization, bill of materials (BOM).
   * **Rapid Prototyping:** 3D printing (FDM/SLA/SLS), functional fit testing, validation.
   * **Vendor Sourcing & Procurement:** Local Southern California network & vetted global fabrication partners.

4. **Featured Portfolio & Case Studies:**
   * Southland Sensing Ltd. (Analytical sensors)
   * Hyon USA (CUETÉ 303 Stainless Steel RDA)
   * 500 Stones (Jeep Wrangler Bare Back Rack)
   * Trinity Racing / Streamline Brakes (Off-road vehicle mounts & clamps)
   * Industrial Chemical Processing Equipment
   * Coolit Baskit (Consumer product prototyping to mass manufacturing)

5. **Client Testimonial:**
   * Featured quote from Ben Barker, President of Southland Sensing Ltd.

6. **Interactive Quote & RFQ Module:**
   * Name, Company, Email, Phone, Project Type dropdown
   * Project timeline & description
   * CAD file attachment support (`.sldprt`, `.step`, `.iges`, `.x_t`, `.dwg`, `.pdf`)
   * Submits directly to Chris's designated Gmail inbox.

7. **Footer & Technical Metadata:**
   * Full contact details, location, privacy policy, copyright.
   * Embedded JSON-LD schema for Generative Engine Optimization (GEO).

---

## 3. Generative Engine Optimization (GEO) & SEO Strategy
* Embedded `schema.org/ProfessionalService` and `schema.org/EngineeringOrganization`.
* Specific entity tagging for AI search bots:
  * Entities: "SolidWorks Mechanical Design", "CAD Contractor Southern California", "Industrial Engineering Consultant", "Design for Manufacturability".
  * Direct question-and-answer FAQ structured data for LLM citation ingestion.
