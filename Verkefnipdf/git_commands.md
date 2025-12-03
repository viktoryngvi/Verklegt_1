Git commands

- git add
  1. git add . = bætir öllum skrám í möppunni í stage-ið 
  2. git add <file> =  bætir bara file-inum sem þú velur

- git commit
  1. git commit = þarft síðan að skrifa inn í inputtið til að halda áfram í næsta skref.
  2. git commit -m = bil eftir m og skrifar svo skilaboð inní "" getur líka verið með -m -m til að hafa mörg skilaboð
  3. git commit file1 file2 = til að velja skrár sem þú vilt committa
  4. getur breytt committi seinna meir með git commit

- git branch
  1. git branch = sýnir þér þín branches með * hjá því sem þú ert í
  2. git branch = sýnir þér öll branches
  3. git branch <branch_name> = býr til nýjan branch
  4. git branch -d <branch_name> = eyðir branchi ef það er full merge-að
  5. git checkout <branch) = færir þig í það branch
  6. git log = sýnir öll commit í þessu branchi

- git rm
  1. git rm <file> eyðir file

- git clean
  1. git clean -n = sýnir hverju myndi vera eytt
  2. git clean -f = eyðir untracked files
  3. git clean - d = eyðir ócommituðum skrám

- git status
  1. git status = sýnir þér hvaða branch þú ert á og hvort þú ert með eitthvað til að commita

- git reset
  1. git reset hendir öllum local breytingum og syncar þig við remote repository.

- git rebase
  1. git rebase setur þínar breytingar ofan á það sem er í skjalinu

- git push
  1. git push færir allar breytingar frá þínu local repository yfir í remote repository-ið

- git pull
  1. git pull tekur breytingar frá remote repository og setur það á local








