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
- **Official Domain**: Canonicalized to `https://www.akruradindigul.in/`.
- **Permanent 301 Redirect**: Fully configured to permanently redirect `https://www.akruradindigul.in/index.html` to `https://www.akruradindigul.in/` across all platforms (Apache, Nginx, Netlify, Cloudflare Pages, Vercel, and client-side fallback).

---

## 📁 Production Directory Structure

```text
akura/
├── index.html                     # Home page (with client-side fallback redirect)
├── about.html                     # About Us page
├── services.html                  # Treatments & Services page
├── facilities.html                # Vadipatti Campus page
├── contact.html                   # Contact & Admissions page
├── styles.css                     # Production CSS stylesheet
├── .htaccess                      # Apache / LiteSpeed server rules (301 redirect, HTTPS, non-www -> www)
├── _redirects                     # Netlify & Cloudflare Pages 301 permanent redirect rules
├── netlify.toml                   # Netlify configuration file
├── vercel.json                    # Vercel permanent redirect configuration
├── logo.png                       # Official transparent logo (navbar)
├── logo-white.png                 # Official white logo (footer)
├── favicon.png                    # Brand favicon (32x32)
├── apple-touch-icon.png           # iOS home screen icon (180x180)
├── favicon-192.png                # Android PWA icon (192x192)
├── favicon-512.png                # High-res PWA icon (512x512)
├── site.webmanifest               # Web application manifest
├── robots.txt                     # Search engine crawler instructions
├── sitemap.xml                    # Production XML sitemap (canonical URLs)
├── clinic-*.jpg                   # 14 authentic clinic & facility photos
└── README.md                      # Project documentation
```

---

## 🔄 Permanent 301 Redirect Configuration (`/index.html` → `/`)

The official domain is `https://www.akruradindigul.in/`. To prevent duplicate content penalties, consolidate Google ranking signals, and ensure clean URLs, all traffic to `/index.html` is permanently 301 redirected to `/`.

### 1. Apache / LiteSpeed / cPanel / Hostinger (`.htaccess`)
Pre-configured in [`.htaccess`](.htaccess) using `%{THE_REQUEST}` to prevent infinite directory index loops:
```apache
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteBase /

  # 301 Permanent Redirect: /index.html -> /
  RewriteCond %{THE_REQUEST} ^[A-Z]{3,9}\ /index\.html[?\s] [NC]
  RewriteRule ^index\.html$ https://www.akruradindigul.in/ [R=301,L]

  # non-www to www redirect
  RewriteCond %{HTTP_HOST} ^akruradindigul\.in$ [NC]
  RewriteRule ^(.*)$ https://www.akruradindigul.in/$1 [R=301,L]

  # Force HTTPS
  RewriteCond %{HTTPS} off
  RewriteCond %{HTTP:X-Forwarded-Proto} !https
  RewriteRule ^(.*)$ https://www.akruradindigul.in/$1 [R=301,L]
</IfModule>
```

### 2. Nginx Configuration
If hosting on Nginx (Ubuntu/Debian VPS or AWS EC2), add the following inside your `server { ... }` block:
```nginx
server {
    server_name akruradindigul.in;
    return 301 https://www.akruradindigul.in$request_uri;
}

server {
    server_name www.akruradindigul.in;

    # 301 Permanent Redirect for index.html
    if ($request_uri ~ ^/index\.html($|\?)) {
        return 301 https://www.akruradindigul.in/;
    }

    root /var/www/akura;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### 3. Netlify & Cloudflare Pages (`_redirects` & `netlify.toml`)
Pre-configured in [`_redirects`](_redirects) and [`netlify.toml`](netlify.toml):
```text
/index.html    /    301!
https://akruradindigul.in/*    https://www.akruradindigul.in/:splat    301!
```

### 4. Vercel (`vercel.json`)
Pre-configured in [`vercel.json`](vercel.json):
```json
{
  "redirects": [
    {
      "source": "/index.html",
      "destination": "/",
      "permanent": true
    }
  ]
}
```

### 5. Client-Side Fallback (`index.html`)
For environments where server-level rewrite rules cannot be set, a zero-latency script in `<head>` ensures immediate browser URL correction:
```html
<script>
  if (window.location.pathname.endsWith('/index.html')) {
    var cleanPath = window.location.pathname.replace(/\/index\.html$/, '/') || '/';
    window.location.replace(window.location.origin + cleanPath + window.location.search + window.location.hash);
  }
</script>
```

---

## 🌐 Deploying to Production ("Going Live")

### Hostinger / cPanel / Apache / LiteSpeed
1. Upload all files from this directory directly to your `public_html` root folder via FTP or File Manager.
2. Confirm `.htaccess` (hidden dot file) is uploaded to the root.
3. Test visiting `https://www.akruradindigul.in/index.html` — it will immediately 301 redirect to `https://www.akruradindigul.in/`.

### Netlify / Vercel
- Drag and drop this folder directly into the Netlify dashboard, or connect the GitHub repository.
- Build command: *None* (Static HTML), Publish directory: `.`
- All redirect rules in `_redirects` / `vercel.json` are applied automatically.

### GitHub Pages
1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Branch**, select `main` and root `/`, then click **Save**.
4. Set custom domain to `www.akruradindigul.in` and enforce HTTPS.
