# AKRURA DE ADDICTION & REHABILITATION CENTRE

Official responsive, modern, production-ready website for **Akrura De Addiction & Rehabilitation Centre** (Vadipatti, Madurai, Tamil Nadu).

---

## 🌟 About The Centre

> **Akrura De Addiction & Rehabilitation Centre** is a trusted sanctuary for Alcohol, Drug De-addiction and Psychiatric Care. Located at Vadipatti, Madurai, we serve patients from all over Tamil Nadu including Chennai, Erode, Salem, Tiruppur, Coimbatore, Madurai, and Dindigul. Our treatment includes 24/7 Medical Support, Counseling, Yoga, Meditation, and Mind Refreshment activities. We help every person to recover with dignity and rejoin their family.

- **24/7 Emergency & Admission Helpline:** [+91 93841 90971](tel:9384190971) / [WhatsApp](https://wa.me/919384190971)
- **Facility Address:** 5/96/13, Street-3, Mettuperumal Nagar, Vadipatti, Madurai - 625218, Tamil Nadu (Near Madurai - Dindigul Main Road)
- **Instagram:** [@akrura_de_addiction](https://www.instagram.com/akrura_de_addiction)
- **Facebook:** [Akrura De Addiction Centre](https://www.facebook.com/share/1KWuSgFxir/)

---

## 🚀 Pages & Structure

1. **[index.html](index.html)**: Comprehensive Home page featuring emergency hero, clinical focus switcher, 8 clinical treatments, authentic sanctuary campus preview, patient stories, and interactive consultation form.
2. **[about.html](about.html)**: Dedicated About Us page detailing clinical philosophy, medical team leadership, recovery methodology, and family reunification mission.
3. **[services.html](services.html)**: Complete Treatments page covering Alcohol De-Addiction, Drug Rehabilitation, 24/7 Medical Detox, Psychiatric Care, Individual CBT, Family Therapy, Yoga/Brain Gym, and Relapse Prevention Aftercare.
4. **[facilities.html](facilities.html)**: Vadipatti Campus & Sanctuary tour showcasing inpatient residential suites, 24/7 nursing clinic, meditation hall, dining facilities, and quiet recovery grounds.
5. **[contact.html](contact.html)**: Contact & 24/7 Admissions page with driving directions, Google Maps location, emergency ambulance escort details, and admission intake form.

---

## 🎨 Design & Technical Highlights

- **Clean Minimal UI**: Zero box shadows (`box-shadow: none !important`), crisp hairline borders, and pure clinical aesthetics.
- **Official Brand Logo**: High-resolution official head profile emblem & typography (`logo.png` for light navbar, `logo-white.png` for dark navy footer).
- **Shopify Polaris SVG Icons**: Lightweight, ultra-crisp vector icons throughout all cards and buttons.
- **Authentic Clinic Imagery**: 14 high-resolution, web-optimized photographs depicting the actual Vadipatti clinic campus, doctors, patient counseling, and medical consultations.
- **100% Mobile Optimized**: Touch-friendly floating WhatsApp & call buttons, responsive mobile navigation drawer, fluid typography, and zero horizontal overflow.
- **SEO & PWA Ready**: JSON-LD Structured Data (`MedicalOrganization`), OpenGraph / Twitter Cards, XML Sitemap (`sitemap.xml`), `robots.txt`, and Web App Manifest (`site.webmanifest`).

---

## 📁 Production Directory Structure

```text
akura/
├── index.html                     # Home page
├── about.html                     # About Us page
├── services.html                  # Treatments & Services page
├── facilities.html                # Vadipatti Campus page
├── contact.html                   # Contact & Admissions page
├── styles.css                     # Production CSS stylesheet
├── logo.png                       # Official transparent logo (navbar)
├── logo-white.png                 # Official white logo (footer)
├── favicon.png                    # Brand favicon (32x32)
├── apple-touch-icon.png           # iOS home screen icon (180x180)
├── favicon-192.png                # Android PWA icon (192x192)
├── favicon-512.png                # High-res PWA icon (512x512)
├── site.webmanifest               # Web application manifest
├── robots.txt                     # Search engine crawler instructions
├── sitemap.xml                    # Production XML sitemap
├── clinic-*.jpg                   # 14 authentic clinic & facility photos
└── README.md                      # Project documentation
```

---

## 🌐 Deploying to Production ("Going Live")

### GitHub Pages (Instant Free Hosting)
1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Branch**, select `main` and root `/`, then click **Save**.
4. The website will be live in 60 seconds at `https://<username>.github.io/<repo-name>/`.

### Netlify / Vercel
- Drag and drop this folder directly into the Netlify dashboard, or connect the GitHub repository. Build command: None (Static HTML), Publish directory: `.`

### cPanel / Apache / Nginx / Hostinger
- Upload all files from this directory to `public_html` via FTP or File Manager.
- Ensure `robots.txt`, `sitemap.xml`, and `site.webmanifest` are in the document root.
