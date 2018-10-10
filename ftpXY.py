import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'
def main():
    try:
        f=ftplib.FTP(HOST)
    except:
        print('Error:cannnot reach "%s"' %HOST)
        return
    print('***contected to host "%s"' %HOST)
    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR:cannot login anonymously')
        f.quit()
        return
    print('***login in as "anonymously"')
    try:
        f.cwd(DIRN)
    except:
        print('ERRPR:cannot CD to "%s"'%DIRN)
        f.quit()
        return
    print('change to "%s" folder'%DIRN)
    try:
        f.retrbinary('RETR %s' %FILE,open(FILE,'wb').write())
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"'%FILE)
        os.unlink(FILE)
    else:
        print('***Download "%s" to CWD'%FILE)
        f.quit()


main()


