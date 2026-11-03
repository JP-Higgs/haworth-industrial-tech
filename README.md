# Haworth Industrial Technologies

Official static website repository for **Haworth Industrial Technologies** (`haworthindustrialtechnologies.com`).

Expert SolidWorks CAD design, mechanical prototyping, and industrial engineering consulting based in Southern California.

## Project Structure

```
├── public/                 # Production static site assets
│   ├── assets/             # Images, portfolio assets, favicons
│   ├── _headers            # Cloudflare Pages security & caching headers
│   ├── _redirects          # Cloudflare Pages redirection rules
│   ├── index.html          # Main landing page
│   ├── robots.txt          # Search engine crawler instructions
│   └── sitemap.xml         # XML sitemap
├── docs/                   # Architecture, DNS audit, and design specs
├── build.js                # Zero-dependency build script
├── package.json            # Project manifest & build scripts
└── README.md
```

## Local Development & Build

1. **Build the site for production:**
   ```bash
   npm run build
   ```
   This generates the deployment bundle in `dist/`.

2. **Preview locally:**
   ```bash
   npx serve dist
   ```

## Deployment

Automated via **Cloudflare Pages**:
- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Domain:** `haworthindustrialtechnologies.com` / `www.haworthindustrialtechnologies.com`
