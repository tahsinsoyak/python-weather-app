import requests
#istekleri yapmak için modül

#Api key silinmiştir 
api_key = "f493235022f117443717201d55ff1d93"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

#Aranacak şehir ismini alacağız
city = input ("Şehir ismi girin: ")

#Verileri çekeceğimiz urlyi ayarlıyoruz
request_url = f"{base_url}q={city}&appid={api_key}&lang=tr"

#Farklı request çeşitleri vardır.
"""
GET
HEAD
POST
PUT
DELETE
"""
#veri çekeceğimiz için get kullanacağız
response = requests.get(request_url)


#Verimizin başarılı çekilip çekilmediğini kontrol etmek için
#requests'den dönen koda bakacağız
if response.status_code == 200:
    data = response.json() #json datasını dictonary olarak verir
    #print(data) #json dosyasına bakıp içinden ne istediğimize bakıyoruz
    weather = data['weather'][0]['description']#0 listedeki ilk eleman için
    temperature = round(data["main"]["temp"] - 273.1, 2) #mainin içindeki derece erişip celciusa çevirdik
    print("Hava Durumu:", weather)
    print("Derece:", temperature, "C°")
else:
    data = response.json()
    print("Hata meydana geldi. " + data['message'])



