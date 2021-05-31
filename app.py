from flask import Flask,render_template,request
import requests

app = Flask(__name__)
@app.route('/',methods=['GET'])
def weather():
    i1 = "https://ipinfo.io?"
    api_address1 = i1
    res1=requests.get(api_address1)
    data = res1.json()
    print(data)
    IP = data['ip']
    cityname = data['city']
    location = data['loc']
    print(location)
    location = data['loc'].split(',')
    latiname=location[0]
    longiname=location[1]
    print("City: ",cityname)
    context = {
        "weatherdesc": weatherf(cityname,latiname,longiname)
    }
    return render_template('location.html',context = context,value1=latiname,value2=longiname,value3=cityname,value4=IP)

def weatherf(cityname,latiname,longiname):
    import socket
    import requests
    try:
        send =[]
        socket.create_connection( ("www.google.com",80) )
        city = cityname
        if(cityname == None):
            pass
        else:
            a1 = "http://api.openweathermap.org/data/2.5/forecast?units=metric"
            a2 = "&q=" + city
            a3 = "&appid=ENTER YOUR APPID"
            api_address2 = a1 + a2 + a3
            res1=requests.get(api_address2)
            data = res1.json()
            list1 = data['list']
            res = [sub['main'] for sub in list1] 
            temp = [t['temp'] for t in res]
            hum = [t['humidity'] for t in res]
            mini = [t['temp_min'] for t in res]
            maxim = [t['temp_max'] for t in res]
            time = [sub['dt_txt'] for sub in list1]  
            weather = [sub['weather'] for sub in list1] 
            wind = [sub['wind']for sub in list1]
            windspeed = [sub['speed']for sub in wind]
            weatherm,weatherd,iconw = [],[],[]
            for i in range(len(temp)):
                for sub in weather[i]:
                    weatherm.append(sub['main'])
                    weatherd.append(sub['description'])
                    iconw.append(sub['icon'])
            a11 = "http://api.openweathermap.org/data/2.5/air_pollution/forecast?"
            a22 = "&lat=" + latiname + "&lon=" + longiname
            a33 = "&appid=ENTER YOUR APPID"
            api_address1 = a11 + a22 + a33
            res=requests.get(api_address1)
            data1 = res.json()
            list2 = data1['list']
            res2 = [sub1['main'] for sub1 in list2]
            aqi = [a['aqi'] for a in res2]
            send.append([time,temp,mini,maxim,hum,windspeed,aqi,weatherm,weatherd,iconw])
    except KeyError as k:
        print("City Not Found")
    except OSError as e:
        print("check network ",e)
    return send


if __name__ == '__main__':
    app.run()


