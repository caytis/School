import os
import exifread
import reverse_geocoder

def scan(curdir):
    filescan = os.scandir(curdir)
    dirscan = os.scandir(curdir)
    files = list(entry.name for entry in filescan if entry.is_file())
    dirs = list(entry.name for entry in dirscan if entry.is_dir())

    if '.DS_Store' in files:
        files.remove('.DS_Store')

    return files, dirs

def search_dir(curdir):

    files, dirs = scan(curdir)

    dirs.sort()
    for file in files:
        if not (".jpeg" in file.lower() or ".jpg" in file.lower() or ".png" in file.lower() or ".gif" in file.lower()):
            files.remove(file)
    files.sort()

    for newdir in dirs:
        createHTML(curdir, dirs, files)
        newdir = curdir + "/" + newdir
        search_dir(newdir)
    createHTML(curdir, dirs, files)

def createHTML(curdir, dirs, files):

    cursplit = curdir.split("/")
    cleancur = cursplit[len(cursplit) - 1]

    towrite = """<html>
    <head>
    <style>
    .dirlink_el {font-size: 125%;}
    .sm_img {max-height: 200px; max-width: 200px;}
    .img_el {display: inline-block; padding-bottom: 15px; padding-right: 10px;}
    </style>
    </head>
    <body>"""

    nextindex = "../index.html"

    if cleancur == "Pictures":
        nextindex = "index.html"

    towrite += f"""<h2><a href="{nextindex}">
    {cleancur}
    </a></h2>
    """

    for dirr in dirs:
        if emptyDir(f"{curdir}/{dirr}"):
            towrite += f"""<div class="dirlink_el">
            <a href=\"{dirr}\">{dirr}</a>
            </div>
            <br>
            """

    for file in files:
        f = open(f"{curdir}/{file}", 'rb')
        exif = exifread.process_file(f)
        towrite += f"""<div class="img_el">
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

        if longi or longiref or lati or latiref:
            longi = longi.values
            deg = longi[0]
            min = longi[1]
            sec = longi[2]
            ddlongi = deg + min / 60 + sec / 3600
            if longiref and longiref.values == "S":
                ddlongi *= -1
            lati = lati.values
            deg = lati[0]
            min = lati[1]
            sec = lati[2]
            ddlati = deg + min / 60 + sec / 3600
            if latiref and latiref.values == "W":
                ddlati *= -1

            found = reverse_geocoder.search((ddlati, ddlongi))[0]
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

def emptyDir(dirr, hasfile = False):
    files, dirs = scan(dirr)
    for file in files:
        if (".jpeg" in file.lower() or ".jpg" in file.lower() or ".png" in file.lower() or ".gif" in file.lower()):
            hasfile = True
            return hasfile
    for nextdir in dirs:
        nextdir = dirr + "/" + nextdir
        hasfile = emptyDir(nextdir, hasfile)
    return hasfile

if __name__ == '__main__':
    search_dir("HTML/Pictures")
