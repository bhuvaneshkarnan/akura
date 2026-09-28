import os

def generate_akrura_html():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=2"/>
  <title>Akrura De Addiction &amp; Rehabilitation Centre | Alcohol, Drug &amp; Psychiatric Care | Vadipatti, Madurai</title>
  
  <meta name="description" content="AKRURA DE ADDICTION &amp; REHABILITATION CENTRE is a trusted centre for Alcohol, Drug De-addiction and Psychiatric Care in Vadipatti, Madurai. 24/7 medical support, counseling, yoga, meditation, serving patients from All Over Tamil Nadu. Call 93841 90971."/>
  <meta property="og:title" content="AKRURA DE ADDICTION &amp; REHABILITATION CENTRE | Vadipatti, Madurai"/>
  <meta property="og:description" content="Trusted Centre for Alcohol, Drug De-Addiction and Psychiatric Care. 24/7 Care available across All Over Tamil Nadu. Call 93841 90971."/>
  <meta property="og:type" content="website"/>
  <meta property="og:url" content="https://www.instagram.com/akrura_de_addiction"/>
  <meta name="theme-color" content="#013126"/>

  <link rel="shortcut icon" href="favicon.png" type="image/x-icon"/>
  <link rel="apple-touch-icon" href="favicon.png"/>

  <!-- Google Fonts: Montserrat & Playfair -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet"/>

  <!-- Core Design System CSS -->
  <link href="shared.min.css" rel="stylesheet" type="text/css"/>
  <link href="page.min.css" rel="stylesheet" type="text/css"/>
  <link href="swiper-bundle.min.css" rel="stylesheet" type="text/css"/>

  <!-- Core Vendor Libraries (Local) -->
  <script src="jquery.min.js"></script>
  <script src="gsap.min.js"></script>
  <script src="ScrollTrigger.min.js"></script>
  <script src="swiper-bundle.min.js"></script>
  <script src="rive.min.js"></script>

  <!-- SplitText Polyfill for word animations -->
  <script>
    if (typeof window.SplitText === 'undefined') {
      window.SplitText = function(target, options) {
        var elements = typeof target === 'string' ? document.querySelectorAll(target) : (target.length !== undefined && !target.nodeType ? target : [target]);
        var allWords = [];
        elements.forEach(function(el) {
          if (!el) return;
          function processNode(node) {
            if (node.nodeType === 3) {
              var text = node.textContent;
              if (!text.trim()) return node;
              var frag = document.createDocumentFragment();
              var parts = text.split(/(\\s+)/);
              parts.forEach(function(part) {
                if (part.trim().length > 0) {
                  var span = document.createElement('span');
                  span.className = 'word';
                  span.style.display = 'inline-block';
                  span.textContent = part;
                  allWords.push(span);
                  frag.appendChild(span);
                } else if (part) {
                  frag.appendChild(document.createTextNode(part));
                }
              });
              return frag;
            } else if (node.nodeType === 1) {
              var children = Array.from(node.childNodes);
              children.forEach(function(child) {
                var res = processNode(child);
                if (res !== child) {
                  node.replaceChild(res, child);
                }
              });
              return node;
            }
            return node;
          }
          processNode(el);
        });
        this.words = allWords;
      };
    }
  </script>

  <!-- JSON-LD Structured Data for Local Medical Business -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "MedicalClinic",
    "name": "AKRURA DE ADDICTION & REHABILITATION CENTRE",
    "alternateName": "Akrura Rehabilitation Centre Vadipatti",
    "description": "Akrura De Addiction & Rehabilitation Centre is a trusted centre for Alcohol, Drug De-addiction and Psychiatric Care in Vadipatti, Madurai, serving patients from All Over Tamil Nadu.",
    "telephone": "+919384190971",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "5/96/13, Street-3, Mettuperumal Nagar, Vadipatti",
      "addressLocality": "Madurai",
      "addressRegion": "Tamil Nadu",
      "postalCode": "625218",
      "addressCountry": "IN"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 10.0815,
      "longitude": 77.9622
    },
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
      ],
      "opens": "00:00",
      "closes": "23:59"
    },
    "sameAs": [
      "https://www.instagram.com/akrura_de_addiction",
      "https://www.facebook.com/share/1KWuSgFxir/"
    ]
  }
  </script>

  <style>
    :root {
      --akrura-emerald: #00856F;
      --akrura-deep-green: #013126;
      --akrura-teal: #039775;
      --akrura-light-teal: #2EDAF1;
      --akrura-gold: #FFC728;
      --akrura-purple: #B69EFF;
      --akrura-bg-cream: #F8F6F2;
    }
    body {
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      color: #263633;
      background-color: #013126;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }
    .serif-heading {
      font-family: 'Playfair Display', Georgia, serif;
    }
    /* Floating Action Buttons */
    .akrura-floating-cta {
      position: fixed;
      bottom: 24px;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.3);
      border-radius: 50px;
      padding: 12px 20px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      transition: all 0.3s ease;
    }
    .akrura-floating-wa {
      right: 24px;
      background: #25D366;
      color: #fff;
    }
    .akrura-floating-wa:hover {
      background: #1EBE5D;
      transform: translateY(-3px) scale(1.03);
      color: #fff;
    }
    .akrura-floating-call {
      left: 24px;
      background: #00856F;
      color: #fff;
    }
    .akrura-floating-call:hover {
      background: #039775;
      transform: translateY(-3px) scale(1.03);
      color: #fff;
    }
    @media (max-width: 600px) {
      .akrura-floating-cta span { display: none; }
      .akrura-floating-cta { padding: 14px; border-radius: 50%; }
      .akrura-floating-wa { right: 16px; bottom: 16px; }
      .akrura-floating-call { left: 16px; bottom: 16px; }
    }
    /* Logo styling */
    .akrura-brand-link {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }
    .akrura-logo-img {
      height: 48px;
      width: auto;
      max-width: 340px;
    }
    @media (max-width: 768px) {
      .akrura-logo-img { height: 38px; max-width: 250px; }
    }
    /* Smooth Anchor Scroll */
    html {
      scroll-behavior: smooth;
    }
    /* Top Banner */
    .web-banner-container {
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 600;
    }
    /* Treatment Card hover image */
    .n4-services_card_wrap {
      border-radius: 16px;
      overflow: hidden;
      position: relative;
    }
    /* Custom Facility Grid */
    .facility-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 40px;
    }
    .facility-card {
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .facility-card:hover {
      transform: translateY(-5px);
      border-color: #58EDA2;
    }
    .facility-card-img {
      width: 100%;
      height: 220px;
      object-fit: cover;
    }
    .facility-card-body {
      padding: 24px;
    }
    .facility-badge {
      display: inline-block;
      padding: 4px 10px;
      background: rgba(0, 133, 111, 0.2);
      color: #58EDA2;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
  </style>
</head>

<body data-body-n4="" class="n4-body">
  <div class="n4-page_wrap">

    <!-- Floating Quick Actions -->
    <a href="https://wa.me/919384190971?text=Hello%20Akrura%20De%20Addiction%20Centre,%20I%20would%20like%20to%20know%20more%20about%20your%20rehabilitation%20treatments." target="_blank" rel="noopener" class="akrura-floating-cta akrura-floating-wa" aria-label="WhatsApp Us">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.062-2.148-.544-1.859-.774-3.056-2.656-3.149-2.78-.093-.124-.755-.999-.755-1.906 0-.907.477-1.354.646-1.539.17-.185.372-.232.496-.232.124 0 .248.001.356.006.114.006.266-.043.416.319.155.372.529 1.298.575 1.391.046.093.078.202.016.326-.062.124-.093.202-.186.31-.093.109-.196.243-.28.326-.093.093-.19.195-.082.381.108.186.48 7.93 1.031 1.42.71.633 1.309.829 1.495.922.186.093.295.078.404-.047.108-.124.465-.543.59-.73.124-.186.248-.155.416-.093.17.062 1.077.508 1.263.601.186.093.31.139.356.217.047.077.047.45-.097.855zM12 2C6.477 2 2 6.477 2 12c0 1.891.524 3.66 1.434 5.176L2 22l4.954-1.397C8.423 21.49 10.158 22 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg>
      <span>WhatsApp 24/7</span>
    </a>
    <a href="tel:9384190971" class="akrura-floating-cta akrura-floating-call" aria-label="Call 24/7 Helpline">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      <span>Helpline: 93841 90971</span>
    </a>

    <!-- Top Announcement Banner -->
    <div class="web-banner-wrapper">
      <div class="div-block-62">
        <div class="web-banner" style="background-color: #ede9e3; border-bottom: 1px solid rgba(0,133,111,0.2);">
          <div class="web-banner-container">
            <div style="color:#013126; text-align:center;">
              <span>🚨 <strong>24/7 Confidential Helpline &amp; Emergency Admission:</strong> Call <a href="tel:9384190971" style="color:#00856F; font-weight:800; text-decoration:underline;">93841 90971</a> | AKRURA DE ADDICTION &amp; REHABILITATION CENTRE (Vadipatti, Madurai)</span>
            </div>
            <a href="#" class="web-banner-close w-inline-block" aria-label="Close notification" style="margin-left: 16px; cursor: pointer; text-decoration: none;">
              <div class="button-close" style="color: #013126; font-size: 1.3rem; font-weight: bold;">&times;</div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Navigation Bar -->
    <div role="banner" class="navbar nav-v2 w-nav" style="background-color: rgba(1, 49, 38, 0.96); backdrop-filter: blur(10px); position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid rgba(255,255,255,0.08);">
      <div class="content__nav">
        <div class="container__navigation" style="display: flex; align-items: center; justify-content: space-between; width: 100%; max-width: 1400px; margin: 0 auto; padding: 12px 24px;">
          
          <!-- Akrura Brand Logo -->
          <a href="#" class="akrura-brand-link" aria-label="Akrura De Addiction Centre Home">
            <img src="akrura-logo-white.svg" alt="AKRURA DE ADDICTION &amp; REHABILITATION CENTRE" class="akrura-logo-img"/>
          </a>

          <!-- Nav Menu -->
          <nav role="navigation" class="nav-menu-4 w-nav-menu" style="display: flex; align-items: center; gap: 8px;">
            
            <!-- Treatments Dropdown -->
            <div class="dropdown w-dropdown">
              <div class="nav__link-drop w-dropdown-toggle" tabindex="0" style="color: #ffffff; font-weight: 600; cursor: pointer;">
                <div class="nav-drop-arrow w-icon-dropdown-toggle"></div>
                <div class="text-block-32 cc-nav">Treatments &amp; Programs</div>
              </div>
              <nav class="nav-drop-list mb-12 w-dropdown-list" style="background: #013126; border: 1px solid rgba(88,237,162,0.3); border-radius: 12px; box-shadow: 0 15px 40px rgba(0,0,0,0.4); padding: 16px;">
                <div class="wrap__nav-drop-list mega-nav-v2">
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; min-width: 520px; padding: 10px;">
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #58EDA2; display: block;">1. Alcohol De-Addiction</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Medically supervised detox &amp; sobriety support</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #2EDAF1; display: block;">2. Drug De-Addiction</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Substance recovery &amp; behavioral restructuring</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #B69EFF; display: block;">3. Psychiatric Care &amp; Counseling</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Dual-diagnosis, depression &amp; clinical therapy</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #58EDA2; display: block;">4. Detoxification &amp; Medical Support</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">24/7 doctor supervision &amp; vital monitoring</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #2EDAF1; display: block;">5. Individual Counseling</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Root trauma, emotional healing &amp; coping skills</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #B69EFF; display: block;">6. Family Counseling</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Healing relationships &amp; family guidance</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #FFC728; display: block;">7. Yoga, Meditation &amp; Brain Gym</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Holistic mind refreshment &amp; physical wellness</span>
                    </a>
                    <a href="#services" class="nav__dropdown-item" style="color: #fff; text-decoration: none; padding: 8px 12px; border-radius: 8px; background: rgba(255,255,255,0.03); transition: background 0.2s;" onmouseover="this.style.background='rgba(88,237,162,0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                      <strong style="color: #58EDA2; display: block;">8. Aftercare &amp; Rehabilitation</strong>
                      <span style="font-size: 0.8rem; color: #BAC8C6;">Relapse prevention &amp; long-term integration</span>
                    </a>
                  </div>
                </div>
              </nav>
            </div>

            <a href="#about" class="nav__link-item cc-nav w-nav-link" style="color: #ffffff; font-weight: 600; padding: 8px 14px;">About Us</a>
            <a href="#facilities" class="nav__link-item cc-nav w-nav-link" style="color: #ffffff; font-weight: 600; padding: 8px 14px;">Campus &amp; Facilities</a>
            <a href="#why-us" class="nav__link-item cc-nav w-nav-link" style="color: #ffffff; font-weight: 600; padding: 8px 14px;">Why Akrura</a>
            <a href="#service-area" class="nav__link-item cc-nav w-nav-link" style="color: #ffffff; font-weight: 600; padding: 8px 14px;">Tamil Nadu Reach</a>
            <a href="#contact" class="nav__link-item cc-nav w-nav-link" style="color: #ffffff; font-weight: 600; padding: 8px 14px;">Contact</a>
          </nav>

          <!-- Right Action CTA -->
          <div class="nav__right-block" style="display: flex; align-items: center; gap: 12px;">
            <a href="tel:9384190971" class="cta__green cta__outlined w-button" style="border: 1px solid #58EDA2; color: #58EDA2; border-radius: 50px; padding: 8px 18px; font-weight: 700; text-decoration: none; font-size: 0.88rem;">
              📞 93841 90971
            </a>
            <a href="https://wa.me/919384190971?text=Hello%20Akrura%20Rehabilitation%20Centre,%20I%20need%20urgent%20admission%20assistance." target="_blank" rel="noopener" class="cta__green w-button" style="background-color: #00856F; color: #ffffff; border-radius: 50px; padding: 8px 20px; font-weight: 700; text-decoration: none; font-size: 0.88rem; transition: background 0.3s;" onmouseover="this.style.background='#039775'" onmouseout="this.style.background='#00856F'">
              24/7 Admission
            </a>
            <div class="header-nav-btn mr-0 w-nav-button" aria-label="Toggle Mobile Menu" style="cursor: pointer; padding: 8px;">
              <div class="menu-button menu-btn-v2 w-nav-button">
                <div class="menu-icon-v2">
                  <div class="icon-line"></div>
                  <div class="icon-line"></div>
                  <div class="icon-line"></div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- MAIN PAGE CONTENT -->
    <main id="main" class="n4-page_main">

      <!-- HERO SECTION -->
      <header hero-main="" class="n4-hero_main_wrap n4-u-theme-dark" style="min-height: 85vh; position: relative; overflow: hidden; display: flex; align-items: center;">
        
        <div class="n4-hero_main_component" style="width: 100%; position: relative; z-index: 10;">
          <div class="n4-hero_main_contain n4-u-container n4-u-zindex-2" style="max-width: 1300px; margin: 0 auto; padding: 60px 24px;">
            <div class="n4-hero_main_layout n4-u-vflex-left-center">
              
              <div class="n4-hero_main_body n4-u-vflex-left-top n4-u-gap-row-4" style="max-width: 820px;">
                
                <!-- Dynamic Pill Tag -->
                <div data-animation-css="fade-d2" class="n4-hero_main_pill" style="margin-bottom: 16px;">
                  <div data-hero-pill="" class="n4-hero_main_pill_wrap" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(8px); padding: 6px 16px; border-radius: 50px;">
                    <div data-hero-pill-circle="" class="n4-hero_main_pill_circle" style="width: 10px; height: 10px; border-radius: 50%; background-color: #FFC728;"></div>
                    <div data-hero-pill-text="" class="n4-hero_main_pill_text" style="color: #fff; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">Alcohol &amp; Drug De-Addiction</div>
                  </div>
                </div>

                <!-- Main Hero Heading -->
                <div data-number="16" data-animation-css="fade" class="n4-hero_main_heading n4-u-text-style-display-small n4-g_heading n4-u-color-primary w-richtext">
                  <h1 style="color: #ffffff; font-size: clamp(2.3rem, 4.5vw, 4.2rem); font-weight: 700; line-height: 1.15; margin-bottom: 20px;">
                    AKRURA DE ADDICTION &amp; <br/>REHABILITATION <strong style="color: #58EDA2;">CENTRE</strong>
                  </h1>
                </div>

                <!-- Subhead -->
                <p data-animation-css="fade-d1" class="n4-hero_main_text n4-u-text-style-large" style="color: rgba(255,255,255,0.9); font-size: clamp(1.05rem, 1.8vw, 1.32rem); line-height: 1.65; margin-bottom: 30px; font-weight: 400;">
                  A trusted centre for <strong>Alcohol, Drug De-addiction and Psychiatric Care</strong>. Located at Vadipatti, Madurai, we serve patients from <strong>All Over Tamil Nadu</strong> including Chennai, Erode, Salem, Tiruppur, Coimbatore, and Dindigul. Our treatment includes Medical Support, Counseling, Yoga, Meditation, and Mind Refreshment activities. <em>We help every person to recover with dignity and rejoin their family.</em>
                </p>

                <!-- Hero CTA Buttons -->
                <div data-animation-css="fade-d2" class="n4-hero_btn_group n4-u-btn-group" style="display: flex; flex-wrap: wrap; gap: 16px;">
                  <a href="tel:9384190971" class="n4-btn_main_wrap" style="background-color: #00856F; color: #fff; padding: 14px 28px; border-radius: 50px; font-weight: 700; font-size: 1rem; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; transition: all 0.3s; border: 2px solid #00856F;" onmouseover="this.style.background='#039775'; this.style.borderColor='#039775'" onmouseout="this.style.background='#00856F'; this.style.borderColor='#00856F'">
                    <span>📞 24/7 Helpline: 93841 90971</span>
                  </a>
                  <a href="https://wa.me/919384190971?text=Hello%20Akrura%20Rehabilitation%20Centre,%20I%20need%20details%20about%20treatment%20and%20admission." target="_blank" rel="noopener" class="n4-btn_main_wrap" style="background: transparent; color: #58EDA2; border: 2px solid #58EDA2; padding: 14px 28px; border-radius: 50px; font-weight: 700; font-size: 1rem; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; transition: all 0.3s;" onmouseover="this.style.background='rgba(88,237,162,0.15)'" onmouseout="this.style.background='transparent'">
                    <span>💬 WhatsApp Us</span>
                  </a>
                </div>

                <!-- Trust Badges Under Hero -->
                <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 32px; color: rgba(255,255,255,0.8); font-size: 0.85rem; font-weight: 600;">
                  <span style="display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="#58EDA2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> 100% Confidential</span>
                  <span style="display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="#58EDA2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> 24/7 Medical Care</span>
                  <span style="display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="#58EDA2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> Vadipatti, Madurai</span>
                  <span style="display: flex; align-items: center; gap: 6px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="#58EDA2"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg> Serving All Tamil Nadu</span>
                </div>

              </div>

            </div>
          </div>
        </div>

        <!-- Hero Background Images (Smooth Cross-fade matching rotating pills) -->
        <div hero-bg="" class="n4-hero_main_bg_wrap n4-u-cover-absolute" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;">
          <div class="n4-hero_main_bg_inner" style="position: relative; width: 100%; height: 100%;">
            <!-- Image 1: Serene meditation & morning dawn -->
            <img class="n4-hero_main_bg n4-u-cover-absolute" src="hero-bg-1.jpg" alt="Meditation and Mind Refreshment at Akrura" data-hero-bg="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 1; transition: opacity 0.8s ease-in-out;"/>
            <!-- Image 2: Medical doctor & psychiatric support -->
            <img class="n4-hero_main_bg n4-u-cover-absolute" src="hero-bg-2.jpg" alt="Psychiatric and Medical Detox Care" data-hero-bg="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.8s ease-in-out;"/>
            <!-- Image 3: Compassionate counseling session -->
            <img class="n4-hero_main_bg n4-u-cover-absolute" src="hero-bg-3.jpg" alt="Individual and Family Counseling" data-hero-bg="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.8s ease-in-out;"/>
            <!-- Image 4: Rejoining family with dignity -->
            <img class="n4-hero_main_bg n4-u-cover-absolute" src="hero-bg-4.jpg" alt="Recover with Dignity and Rejoin Family" data-hero-bg="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transition: opacity 0.8s ease-in-out;"/>
            
            <!-- Dark gradient overlay for perfect readability -->
            <div class="n4-hero_main_fade n4-u-cover-absolute" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(1, 49, 38, 0.92) 0%, rgba(1, 49, 38, 0.75) 50%, rgba(1, 49, 38, 0.85) 100%);"></div>
          </div>
        </div>

      </header>

      <!-- DISTRICT MARQUEE (Serving All Over Tamil Nadu) -->
      <section class="n4-trusted_wrap n4-u-overflow-clip" style="background-color: #03251D; padding: 22px 0; border-top: 1px solid rgba(88,237,162,0.15); border-bottom: 1px solid rgba(88,237,162,0.15);">
        <div style="max-width: 1400px; margin: 0 auto; display: flex; align-items: center; justify-content: center; overflow: hidden; white-space: nowrap;">
          <div style="display: inline-flex; gap: 36px; color: #58EDA2; font-weight: 700; font-size: 0.92rem; text-transform: uppercase; letter-spacing: 2px; animation: marqueeScroll 28s linear infinite;">
            <span>★ Serving Patients Across All Over Tamil Nadu</span>
            <span>• Madurai</span>
            <span>• Chennai</span>
            <span>• Coimbatore</span>
            <span>• Salem</span>
            <span>• Tiruppur</span>
            <span>• Erode</span>
            <span>• Dindigul</span>
            <span>• Tiruchirappalli</span>
            <span>• Tirunelveli</span>
            <span>• Theni</span>
            <span>• Thanjavur</span>
            <span>• Vellore</span>
            <span>• Karur</span>
            <span>• Virudhunagar</span>
            <span>• 24/7 Medical Care &amp; Admission Helpline: 93841 90971</span>
          </div>
        </div>
      </section>

      <style>
        @keyframes marqueeScroll {
          0% { transform: translateX(0%); }
          100% { transform: translateX(-50%); }
        }
      </style>

      <!-- ABOUT THE CENTER SECTION -->
      <section id="about" style="background-color: #013126; padding: 100px 24px; position: relative;">
        <div style="max-width: 1200px; margin: 0 auto;">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 60px; align-items: center;">
            
            <!-- Left Text Content -->
            <div>
              <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
                About Akrura Rehabilitation Centre
              </div>
              <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 700; line-height: 1.25; margin-bottom: 24px;">
                A trusted haven for <span style="color: #58EDA2;">de-addiction, healing,</span> and psychiatric recovery
              </h2>
              <p style="color: rgba(255,255,255,0.85); font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
                <strong>Akrura De Addiction &amp; Rehabilitation Centre</strong> is a trusted centre for Alcohol, Drug De-addiction, and Psychiatric Care. Located at Vadipatti, Madurai, we serve patients from <strong>All Over Tamil Nadu including Chennai, Erode, Salem, Tiruppur, Coimbatore, and Dindigul</strong>.
              </p>
              <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin-bottom: 28px;">
                Our treatment includes <strong>Medical Support, Individual &amp; Family Counseling, Yoga, Meditation, and Mind Refreshment activities</strong>. We believe addiction is a treatable medical condition, not a moral failure. With compassionate care and clinical rigor, <strong>we help every person to recover with dignity and rejoin their family</strong>.
              </p>
              <div style="display: flex; flex-wrap: wrap; gap: 16px;">
                <a href="#services" style="background: #00856F; color: #fff; padding: 12px 26px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 0.95rem;">Explore All 8 Treatments</a>
                <a href="tel:9384190971" style="border: 1px solid #58EDA2; color: #58EDA2; padding: 12px 26px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 0.95rem;">Speak With Counselor</a>
              </div>
            </div>

            <!-- Right Visual Feature -->
            <div style="position: relative;">
              <div style="border-radius: 24px; overflow: hidden; box-shadow: 0 25px 60px rgba(0,0,0,0.5); border: 1px solid rgba(88,237,162,0.2);">
                <img src="facility-campus.jpg" alt="Akrura Rehabilitation Centre Vadipatti Madurai" style="width: 100%; height: 420px; object-fit: cover; display: block;"/>
              </div>
              <div style="position: absolute; bottom: -24px; left: -24px; background: #035748; border: 1px solid rgba(88,237,162,0.3); padding: 20px 24px; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.4); max-width: 280px;">
                <div style="font-size: 2.2rem; font-weight: 800; color: #58EDA2; line-height: 1;">24/7</div>
                <div style="color: #ffffff; font-weight: 700; font-size: 0.95rem; margin-top: 4px;">Continuous Care &amp; Medical Oversight</div>
                <div style="color: #BAC8C6; font-size: 0.8rem; margin-top: 4px;">Doctors, Nurses &amp; Counselors On-Site</div>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- SERVICES & TREATMENT PROGRAMS SECTION (8 Detailed Services) -->
      <section id="services" class="n4-section_wrap" style="background-color: #03251D; padding: 100px 24px;">
        <div style="max-width: 1300px; margin: 0 auto;">
          
          <div style="text-align: center; max-width: 820px; margin: 0 auto 60px auto;">
            <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
              Our 8 Comprehensive Recovery Services
            </div>
            <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.8vw, 3.2rem); font-weight: 700; line-height: 1.25; margin-bottom: 20px;">
              Evidence-based treatments designed for <span style="color: #58EDA2;">holistic recovery</span>
            </h2>
            <p style="color: #BAC8C6; font-size: 1.15rem; line-height: 1.7;">
              From medically supervised detoxification to psychological counseling and mind refreshment, our 8-pillar care model guides every individual toward lasting sobriety and mental peace.
            </p>
          </div>

          <!-- 4 Core Expandable Service Cards -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
            
            <!-- Service 1: Alcohol De-Addiction -->
            <div class="n4-services_card_wrap" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(88,237,162,0.15); min-height: 440px; display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; position: relative;">
              <img src="service-alcohol.jpg" alt="Alcohol De-Addiction Treatment" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(1,49,38,0.2) 0%, rgba(1,49,38,0.92) 80%);"></div>
              <div style="position: relative; z-index: 2;">
                <span style="display: inline-block; padding: 4px 10px; background: rgba(3,151,117,0.3); color: #58EDA2; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 10px;">Program 01</span>
                <h3 style="color: #ffffff; font-size: 1.45rem; font-weight: 700; margin-bottom: 10px;">1. Alcohol De-Addiction Treatment</h3>
                <p style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.6; margin-bottom: 18px;">
                  Comprehensive medical withdrawal management, craving control therapy, cognitive behavioral intervention, and relapse prevention to overcome chronic alcoholism permanently.
                </p>
                <a href="tel:9384190971" style="color: #58EDA2; font-weight: 700; text-decoration: none; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 6px;">
                  Consult Now &rarr;
                </a>
              </div>
            </div>

            <!-- Service 2: Drug De-Addiction -->
            <div class="n4-services_card_wrap" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(88,237,162,0.15); min-height: 440px; display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; position: relative;">
              <img src="service-drugs.jpg" alt="Drug De-Addiction Treatment" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(1,49,38,0.2) 0%, rgba(1,49,38,0.92) 80%);"></div>
              <div style="position: relative; z-index: 2;">
                <span style="display: inline-block; padding: 4px 10px; background: rgba(46,218,241,0.2); color: #2EDAF1; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 10px;">Program 02</span>
                <h3 style="color: #ffffff; font-size: 1.45rem; font-weight: 700; margin-bottom: 10px;">2. Drug De-Addiction Treatment</h3>
                <p style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.6; margin-bottom: 18px;">
                  Specialized inpatient rehabilitation for chemical dependency, psychological de-conditioning, emotional coping mechanisms, and long-term clean lifestyle rebuilding.
                </p>
                <a href="tel:9384190971" style="color: #2EDAF1; font-weight: 700; text-decoration: none; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 6px;">
                  Consult Now &rarr;
                </a>
              </div>
            </div>

            <!-- Service 3: Psychiatric Care & Counseling -->
            <div class="n4-services_card_wrap" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(88,237,162,0.15); min-height: 440px; display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; position: relative;">
              <img src="service-psychiatric.jpg" alt="Psychiatric Care &amp; Counseling" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(1,49,38,0.2) 0%, rgba(1,49,38,0.92) 80%);"></div>
              <div style="position: relative; z-index: 2;">
                <span style="display: inline-block; padding: 4px 10px; background: rgba(182,158,255,0.2); color: #B69EFF; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 10px;">Program 03</span>
                <h3 style="color: #ffffff; font-size: 1.45rem; font-weight: 700; margin-bottom: 10px;">3. Psychiatric Care &amp; Counseling</h3>
                <p style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.6; margin-bottom: 18px;">
                  Expert psychiatrist consultations, dual-diagnosis management, treatment for depression, anxiety, mood disorders, hallucinations, and trauma-informed clinical care.
                </p>
                <a href="tel:9384190971" style="color: #B69EFF; font-weight: 700; text-decoration: none; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 6px;">
                  Consult Now &rarr;
                </a>
              </div>
            </div>

            <!-- Service 4: Yoga, Meditation, Exercise & Brain Gym -->
            <div class="n4-services_card_wrap" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(88,237,162,0.15); min-height: 440px; display: flex; flex-direction: column; justify-content: flex-end; padding: 28px; position: relative;">
              <img src="service-yoga.jpg" alt="Yoga, Meditation and Brain Gym" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; transition: transform 0.5s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'"/>
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(1,49,38,0.2) 0%, rgba(1,49,38,0.92) 80%);"></div>
              <div style="position: relative; z-index: 2;">
                <span style="display: inline-block; padding: 4px 10px; background: rgba(255,199,40,0.2); color: #FFC728; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 10px;">Program 04</span>
                <h3 style="color: #ffffff; font-size: 1.45rem; font-weight: 700; margin-bottom: 10px;">7. Yoga, Meditation, Exercise &amp; Brain Gym</h3>
                <p style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.6; margin-bottom: 18px;">
                  Daily morning yoga, pranayama, guided mindfulness, physical exercise, brain gym cognitive workouts, and mind refreshment activities that rejuvenate cognitive functioning.
                </p>
                <a href="tel:9384190971" style="color: #FFC728; font-weight: 700; text-decoration: none; font-size: 0.9rem; display: inline-flex; align-items: center; gap: 6px;">
                  Consult Now &rarr;
                </a>
              </div>
            </div>

          </div>

          <!-- 4 Care Extensions & Clinical Support Cards -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
            
            <!-- Service 4: Detoxification & Medical Support -->
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 28px; transition: border-color 0.3s;" onmouseover="this.style.borderColor='#58EDA2'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'">
              <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(88,237,162,0.15); display: flex; align-items: center; justify-content: center; color: #58EDA2; font-size: 1.3rem; margin-bottom: 16px;">
                🩺
              </div>
              <h4 style="color: #ffffff; font-size: 1.25rem; font-weight: 700; margin-bottom: 10px;">4. Detoxification &amp; Medical Support</h4>
              <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                Round-the-clock doctor supervision, vitals monitoring, and gentle medical management to ease withdrawal symptoms comfortably and safely in a secure medical setup.
              </p>
            </div>

            <!-- Service 5: Individual Counseling -->
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 28px; transition: border-color 0.3s;" onmouseover="this.style.borderColor='#58EDA2'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'">
              <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(46,218,241,0.15); display: flex; align-items: center; justify-content: center; color: #2EDAF1; font-size: 1.3rem; margin-bottom: 16px;">
                🧠
              </div>
              <h4 style="color: #ffffff; font-size: 1.25rem; font-weight: 700; margin-bottom: 10px;">5. Individual Counseling</h4>
              <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                One-on-one confidential sessions with certified psychologists to address underlying emotional trauma, unresolved grief, low self-esteem, and behavioral triggers.
              </p>
            </div>

            <!-- Service 6: Family Counseling -->
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 28px; transition: border-color 0.3s;" onmouseover="this.style.borderColor='#58EDA2'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'">
              <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(182,158,255,0.15); display: flex; align-items: center; justify-content: center; color: #B69EFF; font-size: 1.3rem; margin-bottom: 16px;">
                👨‍👩‍👧‍👦
              </div>
              <h4 style="color: #ffffff; font-size: 1.25rem; font-weight: 700; margin-bottom: 10px;">6. Family Counseling</h4>
              <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                Structured family therapy to heal broken bonds, rebuild mutual trust, educate family members on enabling behaviors, and prepare a supportive home environment.
              </p>
            </div>

            <!-- Service 8: Aftercare & Rehabilitation Support -->
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 28px; transition: border-color 0.3s;" onmouseover="this.style.borderColor='#58EDA2'" onmouseout="this.style.borderColor='rgba(255,255,255,0.08)'">
              <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(255,199,40,0.15); display: flex; align-items: center; justify-content: center; color: #FFC728; font-size: 1.3rem; margin-bottom: 16px;">
                🤝
              </div>
              <h4 style="color: #ffffff; font-size: 1.25rem; font-weight: 700; margin-bottom: 10px;">8. Aftercare &amp; Rehabilitation Support</h4>
              <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                Long-term post-discharge follow-ups, tele-counseling support, relapse prevention check-ins, and life-skills training ensuring lasting sobriety in daily life.
              </p>
            </div>

          </div>

        </div>
      </section>

      <!-- BENTO FEATURES GRID SECTION ("Why Akrura") -->
      <section id="why-us" class="n4-features_wrap n4-u-theme-light" style="background-color: #013126; padding: 100px 24px; position: relative;">
        <div style="max-width: 1300px; margin: 0 auto;">
          
          <div style="text-align: center; max-width: 820px; margin: 0 auto 50px auto;">
            <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
              Why Choose Akrura
            </div>
            <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.8vw, 3.2rem); font-weight: 700; line-height: 1.25; margin-bottom: 20px;">
              Clinical excellence, compassionate care, and <span style="color: #58EDA2;">serene surroundings</span>
            </h2>
            <p style="color: #BAC8C6; font-size: 1.15rem; line-height: 1.7;">
              Located near the Madurai–Dindigul Main Road at Vadipatti, our peaceful centre provides the optimal atmosphere for physical, mental, and spiritual restoration.
            </p>
          </div>

          <!-- Bento Grid Layout -->
          <div style="display: grid; grid-template-columns: repeat(12, 1fr); gap: 24px;">
            
            <!-- Bento 1 (Large 7 Cols): Serving All Tamil Nadu -->
            <div style="grid-column: span 7; background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; position: relative; overflow: hidden; min-height: 340px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <span style="display: inline-block; padding: 4px 12px; background: rgba(88,237,162,0.15); color: #58EDA2; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 14px;">TAMIL NADU-WIDE REACH</span>
                <h3 style="color: #ffffff; font-size: 1.8rem; font-weight: 700; line-height: 1.3; max-width: 480px; margin-bottom: 12px;">
                  Serving patients from Chennai, Coimbatore, Salem, Erode, Tiruppur &amp; beyond
                </h3>
                <p style="color: #BAC8C6; font-size: 1rem; line-height: 1.7; max-width: 500px;">
                  Patients and families from across Tamil Nadu choose Akrura for our high standard of medical detox, specialized psychiatric care, and peaceful residential campus away from city noise.
                </p>
              </div>
              <div style="margin-top: 24px;">
                <a href="#service-area" style="color: #58EDA2; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">View All Supported Districts &rarr;</a>
              </div>
            </div>

            <!-- Bento 2 (5 Cols): 24/7 Care with Live Clock -->
            <div style="grid-column: span 5; background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; position: relative; overflow: hidden; min-height: 340px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <span style="display: inline-block; padding: 4px 12px; background: rgba(46,218,241,0.15); color: #2EDAF1; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 14px;">24/7 AVAILABILITY</span>
                <h3 style="color: #ffffff; font-size: 1.6rem; font-weight: 700; line-height: 1.3; margin-bottom: 12px;">
                  24/7 Medical Care &amp; Immediate Admission
                </h3>
                <p style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.6;">
                  Addiction emergencies cannot wait. Our medical officers, nurses, and admission counselors are ready 24 hours a day, 7 days a week.
                </p>
              </div>
              <div style="display: flex; align-items: center; gap: 14px; background: rgba(255,255,255,0.04); padding: 14px 18px; border-radius: 12px; margin-top: 20px;">
                <span style="font-size: 1.8rem;">⏰</span>
                <div>
                  <div style="color: #fff; font-weight: 700; font-size: 0.95rem;">Helpline Active 24/7</div>
                  <div style="color: #58EDA2; font-size: 0.85rem;">Call: 93841 90971</div>
                </div>
              </div>
            </div>

            <!-- Bento 3 (5 Cols): Multidisciplinary Specialist Team -->
            <div style="grid-column: span 5; background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; position: relative; overflow: hidden; min-height: 340px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <span style="display: inline-block; padding: 4px 12px; background: rgba(182,158,255,0.15); color: #B69EFF; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 14px;">SPECIALIST TEAM</span>
                <h3 style="color: #ffffff; font-size: 1.6rem; font-weight: 700; line-height: 1.3; margin-bottom: 12px;">
                  Multidisciplinary Clinical Team
                </h3>
                <ul style="color: #BAC8C6; font-size: 0.95rem; line-height: 1.8; padding-left: 20px; list-style-type: disc;">
                  <li>Consultant Psychiatrists &amp; Medical Doctors</li>
                  <li>Experienced Clinical Psychologists</li>
                  <li>Dedicated Addiction Counselors</li>
                  <li>Certified Yoga &amp; Meditation Instructors</li>
                  <li>Trained 24/7 Nursing Staff</li>
                </ul>
              </div>
            </div>

            <!-- Bento 4 (7 Cols): Recovery with Dignity & Family Reunion -->
            <div style="grid-column: span 7; background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; position: relative; overflow: hidden; min-height: 340px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <span style="display: inline-block; padding: 4px 12px; background: rgba(255,199,40,0.15); color: #FFC728; border-radius: 20px; font-size: 0.75rem; font-weight: 700; margin-bottom: 14px;">OUR PHILOSOPHY</span>
                <h3 style="color: #ffffff; font-size: 1.8rem; font-weight: 700; line-height: 1.3; max-width: 520px; margin-bottom: 12px;">
                  Recover with Dignity &amp; Rejoin Your Family
                </h3>
                <p style="color: #BAC8C6; font-size: 1rem; line-height: 1.7; max-width: 520px;">
                  We treat every patient with absolute respect, empathy, and confidentiality. Through Brain Gym, creative mind refreshment, and family counseling, we help each person rebuild confidence and return home to a joyful, united family life.
                </p>
              </div>
              <div style="display: flex; gap: 14px; margin-top: 20px;">
                <span style="background: rgba(255,255,255,0.06); padding: 8px 16px; border-radius: 30px; color: #fff; font-size: 0.85rem; font-weight: 600;">✨ Zero Stigma</span>
                <span style="background: rgba(255,255,255,0.06); padding: 8px 16px; border-radius: 30px; color: #fff; font-size: 0.85rem; font-weight: 600;">🧘 Mind Refreshment</span>
                <span style="background: rgba(255,255,255,0.06); padding: 8px 16px; border-radius: 30px; color: #fff; font-size: 0.85rem; font-weight: 600;">❤️ Family Bonding</span>
              </div>
            </div>

          </div>

        </div>
      </section>

      <style>
        @media (max-width: 991px) {
          #why-us div[style*="grid-column: span"] {
            grid-column: span 12 !important;
          }
        }
      </style>

      <!-- PARALLAX & PROVEN CLINICAL OUTCOMES (Stats Section) -->
      <div class="n4-parallax_wrap" style="position: relative; overflow: hidden;">
        
        <!-- Parallax Background Visual -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;">
          <img src="parallax-bg.jpg" alt="Akrura Recovery Sanctuary" style="width: 100%; height: 120%; object-fit: cover; filter: brightness(0.35);"/>
        </div>

        <div style="position: relative; z-index: 2; padding: 120px 24px;">
          <div style="max-width: 1200px; margin: 0 auto;">
            
            <div style="text-align: center; max-width: 800px; margin: 0 auto 60px auto;">
              <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2.2rem, 4vw, 3.4rem); font-weight: 700; line-height: 1.2; margin-bottom: 20px;">
                Proven recovery outcomes, <span style="color: #58EDA2;">measurable healing</span>
              </h2>
              <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; line-height: 1.7;">
                By combining medical detox with psychological counseling, yoga, and family inclusion, we help patients overcome addiction safely and sustainably.
              </p>
            </div>

            <!-- 4 Circular Progress Stats Cards -->
            <div class="n4-stats_layout" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 30px;">
              
              <!-- Stat 1: 95% -->
              <div data-stats="item" style="background: rgba(1, 49, 38, 0.85); backdrop-filter: blur(10px); border: 1px solid rgba(88,237,162,0.25); border-radius: 20px; padding: 36px 24px; text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 800; color: #58EDA2; line-height: 1; margin-bottom: 12px;">95%</div>
                <h3 style="color: #ffffff; font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">Detox &amp; Recovery Rate</h3>
                <p style="color: #BAC8C6; font-size: 0.88rem; line-height: 1.6;">Over 95% of patients successfully complete medical detoxification without withdrawal complications.</p>
              </div>

              <!-- Stat 2: 100% -->
              <div data-stats="item" style="background: rgba(1, 49, 38, 0.85); backdrop-filter: blur(10px); border: 1px solid rgba(46,218,241,0.25); border-radius: 20px; padding: 36px 24px; text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 800; color: #2EDAF1; line-height: 1; margin-bottom: 12px;">100%</div>
                <h3 style="color: #ffffff; font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">Confidential &amp; Dignified</h3>
                <p style="color: #BAC8C6; font-size: 0.88rem; line-height: 1.6;">Complete identity protection, zero stigma, and respectful residential care guaranteed.</p>
              </div>

              <!-- Stat 3: 24/7 -->
              <div data-stats="item" style="background: rgba(1, 49, 38, 0.85); backdrop-filter: blur(10px); border: 1px solid rgba(182,158,255,0.25); border-radius: 20px; padding: 36px 24px; text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 800; color: #B69EFF; line-height: 1; margin-bottom: 12px;">24/7</div>
                <h3 style="color: #ffffff; font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">Medical &amp; Nursing Care</h3>
                <p style="color: #BAC8C6; font-size: 0.88rem; line-height: 1.6;">Continuous doctor oversight, psychiatric care, and round-the-clock emergency support.</p>
              </div>

              <!-- Stat 4: 38+ Districts -->
              <div data-stats="item" style="background: rgba(1, 49, 38, 0.85); backdrop-filter: blur(10px); border: 1px solid rgba(255,199,40,0.25); border-radius: 20px; padding: 36px 24px; text-align: center;">
                <div style="font-size: 3.5rem; font-weight: 800; color: #FFC728; line-height: 1; margin-bottom: 12px;">38+</div>
                <h3 style="color: #ffffff; font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">Districts in Tamil Nadu</h3>
                <p style="color: #BAC8C6; font-size: 0.88rem; line-height: 1.6;">Active patient recovery and family outreach across all districts of Tamil Nadu.</p>
              </div>

            </div>

          </div>
        </div>

      </div>

      <!-- CAMPUS & FACILITIES SECTION (Gallery & Infrastructure Placeholders) -->
      <section id="facilities" style="background-color: #013126; padding: 100px 24px;">
        <div style="max-width: 1300px; margin: 0 auto;">
          
          <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px; margin-bottom: 50px;">
            <div>
              <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 12px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
                Campus &amp; Healing Environment
              </div>
              <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 700; line-height: 1.2;">
                Designed for peaceful reflection and <span style="color: #58EDA2;">mind refreshment</span>
              </h2>
            </div>
            <div>
              <a href="tel:9384190971" style="background: rgba(88,237,162,0.15); color: #58EDA2; border: 1px solid rgba(88,237,162,0.3); padding: 12px 24px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 0.9rem;">Schedule a Campus Visit</a>
            </div>
          </div>

          <div class="facility-grid">
            
            <!-- Facility 1: Serene Vadipatti Campus -->
            <div class="facility-card">
              <img src="facility-campus.jpg" alt="Akrura Vadipatti Campus" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Sanctuary</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">Serene Campus at Vadipatti</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  Situated in a calm, pollution-free atmosphere near the Madurai–Dindigul corridor, surrounded by natural fresh air and tranquil hills.
                </p>
              </div>
            </div>

            <!-- Facility 2: Meditation & Yoga Hall -->
            <div class="facility-card">
              <img src="facility-meditation.jpg" alt="Yoga &amp; Meditation Hall" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Mind Refreshment</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">Yoga, Meditation &amp; Brain Gym Hall</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  Dedicated hall equipped for morning mindfulness, breathwork (pranayama), cognitive Brain Gym games, and relaxing mind refreshment sessions.
                </p>
              </div>
            </div>

            <!-- Facility 3: Private Counseling Rooms -->
            <div class="facility-card">
              <img src="facility-counseling.jpg" alt="Private Counseling Rooms" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Confidential</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">Private Consultation Chambers</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  Comfortable, private consultation rooms where patients and families receive one-on-one psychiatric evaluations and confidential therapy.
                </p>
              </div>
            </div>

            <!-- Facility 4: 24/7 Nursing & Medical Station -->
            <div class="facility-card">
              <img src="service-detox.jpg" alt="24/7 Nursing and Medical Support" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Medical Care</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">24/7 Medical Care &amp; Monitoring</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  Equipped medical room with continuous vitals tracking, physician oversight, and nursing care to handle all detox and psychiatric requirements.
                </p>
              </div>
            </div>

            <!-- Facility 5: Nutritious Dining & Healthy Food -->
            <div class="facility-card">
              <img src="service-aftercare.jpg" alt="Nutritious Food and Community" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Nutrition</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">Wholesome Nutrition &amp; Recreation</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  Freshly cooked, nutrient-rich vegetarian and non-vegetarian meals planned to restore physical stamina, rebuild gut health, and boost immunity.
                </p>
              </div>
            </div>

            <!-- Facility 6: Family Reunion Lounge -->
            <div class="facility-card">
              <img src="service-family.jpg" alt="Family Lounge" class="facility-card-img"/>
              <div class="facility-card-body">
                <span class="facility-badge">Family Healing</span>
                <h3 style="color: #fff; font-size: 1.3rem; font-weight: 700; margin-bottom: 8px;">Family Interaction &amp; Guidance Lounge</h3>
                <p style="color: #BAC8C6; font-size: 0.92rem; line-height: 1.6;">
                  A warm, welcoming space for scheduled family visits, joint counseling, and celebration of recovery milestones.
                </p>
              </div>
            </div>

          </div>

          <div style="background: rgba(88,237,162,0.06); border: 1px dashed rgba(88,237,162,0.3); border-radius: 12px; padding: 20px; text-align: center; margin-top: 36px; color: #BAC8C6; font-size: 0.92rem;">
            📸 <em>Live Center facility &amp; photo gallery images will be updated as shared. Families are cordially invited to visit our Vadipatti, Madurai campus in person.</em>
          </div>

        </div>
      </section>

      <!-- TAMIL NADU SERVICE REGIONS SECTION -->
      <section id="service-area" style="background-color: #03251D; padding: 100px 24px;">
        <div style="max-width: 1200px; margin: 0 auto;">
          
          <div style="text-align: center; max-width: 820px; margin: 0 auto 50px auto;">
            <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
              Service Area: All Over Tamil Nadu
            </div>
            <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.8vw, 3.2rem); font-weight: 700; line-height: 1.25; margin-bottom: 20px;">
              Welcoming patients from <span style="color: #58EDA2;">every district</span> across Tamil Nadu
            </h2>
            <p style="color: #BAC8C6; font-size: 1.15rem; line-height: 1.7;">
              Distance is never a barrier to recovery. We assist families with seamless transportation guidance and emergency pick-up coordination from major hubs.
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
            
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #58EDA2; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Madurai &amp; Dindigul</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Vadipatti, Melur, Usilampatti, Tirumangalam, Dindigul town, Palani, Kodaikanal foothills.</p>
            </div>

            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #2EDAF1; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Coimbatore &amp; Tiruppur</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Coimbatore City, Pollachi, Mettupalayam, Tiruppur, Avinashi, Kangeyam, Palladam.</p>
            </div>

            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #FFC728; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Erode &amp; Salem</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Erode, Gobichettipalayam, Bhavani, Salem City, Attur, Mettur, Omalur, Namakkal.</p>
            </div>

            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #B69EFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Chennai &amp; North TN</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Chennai, Kanchipuram, Chengalpattu, Vellore, Tiruvannamalai, Cuddalore, Villupuram.</p>
            </div>

            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #58EDA2; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Trichy &amp; Central TN</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Tiruchirappalli, Thanjavur, Karur, Pudukkottai, Perambalur, Ariyalur, Tiruvarur.</p>
            </div>

            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(88,237,162,0.15); border-radius: 16px; padding: 24px;">
              <h3 style="color: #2EDAF1; font-size: 1.25rem; font-weight: 700; margin-bottom: 8px;">Southern Districts</h3>
              <p style="color: #BAC8C6; font-size: 0.9rem; line-height: 1.6;">Theni, Virudhunagar, Sivagangai, Ramanathapuram, Tirunelveli, Tenkasi, Thoothukudi, Kanyakumari.</p>
            </div>

          </div>

          <div style="text-align: center; margin-top: 48px;">
            <a href="tel:9384190971" style="background: #00856F; color: #fff; padding: 14px 32px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 1rem; display: inline-flex; align-items: center; gap: 8px;">
              <span>Call 24/7 Helpline for Admission from Your District: 93841 90971</span>
            </a>
          </div>

        </div>
      </section>

      <!-- TESTIMONIALS / RECOVERY STORIES -->
      <section style="background-color: #013126; padding: 100px 24px;">
        <div style="max-width: 1200px; margin: 0 auto;">
          
          <div style="text-align: center; max-width: 800px; margin: 0 auto 60px auto;">
            <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
              Real Transformation Stories
            </div>
            <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.8vw, 3.2rem); font-weight: 700; line-height: 1.25; margin-bottom: 20px;">
              Heartfelt stories of <span style="color: #58EDA2;">hope and restored families</span>
            </h2>
            <p style="color: #BAC8C6; font-size: 1.15rem; line-height: 1.7;">
              Read how our compassionate medical detox, counseling, and mind refreshment activities gave individuals their lives and families back.
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
            
            <!-- Story 1 -->
            <div style="background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="color: #FFC728; font-size: 1.4rem; margin-bottom: 16px;">★★★★★</div>
                <p style="color: #ffffff; font-size: 1.05rem; line-height: 1.8; font-style: italic; margin-bottom: 24px;">
                  “Akrura gave my husband back to me and our two children. After 7 years of heavy drinking, we had lost all hope. The medical detox was completely smooth and safe, and the family counseling helped us heal emotionally. Today he has been sober for 18 months.”
                </p>
              </div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 18px; display: flex; align-items: center; gap: 14px;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: #00856F; color: #fff; font-weight: 700; display: flex; align-items: center; justify-content: center;">P</div>
                <div>
                  <div style="color: #fff; font-weight: 700; font-size: 0.95rem;">Preetha S.</div>
                  <div style="color: #58EDA2; font-size: 0.8rem;">Wife of Recovered Member • Chennai</div>
                </div>
              </div>
            </div>

            <!-- Story 2 -->
            <div style="background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="color: #FFC728; font-size: 1.4rem; margin-bottom: 16px;">★★★★★</div>
                <p style="color: #ffffff; font-size: 1.05rem; line-height: 1.8; font-style: italic; margin-bottom: 24px;">
                  “I came to Akrura feeling broken and trapped in substance dependency. The daily routine of yoga, morning meditation, brain gym, and individual counseling in Vadipatti gave me a fresh perspective on life. The staff treated me like a brother with absolute dignity.”
                </p>
              </div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 18px; display: flex; align-items: center; gap: 14px;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: #2EDAF1; color: #013126; font-weight: 700; display: flex; align-items: center; justify-content: center;">V</div>
                <div>
                  <div style="color: #fff; font-weight: 700; font-size: 0.95rem;">Vignesh K.</div>
                  <div style="color: #2EDAF1; font-size: 0.8rem;">Recovered Member (2 Years Sober) • Coimbatore</div>
                </div>
              </div>
            </div>

            <!-- Story 3 -->
            <div style="background: #03251D; border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <div style="color: #FFC728; font-size: 1.4rem; margin-bottom: 16px;">★★★★★</div>
                <p style="color: #ffffff; font-size: 1.05rem; line-height: 1.8; font-style: italic; margin-bottom: 24px;">
                  “My brother was suffering from severe depression coupled with alcohol addiction. The psychiatrists at Akrura accurately diagnosed his condition and provided genuine compassionate care. Our entire family is deeply thankful to the Vadipatti team.”
                </p>
              </div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 18px; display: flex; align-items: center; gap: 14px;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: #B69EFF; color: #013126; font-weight: 700; display: flex; align-items: center; justify-content: center;">R</div>
                <div>
                  <div style="color: #fff; font-weight: 700; font-size: 0.95rem;">Ramesh P.</div>
                  <div style="color: #B69EFF; font-size: 0.8rem;">Brother of Recovered Patient • Madurai</div>
                </div>
              </div>
            </div>

          </div>

        </div>
      </section>

      <!-- BOTTOM CALL TO ACTION -->
      <section style="background: linear-gradient(135deg, #035748 0%, #013126 100%); padding: 100px 24px; text-align: center; border-top: 1px solid rgba(88,237,162,0.2); position: relative;">
        <div style="max-width: 900px; margin: 0 auto; position: relative; z-index: 2;">
          <span style="display: inline-block; padding: 6px 18px; background: rgba(88,237,162,0.15); color: #58EDA2; border-radius: 50px; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 20px;">
            Immediate 24/7 Help Available
          </span>
          <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2.4rem, 4.5vw, 3.8rem); font-weight: 700; line-height: 1.2; margin-bottom: 20px;">
            Begin your journey to recovery today
          </h2>
          <p style="color: #BAC8C6; font-size: 1.25rem; line-height: 1.7; margin-bottom: 36px;">
            You or your loved one do not have to struggle alone. Our compassionate medical team and counselors are available 24/7 to guide you with complete privacy and dignity.
          </p>
          <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 16px;">
            <a href="tel:9384190971" style="background: #58EDA2; color: #013126; padding: 16px 36px; border-radius: 50px; font-weight: 800; font-size: 1.05rem; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 10px 30px rgba(88,237,162,0.3); transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
              <span>📞 Call 24/7 Helpline: 93841 90971</span>
            </a>
            <a href="https://wa.me/919384190971?text=Hello%20Akrura%20Rehabilitation%20Centre,%20I%20would%20like%20to%20consult%20for%20admission." target="_blank" rel="noopener" style="background: transparent; color: #fff; border: 2px solid #fff; padding: 16px 36px; border-radius: 50px; font-weight: 700; font-size: 1.05rem; text-decoration: none; display: inline-flex; align-items: center; gap: 10px; transition: background 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.1)'" onmouseout="this.style.background='transparent'">
              <span>💬 WhatsApp Consultation</span>
            </a>
          </div>
        </div>
      </section>

      <!-- CONTACT & LOCATION DETAILS SECTION (With Google Maps Embed) -->
      <section id="contact" style="background-color: #01221A; padding: 100px 24px; border-top: 1px solid rgba(255,255,255,0.06);">
        <div style="max-width: 1250px; margin: 0 auto;">
          
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 50px;">
            
            <!-- Contact Info Column -->
            <div>
              <div style="display: inline-flex; align-items: center; gap: 8px; color: #58EDA2; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 16px;">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #58EDA2;"></span>
                Contact &amp; Location
              </div>
              <h2 class="serif-heading" style="color: #ffffff; font-size: clamp(2rem, 3.2vw, 2.8rem); font-weight: 700; line-height: 1.25; margin-bottom: 24px;">
                Visit our Vadipatti Centre or reach us 24/7
              </h2>
              
              <div style="display: flex; flex-direction: column; gap: 24px; margin-top: 30px;">
                
                <!-- Phone -->
                <div style="display: flex; gap: 16px;">
                  <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(88,237,162,0.15); display: flex; align-items: center; justify-content: center; color: #58EDA2; font-size: 1.3rem; flex-shrink: 0;">
                    📞
                  </div>
                  <div>
                    <div style="color: #BAC8C6; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">24/7 Contact &amp; Helpline</div>
                    <a href="tel:9384190971" style="color: #ffffff; font-size: 1.25rem; font-weight: 700; text-decoration: none; display: block; margin-top: 4px;">
                      93841 90971
                    </a>
                  </div>
                </div>

                <!-- WhatsApp -->
                <div style="display: flex; gap: 16px;">
                  <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(37,211,102,0.15); display: flex; align-items: center; justify-content: center; color: #25D366; font-size: 1.3rem; flex-shrink: 0;">
                    💬
                  </div>
                  <div>
                    <div style="color: #BAC8C6; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">WhatsApp Support</div>
                    <a href="https://wa.me/919384190971" target="_blank" rel="noopener" style="color: #25D366; font-size: 1.25rem; font-weight: 700; text-decoration: none; display: block; margin-top: 4px;">
                      93841 90971 (Click to Chat)
                    </a>
                  </div>
                </div>

                <!-- Address -->
                <div style="display: flex; gap: 16px;">
                  <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(255,199,40,0.15); display: flex; align-items: center; justify-content: center; color: #FFC728; font-size: 1.3rem; flex-shrink: 0;">
                    📍
                  </div>
                  <div>
                    <div style="color: #BAC8C6; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Centre Address</div>
                    <p style="color: #ffffff; font-size: 1rem; line-height: 1.6; margin-top: 4px;">
                      <strong>5/96/13, Street-3, Mettuperumal Nagar,</strong><br/>
                      Vadipatti, Madurai - 625218, Tamil Nadu
                    </p>
                    <p style="color: #58EDA2; font-size: 0.88rem; margin-top: 4px; font-weight: 600;">
                      Landmark: Near Madurai - Dindigul Main Road
                    </p>
                  </div>
                </div>

                <!-- Socials -->
                <div style="display: flex; gap: 16px;">
                  <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(46,218,241,0.15); display: flex; align-items: center; justify-content: center; color: #2EDAF1; font-size: 1.3rem; flex-shrink: 0;">
                    🌐
                  </div>
                  <div>
                    <div style="color: #BAC8C6; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">Follow Our Social Channels</div>
                    <div style="display: flex; gap: 14px; margin-top: 8px;">
                      <a href="https://www.instagram.com/akrura_de_addiction" target="_blank" rel="noopener" style="color: #fff; background: rgba(255,255,255,0.06); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; text-decoration: none; border: 1px solid rgba(255,255,255,0.1);">Instagram</a>
                      <a href="https://www.facebook.com/share/1KWuSgFxir/" target="_blank" rel="noopener" style="color: #fff; background: rgba(255,255,255,0.06); padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; text-decoration: none; border: 1px solid rgba(255,255,255,0.1);">Facebook</a>
                    </div>
                  </div>
                </div>

              </div>

            </div>

            <!-- Google Maps & Callback Form Column -->
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(88,237,162,0.2); border-radius: 20px; padding: 36px;">
              <h3 style="color: #ffffff; font-size: 1.45rem; font-weight: 700; margin-bottom: 8px;">Request a Confidential Callback</h3>
              <p style="color: #BAC8C6; font-size: 0.92rem; margin-bottom: 24px;">Our doctor or counselor will call you back within 15 minutes.</p>

              <form onsubmit="event.preventDefault(); document.getElementById('cb-success').style.display='block'; this.reset();" style="display: flex; flex-direction: column; gap: 16px;">
                <div>
                  <label style="color: #BAC8C6; font-size: 0.82rem; font-weight: 600; text-transform: uppercase;">Your Name</label>
                  <input type="text" required placeholder="Enter your name" style="width: 100%; padding: 12px 16px; border-radius: 8px; background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.15); color: #fff; margin-top: 6px; outline: none; box-sizing: border-box;"/>
                </div>
                <div>
                  <label style="color: #BAC8C6; font-size: 0.82rem; font-weight: 600; text-transform: uppercase;">Contact Number</label>
                  <input type="tel" required placeholder="Enter 10-digit phone number" style="width: 100%; padding: 12px 16px; border-radius: 8px; background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.15); color: #fff; margin-top: 6px; outline: none; box-sizing: border-box;"/>
                </div>
                <div>
                  <label style="color: #BAC8C6; font-size: 0.82rem; font-weight: 600; text-transform: uppercase;">Care Required</label>
                  <select style="width: 100%; padding: 12px 16px; border-radius: 8px; background: #013126; border: 1px solid rgba(255,255,255,0.15); color: #fff; margin-top: 6px; outline: none; box-sizing: border-box;">
                    <option>Alcohol De-Addiction Treatment</option>
                    <option>Drug De-Addiction Treatment</option>
                    <option>Psychiatric Care &amp; Counseling</option>
                    <option>Detoxification &amp; Medical Support</option>
                    <option>Individual Counseling</option>
                    <option>Family Counseling &amp; Guidance</option>
                    <option>Yoga, Meditation &amp; Brain Gym</option>
                    <option>Immediate 24/7 Admission</option>
                  </select>
                </div>
                <button type="submit" style="background: #00856F; color: #fff; border: none; padding: 14px; border-radius: 50px; font-weight: 700; font-size: 1rem; cursor: pointer; margin-top: 10px; transition: background 0.3s;" onmouseover="this.style.background='#039775'" onmouseout="this.style.background='#00856F'">
                  Request Free Callback
                </button>
                <div id="cb-success" style="display: none; background: rgba(88,237,162,0.15); border: 1px solid #58EDA2; color: #58EDA2; padding: 12px; border-radius: 8px; font-size: 0.88rem; text-align: center;">
                  ✓ Thank you. Our counselor will call you confidentially shortly.
                </div>
              </form>

              <!-- Interactive Google Map Embed -->
              <div style="margin-top: 24px; border-radius: 12px; overflow: hidden; height: 180px; border: 1px solid rgba(88,237,162,0.2);">
                <iframe 
                  src="https://maps.google.com/maps?q=Vadipatti,+Madurai,+Tamil+Nadu&t=&z=13&ie=UTF8&iwloc=&output=embed" 
                  width="100%" 
                  height="100%" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy" 
                  referrerpolicy="no-referrer-when-downgrade">
                </iframe>
              </div>

              <!-- Direct Google Maps Link Card -->
              <div style="margin-top: 12px;">
                <a href="https://maps.google.com/?q=Vadipatti,+Madurai" target="_blank" rel="noopener" style="display: flex; align-items: center; justify-content: space-between; text-decoration: none; color: #fff; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08);">
                  <span style="font-size: 0.85rem; font-weight: 600;">📍 Open Vadipatti, Madurai in Google Maps App</span>
                  <span style="color: #58EDA2; font-weight: bold;">&rarr;</span>
                </a>
              </div>

            </div>

          </div>

        </div>
      </section>

    </main>

    <!-- COMPREHENSIVE FOOTER -->
    <footer class="n4-footer_wrap n4-u-theme-light" style="background-color: #001A14; color: #BAC8C6; padding: 80px 24px 40px 24px; border-top: 1px solid rgba(255,255,255,0.08);">
      <div style="max-width: 1300px; margin: 0 auto;">
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 40px; margin-bottom: 60px;">
          
          <!-- Column 1: Brand Info -->
          <div>
            <div style="margin-bottom: 18px;">
              <img src="akrura-logo-white.svg" alt="AKRURA DE ADDICTION &amp; REHABILITATION CENTRE Logo" style="height: 48px; width: auto;"/>
            </div>
            <p style="font-size: 0.88rem; line-height: 1.7; color: #BAC8C6; margin-bottom: 18px;">
              <strong>AKRURA DE ADDICTION &amp; REHABILITATION CENTRE</strong> is a trusted centre for Alcohol, Drug De-addiction, and Psychiatric Care located at Vadipatti, Madurai.
            </p>
            <div style="font-size: 0.85rem; color: #58EDA2; font-weight: 700;">
              24/7 Care &amp; Admission Available
            </div>
          </div>

          <!-- Column 2: Treatments -->
          <div>
            <h4 style="color: #ffffff; font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 18px;">Treatments</h4>
            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
              <li><a href="#services" style="color: inherit; text-decoration: none;">1. Alcohol De-Addiction</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">2. Drug De-Addiction</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">3. Psychiatric Care &amp; Counseling</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">4. Detoxification &amp; Medical Support</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">5. Individual Counseling</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">6. Family Counseling</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">7. Yoga, Meditation &amp; Brain Gym</a></li>
              <li><a href="#services" style="color: inherit; text-decoration: none;">8. Aftercare &amp; Rehabilitation</a></li>
            </ul>
          </div>

          <!-- Column 3: Quick Links -->
          <div>
            <h4 style="color: #ffffff; font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 18px;">Navigation</h4>
            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
              <li><a href="#about" style="color: inherit; text-decoration: none;">About the Centre</a></li>
              <li><a href="#facilities" style="color: inherit; text-decoration: none;">Campus &amp; Facilities</a></li>
              <li><a href="#why-us" style="color: inherit; text-decoration: none;">Why Akrura</a></li>
              <li><a href="#service-area" style="color: inherit; text-decoration: none;">Tamil Nadu Service Area</a></li>
              <li><a href="#contact" style="color: inherit; text-decoration: none;">Contact Details</a></li>
              <li><a href="tel:9384190971" style="color: #58EDA2; text-decoration: none; font-weight: 700;">24/7 Helpline: 93841 90971</a></li>
            </ul>
          </div>

          <!-- Column 4: Contact & Socials -->
          <div>
            <h4 style="color: #ffffff; font-size: 1rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 18px;">Connect With Us</h4>
            <p style="font-size: 0.88rem; line-height: 1.6; margin-bottom: 14px;">
              5/96/13, Street-3, Mettuperumal Nagar, Vadipatti, Madurai - 625218
            </p>
            <div style="margin-bottom: 12px;">
              <a href="tel:9384190971" style="color: #ffffff; font-weight: 700; font-size: 1.1rem; text-decoration: none;">📞 93841 90971</a>
            </div>
            <div style="display: flex; gap: 12px; margin-top: 14px;">
              <a href="https://www.instagram.com/akrura_de_addiction" target="_blank" rel="noopener" style="color: #58EDA2; text-decoration: none; font-weight: 600; font-size: 0.85rem;">Instagram</a>
              <span style="color: rgba(255,255,255,0.2);">|</span>
              <a href="https://www.facebook.com/share/1KWuSgFxir/" target="_blank" rel="noopener" style="color: #58EDA2; text-decoration: none; font-weight: 600; font-size: 0.85rem;">Facebook</a>
              <span style="color: rgba(255,255,255,0.2);">|</span>
              <a href="https://wa.me/919384190971" target="_blank" rel="noopener" style="color: #25D366; text-decoration: none; font-weight: 600; font-size: 0.85rem;">WhatsApp</a>
            </div>
          </div>

        </div>

        <!-- Bottom Copyright -->
        <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 0.8rem; color: #7F9390;">
          <div>
            &copy; <span id="cr-year">2026</span> AKRURA DE ADDICTION &amp; REHABILITATION CENTRE. All Rights Reserved. Vadipatti, Madurai, Tamil Nadu.
          </div>
          <div>
            24/7 Helpline: <a href="tel:9384190971" style="color: #BAC8C6; text-decoration: underline;">+91 93841 90971</a>
          </div>
        </div>

      </div>
    </footer>

  </div>

  <!-- Interactive Scripts & Hero Animation Controller -->
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      // 1. Current Year
      const yearEl = document.getElementById("cr-year");
      if (yearEl) yearEl.textContent = new Date().getFullYear();

      // 2. Banner Close
      const bannerClose = document.querySelector(".web-banner-close");
      const bannerWrapper = document.querySelector(".web-banner-wrapper");
      if (bannerClose && bannerWrapper) {
        bannerClose.addEventListener("click", function(e) {
          e.preventDefault();
          bannerWrapper.style.transition = "all 0.3s ease";
          bannerWrapper.style.maxHeight = "0";
          bannerWrapper.style.opacity = "0";
          bannerWrapper.style.overflow = "hidden";
          setTimeout(() => bannerWrapper.remove(), 300);
        });
      }

      // 3. Dropdowns
      const dropdowns = document.querySelectorAll(".dropdown");
      dropdowns.forEach(function(dp) {
        const toggle = dp.querySelector(".w-dropdown-toggle");
        const list = dp.querySelector(".w-dropdown-list");
        if (!toggle || !list) return;

        dp.addEventListener("mouseenter", function() {
          if (window.innerWidth > 991) {
            list.classList.add("w--open");
            list.style.opacity = "1";
            list.style.visibility = "visible";
          }
        });
        dp.addEventListener("mouseleave", function() {
          if (window.innerWidth > 991) {
            list.classList.remove("w--open");
            list.style.opacity = "";
            list.style.visibility = "";
          }
        });
        toggle.addEventListener("click", function(e) {
          e.preventDefault();
          const open = list.classList.toggle("w--open");
          list.style.opacity = open ? "1" : "";
          list.style.visibility = open ? "visible" : "";
        });
      });

      // 4. Mobile Menu Toggle
      const menuBtn = document.querySelector(".header-nav-btn, .menu-button");
      const navMenu = document.querySelector(".nav-menu-4");
      if (menuBtn && navMenu) {
        menuBtn.addEventListener("click", function(e) {
          e.preventDefault();
          const isOpen = navMenu.classList.toggle("w--open");
          if (isOpen) {
            navMenu.style.display = "flex";
            navMenu.style.flexDirection = "column";
            navMenu.style.position = "absolute";
            navMenu.style.top = "100%";
            navMenu.style.left = "0";
            navMenu.style.width = "100%";
            navMenu.style.backgroundColor = "#013126";
            navMenu.style.padding = "24px";
            navMenu.style.boxShadow = "0 10px 30px rgba(0,0,0,0.5)";
          } else {
            navMenu.style.display = "";
          }
        });
      }

      // 5. Hero Looping Background & Pill Text Animation
      const heroPills = [
        { text: "Alcohol & Drug De-Addiction", color: "#FFC728" },
        { text: "Psychiatric Care & Counseling", color: "#039775" },
        { text: "Yoga, Meditation & Brain Gym", color: "#2EDAF1" },
        { text: "Recover with Dignity & Rejoin Family", color: "#B69EFF" }
      ];
      let currentPillIdx = 0;
      const pillCircle = document.querySelector("[data-hero-pill-circle]");
      const pillText = document.querySelector("[data-hero-pill-text]");
      const heroBgs = document.querySelectorAll("[data-hero-bg]");

      if (pillCircle && pillText && heroBgs.length > 0) {
        setInterval(function() {
          currentPillIdx = (currentPillIdx + 1) % heroPills.length;
          const conf = heroPills[currentPillIdx];
          
          // Animate text and circle
          pillText.style.opacity = "0";
          setTimeout(function() {
            pillText.textContent = conf.text;
            pillCircle.style.backgroundColor = conf.color;
            pillText.style.opacity = "1";
          }, 250);

          // Animate background cross-fade
          heroBgs.forEach((bg, idx) => {
            bg.style.opacity = idx === currentPillIdx ? "1" : "0";
          });
        }, 4000);
      }
    });
  </script>
</body>
</html>
"""
    with open(r'e:\Clients\Website\From Sathesh bro\akura\index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Akrura index.html compiled successfully. File size:", len(html_content))

if __name__ == "__main__":
    generate_akrura_html()
