'''
SESSION28 - FLASK POST REQUEST, FORMULARE, LOGGER, REDIRECT

Dokoncenie SESSION27 -

# 5 Prezentacia cien kuracich kridel vypisanych pomocou Jinja 2 v template kurzkk.html

## Predstavenie CSS - kaskadovych stylov a rozny sposob ich tvorby v tagoch, v Heade a samostatnom .css subore
v adresari static

## Manipulacia v kurzkk.html pomocou Jinja2 nastavujeme aby sa pozitivne a negativne cisla zobrazovali v roznych farbach

# 6 Jednoduchy formular v html, ktory pomocou POST requestu posiela info do funkcie form()

!!! POZOR - FORMULAR ANI JEHO OBSAH NESPLNAJU ZAKLADNE PREDPOKLADY NA MINIMALNU BEZPECNOST  !!!

Formular je vyktvoreny pomocou html tagov <form>, <label> a <input> a posiela data v surovej forme.

Aby bolo mozne z funkcie form() ziskane user a pwd dostat von, vytvarame BUFFER list do ktoreho ich vlozime ako tuple()


POKRACUJEME VYTVORENIM CISTEHO FLASK PROJEKTU V OBALKE WEBFLASA2
pip install flask
pip install flask-wtf
pip install wtforms

Spravime si zakladnu route '/' a '/index' s index.html v adresari templates

Pomocou wtforms StringField() a SubmitField() vytvarame triedu MojFormular, ktora dedi po FlaskForm() z flask_wtf
Pouzijeme aj validator z wtforms.validators  DataRequired, ktory bude trvat na zadani dat do formulara.

Vytvorime route '/info' pre nas informacny formular.
Ziskane info budeme ukladat do listu info_list kde mame nejake cvicne data na testovanie

Pomocou podmienky na request zistime ci je POST a vysledok z formulara spracujeme a vlozime do info_listu

Pomocoiu vstavanej funkcionality Flasku app.logger si do vystupu servera zapisujeme vytvorenie formulara aj dalsie
vykonane operacie.

renderujeme formular a pridavame form=form aby sme prepojili udaje z funkcie info a info.html

# 2  Dve samostatne funkcie pre POST a GET
FLASK nam umoznuje jednotlive metody oddelit do dvoch separatnych funkcii info_get() a i  info_post()
Aby sa kod neopakoval po uspesnom odoslani formulara je pomocou redirect presmerovany na submit.html kde uzivatelovi
dakujeme za poskytnute info.

!! POZOR submit musi mat renderovanu samostetne svoju route '/submit' !!

!!!  Nas formular nie je este dokonale osetreny ale pomocou wtforms a flask_wtf sme vyriesili niekolko problemov
Vstupy su osetrene pomocou metod StringField(), ktore su viac pod kontrolou Flasku ako tag <input>
CSRF - Utoky CROSS SITE REQUEST FORGERY - (FALSOVANIE OBSAHU FORMULARA) flaskovanie formularov je osetrene zapnutim
ochrany CSRF_ENABLED = True  a nastavenim SECRET_KEY co je vlastne kryptograficka ochrana naseho formularu.

 Tento utok prebieha pozmenenim obsahu formulara Priklad poslem 10EUR na ucet 123 a Hacker to zmeni na 100EUR na
 ucet 321. Alebo poslem Heslo: veslo a dojde do WebAppky Heslo: kybel.

 Validacia ci bol zadany string nam stale nefunguje.

 Pomocou par riadkov kodu Jinja2 vypisujeme error - chybajuci csrf.token
 Akonahle ho aktivujeme tak Validacia na form.validate() nam zacne vracat True.

# VYTVARAME WEBFLASU3 a doplname route (/info)

Pomocou zobrazovanie flash sprav informujeme uzivatela o dolezitych veciach.

Tentokrat ukladame data do vstavaneho slovnika session, kde mozeme uchovavat nekriticke data.

Tieto data sa uchovavaju pomocou Cookies a ukladaju sa v uzivatelovom browseri. Po odpojeni sa vymazu.

ZObrazujeme ulozene veci zo session v route /view


'''