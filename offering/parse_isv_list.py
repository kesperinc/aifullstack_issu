import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import json

excel_path = Path(r"C:\Users\MZC01-SUNKIM317\Downloads\Master ISV Partner List_Contacts_Final의 사본.xlsx")
out_path = Path("offering/isv_partners_summary.json")

with zipfile.ZipFile(excel_path, 'r') as z:
    shared_strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
            t_el = si.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t')
            shared_strings.append(''.join([t.text for t in t_el if t.text]))

    wb_tree = ET.fromstring(z.read('xl/workbook.xml'))
    sheet_names = [s.attrib.get('name') for s in wb_tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet')]

    def get_sheet_data(sidx):
        s_xml = f'xl/worksheets/sheet{sidx}.xml'
        if s_xml not in z.namelist(): return []
        stree = ET.fromstring(z.read(s_xml))
        rows = []
        for r in stree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            row_vals = []
            for c in r.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                v_tag = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                t_attr = c.attrib.get('t')
                val = ''
                if v_tag is not None and v_tag.text:
                    val = shared_strings[int(v_tag.text)] if t_attr == 's' else v_tag.text
                row_vals.append(val)
            if any(row_vals):
                rows.append(row_vals)
        return rows

    result = {}
    for idx, sname in enumerate(sheet_names, 1):
        rows = get_sheet_data(idx)
        result[sname] = rows

with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"ISV data saved to {out_path}, sheets: {len(result)}")
