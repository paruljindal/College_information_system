import csv
header = ["id","Name","Address","Website","Instate-On campus","Instate-Off campus","Instate-Off Campus with Family","Outstate-On campus","Outstate-Off campus","Outstate-Off Campus with Family"]
with open(r'collegedata.csv', 'w', newline = '') as fp:
    a = csv.writer(fp, delimiter = ',')
    a.writerow(header)
    fp.close()        
    
