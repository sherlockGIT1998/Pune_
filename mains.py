from flask import Flask,render_template,request

from utils import PuneHouseData

app = Flask(__name__)

@app.route('/')

def hello_flask():
    print('Pune House Price Prediction')
    return render_template('index.html')

@app.route('/predict_prices',methods=['GET','POST'])

def price_info():
    
    if request.method == 'GET':
        
        print('GET Method...')
        
        # data = request.form
        # area_type = data[area_type]
        # size = data[size]
        # total_sqft = data[total_sqft]
        # bath = eval(data[bath])
        # balcony = eval(data[balcony])
        # site_location = data[site_location]
        # availability = data[availability]
        
        area_type = request.args.get('area_type')
        size = request.args.get('size')
        total_sqft = request.args.get('total_sqft')
        bath = eval(request.args.get('bath'))
        balcony = eval(request.args.get('balcony'))
        site_location = request.args.get('site_location')
        availability = request.args.get('availability')
        
      
        price = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
        
        predict = price.get_predicted_price()
        
        return render_template('index.html',prediction=round(predict,2))
    
        # return f'Price of Pune Hous eis Rs. {round(predict,2)}Lakh/-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()