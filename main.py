import markdown
import os
from git import Repo

# Read the markdown file with the specified encoding
with open("input.md", "r", encoding="utf-8") as input_file:
    markdown_text = input_file.read()

# Convert the markdown to HTML
html = markdown.markdown(markdown_text)
print('Converted markdown to HTML')

Repo.clone_from('https://github.com/Joshua861/css-themes', 'output/')

os.remove("output/index.html")

title = input("What is the title of your writing.")

# Write the HTML to a file
with open("output/index.html", "w", encoding="utf-8") as index:
    index_text = ('<head>\n<style>\n@keyframes drift {\n0% {\nbackground-position: 0 0;\n}\n100% {\nbackground-position: 100% 0;\n}\n}\n@import url("https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@700&display=swap");\n#loading {\nheight: 50vmin;\nwidth: 50vmin;\nanimation: spin 5s infinite linear;\ndisplay: flex;\njustify-content: center;\nalign-items: center;\nmargin: auto;\nfill: #fff;\n}\n@keyframes spin {\n0% {\ntransform: rotate(0deg);\n}\n100% {\ntransform: rotate(360deg);\n}\n}\n.loading-message {\nmargin: auto;\ntop: 50%;\n}\n#load-bg {\nposition: fixed;\ntop: 0;\nleft: 0;\nwidth: 100%;\nheight: 100%;\nz-index: 9999;\ndisplay: flex;\njustify-content: center;\nalign-items: center;\nbackground-image: url("data:image/svg+xml,%3Csvg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="%239C92AC" fill-opacity="0.1" fill-rule="evenodd"%3E%3Cpath d="M0 40L40 0H20L0 20M40 40V20L20 40"/%3E%3C/g%3E%3C/svg%3E");\nbackground-color: #111;\nanimation: drift 5s infinite linear;\nbackground-size: 10%;\ntransition: opacity 0.5s;\n}\n#loading-text {\nfont-family: "Source Sans Pro", sans-serif;\ncolor: #fff;\nmargin-top: 0em;\ntext-align: centre;\nfont-size: 10vmin;\n}\n</style>\n<div id="load-bg">\n<div class="loading-message">\n<svg id="loading" xmlns="http://www.w3.org/2000/svg" height="48"\nviewBox="0 96 960 960" width="48">\n<path d="M196\n725q-20-36-28-72.5t-8-74.5q0-131 94.5-225.5T480\n258h43l-80-80 39-39 149 149-149 149-40-40 79-79h-41q-107\n0-183.5 76.5T220 578q0 29 5.5 55t13.5 49l-43 43Zm280\n291L327 867l149-149 39 39-80 80h45q107 0 183.5-76.5T740\n577q0-29-5-55t-15-49l43-43q20 36 28.5 72.5T800 577q0\n131-94.5 225.5T480 897h-45l80 80-39 39Z" />\n</svg>\n<h1 id="loading-text">Loading...</h1>\n</div>\n</div>\n<script src="loading-screen.js"></script>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width,\ninitial-scale=1.0">\n<link rel="stylesheet" href="css/modern.css" id="theme-link" />\n<title>Theme Test</title>\n<style>\n#overlay {\nposition: fixed;\ntop: 0;\nleft: 0;\nwidth: 100%;\nheight: 100%;\nbackground-color: #ffffff33;\nz-index: 9999;\ndisplay: flex;\njustify-content: center;\nalign-items: center;\n}\n#loading {\nwidth: 50vmin;\nheight: 50vmin;\nanimation: spin 2s linear infinite;\n}\n@keyframes spin {\n0% {transform: rotate(0deg);}\n100% {transform: rotate(360deg);}\n} \n</style>\n</head>\n<body>\n<select id="theme-select">\n<option value="modern.css">Modern light theme</option>\n<option value="neon.css">Dark neon theme</option>\n<option value="serif-dark.css">Dark serif theme</option>\n<option value="serif-light.css">Light serif theme</option>\n<option value="hyperlegible-dark.css">Dark hyperlegible theme</option>\n<option value="hyperlegible-light.css">Light hyperlegible theme</option>\n<option value="dyslexic-dark.css">Dark dyslexic friendly theme </option>\n<option value="dyslexic-light.css">Light dyslexic friendly theme </option>\n</select>\n<script src="theme-switcher.js"></script>\n<br>\n<br>')
    index_text += (html)
    index_text += ('\n</body>\n</html>\n')
    index.write(index_text)
