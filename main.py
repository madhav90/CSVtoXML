import csv
import re

csvFile = 'myCSV.csv'
xmlFile = 'myXML.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<PolicySynchronizationProcess>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        for i in range(len(tags)):
            tags[i] = re.sub('[^A-Za-z0-9]+', '_',tags[i])

    else:
        xmlData.write('<PolicySynchronization>' + "\n")
        for i in range(len(tags)):
            if row[i]:
                xmlData.write('    ' + '<' + tags[i] + '>' \
                              + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</PolicySynchronization>' + "\n")

    rowNum += 1

xmlData.write('</PolicySynchronizationProcess>' + "\n")
xmlData.close()