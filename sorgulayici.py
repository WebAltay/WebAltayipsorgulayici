import requests,json

print("""
#################################################################
#################################################################
#####################WebAltay İp Sorgulayıcı#####################
#################################################################
#################################################################""")

ip = input("IP ADRESİNİ GİRİNİZ : " + "")
serviceURL = "http://api.ipapi.com/%22+ip+%22?access_key=%22+%22f76460f4e8673c445e56d09769f54243%22+%22&output=json"
r = requests.get(serviceURL)
y = json.loads(r.text)
y = json.loads(r.text)
veri = y["latitude"],y["longitude"]
print("WebAltay veri tabanına bakılıyor       ...")
print("Ulusal Sistem Verileri Araştırılıyor   ...")
print("İP Adresi bulundu                      ...")
print("İP ADRESİ HAKKINDA BİLGİLER YÜKLENİYOR ...")
print("----------------------------------------------")
print("OTURDUĞU ÜLKE :  " + "" +y["country_name"])
print("OTURDUĞU iL : " + "" +y["region_name"])
print("OTURDUĞU Şehir :  "+ "" +y["city"])
print("KONUM KORDİNATLARI : " + "" + str(veri)`)
