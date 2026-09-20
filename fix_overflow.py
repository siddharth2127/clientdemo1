import os

files = ['index.html', 'programs.html', 'testimonials.html', 'about.html', 'career-clarity-sprint.html', 'executive-coaching-retainer.html']

for f in files:
    path = os.path.join('c:\\design', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'html {' not in content:
        content = content.replace('    body {\n      margin: 0;\n      overflow-x: hidden;', 
                                  '    html, body {\n      margin: 0;\n      padding: 0;\n      width: 100%;\n      max-width: 100vw;\n      overflow-x: hidden;\n    }\n    body {\n      position: relative;')
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Body stretching issue fixed.")
