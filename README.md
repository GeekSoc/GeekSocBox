GeekSocBox
==========

Cloud Storage System/FTP client: Created Hackathon October 2013

Needed Python2

Master branch is a dropbox "like" cloud storage system that works with a user's geeksoc account. It is very incomplete and
buggy :/ (do not use unless you want to try and fix it :P) It works by using a file list and the time of when the file was
last editted. It checks the lists and when something has changed it uploads the updated file to the geeksoc server. It
does not do new files added to the directory the program is running from. It currently hangs up on uploads which makes me
believe it is a \n error or something like that.

FTPClient branch is a tiny ftp client that allows a use to enter in server, port number, username and password and transfer
any file via command line to their geeksoc home directory.
