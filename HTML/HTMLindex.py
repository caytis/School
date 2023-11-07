import os
import codecs

def search_dir(dir):
    """Search curr dir, make list with subdirs and images"""
    filescan = os.scandir(dir)
    dirscan = os.scandir(dir)
    files = list(entry.name for entry in filescan if entry.is_file())
    dirs = list(entry.name for entry in dirscan if entry.is_dir())
    index = None
    for file in files:
        if not (".jpeg" in file.lower() or ".jpg" in file.lower() or ".png" in file.lower() or ".gif" in file.lower()):
            files.remove(file)
        # elif "index.html" in file.lower():
        #     index = dir + "/" + file
        else:
            print(file.lower())
    # files = files.sort()
    for newdir in dirs:
        print(newdir)
        newdir = dir + "/" + newdir
        createHTML(dir, newdir) # files
        search_dir(newdir)

def createHTML(dir, newdir): # files
    
    # page_start = """
    # <html>
    # <head>
    # <style>
    # .dirlink_el {font-size: 125%;}
    # .sm_img {max-height: 200px; max-width: 200px;}
    # .img_el {display: inline-block; padding-bottom: 15px; padding-right: 10px;}
    # </style>
    # </head>
    # <body>
    # """

    # page_end = """
    # </body>
    # </html>
    # """

    # title_tmplt = """
    # <style>
    # h2 {}
    # </style>
    # """

    # link_tmplt = """
    # <div class="dirlink_el">
    # <a href="{0}">{1}</a>
    # </div>
    # """

    # img_tmplt = """
    # <div class="img_el">
    # <a href={0}><img src="{0}" class="sm_img"></a>
    # <br>
    # {0}
    # <br>
    # {1}
    # <br>
    # {2}
    # </div>
    # """
    
    
    
    with codecs.open(dir + "/index.html") as file:
        # print(file.read())

        # filestr = ""
        for line in file.readlines():
            # filestr += line
            if "<h2>" in line:
                
                break
        
#         page = file.read() + page_start + page_end + title_tmplt + link_tmplt + img_tmplt
#         with open(dir + "/page.html", "utf-8") as newfile:
#             newfile.write(page)
#             print()
#         # writepage = ""
        
#         # for i, letter in enumerate(page, start=1):
#         #     writepage += unicodedata.name(letter).title()
#             # writepage += f"{'</td><td>'.join(lettercode)}\n"
#         # table_body += "</tbody>\n"

#         # print(f"<table>\n{table_head}{table_body}</table>")
        
#         # print(f"{writepage}")
#         # print(page.encode("utf-8"))
#         # f.write(html_template) 
  
#         # close the file 
#         # f.close() 
        
#         # viewing html files 
#         # below code creates a  
#         # codecs.StreamReaderWriter object 
#         # file = codecs.open("GFG.html", 'r', "utf-8") 
        
#         # using .read method to view the html  
#         # code from our object 
#         # print(file.read()) 


if __name__ == '__main__':
    search_dir("HTML/Pictures")
    pass