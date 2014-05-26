import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
w = QTextBrowser()

# DB type, host, user, password...
db = QSqlDatabase.addDatabase("QPSQL");
db.setHostName("lsnpgt01")
db.setDatabaseName("voiriegeo")
db.setUserName("voiriegeo_adm")
db.setPassword("Ls3Qt6msjmok")
ok = db.open()

# True if connected
if ok:
	w.insertHtml('Connected to Postgresql<br />')
else:
	w.insertHtml('Postgresql<br />')

# do a query "on" a DB connection
query = QSqlQuery(db)
x, y = 538000, 154000
if query.exec_("""
select 
    id, no_parc, type
from
    geo_parc_pol as t
where
    st_dwithin(the_geom, st_setsrid(st_makepoint(%s, %s), 21781), 100)
limit 100
""" % (x, y)):
	w.insertHtml('<br />')
	while query.next():
	    w.insertHtml(query.value(0).toString() + \
                " " + query.value(1).toString() + \
                " " + query.value(2).toString() + "<br />")
	
	w.insertHtml('TOTAL %s ELEMENTS' % query.size())

w.show()
sys.exit(app.exec_())

