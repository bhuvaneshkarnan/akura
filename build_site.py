import re

with open(r'C:\Users\bhuva\.gemini\antigravity\brain\5e1c917c-a072-42e2-8abb-955a855564b1\.system_generated\steps\3\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<!DOCTYPE html>')
if start_idx == -1:
    raise ValueError("<!DOCTYPE html> not found in content.md")

html = text[start_idx:]

# 1. Update CSS links to local
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

# 2. Update Favicon & Logo
html = html.replace('5fb2b678e994734019d950db_fav-icon.png', 'favicon.png')

# 3. Remove trackers and analytics
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
"""

html = html.replace('</head>', core_head + '\n</head>')

# 6. Replace Hubspot embed with clean interactive newsletter form
custom_footer_form = """
<div id="clone-newsletter-form">
  <form id="hsForm_acd12eec-ce16-4f2f-ae7c-f8e595869f7f" onsubmit="event.preventDefault(); document.getElementById('newsletter-success').style.display='block'; this.reset();">
    <div style="position: relative; width: 100%;">
      <input type="email" required placeholder="Enter your business email" style="width: 100%; height: 3rem; background: transparent; border: none; border-bottom: 1px solid rgba(255,255,255,0.4); color: #fff; font-size: 0.95rem; padding-right: 3rem; outline: none;" onfocus="this.style.borderBottomColor='#58EDA2'" onblur="this.style.borderBottomColor='rgba(255,255,255,0.4)'">
      <button type="submit" style="position: absolute; right: 0; top: 0; height: 3rem; background: none; border: none; color: #58EDA2; cursor: pointer; font-size: 1.3rem; padding: 0 0.5rem; transition: transform 0.2s;" onmouseover="this.style.transform='translateX(3px)'" onmouseout="this.style.transform='translateX(0)'">&rarr;</button>
    </div>
    <div id="newsletter-success" style="display: none; color: #58EDA2; font-size: 0.85rem; margin-top: 0.5rem;">Thank you for subscribing!</div>
  </form>
</div>
"""
html = re.sub(r'<div class="n4-form_footer_embed w-embed w-script">.*?</div>\s*<div class="n4-footer_form_disclaimer',
              f'<div class="n4-form_footer_embed w-embed w-script">{custom_footer_form}</div>\n<div class="n4-footer_form_disclaimer',
              html, flags=re.DOTALL)

# 7. Add comprehensive interactions before </body>
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
        else if (u.includes('maven_bento_globe')) c.setAttribute('data-rive-url', 'globe.riv');
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
      const dropdowns = document.querySelectorAll('.dropdown, .dropdown-2');
      dropdowns.forEach(function(dp) {
        const toggle = dp.querySelector('.w-dropdown-toggle, .nav__link-drop');
        const list = dp.querySelector('.w-dropdown-list, .nav-drop-list');
        if (!toggle || !list) return;

        // Desktop Hover
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

        // Click / Touch toggle
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
        if (!e.target.closest('.dropdown') && !e.target.closest('.dropdown-2')) {
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
      const navMenu = document.querySelector('.nav-menu-4, .w-nav-menu');
      if (menuBtn && navMenu) {
        menuBtn.addEventListener('click', function(e) {
          e.preventDefault();
          const isOpen = menuBtn.classList.toggle('w--open');
          if (isOpen) {
            navMenu.style.display = 'flex';
            navMenu.style.flexDirection = 'column';
            navMenu.style.height = 'auto';
            navMenu.style.position = 'absolute';
            navMenu.style.top = '100%';
            navMenu.style.left = '0';
            navMenu.style.width = '100%';
            navMenu.style.backgroundColor = '#013126';
            navMenu.style.padding = '1.5rem';
            navMenu.style.zIndex = '999';
            navMenu.style.boxShadow = '0 10px 30px rgba(0,0,0,0.3)';
          } else {
            navMenu.style.display = 'none';
          }
        });
      }

      // 4. Fallback ensuring all animations reveal smoothly
      setTimeout(function() {
        document.querySelectorAll("[data-split-gsap='words'], [data-animation-gsap]").forEach(function(el) {
          el.style.opacity = '1';
          el.style.visibility = 'visible';
        });
      }, 1000);
    });
  })();
</script>
"""

html = html.replace('</body>', enhancements + '\n</body>')

with open(r'e:\Clients\Website\From Sathesh bro\akura\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html compiled successfully. File length:", len(html))
