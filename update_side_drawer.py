import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']

menu_btn_old = '      <nav class="nav-links">'
menu_btn_new = '''      <div class="menu-overlay"></div>
      <nav class="nav-links">
        <button class="menu-close" aria-label="Close menu">
          <svg viewBox="0 0 24 24" width="28" height="28" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>'''

css_base_old = '''    .menu-toggle {
      display: none;
      background: none;
      border: none;
      color: var(--text-primary);
      cursor: pointer;
      padding: 4px;
      margin-right: 4px;
    }'''

css_base_new = '''    .menu-toggle, .menu-close {
      display: none;
      background: none;
      border: none;
      color: var(--text-primary);
      cursor: pointer;
      padding: 4px;
    }
    .menu-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(23, 31, 44, 0.8);
      z-index: 90;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.3s ease, visibility 0.3s ease;
    }'''

mobile_css_old = '''    @media (max-width: 768px) {
      .header-inner {
        flex-wrap: wrap;
        flex-direction: row;
        align-items: center;
        gap: 16px 8px;
      }
      .logo {
        flex: 1;
      }
      .menu-toggle {
        display: block;
        order: 2;
      }
      .header-cta {
        order: 3;
        padding: 8px 16px;
        font-size: 0.85rem;
      }
      .nav-links {
        display: none;
        width: 100%;
        order: 4;
        flex-direction: column;
        align-items: center;
        padding: 16px 0;
        border-top: 1px solid var(--border-color);
        margin-top: 8px;
        gap: 16px;
      }
      .nav-links.active {
        display: flex;
      }
      .hero::before, .about-section::before {
        width: 150vw;
        height: 150vw;
        opacity: 1;
        filter: blur(50px);
      }'''

mobile_css_new = '''    @media (max-width: 768px) {
      .header-inner {
        flex-wrap: nowrap;
        flex-direction: row;
        align-items: center;
        gap: 12px;
      }
      .logo {
        flex: 1;
      }
      .header-cta {
        order: 2;
        padding: 8px 16px;
        font-size: 0.85rem;
      }
      .menu-toggle {
        display: block;
        order: 3;
      }
      .menu-overlay.active {
        opacity: 1;
        visibility: visible;
      }
      .nav-links {
        display: flex;
        position: fixed;
        top: 0;
        right: -280px;
        width: 280px;
        height: 100vh;
        background-color: var(--card-bg);
        flex-direction: column;
        align-items: flex-start;
        padding: 80px 32px 32px;
        margin: 0;
        border-top: none;
        border-left: 1px solid var(--border-color);
        z-index: 100;
        transition: right 0.3s ease;
        gap: 24px;
      }
      .nav-links.active {
        right: 0;
      }
      .menu-close {
        display: block;
        position: absolute;
        top: 24px;
        right: 24px;
      }
      .hero::before, .about-section::before {
        width: 150vw;
        height: 150vw;
        opacity: 1;
        filter: blur(50px);
      }'''

js_old = '''  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggle = document.querySelector('.menu-toggle');
      const nav = document.querySelector('.nav-links');
      if (toggle && nav) {
        toggle.addEventListener('click', () => {
          nav.classList.toggle('active');
        });
      }
    });
  </script>'''

js_new = '''  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggle = document.querySelector('.menu-toggle');
      const closeBtn = document.querySelector('.menu-close');
      const nav = document.querySelector('.nav-links');
      const overlay = document.querySelector('.menu-overlay');
      
      const toggleMenu = () => {
        nav.classList.toggle('active');
        if(overlay) overlay.classList.toggle('active');
        document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
      };
      
      if (toggle && nav) {
        toggle.addEventListener('click', toggleMenu);
        if(closeBtn) closeBtn.addEventListener('click', toggleMenu);
        if(overlay) overlay.addEventListener('click', toggleMenu);
      }
    });
  </script>'''

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'menu-overlay' in content:
        continue
        
    content = content.replace(menu_btn_old, menu_btn_new)
    content = content.replace(css_base_old, css_base_new)
    content = content.replace(mobile_css_old, mobile_css_new)
    content = content.replace(js_old, js_new)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Side drawer menu implemented successfully.")
