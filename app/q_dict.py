question_id_dict = {
    '153515210':'date ', # Datum för genomgången
    '153515905':'afNum', # ÅF-nummer
    '153518228':'creator', # Skaparen av denna analys (ditt namn)
    '153519605':'orgNum', # Org. nummer
    '158321490':'CompName', # Företagets namn:
    '158321564':'CompContact', # Kontaktpersonens Namn:
    '158321689':'CompEmail', # Kontaktpersonens mailadress:
    '158321819':'CompPhone', # Kontaktpersonens telefonnummer:
    '141491927':'q1', # Hur vill ni att <span style="text-decoration: underline;">era</span> kunder ska uppfatta ert val av bilar?
    '141247144':'q2', # Hur viktigt är det att bilarna matchar ert varumärke? (På en femgradig skala där 1 = "Inte alls viktigt" till 5 = "mycket viktigt")
    '141503254':'q3', # Vad är er image och vad vill ni kommunicera med bilarna?
    '141509234':'q4', # Hur nöjda är ni med hur era nuvarande bilar matchar ert varumärke? (1 = "mycket missnöjda" och 5 = "mycket nöjda")
    '146066689':'q5', # Stripar ni några av bilarna?
    '141513327':'q6', # Vilka bilar stripar ni? Hur stripas dom? Vem stripar dem? Kostnad?
    '141248946':'q7', # Hur viktigt är det att minimera bilarnas miljöpåverkan? ( 5 = mycket viktigt)
    '141558341':'q8', # Hur påverkas er verksamhet av bilarnas miljövänlighet?
    '141561121':'q9', # Har ni några mål eller krav kring bilarnas miljöpåverkan? (Tips: Co2, kolväten, partiklar, dubbdäck)
    '141247180':'q10', # Hur nöjda är ni med nuvarande vagnparks miljöpåverkan? ( 5 = "mycket nöjda")
    '141567830':'q11', # Vad är det ni inte är nöjda med och har ni några planer på att åtgärda detta?
    '141508263':'q11-1', # Vad är det ni inte är nöjda med med och planerar ni att åtgärda detta?
    '141247178':'q12', # Hur viktigt är de för er att ha attraktiva tjänste- och förmånsbilar i rekryteringssyfte? ( 5 = "mycket viktigt")
    '143320255':'q13', # Vad är er arbetsgivarerimage och vad vill ni att era bilar och bilpolicy ska kommuicera till potentiella medarbetare?
    '143320637':'q14', # Vilka roller är svår-rekryterade och hur viktigt är det att kandidaterna inte tackar nej till era jobberbjudanden?
    '143321570':'q15', # Hur viktigt är det att era medarbetare är nöjda med bilarna de får köra? (5 = "mycket viktigt")
    '143322331':'q16', # Har medarbetarna några önskemål på bilpolicyn eller bilarna?
    '143322765':'q17', # Vad har de för önskemål eller klagomål?
    '143322967':'q18', # Vilka säkerhetskriterier har ni för bilarna?
    '141247150':'q19', # Förargrupp 1: Ange en benämning för gruppen förare
    '141247223':'q20', # Omfattning
    '141247224':'q21', # Fordonens huvudsakliga tillhörighet:
    '141247225':'q22', # Krav på bilarna för denna förargrupp?
    '143328921':'q23', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '141247226':'q24', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '141247227':'q25', # Får ni höra klagomål eller synpunkter från dessa förare?
    '143328590':'q26', # Vilka klagomål eller synpunkter? Hur ofta? Planerar ni göra något åt detta?
    '143329541':'q27', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '143330071':'q28', # Vad gör ni för att undvika att dessa förare står utan bil temporärt?
    '143330931':'q29', # Finns det någon annan förargrupp som använder företagets bilar?
    '146996435':'q30', # Förargrupp 2:
    '146996436':'q31', # Omfattning
    '146996437':'q32', # Fordonens huvudsakliga tillhörighet:
    '146996438':'q33', # Krav på bilarna för denna förargrupp?
    '146996439':'q34', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997307':'q35', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997308':'q36', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146997731':'q37', # Vilka klagomål eller synpunkter? Hur ofta? Planerar ni göra något åt detta?
    '146998739':'q38', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146998118':'q39', # Vi har nu identifierat 2 förargrupper. Finns det ytterligare någon förargrupp som använder företagets bilar?
    '146996832':'q40', # Förargrupp 3:
    '146996833':'q41', # Omfattning
    '146996834':'q42', # Fordonens huvudsakliga tillhörighet:
    '146996835':'q43', # Krav på bilarna för denna förargrupp?
    '146996836':'q44', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997377':'q45', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997378':'q46', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146999014':'q47', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146999537':'q48', # Vad gör ni för att undvika att dessa förare står utan bil temporärt?
    '146998129':'q49', # Vi har nu identifierat 3 förargrupper. Finns det ytterligare någon förargrupp som använder företagets bilar?
    '146996880':'q50', # Förargrupp 4:
    '146996881':'q51', # Omfattning
    '146996882':'q52', # Fordonens huvudsakliga tillhörighet:
    '146996883':'q53', # Krav på bilarna för denna förargrupp?
    '146996884':'q54', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997477':'q55', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997478':'q56', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146997872':'q57', # Vilka klagomål eller synpunkter? Hur ofta? Planerar ni göra något åt detta?
    '146999060':'q58', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146998279':'q59', # Vi har nu identifierat 4 förargrupper. Finns det någon annan förargrupp som använder företagets bilar?
    '146997016':'q60', # Förargrupp 5:
    '146997017':'q61', # Omfattning
    '146997018':'q62', # Fordonens huvudsakliga tillhörighet:
    '146997019':'q63', # Krav på bilarna för denna förargrupp?
    '146997020':'q64', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997488':'q65', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997489':'q66', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146997945':'q67', # Vilka klagomål eller synpunkter? Hur ofta? Planerar ni göra något åt detta?
    '146999086':'q68', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146999721':'q69', # Vad gör ni för att undvika att dessa förare står utan bil temporärt?
    '146998324':'q70', # Vi har nu identifierat 5 förargrupper. Finns det någon annan förargrupp som använder företagets bilar?
    '146997078':'q71', # Förargrupp 6:
    '146997079':'q72', # Omfattning
    '146997080':'q73', # Fordonens huvudsakliga tillhörighet:
    '146997081':'q74', # Krav på bilarna för denna förargrupp?
    '146997082':'q75', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997523':'q76', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997524':'q77', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146999113':'q78', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146998355':'q79', # Vi har nu identifierat 6 förargrupper. Finns det någon annan förargrupp som använder företagets bilar?
    '146997114':'q80', # Förargrupp 7:
    '146997115':'q81', # Omfattning
    '146997116':'q82', # Fordonens huvudsakliga tillhörighet:
    '146997117':'q83', # Krav på bilarna för denna förargrupp?
    '146997118':'q84', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997573':'q85', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997574':'q86', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146999163':'q87', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '146998378':'q88', # Vi har nu identifierat 7 förargrupper. Vi har utrymmer för ytterligare en. Finns det någon slutlig förargrupp som använder företagets bilar?
    '146997169':'q89', # Förargrupp 8:
    '146997170':'q90', # Omfattning
    '146997171':'q91', # Fordonens huvudsakliga tillhörighet:
    '146997172':'q92', # Krav på bilarna för denna förargrupp?
    '146997173':'q93', # Finns det några kostnadsbegränsningar för förargruppen (t.ex basbelopp)?
    '146997643':'q94', # Hur och var används dessa bilar i tjänsten? (Speciella behov utöver normal körning)
    '146997644':'q95', # Får ni höra klagomål eller synpunkter från dessa förare?
    '146999194':'q96', # Hur viktigt är det att dessa förare inte står utan bil temporärt? ( 5 = "mycket viktigt")
    '143332461':'q97', # Hur beräknar/mäter ni den verkliga månadskostnaden?
    '143332596':'q98', # Hur länge behåller ni bilarna?
    '143332710':'q99', # Har ni några besparingsmål?
    '143336110':'q100', # Vad är besparingsmålen och har ni planer på att spara in på billösningen?
    '143336422':'q101', # Vad har ni för ägandeform på bilarna?
    '143336915':'q102', # Hur viktigt är det att minimera risken för oväntat låga priser på andrahandsmarknaden?
    '143337159':'q103', # Varför har ni operationell leasing? (Trots att det inte är viktigt att minimera risken för oväntat låga andrahandsvärden)
    '147008627':'q104', # Vilket finansbolag använder ni?
    '143340230':'q105', # Vem sköter administrationen?
    '143340267':'q106', # Är ni missnöjda med något med finansieringslösningen eller administrationen?
    '143340498':'q107', # Vad är ni missnöjda med? Planerar ni att åtgärda detta?
    '143341102':'q108', # Får ni dra av momsen?
    '146072497':'q109', # Hur nöjda är ni med arbetstiden förarna spenderar på att välja bil?
    '146074246':'q110', # Hur nöjda är ni med arbetstiden det tar <span style="text-decoration: underline;">er</span> att hjälpa förarna att välja bil och beställa den (exempel; förklara valmöjligheter, offertförfrågan, förmånsvärden, orderläggning)?
    '146075429':'q111', # Planerar ni att åtgärda detta?
    '146076084':'q112', # Blir det någonsin fel i ärendehanteringen?
    '146077274':'q113', # Vilka fel har inträffat? Planerar ni att åtgärda detta?
    '146077785':'q114', # Hur avyttrar ni bilarna?
    '146078512':'q115', # Har ni några dotterbolag?
    '146078874':'q116', # Hur skiljer sig bilpolicyn mellan dotterbolagen? Har ni några planer på att samordna bilpolicy inom koncernen?
    '146079692':'q117', # Är ni ett dotterbolag?
    '146080071':'q118', # Vad har ni för riktlinjer kring bilpolicyn och billösningen från moderbolaget?
    '146080551':'q119', # Vad har ni för bilavtal på koncernbolagsnivå?
    '146080900':'q120', # Samarbetar ni med systerbolagen kring bilfrågorna?
    '141247152':'q121', # Några frågor rörande senaste ändringen av bilpolicy/fordonsparken
    '141247151':'q122', # Planerar ni att göra någon ändring av er bilpolicy eller billösning?
    '146991048':'q123', # Vilka ändringar planerar ni och när?
    '146991264':'q124', # Vad föranledde att ni prioriterar denna ändring?
    '146084205':'q125', # Har ni någon upphandling på gång?
    '141247148':'q126', # Frågor rörande nuvarande upphandling
    '146089370':'q127', # Innan vi avrundar och jag skickar in behovsanalysen, är det något du vill lägga till - något som vi missat under genomgången?
    '143337362':'q128'} ## Hur nöjda är ni med att ha finansiell leasing  - givet risken detta medför?