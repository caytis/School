import requests
import os
# import threading

def find_urls(url, full_parent_name='Manuals'):
    response = requests.get(url)
    file = response.text
    if "<name>" in file:
        name = file.split("<name>")[1].split("</name>")[0]
    else:
        name = url.split("/")[-1].split(".")[0]
    
    if '-' in name:
        name = " ".join(name.split('-'))
        
    if '&amp;' in name:
        name = name.replace('&amp;', '')
    
    name = name.strip()
    
    parent_name = full_parent_name.split('/')[-1]
    full_name = f'{full_parent_name}/{name}'
        
    if "<files>" in file:
        files_section = file.split("<files>")[1].split("</files>")[0]
        urls = [x[1].split(' url="')[1].split('" />')[0].strip('\n\t \'\"') for x in [f.split("<file") for f in files_section.split("\n") if "<file" in f] if len(x) > 0]
        os.makedirs(full_name, exist_ok=True)
        url_name = f'{full_name}/index.html'
        with open(url_name, 'w') as f:
            f.write(f'<h1>{name}</h1>\n')
            f.write(f'<h3>Back to <a href="../index.html">{parent_name}</a></h3>\n')
            for new_file in urls:
                # threading.Thread(target=find_urls, args=(newFile, full_name)).start()
                new_name, path = find_urls(new_file, full_name)
                f.write(f'<div>Go to <a href="{path}">{new_name}</a></div>\n')

    if '.xml' in url:
        full_name = f'{full_name.split('.xml')[0]}.html'
        relative_path = f'{name}.html'
        name = name.title()
        print(name)

        with open(full_name, 'w') as f:
            f.write(f'<h1>{name}</h1>\n')
            f.write(f'<h3>Back to <a href="index.html">{parent_name}</a></h3>\n')
            f.write(file)
    
    else:
        relative_path = f'{name}/index.html'
    
    return name, relative_path

if __name__ == '__main__': # thread here
    find_urls('https://raw.githubusercontent.com/aurorabuilder/elements/master/core.index')
    find_urls('https://raw.githubusercontent.com/aurorabuilder/elements/master/supplements.index')
    find_urls('https://raw.githubusercontent.com/aurorabuilder/elements/master/third-party.index')
    find_urls('https://raw.githubusercontent.com/aurorabuilder/elements/master/unearthed-arcana.index')
    pass
