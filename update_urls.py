import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']
url_replacements = {
    'href="/"': 'href="index.html"',
    'href="/about"': 'href="about.html"',
    'href="/programs"': 'href="programs.html"',
    'href="/testimonials"': 'href="testimonials.html"',
    'href="/programs/career-clarity-sprint"': 'href="career-clarity-sprint.html"',
    'href="/programs/executive-coaching-retainer"': 'href="executive-coaching-retainer.html"'
}

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Revert URLs
    for old, new in url_replacements.items():
        content = content.replace(old, new)
    
    # Add overflow-x: hidden to body to prevent horizontal scrolling on mobile
    if 'overflow-x: hidden;' not in content:
        content = content.replace('body {\n      margin: 0;', 'body {\n      margin: 0;\n      overflow-x: hidden;')
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Reverted URLs and improved mobile responsiveness (overflow-x hidden).")
