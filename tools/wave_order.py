#!/usr/bin/env python3
"""Print talk folders in publishing order, from the "Publishing waves" sheet of category_mapping.xlsx.

Usage: wave_order.py                 every talk, wave by wave
       wave_order.py --wave 3        the talks of wave 3
       wave_order.py --waves 2-10    the talks of waves 2 to 10
       wave_order.py --table         wave, order and talk, one per line

Reads the workbook with the standard library only (no openpyxl), so it runs in any Python 3.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent / 'category_mapping.xlsx'
SHEET = 'Publishing waves'
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}


def rows():
    """The sheet's rows as lists of cell strings."""
    z = zipfile.ZipFile(BOOK)
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', NS):
            shared.append(''.join(t.text or '' for t in si.iter(f'{{{NS["m"]}}}t')))
    book = ET.fromstring(z.read('xl/workbook.xml'))
    rid = next(s.get(f'{{{NS["r"]}}}id') for s in book.find('m:sheets', NS) if s.get('name') == SHEET)
    rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    target = next(r.get('Target') for r in rels if r.get('Id') == rid).lstrip('/')
    sheet = ET.fromstring(z.read(target if target.startswith('xl/') else 'xl/' + target))
    for row in sheet.iter(f'{{{NS["m"]}}}row'):
        cells = {}
        for c in row.findall('m:c', NS):
            col = re.match(r'[A-Z]+', c.get('r')).group()
            v = c.find('m:v', NS)
            if c.get('t') == 's' and v is not None:
                val = shared[int(v.text)]
            elif c.get('t') == 'inlineStr':
                val = ''.join(t.text or '' for t in c.iter(f'{{{NS["m"]}}}t'))
            else:
                val = v.text if v is not None else ''
            cells[col] = val
        width = max((ord(k[-1]) - 64 for k in cells), default=0)
        yield [cells.get(chr(65 + i), '') for i in range(width)]


def waves():
    """[(wave, order, talk)] in publishing order."""
    it = rows()
    head = next(it)
    iw, io, it_ = head.index('Wave'), head.index('Order'), head.index('Talk folder')
    out = []
    for r in it:
        if len(r) > it_ and r[iw] and r[it_]:
            out.append((int(float(r[iw])), int(float(r[io])), r[it_].strip()))
    return sorted(out)


def main(argv):
    lo, hi = 1, 10 ** 6
    if '--wave' in argv:
        lo = hi = int(argv[argv.index('--wave') + 1])
    if '--waves' in argv:
        a, b = argv[argv.index('--waves') + 1].split('-')
        lo, hi = int(a), int(b)
    for w, o, talk in waves():
        if lo <= w <= hi:
            print(f'{w}\t{o}\t{talk}' if '--table' in argv else talk)


if __name__ == '__main__':
    main(sys.argv[1:])
