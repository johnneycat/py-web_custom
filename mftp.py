from ftplib import FTP as mftp


'''
download from ftp server
'''

'''
def writeline(data):
    fd.write(data + '\n')


f = mftp('ftp.kernel.org')
print 'Welcome: ', f.getwelcome()
f.login()
print 'passwd: ', f.pwd()
#jump to x dictionary
f.cwd('/pub/linux/kernel')
#store in local folder
fd = open('READ', 'wt')

f.retrlines('RETR README', writeline)
fd.close()

f.quit()
'''

'''
upload to ftp server
'''

import sys, getpass, os.path

#host, user, localfile, remotepath = sys.argv[1:]
host = 'ftp.kernel.org'
user = 'anonymous'
localfile='READ'
remotepath = '/pub/linux/kernel'
passwd = getpass.getpass("Enter passwd: ")
f = mftp(host)
f.login(user, passwd)

f.cwd(remotepath)
try:
    fd.open(localfile,'rb')
except e:
    print e.

f.storbinary('STOR %s' % os.path.basename(localfile), fd)
fd.close()

f.close()
