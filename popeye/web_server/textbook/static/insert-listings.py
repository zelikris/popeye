import os
import re
from listings import listings

docs_src = 'sphinx/docs/'
listings = listings()

pattern = re.compile('m[0-9]+\.html')
for item in os.listdir(docs_src):
    if os.path.isfile(docs_src + item) and pattern.match(item):
        chNum = item[1:-5]

        # open file and copy to string
        textfile = open(docs_src + 'm' + chNum + '.html', 'r')
        text = textfile.read()
        textfile.close()

        # regex for getting chapter/figure
        regex = '<p>&lt;popeye-listing&gt;c([0-9]+)f([0-9]+)&lt;\/popeye-listing&gt;<\/p>'
        tag = re.compile(regex)
        # finds all popeye tage and saves the chapter/figure
        blocks = re.findall(tag, text)
        chapter = []
        figure = []
        for x in blocks:
            chapter.append(x[0])
            figure.append(x[1])

        # open editor code and copy to string
        editor = open('edit-window/editorcode.html', 'r')
        editortext = editor.read()
        editor.close()

        # regex to split for editor code insert
        regex2 = '<p>&lt;popeye-listing&gt;c[0-9]+f[0-9]+&lt;\/popeye-listing&gt;<\/p>'
        tag2 = re.compile(regex2)
        blocks2 = re.split(regex2, text)

        # assemble html with editor
        count = 0

        finalfile = open(docs_src + 'm' + chNum + '.html', 'w')
        for x in range(0, len(blocks2) - 1):
            finalfile.write(blocks2[count] + '<br>\n')
            finalfile.write('Figure ' + figure[count] + '\n<br>\n')

            regex3 = '<div id="editor">(.+?)</div>'
            tag3 = re.compile(regex3)
            blocks3 = re.findall(tag3, editortext)

            try:
                editortext = editortext.replace("<imports-go-here>",
                    listings.get_imports(chapter[count], figure[count]) + "\n");

            except KeyError:
                print("Missing import",  chapter[count], figure[count]);

            editorsplit = editortext.split("purgeryUrsula")
            editorfinal = editorsplit[0]
            try:
                editorfinal += listings.get(chapter[count], figure[count])
            except KeyError:
                editorfinal += 'print "listing c' + str(chapter[count]) + 'f' + \
                str(figure[count]) + ' missing"'
                continue;
            print("" + chapter[count] + figure[count]);
            print(editorfinal);
            editorfinal += editorsplit[1]

            finalfile.write(
                editorfinal.replace(
                    'results',
                    'results' +
                    str(count)).replace(
                    'editor',
                    'editor' +
                    str(count)) +
                '<br>\n')
            count += 1

        finalfile.write(blocks2[count])
        finalfile.close()
        ############
        # open file and copy to string
        textfile = open(docs_src + 'm' + chNum + '.html', 'r')
        text = textfile.read()
        textfile.close()

        # regex for getting chapter/figure
        regex = '<p>&lt;popeye-image&gt;c([0-9]+)f([0-9]+)&lt;\/popeye-image&gt;<\/p>'
        tag = re.compile(regex)
        # finds all popeye tage and saves the chapter/figure
        blocks = re.findall(tag, text)
        chapter = []
        figure = []
        for x in blocks:
            chapter.append(x[0])
            figure.append(x[1])

        # regex to split for editor code insert
        regex2 = '<p>&lt;popeye-image&gt;c[0-9]+f[0-9]+&lt;\/popeye-image&gt;<\/p>'
        tag2 = re.compile(regex2)
        blocks2 = re.split(regex2, text)

        # assemble html with editor
        count = 0

        finalfile = open(docs_src + 'm' + chNum + '.html', 'w')
        for x in range(0, len(blocks2) - 1):
            finalfile.write(blocks2[count] + '<br>\n')
            imageNumberTemp = str((int)(figure[count]) + 1)
            finalfile.write('Image ' + imageNumberTemp + '\n<br>\n')
            imgtag = ''
            try:
                imgtag += '<img id="img'
                imgtag += imageNumberTemp
                imgtag += '" width="500" height="338" src="'
                imgtag += listings.get_cache(chapter[count], (int)(figure[count]) + 1)
                imgtag += '"></img>'
                # imgtag += '<object id="pdf'
                # imgtag += imageNumberTemp
                # imgtag += '" width="500" height="338" type="application/pdf" data="'
                # imgtag += listings.get_cache(chapter[count], (int)(figure[count]) + 1)
                # imgtag += '"></object>'
                finalfile.write(imgtag + "\n<br>")
            except KeyError:
                imgtag += 'print "listing c' + str(chapter[count]) + 'f' + \
                str(figure[count]) + ' missing"'
                finalfile.write(imgtag + "\n<br>")
            count += 1

        finalfile.write(blocks2[count])
        finalfile.close()
        ###########

        # insert top level listing
        topListing = open('edit-window/toplevel.html', 'r')
        topListingText = topListing.read()
        topListing.close()
        topListingText = '</title>' + topListingText

        f = open(docs_src + 'm' + chNum + '.html', 'r')
        contents = f.read()
        f.close()

        contents = contents.replace("</title>", topListingText)

        f = open(docs_src + 'm' + chNum + '.html', 'w')
        f.write(contents)
        f.close()
