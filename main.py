import pyttsx3


print("hello resan")

banglaDeshNationalSong = '''Amar shonar Bangla, ami tomay bhalobashi.
𝄆 Cirodin tomar akash, 𝄇
Tomar batash, amar prane
O ma, amar prane bajay bãshi.
Shonar Bangla, ami tomay bhalobashi.
O ma, phagune tor amer bone ghrane pagol kôre,
Mori hay, hay re:
O ma, phagune tor amer bone ghrane pagol kôre,
O ma, Ôghrane tor bhôra khete ki dekhechi
Ami ki dekhechi modhur hashi.
Shonar Bangla, ami tomay bhalobashi.

Ki shobha, ki chaya go, ki sneho, ki maya go,
Ki ãcol bichayecho bôṭer mule, nodir kule kule.
Ma, tor mukher bani amar kane lage shudhar môto,
Mori hay, hay re:
Ma, tor mukher bani amar kane lage shudhar môto,
Ma, tor bôdonkhani molin hole, ami nôyon
O ma, ami nôyonjôle bhashi.
Shonar Bangla, ami tomay bhalobashi.''' 

# print(banglaDeshNationalSong)

# text to  speech by using pyttsx3

engine = pyttsx3.init()

# change engine voice rete

rate = engine.getProperty("rate")
print(rate)
engine.setProperty("rate" , 400)

engine.say(banglaDeshNationalSong)
engine.runAndWait()
engine.stop()
