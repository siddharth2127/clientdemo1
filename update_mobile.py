import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']

menu_btn_html = '''      <button class="menu-toggle" aria-label="Toggle menu">
        <svg viewBox="0 0 24 24" width="28" height="28" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
      <nav class="nav-links">'''

script_html = '''  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggle = document.querySelector('.menu-toggle');
      const nav = document.querySelector('.nav-links');
      if (toggle && nav) {
        toggle.addEventListener('click', () => {
          nav.classList.toggle('active');
        });
      }
    });
  </script>
</body>'''

menu_css = '''    .menu-toggle {
      display: none;
      background: none;
      border: none;
      color: var(--text-primary);
      cursor: pointer;
      padding: 4px;
      margin-right: 4px;
    }

    /* Responsive */'''

mobile_css_target = '''    @media (max-width: 768px) {
      .header-inner {
        flex-direction: column;
        gap: 24px;
      }
      .nav-links {
        flex-wrap: wrap;
        justify-content: center;
      }'''

mobile_css_replacement = '''    @media (max-width: 768px) {
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

old_btn = '<a href="https://calendly.com/sidd-cw21/new-meeting" class="btn" target="_blank" rel="noopener noreferrer">book a call</a>'
new_btn = '<a href="https://calendly.com/sidd-cw21/new-meeting" class="btn header-cta" target="_blank" rel="noopener noreferrer">book a call</a>'

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'menu-toggle' in content:
        continue
        
    content = content.replace('      <nav class="nav-links">', menu_btn_html)
    content = content.replace(old_btn, new_btn)
    content = content.replace('    /* Responsive */', menu_css)
    content = content.replace(mobile_css_target, mobile_css_replacement)
    content = content.replace('</body>', script_html)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Mobile navigation and glow effect updated successfully.")
