# -*- coding: utf-8 -*-
"""
Tools for gathering and analyzing data from Google Sheets instances of VES metadata survey worksheets
===================

"""

import requests
import pandas as pd

__author__ = 'Joseph Goldstone'
__copyright__ = 'Copyright (C) 2021 Arnold & Richter Cine Technik GmbH & Co. Betriebs KG'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Joseph Goldstone'
__email__ = 'jgoldstone@arri.com'
__status__ = 'Experimental'

__all__ = [
]
UR_SHEET_URL = 'https://docs.google.com/spreadsheets/d/10QmFiN34oBgRuPfNd_HwOJos8hDmG9MS9j6CmCEDFv8/export?format=csv&gid=0'


class VESWorksheet(object):
    def __init__(self, url):
        self.url = url
        # r = requests.get(url)
        # self.url = url + '/export?format=csv&gid='
        # self.url = url.replace("/edit#gid=", "/export?format=csv&gid=")
        self.df = pd.read_csv(self.url, skiprows=24, nrows=5)
        print('foo')


if __name__ == '__main__':
    s = VESWorksheet(UR_SHEET_URL)
    print('read worksheet')
