import sys
import os.path
from os import listdir
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class listings(object):

    def __init__(self):
        self.listings = dict()
        self.listing_cache = dict()
        self.imports = dict()

        dirs = [d for d in listdir(
            './default_code') if os.path.isdir(os.path.join('./default_code', d))]
        for d in dirs:
            files = [
                f for f in listdir('./default_code/' + d) if os.path.isfile(
                    os.path.join('./default_code/' + d, f))]
            for f in files:
                try:
                    myfile = open(os.path.join('./default_code/' + d, f), 'r')
                    data = myfile.readlines()

                    start = data.index('# Imports\n') + 1
                    end = data.index('# Endports\n')
                    self.imports[f] = ''.join(data[start:end]).strip()

                    start = data.index('# Begin\n') + 1
                    end = data.index('# End\n')
                    self.listings[f] = ''.join(data[start:end]).strip()
                except ValueError:
                    print('[listings] warning: ignoring %s' % f)

            if os.path.isdir(os.path.join('./default_code/' + d + '/img_cache/')):
                chapter = d.split('_')[1]
                cache_files = [f for f in listdir(os.path.join('./default_code/' + d + '/img_cache/')) if os.path.isfile(os.path.join('./default_code/' + d + '/img_cache/' + f))]
                for f in cache_files:
                    try:
                        listing_number = f.split('_')[2].split('.')[0]
                        self.listing_cache['%s_%s' % (chapter, listing_number)] = os.path.join('../../default_code/' + d + '/img_cache/' + f)
                    except (IndexError, ValueError):
                        print('[listings cache] warning: ignoring %s' % f)


    def parse(self, fstr):
        """
        Returns a string representation of a chapter figure.

        Attributes:
            fstr (string): string of format c11f1, where 11 is the chapter and
                           1 is the figure

        Returns:
            string: the chapter figure
        """
        chapter = fstr.split('f')[0][1:]
        fig = fstr.split('f')[1]
        return self.listings['Listing_%s_%s.py' % (chapter, fig)]


    def get(self, chapter, fig):
        """
        Returns a string representation of a chapter figure.

        Attributes:
            chapter (int): the chapter number
            fig (int): the figure number

        Returns:
            string: the chapter figure
        """
        return self.listings['Listing_%s_%s.py' % (str(chapter), str(fig))]


    def get_cache(self, chapter, fig):
        """
        Returns a string representation of a chapter figure.

        Attributes:
            chapter (int): the chapter number
            fig (int): the figure number

        Returns:
            string: path to the listing pdf
        """
        return self.listing_cache['%s_%s' % (str(chapter), str(fig))]


    def get_imports(self, chapter, fig):
        return self.imports['Listing_%s_%s.py' % (str(chapter), str(fig))]
