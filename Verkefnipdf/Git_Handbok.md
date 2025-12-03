


GitHub Desktop. Notendahandbók.
(Daglegt vinnuflæði er neðst.)

Inngangur:

GitHub er netþjónusta sem notendum kleift að geyma, deila og vinna með kóða með öðrum á öruggan og skipulagðan hátt:

-	Vista verkefni miðlægt á netinu (remote repositories).
-	Fylgjast með öllum breytingum sem gerðar eru í skrám.
-	Vinna í teymi án þess að skrifa yfir kóða hjá öðrum.
-	Búa til branches til að vinna með og prófa nýjar hugmyndir.
-	Sameina breytingar með Pull Requests.
-	Geyma afrit (backup) af kóðum í skýinu.
-	Skoða sögu verkefnis og sjá nákvæmlega hvað breyttist hvenær.
-	Birta verkefni eða halda þeim private.

Basic workflow:

Basic Order of Git Commands (Correct Sequence)
1. git pull
Always start by getting the newest version of the project.

2. Make your changes
Edit or add files.

3. git add .
Mark all changed files to be included in the next commit.

4. git commit -m "message"
Save your changes as a snapshot with a clear message.

5. git push
Send your committed changes to GitHub.

Nánar:

1. Setja upp GitHub Desktop
- Fara á: https://desktop.github.com
- Sækja og setja upp
- Búa til GitHub aðgang

2. Búa til nýtt verkefni (Repository)
File > New Repository
Býr til nýtt Git-repo á tölvunni (local). Git fer að fylgjast með skrám og breytingum í möppunni sem þú velur.

2.1. File > New Repository
2.2. Gefðu verkefninu nafn
2.3. Veldu möppu á tölvunni
2.4. Ýttu á Create Repository

3. Klóna (Clone) verkefni af GitHub
File > Clone Repository
Sækja verkefni sem er á GitHub niður á tölvuna þína og tengir GitHub Desktop við það.

4. Breyta skrám og Commit-a
Git fylgist með öllum breytingum sem þú gerir í skrám.

Commit message:
Stutt lýsing á breytingunum sem þú gerðir.

Commit to main:
Vista breytingarnar inn í verkefnið.

5. Push og Pull
Sendir commit-in þín á GitHub.

Fetch origin:
Athugar hvort það séu nýjar breytingar á GitHub.

Pull:
Sækir nýjustu breytingar og uppfærir branchið.

6. Branches (útibú)
Current Branch > New Branch:
Býr til nýtt útibú til að vinna í nýjum eiginleika án þess að trufla main.

Merge into Current Branch:
Sameinar breytingar úr öðru branchi inn í það sem þú ert í.

7. Eyða branches
Branch > Delete:
Eyðir útibúi sem er búið að merge-a og þú þarft ekki lengur.

8. History
Sýnir öll commit, hver gerði þau og hvaða breytingar urðu.

9. Undo / Mistök
Undo last commit:
Tekur nýjasta commit til baka án þess að tapa breytingunum.

Discard changes:
Hendir nýjustu breytingum á skrá og endurstillir hana.

Undo discard:
Nær aftur í breytingar sem þú hendir óvart.

10. Publish Repository
Sendir local repo upp á GitHub.

          Hvað þarf að varast þegar unnið er í Git:

Ekki vinna beint í main
Main á alltaf að vera stöðug og keyrsluhæf útgáfa. Breytingar eiga að fara í sér-branches.

Ekki gera stórar breytingar án þess að búa til branch
Allar nýjar síður, eiginleikar eða tilraunir ættu að fara í eigin branch til að forðast ringulreið.

Varast að sameina (merge) óreyndar breytingar inn í main
Athugaðu kóða og prófaðu áður en þú sameinar. Pull Request er best.

Ekki gera of stór eða ruglingsleg commit
Gerðu lítil, skýr commit með góðum skilaboðum. Auðveldara að rekja villur.

Passaðu að pull-a áður en þú push-ar
Ef þú push-ar án þess að sækja nýjustu breytingarnar getur það valdið árekstrum.

Ekki henda breytingum óvart með „discard changes“ án þess að vera viss
Þetta eyðir breytingum varanlega – nema hugsanlega ef gert er strax „Undo discard“.

Varastu merge conflict
Forðastu þau með því að vinna skipulega, uppfæra branch-ið þitt reglulega og halda commit-um litlum.

Ekki eyða branches fyrr en þau eru merge-aðar
Annars getur þú misst breytingar.

          Daglegt vinnuflæði:

Daglegt vinnuflæði fyrir grunnnotanda í Git er alltaf í sömu röð og tryggir að verkefnið haldist stöðugt og skipulagt.  
PULL          Fyrst er alltaf kallað í git pull til að sækja nýjustu útgáfu verkefnisins áður en byrjað er að vinna.  
Þá er búið til branch til að vinna í svo main haldist stöðug.  
ADD > COMMIT  Þegar búið er að vinna í skránum eru breytingarnar merktar með git add og vistaðar með git commit ásamt stuttum skilaboðum.  
PUSH          Að lokum eru breytingarnar sendar upp á GitHub með git push. Þar býr notandinn til Pull Request sem biður um að kóðinn verði sameinaður í main.  

Pull Request er annað hvort samþykktur eða hafnaður af yfirferðaraðila (t.d. senior developer).
Ef hann er samþykktur er kóðinn sameinaður inn í main.
Ef hann er hafnaður þarf notandinn að gera breytingar, commit-a aftur og push-a, þá uppfærir Pull Request sig sjálfkrafa þar til hann er samþykktur.
