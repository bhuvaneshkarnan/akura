"""
Compiles the Akrura De Addiction & Rehabilitation Centre website
directly into the authentic, replicated Maven Clinic DOM structure,
preserving 100% of Maven Clinic's layout, Webflow classes, animations,
typography (Ivarheadline, Domaine Display, Helvetica Now Text, Montserrat),
and color tokens.
"""

import re
import os
import urllib.parse
from bs4 import BeautifulSoup, NavigableString

# 1. Read original Maven Clinic HTML
with open(r'C:\Users\bhuva\.gemini\antigravity\brain\5e1c917c-a072-42e2-8abb-955a855564b1\.system_generated\steps\3\content.md', 'r', encoding='utf-8') as f:
    raw_text = f.read()

start_idx = raw_text.find('<!DOCTYPE html>')
if start_idx == -1:
    raise ValueError("<!DOCTYPE html> not found in content.md")

html = raw_text[start_idx:]

# 2. Localize Stylesheets and Favicons
html = re.sub(
    r'<link href="[^"]*maven-clinic\.shared[^"]*"[^>]*>',
    '<link href="shared.min.css" rel="stylesheet" type="text/css"/>',
    html
)
html = re.sub(
    r'<link href="[^"]*maven-clinic\.[0-9a-f]+\.[0-9a-f]+\.opt\.min\.css"[^>]*>',
    '<link href="page.min.css" rel="stylesheet" type="text/css"/>\n<link href="swiper-bundle.min.css" rel="stylesheet" type="text/css"/>',
    html
)
html = html.replace('5fb2b678e994734019d950db_fav-icon.png', 'favicon.png')

# 3. Clean trackers and analytics
html = re.sub(r'<!-- Ketch -->.*?<!-- end Ketch -->', '', html, flags=re.DOTALL)
html = re.sub(r'<script[^>]*intellimize.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = re.sub(r'<link[^>]*intellimize.*?>', '', html, flags=re.IGNORECASE)
html = re.sub(r'<script[^>]*gtm.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
html = re.sub(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', '', html, flags=re.DOTALL)
html = re.sub(r'<!-- Google Tag Manager \(noscript\) -->.*?<!-- End Google Tag Manager \(noscript\) -->', '', html, flags=re.DOTALL)

# 4. Remove duplicate script tags at bottom
html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/swiper@8/swiper-bundle\.min\.js"[^>]*></script>', '', html)
html = re.sub(r'<script src="https://unpkg\.com/@rive-app/canvas"[^>]*></script>', '', html)
html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/gsap@3\.13\.0/dist/gsap\.min\.js"></script>', '', html)
html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/gsap@3\.13\.0/dist/ScrollTrigger\.min\.js"></script>', '', html)
html = re.sub(r'<script src="https://cdn\.jsdelivr\.net/npm/gsap@3\.13\.0/dist/SplitText\.min\.js"></script>', '', html)

# 5. Core Libraries & SplitText Polyfill in Head
core_head = """
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
  <style>
    html {
      scroll-behavior: smooth;
    }

    /* Fixed Navigation Bar */
    .navbar.nav-v2 {
      position: fixed !important;
      top: 14px !important;
      left: 0 !important;
      right: 0 !important;
      width: 92% !important;
      max-width: 1240px !important;
      margin: 0 auto !important;
      z-index: 9999 !important;
      padding: 0 !important;
    }

    /* Spacious, Airy Floating Header Pill - Clean & Minimal without Shadow */
    .content__nav {
      background-color: #ffffff !important;
      border-radius: 8px !important;
      padding: 14px 28px !important;
      min-height: 68px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      box-shadow: none !important;
      border: 1px solid rgba(0, 0, 0, 0.08) !important;
      box-sizing: border-box !important;
    }

    .container__navigation {
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      width: 100% !important;
      gap: 36px !important;
      min-height: 40px !important;
    }

    /* Logo Branding */
    .branding__maven {
      display: flex !important;
      align-items: center !important;
      flex-shrink: 0 !important;
      padding: 0 !important;
      margin: 0 !important;
      text-decoration: none !important;
    }

    .branding__maven img.nav-logo-lg {
      height: 38px !important;
      width: auto !important;
      max-width: 210px !important;
      display: block !important;
    }

    /* Desktop Nav Menu Links */
    @media (min-width: 992px) {
      .header-nav-btn {
        display: none !important;
      }

      .nav-menu-4 {
        display: flex !important;
        align-items: center !important;
        gap: 32px !important;
        margin: 0 !important;
        padding: 0 !important;
        background: transparent !important;
        box-shadow: none !important;
        overflow: visible !important;
        position: static !important;
        width: auto !important;
      }

      .nav-menu-4 .nav__link-item {
        font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
        font-size: 15.5px !important;
        font-weight: 500 !important;
        color: #1E293B !important;
        padding: 6px 4px !important;
        text-decoration: none !important;
        letter-spacing: 0.2px !important;
        line-height: 1.2 !important;
        transition: color 0.2s ease !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
      }

      .nav-menu-4 .nav__link-item:hover {
        color: #0066CC !important;
      }

      .nav-menu-4 .nav__link-item.w--current {
        color: #0066CC !important;
        border-bottom: 2px solid #0066CC !important;
      }

      .mobile-menu-cta-wrap {
        display: none !important;
      }
    }

    /* Right Block & Book Consultation Button */
    .nav__right-block {
      display: flex !important;
      align-items: center !important;
      flex-shrink: 0 !important;
    }

    .header__btn-block {
      display: flex !important;
      align-items: center !important;
      flex-shrink: 0 !important;
      margin-left: 8px !important;
    }

    .header__btn-block .cta__green.mr-0 {
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-size: 14.5px !important;
      font-weight: 600 !important;
      background-color: #0066CC !important;
      color: #ffffff !important;
      height: 42px !important;
      line-height: 42px !important;
      padding: 0 24px !important;
      border-radius: 4px !important;
      text-decoration: none !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      letter-spacing: 0.2px !important;
      white-space: nowrap !important;
      box-shadow: none !important;
      transition: background-color 0.2s ease, transform 0.15s ease !important;
      margin: 0 !important;
    }

    .header__btn-block .cta__green.mr-0:hover {
      background-color: #0052A3 !important;
      transform: translateY(-1px) !important;
    }

    /* Footer Clean, Minimal & High-Contrast Typography */
    footer#contact,
    .n4-footer_wrap,
    .n4-footer_inner {
      background-color: #0B1E36 !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
    }

    .n4-footer_top {
      display: flex !important;
      justify-content: space-between !important;
      align-items: flex-start !important;
      gap: 48px !important;
    }

    .n4-footer_content_left {
      display: grid !important;
      grid-template-columns: repeat(4, minmax(160px, 1fr)) !important;
      gap: 36px !important;
      flex: 1 !important;
    }

    .footer-col-title,
    .n4-footer_content_list .n4-footer_link_text.n4-u-color-primary-green950 {
      color: #38BDF8 !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-weight: 700 !important;
      font-size: 13.5px !important;
      text-transform: uppercase !important;
      letter-spacing: 1.2px !important;
      margin-bottom: 14px !important;
      display: block !important;
    }

    .n4-footer_content_list .n4-footer_link_wrap .n4-footer_link_text,
    .n4-footer_link_text {
      color: rgba(255, 255, 255, 0.78) !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-size: 14.5px !important;
      line-height: 1.8 !important;
      font-weight: 400 !important;
      transition: color 0.2s ease !important;
    }

    .n4-footer_content_list .n4-footer_link_wrap:hover .n4-footer_link_text,
    .n4-footer_link_wrap:hover .n4-footer_link_text {
      color: #58EDA2 !important;
    }

    .n4-footer_content_right {
      display: flex !important;
      flex-direction: column !important;
      gap: 16px !important;
      min-width: 220px !important;
    }

    .n4-footer_bottom_rating_text {
      color: rgba(255, 255, 255, 0.9) !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-size: 13.5px !important;
      font-weight: 500 !important;
    }

    .n4-footer_bottom_text,
    .n4-footer_bottom_text * {
      color: rgba(255, 255, 255, 0.6) !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-size: 13px !important;
    }

    .n4-footer_bottom_link_list a .n4-footer_link_text {
      color: rgba(255, 255, 255, 0.6) !important;
      font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', -apple-system, BlinkMacSystemFont, Arial, sans-serif !important;
      font-size: 13px !important;
      transition: color 0.2s ease !important;
    }

    .n4-footer_bottom_link_list a:hover .n4-footer_link_text {
      color: #38BDF8 !important;
    }

    .n4-footer_bottom_content {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
    }
    .n4-footer_bottom_body2 {
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
      width: 100% !important;
    }
    .n4-footer_bottom_text {
      text-align: center !important;
      width: 100% !important;
    }

    @media (max-width: 991px) {
      .navbar.nav-v2 {
        width: 94% !important;
        max-width: 100% !important;
        top: 10px !important;
      }

      .content__nav {
        position: relative !important;
        padding: 8px 14px !important;
        min-height: 54px !important;
        border-radius: 12px !important;
        background-color: #ffffff !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
        border: 1px solid rgba(0, 0, 0, 0.08) !important;
      }

      .container__navigation {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        gap: 6px !important;
      }

      .branding__maven {
        flex-shrink: 0 !important;
      }

      .branding__maven img.nav-logo-lg {
        height: 28px !important;
        width: auto !important;
        max-width: 145px !important;
      }

      .nav__right-block {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
      }

      .header__btn-block .cta__green.mr-0 {
        height: 36px !important;
        line-height: 36px !important;
        padding: 0 12px !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        border-radius: 6px !important;
        margin: 0 !important;
        white-space: nowrap !important;
      }

      .header-nav-btn {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 38px !important;
        height: 38px !important;
        cursor: pointer !important;
        padding: 0 !important;
        margin: 0 !important;
        background: transparent !important;
        border: none !important;
      }

      .menu-button {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 38px !important;
        height: 38px !important;
        padding: 0 !important;
        margin: 0 !important;
      }

      .menu-icon-v2 {
        width: 22px !important;
        height: 16px !important;
        position: relative !important;
      }

      /* Mobile Nav Menu Dropdown */
      .nav-menu-4 {
        display: none !important;
        position: absolute !important;
        top: calc(100% + 8px) !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        background-color: #0B1E36 !important;
        border-radius: 12px !important;
        padding: 16px 20px !important;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        box-sizing: border-box !important;
        z-index: 10000 !important;
        margin: 0 !important;
      }

      .nav-menu-4.is-open {
        display: flex !important;
        flex-direction: column !important;
        animation: mobileNavFade 0.2s ease forwards !important;
      }

      .nav-menu-4.is-open .nav__link-item {
        font-family: Helveticanowdisplay, 'Helvetica Now Display', 'Helvetica Now Text', Arial, sans-serif !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        color: #ffffff !important;
        padding: 13px 4px !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        text-decoration: none !important;
        transition: color 0.2s ease, padding-left 0.2s ease !important;
        background: transparent !important;
      }

      .nav-menu-4.is-open .nav__link-item:hover,
      .nav-menu-4.is-open .nav__link-item:active {
        color: #38BDF8 !important;
        padding-left: 6px !important;
      }

      .nav-menu-4.is-open .mobile-menu-cta-wrap {
        display: flex !important;
        flex-direction: column !important;
        gap: 10px !important;
        margin-top: 14px !important;
        padding-top: 14px !important;
        border-top: 1px solid rgba(255, 255, 255, 0.15) !important;
      }

      .nav-menu-4.is-open .mobile-menu-cta-wrap a {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        border-radius: 6px !important;
        padding: 11px 16px !important;
        font-family: Helveticanowdisplay, Arial, sans-serif !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
      }

      .n4-footer_top {
        flex-direction: column !important;
        gap: 32px !important;
      }
      .n4-footer_content_left {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 24px !important;
      }
    }

    @keyframes mobileNavFade {
      from {
        opacity: 0;
        transform: translateY(-8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }


    /* Blue Theme Global Overrides */
    .cta__green,
    .cta__green.mr-0 {
      background-color: #0066CC !important;
    }
    .cta__green:hover,
    .cta__green.mr-0:hover {
      background-color: #0052A3 !important;
    }
    .cta__outlined {
      color: #0066CC !important;
      outline-color: #0066CC !important;
    }
    ::selection {
      background: #0066CC !important;
      color: #ffffff !important;
    }
    .w-slider-dot.w-active::before {
      background-color: #0066CC !important;
    }
    .web-banner.background-color-dark-green {
      background-color: #F0F9FF !important;
    }
    .banner-text p, .banner-text a, .web-banner-close .button-close {
      color: #0B1E36 !important;
    }
    .video-placeholder-normal p.video-placeholder-text-normal {
      border-color: #0066CC !important;
      background-color: #0066CC !important;
    }
    .w-tab-link.w--current {
      color: #0066CC !important;
    }
    .w-tab-link.w--current::after {
      background-color: #0066CC !important;
    }

    @media (max-width: 480px) {
      .branding__maven img.nav-logo-lg {
        height: 24px !important;
        max-width: 120px !important;
      }
      .header__btn-block .cta__green.mr-0 {
        padding: 0 9px !important;
        font-size: 11.5px !important;
        height: 32px !important;
        line-height: 32px !important;
      }
      .n4-footer_content_left {
        grid-template-columns: 1fr !important;
      }
    }
  </style>
"""
html = html.replace('</head>', core_head + '\n</head>')

# 6. Parse DOM with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Page Title and Meta
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "Akrura De Addiction & Rehabilitation Centre | Vadipatti, Madurai - 24/7 Care"

for meta in soup.find_all('meta'):
    name = meta.get('name', '').lower()
    prop = meta.get('property', '').lower()
    if name == 'description' or prop == 'og:description' or prop == 'twitter:description' or name == 'twitter:description':
        meta['content'] = "Akrura De Addiction & Rehabilitation Centre in Vadipatti, Madurai is a trusted centre for Alcohol, Drug De-addiction and Psychiatric Care. Serving All Over Tamil Nadu including Chennai, Erode, Salem, Tiruppur, Coimbatore. Call 93841 90971."
    if prop == 'og:title' or prop == 'twitter:title' or name == 'twitter:title':
        meta['content'] = "Akrura De Addiction & Rehabilitation Centre | Vadipatti, Madurai - 24/7 Care"

# 7. Announcement Bar
announcement_text = soup.find(class_='web-banner-text')
if announcement_text:
    announcement_text.string = "24/7 Confidential Helpline & Emergency Admissions Across Tamil Nadu: Call +91 93841 90971"

announcement_btn = soup.find(class_='web-banner-button')
if announcement_btn:
    announcement_btn['href'] = "tel:9384190971"
    announcement_btn_text = announcement_btn.find(class_='web-banner-button-text')
    if announcement_btn_text:
        announcement_btn_text.string = "Call Now"

# 8. Navbar Logos
nav_brand = soup.find('a', class_='branding__maven')
if nav_brand:
    nav_brand['href'] = "#"
    nav_brand['aria-label'] = "Akrura De Addiction & Rehabilitation Centre Home"
    lg_img = nav_brand.find('img', class_='nav-logo-lg')
    if lg_img:
        lg_img['src'] = "akrura-logo-nav.svg"
        lg_img['alt'] = "Akrura De Addiction & Rehabilitation Centre"
        lg_img['style'] = "height: 38px; width: auto; max-width: 210px; display: block;"
    sm_img = nav_brand.find('img', class_='nav-logo-sm')
    if sm_img:
        sm_img['src'] = "akrura-logo-icon.svg"
        sm_img['alt'] = "Akrura Icon"
        sm_img['style'] = "width: 36px; height: 36px;"

# 9. Navbar Links & Buttons (Home, About, Services, Contact, Book consultation)
nav_menu = soup.find('nav', class_='nav-menu-4')
if nav_menu:
    nav_menu.clear()
    menu_items = [
        ("Home", "#home"),
        ("About", "#about"),
        ("Services", "#services"),
        ("Contact", "#contact")
    ]
    for label, target in menu_items:
        a_link = soup.new_tag('a', attrs={
            'href': target,
            'class': 'nav__link-item cc-nav w-nav-link'
        })
        a_link.string = label
        nav_menu.append(a_link)

    mobile_cta = BeautifulSoup("""
    <div class="mobile-menu-cta-wrap">
      <a href="tel:9384190971" style="background: #0066CC; color: #ffffff;">
        📞 Call 24/7 Helpline: 93841 90971
      </a>
      <a href="https://wa.me/919384190971" target="_blank" style="background: #25D366; color: #ffffff;">
        💬 Chat on WhatsApp
      </a>
    </div>
    """, 'html.parser')
    nav_menu.append(mobile_cta)

# Header Button Block: Remove Login, change Book a demo -> Book consultation
btn_block = soup.find('div', class_='header__btn-block')
if btn_block:
    login_btn = btn_block.find('a', class_='cta__outlined')
    if login_btn:
        login_btn.decompose()

    book_btn = btn_block.find('a', class_='mr-0')
    if book_btn:
        book_btn.clear()
        book_btn.append("Book consultation")
        book_btn['href'] = "#contact"
        if 'style' in book_btn.attrs:
            del book_btn['style']


# 10. Hero Section
hero = soup.find('header', class_='n4-hero_main_wrap')
if hero:
    hero['id'] = "home"
    # Pill Text

    pill_text = hero.find(class_='n4-hero_main_pill_text')
    if pill_text:
        pill_text.string = "Vadipatti, Madurai • 24/7 Care • Serving All Tamil Nadu"

    # Heading
    heading_wrap = hero.find(class_='n4-hero_main_heading')
    if heading_wrap:
        heading_wrap.clear()
        h1 = soup.new_tag('h1')
        h1.append("Evidence-based de-addiction and ")
        h1.append(soup.new_tag('br'))
        h1.append("psychiatric ")
        strong = soup.new_tag('strong')
        strong.string = "care"
        h1.append(strong)
        heading_wrap.append(h1)

    # Subhead
    hero_text = hero.find(class_='n4-hero_main_text')
    if hero_text:
        hero_text.string = "Akrura De Addiction & Rehabilitation Centre is a trusted centre for Alcohol, Drug De-addiction and Psychiatric Care. Located at Vadipatti, Madurai, we serve patients from All Over Tamil Nadu including Chennai, Erode, Salem, Tiruppur, Coimbatore."

    # Hero Buttons
    btn_wraps = hero.find_all(class_='n4-btn_main_wrap')
    if len(btn_wraps) >= 1:
        a1 = btn_wraps[0].find('a')
        if a1: a1['href'] = "tel:9384190971"
        t1 = btn_wraps[0].find(class_='n4-btn_main_text')
        if t1: t1.string = "Call 24/7 Helpline: 93841 90971"
    if len(btn_wraps) >= 2:
        a2 = btn_wraps[1].find('a')
        if a2: a2['href'] = "#services"
        t2 = btn_wraps[1].find(class_='n4-btn_main_text')
        if t2: t2.string = "Explore 8 Services"

    # Hero Background Images
    hero_bgs = hero.find_all(attrs={'data-hero-bg': True})
    hero_imgs = ["hero-bg-1.jpg", "hero-bg-2.jpg", "hero-bg-3.jpg", "hero-bg-4.jpg"]
    for i, bg in enumerate(hero_bgs):
        if i < len(hero_imgs):
            bg['src'] = hero_imgs[i]
            bg['srcset'] = f"{hero_imgs[i]} 800w, {hero_imgs[i]} 1600w"
            bg['style'] = "object-fit: cover; opacity: 0.35;"

# 11. Section 1: Services Slider (section.n4-section_wrap)
sec1 = soup.find_all('section')[0]
sec1['id'] = "services"

services_heading = sec1.find(class_='n4-services_heading')
if services_heading:
    services_heading.clear()
    p1 = soup.new_tag('p')
    p1.string = "De-addiction care designed for individuals & families that's personal"
    p2 = soup.new_tag('p')
    p2.append(" ")
    strong_proven = soup.new_tag('strong', attrs={'class': 'w-variant-e6e6ef85-7f68-b628-dc28-14eb31cddc1a'})
    strong_proven.string = "and proven"
    p2.append(strong_proven)
    services_heading.append(p1)
    services_heading.append(p2)

services_subtext = sec1.find(class_='n4-services_text')
if services_subtext:
    services_subtext.string = "Trusted across Tamil Nadu for alcohol, drug de-addiction, and psychiatric care with 24/7 medical support and compassionate rehabilitation."

services_data = [
    {
        "title": "Alcohol De-Addiction Treatment",
        "eyebrow": "Inpatient Medical Care • 24/7 Monitoring",
        "text": "Medically managed withdrawal, 24/7 physician monitoring, anti-craving protocols, and structured cognitive therapies to safely overcome alcohol dependency.",
        "img": "service-alcohol.jpg"
    },
    {
        "title": "Drug De-Addiction Treatment",
        "eyebrow": "Substance Recovery • Evidence-Based",
        "text": "Specialized clinical rehabilitation programs for prescription drugs, opioids, cannabis, and chemical substances with personalized recovery plans.",
        "img": "service-drugs.jpg"
    },
    {
        "title": "Psychiatric Care & Counseling",
        "eyebrow": "Dual-Diagnosis & Mental Health",
        "text": "Comprehensive psychiatric assessments, mood stabilization, depression and anxiety management, and dedicated clinical counseling support.",
        "img": "service-psychiatric.jpg"
    },
    {
        "title": "Detoxification & Medical Support",
        "eyebrow": "24/7 Physician & Nursing Care",
        "text": "Safe, continuous medical detoxification with round-the-clock doctor care, vital signs monitoring, intravenous therapy, and supportive medication.",
        "img": "service-detox.jpg"
    },
    {
        "title": "Individual Counseling",
        "subtitle": "Confidential One-on-One Psychological Care",
        "eyebrow": "THERAPY",
        "text": "One-on-one psychological counseling, Cognitive Behavioral Therapy (CBT), motivational interviewing, and trauma-informed healing.",
        "img": "facility-counseling.jpg"
    },
    {
        "title": "Family Counseling",
        "subtitle": "Healing Relationships & Rebuilding Trust",
        "eyebrow": "FAMILY",
        "text": "Healing strained relationships, family therapy sessions, codependency guidance, and preparing a loving home environment for recovery.",
        "img": "service-family.jpg"
    },
    {
        "title": "Yoga, Meditation, Exercise & Brain Gym",
        "subtitle": "Mind Refreshment & Holistic Rejuvenation",
        "eyebrow": "HOLISTIC",
        "text": "Daily morning pranayama, guided meditation, brain gym neuroplasticity exercises, and physical fitness to rejuvenate mind and body.",
        "img": "service-yoga.jpg"
    }
]

slides = sec1.find_all(class_='swiper-slide')
for i in range(min(len(slides), len(services_data))):
    data = services_data[i]
    sl = slides[i]
    bg_img = sl.find('img', class_='n4-services_card_bg')
    if bg_img:
        bg_img['src'] = data['img']
        bg_img['srcset'] = f"{data['img']} 500w, {data['img']} 800w, {data['img']} 1200w"

    h = sl.find(['h3', 'h4'], class_=lambda c: c and ('heading' in c or 'title' in c))
    if h: h.string = data['title']

    eb = sl.find(class_='n4-g_eyebrow_text')
    if eb: eb.string = data['eyebrow']

    sub = sl.find(class_='n4-services_card_subtitle')
    if sub and 'subtitle' in data: sub.string = data['subtitle']

    p = sl.find('p', class_='n4-services_card_text')
    if p: p.string = data['text']

    btn_text = sl.find(class_='n4-btn_main_text')
    if btn_text: btn_text.string = "Helpline: 93841 90971"
    btn_a = sl.find('a', class_='n4-g_clickable_wrap')
    if btn_a: btn_a['href'] = "tel:9384190971"

# 12. Section 2: Bento Grid (section.n4-features_wrap)
sec2 = soup.find('section', class_='n4-features_wrap')
if sec2:
    sec2['id'] = "about"
    h2 = sec2.find('h2')
    if h2: h2.string = "24/7 medical care, personalized counseling, & family healing—all in one place."
    
    subhead = sec2.find('p', class_='n4-features_text')
    if subhead:
        subhead.string = "Akrura De Addiction & Rehabilitation Centre brings clinical medical precision, psychiatric expertise, yoga, meditation, and mind refreshment to patients from across Tamil Nadu."

    bento_headings = sec2.find_all(class_='n4-features_card_heading')
    if len(bento_headings) >= 1:
        bento_headings[0].string = "Trusted de-addiction centre, serving patients from All Over Tamil Nadu"
    if len(bento_headings) >= 2:
        bento_headings[1].string = "Your trusted partner in high-quality, 24/7/365 addiction recovery"
    if len(bento_headings) >= 3:
        bento_headings[2].string = "Multi-disciplinary team: Psychiatrists, Doctors, Counselors & Yoga Gurus"
    if len(bento_headings) >= 4:
        bento_headings[3].string = "Evidence-based clinical recovery with dignity & family reunification"
    if len(bento_headings) >= 5:
        bento_headings[4].string = "Centrally located at Vadipatti, Madurai for rapid access across Tamil Nadu"
    if len(bento_headings) >= 6:
        bento_headings[5].string = "Helping every person to recover with dignity and rejoin their family"

    # Update specialty flip card labels in Bento Box
    box_texts = sec2.find_all(class_='n4-featured_card_box_text')
    specialties = ["Psychiatrists", "Clinical Psychologists", "Addiction Counselors"]
    for i in range(min(len(box_texts), len(specialties))):
        box_texts[i].string = specialties[i]

# 13. Section 3: Stats Section (section.n4-stats_wrap)
sec3 = soup.find('section', class_='n4-stats_wrap')
if sec3:
    h_stat = sec3.find(class_='n4-stats_heading')
    if h_stat:
        h_stat.clear()
        h2_s = soup.new_tag('h2')
        h2_s.append("Restoring health by ")
        h2_s.append(soup.new_tag('br'))
        h2_s.append("providing ")
        strong_s = soup.new_tag('strong')
        strong_s.string = "dignified care"
        h2_s.append(strong_s)
        h_stat.append(h2_s)

    p_stat = sec3.find(class_='n4-stats_text')
    if p_stat:
        p_stat.clear()
        p_s = soup.new_tag('p')
        p_s.string = "By guiding patients through evidence-based medical detox and personalized psychiatric counseling, we eliminate physical cravings, heal the mind, and reunite families."
        p_stat.append(p_s)

    stat_items = sec3.find_all(class_='n4-stats_item_wrap')
    stat_replacements = [
        ("95%", "Up to 95% completion rate in medically supported detoxification and withdrawal stabilization."),
        ("88%", "Over 88% of patients report Akrura helped them return to work and rejoin their family with dignity."),
        ("100%", "100% confidential psychiatric care, medical support, and family counseling."),
        ("24/7", "24/7 round-the-clock doctor supervision, nursing care, and emergency admissions.")
    ]
    for i in range(min(len(stat_items), len(stat_replacements))):
        num_val, text_val = stat_replacements[i]
        num_div = stat_items[i].find(class_='n4-stats_item_number')
        if num_div: num_div.string = num_val
        t_div = stat_items[i].find(class_='n4-stats_item_test')
        if t_div:
            t_div.clear()
            h3_t = soup.new_tag('h3')
            h3_t.string = text_val
            t_div.append(h3_t)

# 14. Section 4: Care Pathways Switcher (section.n4-section_wrap[3])
all_sections = soup.find_all('section')
if len(all_sections) >= 4:
    sec4 = all_sections[3]
    sec4['id'] = "service-areas"
    h2_path = sec4.find('h2')
    if h2_path:
        h2_path.string = "Personalized care pathways for every individual and family"
    p_path = sec4.find(class_='n4-industry_text')
    if p_path:
        p_path.string = "Akrura De Addiction & Rehabilitation Centre brings clinical expertise, psychiatric support, and holistic therapies to patients from all across Tamil Nadu."

    tab_links = sec4.find_all(class_='n4-industry_links_heading')
    tab_names = [
        "Alcohol Recovery",
        "Substance Rehab",
        "Psychiatric Care",
        "Family Counseling",
        "Holistic Wellness"
    ]
    for i in range(min(len(tab_links), len(tab_names))):
        tab_links[i].string = tab_names[i]

    for a_tag in sec4.find_all('a'):
        h = a_tag.get('href', '')
        if 'for-' in h or 'mavenclinic' in h:
            a_tag['href'] = "#services"

    # Change button in Section 4
    btn_s4 = sec4.find(class_='n4-btn_main_wrap')
    if btn_s4:
        a_s4 = btn_s4.find('a')
        if a_s4: a_s4['href'] = "tel:9384190971"
        t_s4 = btn_s4.find(class_='n4-btn_main_text')
        if t_s4: t_s4.string = "Admissions Helpline: 93841 90971"

# 15. Section 5: Marquee Section (section.n4-trusted_wrap)
sec5 = soup.find('section', class_='n4-trusted_wrap')
if sec5:
    subtitle = sec5.find(class_='n4-g_subtitle_text')
    if subtitle:
        subtitle.string = "Serving Patients & Families From All Over Tamil Nadu"

    # Replace logo wrappers with clean city typography pills
    marquee_list = sec5.find(class_='n4-main_marquee_list')
    if marquee_list:
        cities = ["MADURAI", "CHENNAI", "COIMBATORE", "ERODE", "SALEM", "TIRUPPUR", "DINDIGUL", "TRICHY", "TIRUNELVELI"]
        marquee_list.clear()
        for city in cities:
            badge = soup.new_tag('div', attrs={'class': 'n4-marquee_logo_wrap', 'data-marquee': 'item', 'style': 'display: flex; align-items: center; justify-content: center; padding: 0 1.5rem;'})
            span = soup.new_tag('span', style="font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif; font-size: 1.1rem; font-weight: 700; letter-spacing: 2px; color: #38BDF8; opacity: 0.9; white-space: nowrap;")
            span.string = f"•  {city}"
            badge.append(span)
            marquee_list.append(badge)

# 16. Section 6: Real Stories / Testimonials (section.n4-stories_wrap)
sec6 = soup.find('section', class_='n4-stories_wrap')
if sec6:
    h2_story = sec6.find(class_='n4-stories_heading')
    if h2_story:
        h2_story.clear()
        h2_st = soup.new_tag('h2')
        h2_st.append("Real ")
        span_st = soup.new_tag('span', style="font-style: italic;")
        span_st.string = "stories"
        h2_st.append(span_st)
        h2_st.append(" of hope, dignity & recovery")
        h2_story.append(h2_st)

    story_quotes = sec6.find_all(class_='n4-stories_tabs_quote')
    story_replacements = [
        "“Akrura gave our family a second chance. The medical detox was smooth, and the counseling helped my brother rebuild his confidence. Today, he is back at work and living alcohol-free.”",
        "“The environment at Vadipatti is calm and peaceful. The doctors, daily yoga, and mind refreshment sessions helped me regain clarity and inner peace. I am forever grateful.”",
        "“We tried multiple places, but Akrura's family counseling and dignified medical approach made all the difference. Our home is peaceful once again.”"
    ]
    for i in range(min(len(story_quotes), len(story_replacements))):
        story_quotes[i].string = story_replacements[i]

    stories_sub = sec6.find(class_='n4-stories_text')
    if stories_sub:
        stories_sub.string = "Discover how our personalized de-addiction and psychiatric care has transformed the lives of patients and families across Tamil Nadu."

    authors = sec6.find_all(class_='n4-stories_tabs_author')
    author_names = ["S. Rajesh", "M. Karthik", "P. Anandhi"]
    for i in range(min(len(authors), len(author_names))):
        authors[i].string = author_names[i]

    roles = sec6.find_all(class_='n4-stories_tabs_role')
    role_titles = ["Family Member", "Recovered Patient", "Family Member"]
    for i in range(min(len(roles), len(role_titles))):
        roles[i].string = role_titles[i]

    companies = sec6.find_all(class_='n4-stories_tabs_company')
    city_names = ["Chennai", "Coimbatore", "Madurai"]
    for i in range(min(len(companies), len(city_names))):
        companies[i].string = city_names[i]

    # Update story images
    story_imgs = sec6.find_all('img', class_='n4-stories_tabs_img')
    story_pics = ["service-family.jpg", "facility-meditation.jpg", "hero-bg-3.jpg", "service-family.jpg", "facility-meditation.jpg", "hero-bg-3.jpg"]
    for i in range(min(len(story_imgs), len(story_pics))):
        story_imgs[i]['src'] = story_pics[i]
        story_imgs[i]['srcset'] = f"{story_pics[i]} 500w, {story_pics[i]} 800w"

# 17. Insert Vadipatti Campus & Facility Gallery Section
facility_html = """
<section class="n4-section_wrap n4-u-overflow-clip" id="facilities" style="padding: 5rem 0; background-color: #FAFAF7;">
  <div class="n4-u-container" style="max-width: 1200px; margin: 0 auto; padding: 0 1.5rem;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
      <div class="n4-g_subtitle_wrap" style="display: inline-block; margin-bottom: 0.75rem;">
        <span class="n4-g_subtitle_text" style="font-size: 0.85rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #0066CC;">Vadipatti, Madurai Campus</span>
      </div>
      <h2 class="n4-g_heading n4-u-text-style-h1" style="font-family: 'Domaine Display', 'Ivarheadline', serif; font-size: 2.75rem; color: #0B1E36; margin-bottom: 1rem; line-height: 1.2;">
        Peaceful healing environment designed for complete recovery
      </h2>
      <p class="n4-u-text-style-medium" style="font-size: 1.1rem; color: #4A5568; line-height: 1.6;">
        Located at Vadipatti, Madurai (near Madurai - Dindigul Main Road), Akrura offers a serene, noise-free sanctuary surrounded by nature, equipped with modern medical support and holistic amenities.
      </p>
    </div>

    <!-- Facility Cards Grid - Clean & Minimal without Shadow -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
      <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #E2E8F0; box-shadow: none; transition: transform 0.3s ease;">
        <div style="position: relative; height: 220px; overflow: hidden;">
          <img src="facility-campus.jpg" alt="Peaceful Vadipatti Campus" style="width: 100%; height: 100%; object-fit: cover;">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(11,30,54,0.85); color: #38BDF8; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; letter-spacing: 0.5px;">Official Photo Updating Soon</span>
        </div>
        <div style="padding: 1.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B1E36; margin-bottom: 0.5rem; font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif;">Peaceful Vadipatti Campus</h3>
          <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0; font-family: Helveticanowdisplay, Arial, sans-serif;">Green, tranquil, and free from urban noise and negative triggers to help individuals focus entirely on physical and mental renewal.</p>
        </div>
      </div>

      <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #E2E8F0; box-shadow: none; transition: transform 0.3s ease;">
        <div style="position: relative; height: 220px; overflow: hidden;">
          <img src="facility-counseling.jpg" alt="Private Counseling Suites" style="width: 100%; height: 100%; object-fit: cover;">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(11,30,54,0.85); color: #38BDF8; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; letter-spacing: 0.5px;">Official Photo Updating Soon</span>
        </div>
        <div style="padding: 1.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B1E36; margin-bottom: 0.5rem; font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif;">Counseling & Therapy Suites</h3>
          <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0; font-family: Helveticanowdisplay, Arial, sans-serif;">100% confidential, comfortable consultation rooms for one-on-one psychological counseling, CBT, and restorative family therapy.</p>
        </div>
      </div>

      <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #E2E8F0; box-shadow: none; transition: transform 0.3s ease;">
        <div style="position: relative; height: 220px; overflow: hidden;">
          <img src="facility-meditation.jpg" alt="Yoga & Meditation Hall" style="width: 100%; height: 100%; object-fit: cover;">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(11,30,54,0.85); color: #38BDF8; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; letter-spacing: 0.5px;">Official Photo Updating Soon</span>
        </div>
        <div style="padding: 1.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B1E36; margin-bottom: 0.5rem; font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif;">Yoga, Meditation & Brain Gym</h3>
          <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0; font-family: Helveticanowdisplay, Arial, sans-serif;">Dedicated open-air and indoor halls for morning pranayama, guided mindfulness meditation, brain gym drills, and physical exercise.</p>
        </div>
      </div>

      <div style="background: #FFFFFF; border-radius: 12px; overflow: hidden; border: 1px solid #E2E8F0; box-shadow: none; transition: transform 0.3s ease;">
        <div style="position: relative; height: 220px; overflow: hidden;">
          <img src="service-aftercare.jpg" alt="Dining & Recreation Area" style="width: 100%; height: 100%; object-fit: cover;">
          <span style="position: absolute; top: 12px; right: 12px; background: rgba(11,30,54,0.85); color: #38BDF8; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 20px; letter-spacing: 0.5px;">Official Photo Updating Soon</span>
        </div>
        <div style="padding: 1.5rem;">
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B1E36; margin-bottom: 0.5rem; font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif;">Recreation & Mind Refreshment</h3>
          <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0; font-family: Helveticanowdisplay, Arial, sans-serif;">Clean, hygienic dining serving nutritious wholesome meals, accompanied by indoor games, library, and community peer bonding.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

sec_cta = all_sections[-1]
facility_soup = BeautifulSoup(facility_html, 'html.parser')
sec_cta.insert_before(facility_soup)

# 18. Section 7: Bottom CTA Banner
if sec_cta:
    h2_cta = sec_cta.find('h2')
    if h2_cta:
        h2_cta.clear()
        h2_c = soup.new_tag('h2')
        h2_c.append("Begin your journey to ")
        h2_c.append(soup.new_tag('br'))
        h2_c.append("recovery and ")
        strong_c = soup.new_tag('strong')
        strong_c.string = "dignity today"
        h2_c.append(strong_c)
        h2_cta.append(h2_c)

    p_cta = sec_cta.find(class_='n4-cta_main_text')
    if p_cta:
        p_cta.string = "A new life is waiting. Our compassionate admissions counselors and doctors are available 24 hours a day, 7 days a week to support you and your family."

    cta_buttons = sec_cta.find_all(class_='n4-btn_main_wrap')
    if len(cta_buttons) >= 1:
        a_b1 = cta_buttons[0].find('a')
        if a_b1: a_b1['href'] = "tel:9384190971"
        t_b1 = cta_buttons[0].find(class_='n4-btn_main_text')
        if t_b1: t_b1.string = "Call 24/7 Helpline: 93841 90971"
    if len(cta_buttons) >= 2:
        a_b2 = cta_buttons[1].find('a')
        if a_b2: a_b2['href'] = "https://wa.me/919384190971"
        t_b2 = cta_buttons[1].find(class_='n4-btn_main_text')
        if t_b2: t_b2.string = "Chat on WhatsApp"

# 19. Section 8: Footer
footer = soup.find('footer')
if footer:
    footer['id'] = "contact"

    # Remove unwanted things: "Stay in the loop" form container
    f_form_wrap = footer.find(class_='n4-form_footer_wrap')
    if f_form_wrap:
        f_form_wrap.decompose()

    # Remove non-used pages from footer: Terms, Privacy, Security, Cookie Policy, Safety Info, Ketch, etc.
    f_bottom_body = footer.find(class_='n4-footer_bottom_body')
    if f_bottom_body:
        f_bottom_body.decompose()

    for el in footer.find_all('a'):
        href = el.get('href', '')
        if any(bad in href for bad in ['/app/', '/lp/', '/security', 'ketch']):
            parent_li = el.find_parent('li')
            if parent_li: parent_li.decompose()
            else: el.decompose()

    # Remove unwanted things: "Verify Approval for www.mavenclinic.com" (LegitScript seal)
    for el in footer.find_all(lambda tag: tag.name in ['div', 'a', 'img'] and (
        'legitscript' in tag.get('href', '').lower() or 
        'legitscript' in tag.get('src', '').lower() or 
        'legit' in ' '.join(tag.get('class', [])).lower() or
        'verify approval' in tag.get('title', '').lower() or
        'verify approval' in tag.get('alt', '').lower()
    )):
        parent_btn = el.find_parent(class_='n4-footer_btn_group')
        if parent_btn:
            parent_btn.decompose()
        else:
            el.decompose()

    # Also remove any stray elements with "Stay in the loop"
    for tag in footer.find_all(string=lambda t: t and 'stay in the loop' in t.lower()):
        parent_el = tag.find_parent(class_='n4-form_footer_wrap')
        if parent_el:
            parent_el.decompose()

    # Update Footer Columns with correct font and high-contrast readable colors
    cols = footer.find_all(class_='n4-footer_content_list')
    if len(cols) >= 1:
        cols[0].clear()
        cols[0].append(BeautifulSoup("""
        <div class="footer-col-title" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;">Our Treatments</div>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Alcohol De-Addiction</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Drug De-Addiction</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Psychiatric Care &amp; Counseling</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Detoxification &amp; Medical Support</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Individual Counseling</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Family Counseling</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Yoga, Meditation &amp; Brain Gym</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#services"><div class="n4-footer_link_text">Aftercare &amp; Rehabilitation Support</div></a>
        """, 'html.parser'))

    if len(cols) >= 2:
        cols[1].clear()
        cols[1].append(BeautifulSoup("""
        <div class="footer-col-title" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;">About The Centre</div>
        <a class="n4-footer_link_wrap w-inline-block" href="#about"><div class="n4-footer_link_text">About Akrura</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#facilities"><div class="n4-footer_link_text">Vadipatti Campus Tour</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Doctor Supervision (24/7)</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="https://wa.me/919384190971"><div class="n4-footer_link_text">Emergency Admissions</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#facilities"><div class="n4-footer_link_text">Mind Refreshment Activities</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="#contact"><div class="n4-footer_link_text">Family Reintegration Protocol</div></a>
        """, 'html.parser'))

    if len(cols) >= 3:
        cols[2].clear()
        cols[2].append(BeautifulSoup("""
        <div class="footer-col-title" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;">Tamil Nadu Coverage</div>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Madurai &amp; Vadipatti (Campus)</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Chennai Patient Admissions</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Coimbatore &amp; Tiruppur</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Salem &amp; Erode</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">Dindigul &amp; Trichy</div></a>
        <a class="n4-footer_link_wrap w-inline-block" href="tel:9384190971"><div class="n4-footer_link_text">All Over Tamil Nadu</div></a>
        """, 'html.parser'))

    if len(cols) >= 4:
        cols[3].clear()
        cols[3].append(BeautifulSoup("""
        <div class="footer-col-title" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;">Contact &amp; Location</div>
        <div style="font-family: Helveticanowdisplay, Arial, sans-serif; font-size: 13.5px; color: rgba(255, 255, 255, 0.85); line-height: 1.6; margin-bottom: 14px;">
          <strong style="color: #ffffff; display: block; margin-bottom: 4px; font-weight: 600;">Vadipatti Campus:</strong>
          5/96/13, Street-3, Mettuperumal Nagar,<br>
          Vadipatti, Madurai - 625218, Tamil Nadu.<br>
          <span style="color: rgba(255, 255, 255, 0.55); font-size: 12.5px;">(Near Madurai - Dindigul Main Road)</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 9px; margin-bottom: 10px;">
          <a href="tel:9384190971" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 600; text-decoration: none; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px; transition: opacity 0.2s;">
            <span>📞</span> +91 93841 90971
          </a>
          <a href="https://wa.me/919384190971" target="_blank" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 600; text-decoration: none; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px; transition: opacity 0.2s;">
            <span>💬</span> WhatsApp 24/7 Helpline
          </a>
          <a href="https://maps.google.com/?q=Vadipatti,+Madurai,+Tamil+Nadu" target="_blank" style="color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 500; text-decoration: none; font-size: 13px; display: inline-flex; align-items: center; gap: 6px; margin-top: 2px;">
            <span>📍</span> View on Google Maps &rarr;
          </a>
        </div>
        """, 'html.parser'))

    # Add aligned title to right column
    right_col = footer.find(class_='n4-footer_content_right')
    if right_col:
        right_title = soup.new_tag('div', attrs={
            'class': 'footer-col-title',
            'style': 'color: #38BDF8; font-family: Helveticanowdisplay, Arial, sans-serif; font-weight: 700; font-size: 13.5px; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;'
        })
        right_title.string = "Connect & Trust"
        right_col.insert(0, right_title)

    # Social links
    social_links = footer.find_all(class_='n4-social_link_wrap')
    for sl in social_links:
        txt = sl.get_text(strip=True).lower()
        if 'instagram' in txt:
            sl['href'] = "https://www.instagram.com/akrura_de_addiction"
            sl['target'] = "_blank"
        elif 'facebook' in txt:
            sl['href'] = "https://www.facebook.com/share/1KWuSgFxir/"
            sl['target'] = "_blank"
        elif 'linkedin' in txt or 'whatsapp' in txt:
            sl['href'] = "https://wa.me/919384190971"
            txt_span = sl.find(class_='n4-footer_link_text')
            if txt_span: txt_span.string = "WhatsApp"

    # Rating text
    rating_text = footer.find(class_='n4-footer_bottom_rating_text')
    if rating_text:
        rating_text.string = "Trusted by families across Tamil Nadu (5.0 ★ Rating)"

    # Replace bottom logo / mission block with crisp white logo and clear high-contrast text
    f_logo = footer.find(class_='n4-footer_logo_svg')
    if f_logo:
        f_logo.replace_with(BeautifulSoup("""
        <div class="n4-footer_brand_block" style="margin-bottom: 2.5rem; border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 2rem;">
          <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 1rem;">
            <img src="akrura-logo-white.svg" alt="Akrura De Addiction &amp; Rehabilitation Centre" style="height: 48px; width: auto; max-width: 100%; display: block;">
          </div>
          <p style="font-family: Helveticanowdisplay, -apple-system, BlinkMacSystemFont, Arial, sans-serif; font-size: 14px; color: rgba(255, 255, 255, 0.75); max-width: 720px; line-height: 1.65; margin: 0;">
            <strong style="color: #ffffff; font-weight: 600;">Akrura De Addiction &amp; Rehabilitation Centre</strong> is a trusted centre for Alcohol, Drug De-addiction and Psychiatric Care. Located at Vadipatti, Madurai, we serve patients from All Over Tamil Nadu including Chennai, Erode, Salem, Tiruppur, Coimbatore. Our treatment includes Medical Support, Counseling, Yoga, Meditation and Mind Refreshment activities. We help every person to recover with dignity and rejoin their family.
          </p>
        </div>
        """, 'html.parser'))

    bottom_text = footer.find(class_='n4-footer_bottom_text')
    if bottom_text:
        bottom_text.string = "© 2026 Akrura De Addiction & Rehabilitation Centre. Vadipatti, Madurai. All rights reserved."

# Clean remaining specific text strings
for el in soup.find_all(string=lambda t: t and 'Maven Consumer' in t):
    el.replace_with("Confidential Inpatient Care")

for el in soup.find_all(string=lambda t: t and 'Free, covered by employer' in t):
    el.replace_with("24/7 Medical Support")

for el in soup.find_all(string=lambda t: t and 'Why Maven' in t):
    el.replace_with("About Akrura")

for el in soup.find_all(string=lambda t: t and 'Maven Member Journey' in t):
    el.replace_with("Recovery Journey")

for el in soup.find_all(string=lambda t: t and 'Maven ROI' in t):
    el.replace_with("Clinical Care Outcomes")

for el in soup.find_all(string=lambda t: t and 'Women’s and Family Health Benefits 2026' in t):
    el.replace_with("Rejoining Family with Dignity - Comprehensive Recovery Guide")

for el in soup.find_all(string=lambda t: t and 'State of Women’s' in t):
    el.replace_with("24/7 Emergency Helpline: Call +91 93841 90971")

for el in soup.find_all(string=lambda t: t and 'See if your company offers Maven' in t):
    el.replace_with("Admissions Helpline: 93841 90971")

for el in soup.find_all(class_='n4-stories_tabs_bio_text'):
    t = el.get_text(strip=True)
    if 'Microsoft' in t: el.string = "Family Member, Chennai"
    elif 'Amazon' in t: el.string = "Recovered Patient, Coimbatore"
    elif 'Vynamic' in t: el.string = "Family Member, Madurai"
    elif 'Han' in t: el.string = "S. Rajesh"
    elif 'Sarah' in t: el.string = "M. Karthik"
    elif 'Mairead' in t: el.string = "P. Anandhi"

for el in soup.find_all(class_='n4-footer_form_disclaimer'):
    el.string = "Your contact information is kept strictly confidential under healthcare privacy regulations."

# Convert back to HTML
final_html = str(soup)

# 20. Update Hero Pill Animation Loop in Script (Regex replacement)
final_html = re.sub(
    r'initial:\s*\{\s*backgroundColor:[^}]*text:\s*"Supporting working parents"\s*\},[\s\n]*looping:\s*\[[^\]]*\]',
    '''initial: {
          backgroundColor: "#0066CC",
          text: "Alcohol & Drug De-Addiction"
        },
        looping: [
          { backgroundColor: "#0066CC", text: "Alcohol & Drug De-Addiction" },
          { backgroundColor: "#2EDAF1", text: "Psychiatric Care & Counseling" },
          { backgroundColor: "#FFC728", text: "Yoga, Meditation & Brain Gym" },
          { backgroundColor: "#38BDF8", text: "Recovering with Dignity" }
        ]''',
    final_html,
    flags=re.DOTALL
)

# Navigation & Interactive Enhancements before </body>
enhancements = """
<!-- Interactive Enhancements (Navbar, Dropdowns, Banner, Rive path resolver, Animations) -->
<script>
  (function() {
    // Resolve Rive paths (use local if on HTTP/server, else fallback to CDN)
    const isFile = window.location.protocol === 'file:';
    if (!isFile) {
      document.querySelectorAll('canvas[data-rive-url]').forEach(c => {
        const u = c.getAttribute('data-rive-url');
        if (u.includes('maven_clock')) c.setAttribute('data-rive-url', 'clock.riv');
        else if (u.includes('maven_bento_flip')) c.setAttribute('data-rive-url', 'flip.riv');
        else if (u.includes('maven_bento_globe')) c.setAttribute('data-rive-url', 'globe.riv?v=2');
      });
    }

    document.addEventListener('DOMContentLoaded', function() {
      // 1. Announcement Banner Close
      const bannerWrapper = document.querySelector('.web-banner-wrapper');
      const bannerCloseBtn = document.querySelector('.web-banner-close');
      if (bannerCloseBtn && bannerWrapper) {
        bannerCloseBtn.addEventListener('click', function(e) {
          e.preventDefault();
          bannerWrapper.style.transition = 'all 0.35s ease';
          bannerWrapper.style.maxHeight = '0px';
          bannerWrapper.style.opacity = '0';
          bannerWrapper.style.overflow = 'hidden';
          setTimeout(() => bannerWrapper.remove(), 350);
        });
      }

      // 2. Navigation Mega Menu Dropdowns
      const dropdowns = document.querySelectorAll('.dropdown, .dropdown-2, .w-dropdown');
      dropdowns.forEach(function(dp) {
        const toggle = dp.querySelector('.w-dropdown-toggle, .nav__link-drop');
        const list = dp.querySelector('.w-dropdown-list, .nav-drop-list');
        if (!toggle || !list) return;

        dp.addEventListener('mouseenter', function() {
          if (window.innerWidth > 991) {
            dropdowns.forEach(d => {
              if (d !== dp) {
                const otherList = d.querySelector('.w-dropdown-list, .nav-drop-list');
                const otherToggle = d.querySelector('.w-dropdown-toggle, .nav__link-drop');
                if (otherList) otherList.classList.remove('w--open');
                if (otherToggle) otherToggle.classList.remove('w--open');
              }
            });
            list.classList.add('w--open');
            toggle.classList.add('w--open');
            list.style.opacity = '1';
            list.style.visibility = 'visible';
            list.style.pointerEvents = 'auto';
          }
        });

        dp.addEventListener('mouseleave', function() {
          if (window.innerWidth > 991) {
            list.classList.remove('w--open');
            toggle.classList.remove('w--open');
            list.style.opacity = '';
            list.style.visibility = '';
            list.style.pointerEvents = '';
          }
        });

        toggle.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          const isOpen = list.classList.contains('w--open');
          dropdowns.forEach(d => {
            const l = d.querySelector('.w-dropdown-list, .nav-drop-list');
            const t = d.querySelector('.w-dropdown-toggle, .nav__link-drop');
            if (l) l.classList.remove('w--open');
            if (t) t.classList.remove('w--open');
          });
          if (!isOpen) {
            list.classList.add('w--open');
            toggle.classList.add('w--open');
            list.style.opacity = '1';
            list.style.visibility = 'visible';
            list.style.pointerEvents = 'auto';
          }
        });
      });

      document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown') && !e.target.closest('.dropdown-2') && !e.target.closest('.w-dropdown')) {
          dropdowns.forEach(d => {
            const l = d.querySelector('.w-dropdown-list, .nav-drop-list');
            const t = d.querySelector('.w-dropdown-toggle, .nav__link-drop');
            if (l) {
              l.classList.remove('w--open');
              l.style.opacity = '';
              l.style.visibility = '';
            }
            if (t) t.classList.remove('w--open');
          });
        }
      });

      // 3. Mobile Hamburger Menu Toggle
      const menuBtn = document.querySelector('.menu-button');
      const navMenu = document.querySelector('.nav-menu-4');
      if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', function(e) {
          e.preventDefault();
          e.stopPropagation();
          const isOpen = navMenu.classList.toggle('is-open');
          menuBtn.classList.toggle('w--open', isOpen);
        });

        // Close menu when clicking any nav link
        navMenu.querySelectorAll('.nav__link-item, a').forEach(function(link) {
          link.addEventListener('click', function() {
            navMenu.classList.remove('is-open');
            menuBtn.classList.remove('w--open');
          });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
          if (!e.target.closest('.navbar')) {
            navMenu.classList.remove('is-open');
            menuBtn.classList.remove('w--open');
          }
        });
      }

      // 4. Ensure animated elements reveal properly
      setTimeout(function() {
        document.querySelectorAll("[data-split-gsap='words'], [data-animation-gsap]").forEach(function(el) {
          el.style.opacity = '1';
          el.style.visibility = 'visible';
        });
      }, 800);
    });
  })();
</script>
"""

final_html = final_html.replace('</body>', enhancements + '\n</body>')

# 21. Global Color Replacement (Green -> Blue theme)
for old_c, new_c in [
    ('#013126', '#0B1E36'),
    ('#00856f', '#0066CC'),
    ('#00856F', '#0066CC'),
    ('#006e5c', '#0052A3'),
    ('#58eda2', '#38BDF8'),
    ('#58EDA2', '#38BDF8'),
    ('#035748', '#0E3A68'),
    ('#005c4d', '#0E3A68'),
    ('#005d4e', '#0E3A68'),
    ('#028c74', '#0066CC'),
    ('#263633', '#1E293B'),
    ('rgba(1,49,38,', 'rgba(11,30,54,'),
    ('rgba(1, 49, 38,', 'rgba(11, 30, 54,'),
]:
    final_html = final_html.replace(old_c, new_c)

# Write output to index.html
with open(r'e:\Clients\Website\From Sathesh bro\akura\index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Akrura site successfully compiled into authentic Maven Clinic clone structure! File length:", len(final_html))
