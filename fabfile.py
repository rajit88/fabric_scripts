from fabric.api import local
def prepare_deploy():
 local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_scripts && touch file1 file2 file3")
 local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_scripts && git add . && git commit -m test")
 local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_scripts && git push origin master")



