Requirements A

Players - Aðeins einn leikmaður í einu liði. Nafn, fæðingardagur, heimilisfang, símanumer, email, social media URL, notendanafn og lið.

Teams - Hvert lið fær nafn og fyrirliða (sem þarf að vera leikmaður í liðinu), Fyrirliðar þurfa að geta bætt leikmönnum, Fyrirliðar geta breytt leikmönnum í sínu líði, Einnig hægt að bæta inn önnur gögn eins og logo eða link á heimasíðu.

Organizer - Einn admin account sem getur bætt við nýjum liðum og planað mót. Aðeins ein týpa af leik getur verið spilað í einu móti.

Tournament - Organizer getur búið til ný mót. Hvert mót þarf að hafa byrjunar dag og lokadag, sér nafn, staðsetningu, og skráð manneskja til að hafa samband við varðandi mótið með email og símanumer. Allir leikir þurfa að vera skráðir eftir byrjunardaginn og fyrir lokadag. 

Tournament - knock out style, þegar eitt lið vinnur fer það áfram og hitt er hent út. The organizer eða sá sem sér um að plana mótið getur búið til skipulagið um leið og öll gögn eru skráð t.d lið og leikmenn. ( þegar buið er að setja upp skipulag er hægt að gera ráð fyrir því að ekki er hægt að gera breytingar á liði eða leikmönnum)

Games and results - The organizer þarf að setja inn úrslit á leikjum. Eftir að niðurstöður eru skráðar þá er hægt að sjá niðurstöður frá nýjustu leikjum.

Information retrieval - Allir eiga að geta séð leikjaplanið. Þeir leikjir sem eru búnir eiga að sýna niðurstöður ef leikur er ekki búinn ætti það að sýna hver er að spila eða hverjir eru að fara spila og hvenær leikurinn verður spilaður. Hver sem er á að geta skoðað upplýsingar um önnur lið og hvaða leikmenn þeir hafa og mótin sem þeir hafa tekið þátt í. ( Allir eiga að geta séð nafn leikmanns og username en alls ekki persónulegar upplýsingar, aðeins the organizer og fyrirliðar geta seð persónuupplýsingar)

Captain - Sér um að skrá leikmenn hvert lið má hafa 3-5 leikmenn. ( til að skrá leikmenn þarf að kalla í players fall sem sér um að skrá leikmenn)

Mikilvæg atriði: 

- Hver leikur þarf að hafa dagssetningu, timasetningu og serverID (þar sem leikurinn er spilaður) 
- Lið getur ekki spilað tvo sitthvora leiki á sama tíma
- Kerfið skal takmarka fjölda samtímis leikja út frá fjölda tiltækra netþjóna




User Groups 

- Administator/Organizer
- Team Captain
- Player
- Spectator/Public User


-------------------------------------------------------------------------------
Funcional requirements

| Number    |    Descripton   |    User group    |    Priority    |   Additional info |
|-----------|------------|------------------|----------------|-------------------|
| R1  |  Register a new player  |  Organizer, Team captain  |  A  |  Player must belong to exactly one team |
| R2  |  View player profile(name and handle)  |  All users  |  A  |  Private info hidden | 
| R3  |  Edit player personal information  |  Team Captain,Organizer  |  A  |  Captain can only edit players in own team |
| R4  |  Create a new team  |  Organizer  |  A  |  Team name must be unique |
| R5  |  Assign a captain to a team  |  Organizer  |  A  |  Captain must be a player in the team |
| R6  |  Add players to team  |  Team captain  |  A  |  Must be 3-5 players |
| R7  |  Create a new tournament  |  Organizer  |  A  |  Requires name, start date, end date, venue or location |
| R8  |  View tournament information  |  All users  |  A  |  schedule and games |
| R9  |  Register teams into a tournament  |  Organizer  |  A   | 16 teams mininum, no changes after schedule creation |
| R10  |  Generate knockout tournament schedule  |  Organizer  |  A  |  schedule must respect server limitations | 
| R11  |  Prevent teams from playing two matches at the same time  |  System  |  A  |  Logical constraint |
| R12  |  Assign date, time and server to each match  |  System  |  A  |  Server availability |
| R13  |  Enter match results  |  Organizer  |  A  |  Update standings |
| R14  |  View match results and completed matches  |  All users  |  A  |  completed matches show results |
| R15  |  View scheduled games and ongoing games  |  All users  |  A  |  If match has not started show scheduled time and who is playing, if game has started show who is playing |
| R16  |  Restrict personal players information to authorized users only  |  System  |  A   | Only organizers and the team captains |


Non functional requirements

| Number | Description | Priority | Additional Info |
|--------|-------------|----------|-----------------|
| N1  |  The system should not crash on invalid input  |  A  |  Show error message |
| N2  |  The UI should be text based  |  A  |  Required |
| N3  |  3 tier architecture  |  A  |  UI,Logic,Data layers |
| N4  |  Data will be stored in text based files  |  A  |  CSV or JSON |


