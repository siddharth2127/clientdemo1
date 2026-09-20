import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']

url_replacements = {
    'href="index.html"': 'href="/"',
    'href="about.html"': 'href="/about"',
    'href="programs.html"': 'href="/programs"',
    'href="testimonials.html"': 'href="/testimonials"',
    'href="career-clarity-sprint.html"': 'href="/programs/career-clarity-sprint"',
    'href="executive-coaching-retainer.html"': 'href="/programs/executive-coaching-retainer"'
}

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for old, new in url_replacements.items():
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated links to clean URLs for Vercel deployment.")
