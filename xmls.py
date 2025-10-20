import xml.etree.ElementTree as et

def findx(file):
 collect=[]
 xm=et.parse(file)
 r=xm.getroot()
 current= None
 for test in r.iter():
   if test.tag == "PO":
     if current:
       collect.append(current)
     po=test.text
     current={"PO":po,"OrderID":None,"ProductID":[]}

   elif test.tag=="OrderID":
     if current:
       current["OrderID"]=test.text

   elif test.tag=="ProductID":
     if current:
       PID=test.text
       current["ProductID"].append(PID)
   
 if current:
   collect.append(current)
 
 return(collect)
 

