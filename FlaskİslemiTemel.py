


from flask import Flask, request #web servislerinde hızlı sonuç elde etmeye yarayan framework

app =Flask(__name__)

@app.route("/",methods=['POST']) #app route ile sayfamızı oluşturuyoruz.
#def ping():
  #  return "Success" #bir şey döndürdügünü görmesi gerektigi için print kullanılmadı



@app.route("/ping_user",methods=['POST']) 
def ping_user():
   print(request)
    ad=request.args.get('ad')
    
    return f"merhaba {ad} servera hoşgeldiniz"
   .format{degisken=ad} f kullanndıgın zaman çagırdıgın şeyi içine gömüyor. yukarıdaki ad yerine degisken yazabilirsin

    
    

if __name__=='__main__':
 #   app.run(port=5000)






