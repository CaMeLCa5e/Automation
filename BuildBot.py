c['status'] = []

from buildbot.status import html
from buildbot.status.web import authz, auth

authz_cfg=authz.Authz(
	#change to true to enable function
	auth=auth.BasicAuth([("pyflakes", "pyflakes")]),
	gracefulShutdown = False, 
	forceBuild = 'auth', #use this to test slave
	pingBuild = False,
	stopBuild = False, 
	stopAllBuilds = False, 
	cancelPendingBuild = False
)
c['status'].append(html.WebStatus(http_port=8010, authz_cfg))

from buildbot.scheduler import Try_Userpass
c['schedulers'].append(Try_Userpass(
									name = 'try'
									builderNames=['runtests'],
									port=5555,
									userpass=[('sampleuser', 'samplepass')]))










