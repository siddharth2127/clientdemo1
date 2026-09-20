import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']
tag = '  <link rel="icon" href="favicon.svg" type="image/svg+xml">\n</head>'

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<link rel="icon"' not in content:
        content = content.replace('</head>', tag)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Favicon added to all files successfully.")
