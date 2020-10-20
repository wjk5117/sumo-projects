#!/usr/bin/python
#parameters
outfile = "sumoolympicWalks.rou.xml"
startEdge = "beg"
endEdge = "end"
departTime = 0. #time of departure
departPos = -30. #position of departure
arrivalPos = 100. #position of arrival
numberTrips = 100 #number of persons walking
#generate XML
xml_string = "<routes>\n"  
for i in range(numberTrips):
    xml_string += '    <person depart="%f" id="p%d" departPos="%f" >\n' % (departTime, i, departPos)
    xml_string += '        <walk edges="%s %s" arrivalPos="%f"/>\n' % (startEdge, endEdge, arrivalPos)
    xml_string += '    </person>\n'
xml_string += "</routes>\n"
with open(outfile, "w") as f:
    f.write(xml_string)