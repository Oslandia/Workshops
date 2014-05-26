import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

app = QApplication(sys.argv)
w = QTableView()
qm = QSqlQueryModel()

# DB type, host, user, password...
db = QSqlDatabase.addDatabase("QPSQL");
db.setHostName("lsnpgt01")
db.setDatabaseName("voiriegeo")
db.setUserName("voiriegeo_adm")
db.setPassword("Ls3Qt6msjmok")
ok = db.open()

# True if connected
if ok:
	print 'Connected to Postgresql'
else:
	print 'Postgresql'

# do a query "on" a DB connection
qm.setQuery("""select 
    id, no_parc, type
from
    geo_parc_pol as t
where
    st_dwithin(the_geom, st_setsrid(st_makepoint(%s, %s), 21781), 100)
limit 100""" % (538000, 154000))
w.setModel(qm)
w.show()
sys.exit(app.exec_())
