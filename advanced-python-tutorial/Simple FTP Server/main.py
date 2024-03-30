# pip install twisted

from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("lUc1f3r11", "123456")
checker.addUser("someuser", "123456")

portal = Portal(FTPRealm("./public"), [AllowAnonymousAccess()])
factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()

