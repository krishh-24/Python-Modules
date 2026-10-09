# 1. first type " git init " for adding git in your folder.

# 2. to add or upload all the file type "git add ." or 
# for uploading particular file type " git add file_name " with that it will upload to your repo.

# 3. whenever you puah or uplOad new things in git you have to commit for that just by giving them little description about what you have changed. 
        # type: " git commit -am whatever-message you want to type "
        # ex: git commit -am module-1

 # 4. After that you have to create an remote folder or environment for work in git. this will create an remote environment to the git that connects your local computer folders and files into remote environment so that git also work with that
        # type: git remote add origin url-ofyour repo.git
        # ex: git remote add origin https://github.com/krishh-24/Python-Modules.git

# 5.check that remote is created succesfully or not, if this will success then it shows you 2 lines push and fetch.
    # git remote -v 
    
# 6. Now finally all set you can push your folder or fies to git repo/
        # git push origin branch-name 