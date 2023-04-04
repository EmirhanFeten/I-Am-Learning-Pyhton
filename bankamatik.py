emirHesap={
    "Ad":"Emirhan Feten",
    "hesapNo":"1235466",
    "miktar":3000,
    "ekHesap":2000
}

yunusHesap={
    "Ad":"Yunus Aydın",
    "hesapNo":"2354211",
    "miktar":2000,
    "ekHesap":1000
}

def paraCek(hesap,miktar):
    print(f'Hoşgeldiniz {hesap["Ad"]}')
    if miktar<=hesap["miktar"]:
        hesap["miktar"] -= miktar
        print("Paranızı Çekebilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam=hesap["miktar"]+hesap["ekHesap"]
        if toplam>=miktar:
            ekHesap=input("Ek Hesabınız Para Çekmek İşlemini Onaylıyor musunuz(e/h): ")
            if ekHesap=="e":
                ekHesapKullanimMiktar=miktar-hesap["miktar"]
                hesap["miktar"]=0
                hesap["ekHesap"]-=ekHesapKullanimMiktar
                print("Paranızı Çekebilirsiniz")
                bakiyeSorgula(hesap)
            else:  
                # print(f"{hesap['hesapNo']} Nolu Hesabınızda {hesap['miktar']} TL Bakiye Bulunmaktadır")  
                bakiyeSorgula(hesap)
        else:
            print("Yetersiz Bakiye")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['miktar']} TL bakiye bulunmaktadır. Ek hesabınızın limiti {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(emirHesap,3000)
print("*********************************")
paraCek(emirHesap,2000)