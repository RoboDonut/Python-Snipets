import urllib2,json
outFile=open(r"C:\ScratchWorkSpace\dummy.csv",'w')
URL = 'http://watersgeo.epa.gov/ARCGIS/REST/services/OWRAD/TMDL_WMERC/MapServer/0/query?text=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&where=1%3D1&returnGeometry=true&outSR=&outFields=*&f=pjson'
#URL= 'http://gis.deq.ok.gov/ArcGIS/rest/services/WaterWeb/MapServer/8/query?where=1%3D1&time=&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=*&f=json'
response = urllib2.urlopen(URL)
data = json.load(response)
#print json.dumps(data,sort_keys = True, indent = 4)
returnedCount =  len(data["features"])
print "Total records returned: {0}\n".format(returnedCount)
spRef =  data["spatialReference"]
# the wkid var hold the string for the well known ID of a projection. use this value to look up the projection parameters from the prj.csv
wkid = spRef["wkid"]
# put your csv dictionary in the dictionaryCSV va
dictionaryCSV = {wkid:"your code to convert csv to distionary"}
# Add code to look up wkid in teh csv and return the parameters as a sting
prjString = dictionaryCSV[wkid]
print prjString
print"_______________________"
# commented out so you dont have to print all the features
#fields =  data["fieldAliases"]
#numFields = len(fields)
#outFile.write("FID"+",")
#for key in fields:
    #print key
    #outFile.write(key+",")
#outFile.write("\n")
#count=0
#for x in range(0,returnedCount):
    #outFile.write(str(count)+",")
    #count+=1
    ##print data["features"][x]["attributes"]
    ##print data["features"][x]["geometry"]
    ##print "************************"
    #for key,value in data["features"][x]["attributes"].iteritems():
        #print key, value
        #outFile.write(str(value).replace(","," ")+",")
    #print"-------------------------"
    #outFile.write("\n")