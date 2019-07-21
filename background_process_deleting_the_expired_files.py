import os
import MySQLdb
from datetime import datetime
format = '%Y-%m-%d %H:%M:%S'
db = MySQLdb.connect(host="localhost", user="pavan", passwd="pavank830", db="Records")
cur = db.cursor()
initialtime = datetime.strptime('1900-01-01 00:00:00', format)
secondtime = datetime.strptime('2000-02-01 22:40:30', format)
while True:
  cur.execute("""select path from File_Table 
				where exptime LIKE %s""",(initialtime.strftime('%Y-%m-%d %H:%M:%S'),))
  for path1 in cur.fetchall():
	try:
         os.remove(path1[0])
	except:
 	 pass
  cur.execute("""delete from File_Table where 
				exptime LIKE %s""",(initialtime.strftime('%Y-%m-%d %H:%M:%S'),))
  db.commit()#so that the changes are stored permanently in database
  cur.execute("select starttime,exptime from File_Table order by exptime")
  for row in cur.fetchall():
       dt1 = datetime.strptime(str(row[1]), format)
       dt0 = datetime.strptime(str(row[0]), format)
       now = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),format)

       if((dt1-dt0).total_seconds()==0):
	      continue
              
       elif(((dt1-now).total_seconds()<=0) and (dt0 != initialtime)and(dt0 != secondtime)):
	      print("ffff")
              cur.execute("""select path from File_Table 
				where exptime LIKE %s""",(dt1.strftime('%Y-%m-%d %H:%M:%S'),))
              for path in cur.fetchall():
	         pass
              cur.execute("""delete from File_Table where 
				exptime LIKE %s""",(dt1.strftime('%Y-%m-%d %H:%M:%S'),))
	      try:
               os.remove(path[0])
	      except:
 	       pass
       db.commit()#so that the changes are stored permanently in database
       break
db.close()
