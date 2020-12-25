import camelot
tables = camelot.read_pdf('invoice.pdf')
print(tables)
tables.export('saas.csv', f='csv', )
tables[0].to_json('saas.json')
