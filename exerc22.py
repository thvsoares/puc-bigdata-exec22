import mincemeat
import glob
import csv

data_files = glob.glob('C:\\Temp\\Join\\Data\\*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()
    
source = dict((file_name, file_contents(file_name))for file_name in data_files)

def mapfn(k,v):
    print 'map ' + k
    for line in v.splitlines():
        if k == 'C:\\Temp\\Join\\Data\\2.2-vendas':
            yield line.split(';')[0], 'Vendas' + ':' + line.split(';')[5]
        if k == 'C:\\Temp\\Join\\Data\\2.2-filiais':
            yield line.split(';')[0], 'Filial' + ':' + line.split(';')[1]

def reducefn(k, v):
    print 'reduce ' + k
    return v

s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="p4ssw0rd")

w = csv.writer(open("C:\\Temp\\Arq_Exerc\\result.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])