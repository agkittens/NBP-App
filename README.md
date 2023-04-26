# NBP-App

## Table of Contents
* [General Info](#general-info)
* [Examples and Usage](#examples-and-usage)
* [Docker and Installation](#docker-and-installation)


## General Info
This project is about simple server that allows to check different combinations of parameters: currency codes, dates and qoutations, to get information about average rates and differences between the buy and ask rate.\
The server will perform internal operations on this data and return simple, plain results to users who input arguments through the endpoints. The project is based on http://api.nbp.pl/ API.

## Example and Usage
To check the output, write down your parameters in chosen windows and press the button of your choice.\
\
Average rate should contain a currency code and date in format YYYY-MM-DD. It returns the value of average rate from chosen day.\
List of currency codes:
```
CODES = ['AUD','THB','BRL','BGN','CAD','CLP','CZK','DDK','EUR','HUF','HKD','UAH','ISK','INR','MYR','MXN','ILS','NZD','NOK','PHP','GBP','ZAR','RON','IDR','SGD','SEK','CHF','TRY','USD','KRW','JPY','CNY','XDR']
```
![output](https://github.com/agkittens/NBP-App/blob/main/assets/example.png?=250x250)

### Conditions
Min and max value shoud contain a currency code and number(N <= 255) of quotations. It returns min and max value of average rate from last N quotations.\
Major difference value shoud contain a currency code and number(N <= 255) of quotations. It returns difference of the buy rate and ask rate from last N quotations.\
\
\
If there occurs any incorrect value the output will be "Incorrect value" - the value must follow mentioned conditions.

## Docker and Installation
To build a Docker Image run this command in the therminal:
```
$ git clone https://github.com/agkittens/NBP-App.git
$ docker image build -t nbp-app .
```
or directly from folder with downloaded zip
```
$ cd [project path]
$ docker image build -t nbp-app .
```
\
Then run the server with:
```
$ docker run -i -p 5000:5000 -d nbp_app
```
\
If you want to run it without a server follow those steps:
The required packages for this project are listed in the requirements.txt file. To install them, simply run the following command:
```
$ pip install -r requirements.txt
```
Then run app with this command:
```
$ python3 app.py
```



