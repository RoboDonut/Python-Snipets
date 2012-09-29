import urllib2,json
outFile=open(r"C:\ScratchWorkSpace\dummy.csv",'w')
URL= 'http://gis.deq.ok.gov/ArcGIS/rest/services/WaterWeb/MapServer/8/query?where=1%3D1&time=&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=*&f=json'
response = urllib2.urlopen(URL)
data = json.load(response)
#print json.dumps(data,sort_keys = True, indent = 4)
returnedCount =  len(data["features"])
print "Total records returned: {0}\n".format(returnedCount)
fields =  data["fieldAliases"]
numFields = len(fields)
outFile.write("FID"+",")
for key in fields:
    print key
    outFile.write(key+",")
outFile.write("\n")
count=0
for x in range(0,returnedCount):
    outFile.write(str(count)+",")
    count+=1
    #print data["features"][x]["attributes"]
    #print data["features"][x]["geometry"]
    #print "************************"
    for key,value in data["features"][x]["attributes"].iteritems():
        print key, value
        outFile.write(str(value).replace(","," ")+",")
    print"-------------------------"
    outFile.write("\n")