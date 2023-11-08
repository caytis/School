import os
import exifread
import reverse_geocoder

def search_dir(olddir, curdir):
    """Search curr dir, make list with subdirs and images"""
    filescan = os.scandir(curdir)
    dirscan = os.scandir(curdir)
    files = list(entry.name for entry in filescan if entry.is_file())
    dirs = list(entry.name for entry in dirscan if entry.is_dir())
    dirs.sort()
    # index = None
    for file in files:
        if not (".jpeg" in file.lower() or ".jpg" in file.lower() or ".png" in file.lower() or ".gif" in file.lower()):
            files.remove(file)
        # elif "index.html" in file.lower():
        #     index = dir + "/" + file
        # else:
        #     print(file.lower())
    files.sort()
    for newdir in dirs:
        # print(newdir)
        newdir = curdir + "/" + newdir
        createHTML(olddir, curdir, dirs, files) # files
        search_dir(curdir, newdir)

def createHTML(olddir, curdir, dirs, files): # dont display dir if all future dirs are empty
    
    cleancur = curdir.split("/")[len(curdir.split("/")) - 1]
    
    towrite = """<html>
    <head>
    <style>
    .dirlink_el {font-size: 125%;}
    .sm_img {max-height: 200px; max-width: 200px;}
    .img_el {display: inline-block; padding-bottom: 15px; padding-right: 10px;}
    </style>
    </head>
    <body>"""


    towrite += f"""<h2><a href="{olddir}">
    {cleancur}
    </a></h2>
    """

    for dir in dirs:
        if not emptyDir(f"{curdir}/{dir}"):
            towrite += f"""<div class="dirlink_el">
            <a href=\"{curdir}/{dir}/index.html\">{dir}</a>
            </div>

            <br>
            """

    for file in files:
        f = open(file, 'rb')
        exif = exifread.process_file(f)
        towrite += f""""<div class="img_el">
        <a href="{file}"><img src="{file}" class="sm_img"></a>
        <br>
        {file}
        <br>
        """
        dateTime = exif.get('Image DateTime')
        if dateTime:
            towrite += f"""{dateTime}
            <br>
            """
        
        longi = exif.get("GPS GPSLongitude")
        longiref = exif.get("GPS GPSLongitudeRef")
        lati = exif.get("GPS GPSLatitude")
        latiref = exif.get("GPS GPSLatitudeREF")
        
        if longi and longiref and lati and latiref:
            longi = longi[1:-1].split(",")
            deg = int(longi[0])
            min = int(longi[1])
            seclist = longi[2].split("/")
            sec = int(seclist[0]) / int(seclist[1])
            ddlongi = deg + min / 60 + sec / 3600
            if latiref == "S":
                ddlongi *= -1
            lati = lati[1:-1].split(",")
            deg = int(lati[0])
            min = int(lati[1])
            seclist = lati[2].split("/")
            sec = int(seclist[0]) / int(seclist[1])
            ddlongi = deg + min / 60 + sec / 3600
            if latiref == "W":
                ddlongi *= -1
                
            found = reverse_geocoder.search(lati, longi)
            name = found.get("name")
            admin1 = found.get("admin1")
            cc = found.get("cc")
            
            towrite += f"""{name}, {admin1} {cc}
            </div>
            """
        else:
            towrite += """&nbsp;
            <br>
            &nbsp;
            </div>
            """
        f.close()
    
        towrite += """</body>
        </html>"""
    
    with open(curdir + "/index.html", "w") as file:
        file.write(towrite)

def emptyDir(dir, hasfile = False):
    filescan = os.scandir(dir)
    dirscan = os.scandir(dir)
    files = list(entry.name for entry in filescan if entry.is_file())
    dirs = list(entry.name for entry in dirscan if entry.is_dir())
    for file in files:
        if (".jpeg" in file.lower() or ".jpg" in file.lower() or ".png" in file.lower() or ".gif" in file.lower()):
            hasfile = True
            return hasfile
    for nextdir in dirs:
        nextdir = dir + "/" + nextdir
        emptyDir(nextdir, hasfile)
    return hasfile

if __name__ == '__main__':
    search_dir("HTML", "HTML/Pictures")
    pass