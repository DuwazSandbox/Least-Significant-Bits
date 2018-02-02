from PIL import Image
import sys

inputMessage = "Esli vy posmotrite na zhizn' "" sredne obrazovannyh, mnogo rabotajushhih ljudej, to uvidite, \
chto kazhdyj chelovek idet odinakovoj dorogoj. Rebenok rozhdaetsja, idet v shkolu. Gordye roditeli schastlivy, \
potomu chto ih rebenok prekrasno uchit'sja, imeet nesomnennye shansy na horoshee obrazovanie, i ego prinimajut \
na uchjobu v kolledzh. Po okonchanii, mozhet byt' poluchaet nauchnuju stepen', zatem dejstvuet kak zaprogrammirovannyj: \
ishhet garantirovanno bezopasnuju rabotu ili kar'eru. Rabotaja, imeja den'gi, obshhaetsja s drugimi ljud'mi, \
nahodit sebe paru, zatem sledujut svidanija, a inogda i zhenit'ba. Zhizn' zhenivshihsja prekrasna, tak kak oba rabotajut. \
Est' dva dohoda. Oni chuvstvuju sebja uspeshnymi ljud'mi, ih zhdet jarkoe budushhee, i oni reshajut kupit' dom, \
mashinu, televizor, ezdit' na otdyh, zavesti detej. Nastupaet schastlivoe vremja. Rastet potrebnost' v sredstvah. \
Schastlivaja para reshaet, chto ih kar'ery zhiznenno vazhny, nachinajut sil'nee vkalyvat', ishha prodvizhenija po \
sluzhbe i pod#ema dohodov. Rozhdajutsja deti, i pojavljaetsja potrebnost' v bol'shom dome. Ljudi rabotajut vse bol'she, \
stanovjatsja horoshimi rabotnikami, pol'zujutsja priznaniem. Oni (snova) uchatsja, chtoby poluchit' bol'she specializirovannyh \
znanij i zarabatyvat' bol'she deneg. Vozmozhno, berutsja za vtoruju rabotu. Ih dohody idut vverh, no uvelichivajutsja nalogi, \
kotorye oni platjat, rastet summa nalogov za novyj bol'shoj dom, nalogi na social'noe obespechenie i drugie nalogi. Ljudi udivljajutsja, \
vrode poluchajut normal'no, a inogda i zhenit'ba. Zhizn' zhenivshihsja prekrasna, tak kak oba rabotajut. Est' dva dohoda. Oni chuvstvuju \
sebja uspeshnymi ljud'mi, ih zhdet jarkoe budushhee, i oni reshajut kupit' dom, mashinu, televizor, ezdit' na otdyh, zavesti detej. \
Nastupaet schastlivoe vremja. Rastet potrebnost' v sredstvah. Schastlivaja para reshaet, chto ih kar'ery zhiznenno vazhny, nachinajut \
sil'nee vkalyvat', ishha prodvizhenija po sluzhbe i pod#ema dohodov. Rozhdajutsja deti, i pojavljaetsja potrebnost' v bol'shom dome. \
Ljudi rabotajut vse bol'she, stanovjatsja horoshimi rabotnikami, pol'zujutsja priznaniem. Oni (snova) uchatsja, chtoby poluchit' bol'she \
specializirovannyh znanij i zarabatyvat' bol'she deneg. Vozmozhno, berutsja za vtoruju rabotu. Ih dohody idut vverh, no uvelichivajutsja nalogi, \
kotorye oni platjat, rastet summa nalogov za novyj bol'shoj dom, nalogi na social'noe obespechenie i drugie nalogi. Ljudi udivljajutsja, \
vrode poluchajut normal'no, a den'gi, kak v pesok uhodjat. Oni pokupajut kakie-to gosudarstvennye obligacii, tovary na svoju kreditnuju kartochku. \
I vot detjam 5-6 let i nuzhda jekonomit' na kolledzh rastet, a parallel'no neobhodimost' otkladyvat' den'gi na starost'. \
I, takim obrazom, schastlivaja para, kotoroj po 35 let, teper' popadaet v kapkan krysinyh gonok do konca svoih rabochih dnej. \
Ljudi rabotajut na vladel'ca svoej kompanii, na pravitel'stvennye nalogi, na vyplaty banku po zakladnoj, a zatem oni sovetujut \
svoim sobstvennym detjam uporno uchit'sja, poluchat' horoshie znanija, iskat' bezopasnuju rabotu i kar'eru. Ljudi ne ponimajut, \
chto takoe den'gi, zato jeto prekrasno ponimajut te, kto zhivet ih naivnost'ju, a ljudi vkalyvajut i vkalyvajut vsju svoju zhizn'. \
Process kopiruetsja sledujushhim, mnogo rabotajushhim pokoleniem. Jeto i est' krysinye gonki. Edinstvennyj put' vybrat'sja iz krysinyh gonok \
- priobresti umenie v uchete sredstv i investirovanii."

original = Image.open('input.png')
width, height = original.size

steg = Image.new('RGB', (width, height))

bits = []

for x in inputMessage:
	str = format(ord(x), 'b')
	for zeros in range(8-len(str)):
		bits += '0'
	for x2 in str:
		bits += x2
		
idx = 0
stop = 0
for i in range(width):
	for j in range(height):
		if sys.version_info <= (3,0):
			r,g,b,_ = original.getpixel((i, j))
		else:
			r,g,b = original.getpixel((i, j))
		if stop == 0:
			if bits[idx] == '0':
				r &= 254
			else:
				r |= 1
		else:
			r &= 254
		steg.putpixel((i,j), (r,g,b))
		idx += 1
		if idx >= len(bits):
			stop = 1

steg.save('output.png')