# Driver/Truck Monitoring App

Driver/Truck Monitoring App is a prototype webapp developed during the Hackathon Unleash Logisitics sponsored by Truck Alliance and hosted in Chengdu, China.

The prototype webapp displays a main score for each drivers based on different facotrs such as safety record, truck age, number of kilometers. It also provides for each driver a more detailled page that include the truck health and maintenance metrics.

## Installation

### Requirements
* MongoDB - Compass Community - [MongoDB Download Center](https://www.mongodb.com/download-center?jmp=nav#community)

* Python 3.6 and up
    * Packages required
    
    ```python
    pip install pymongo
    pip install flask
    pip install CORS
    pip install pandas
    pip install os
    pip install random
    pip install datetime
    ```

* R 3.5 and up
    * Packages required

    ```R
    list.of.packages <- c("dplyr", "mongolite", "lubridate")
    new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
    if (length(new.packages)) install.packages(new.packages)
    ```

### Creation of the mockup database

1. Set up and run your database in MongoDB - Compass Community (localhost)
2. **Download** the repository
3. **Open** `./data-analyze/Upload_Mockdata_DriverTruck_Goods_001.py` in a text editor and **modify** the path to your own directory path:
```python
path = 'C:/Mydrive/Myfolder/truck-security-rate/data-analyze/MockDateTemplate'

```
5.  **Set the number of driver and number of trip** you want to generate. Example: 1000 drivers and 300 trips for each.
```python
# set number of driver/truck to add to DB
n_dt = 1000
# set number of trips for each driver
n_g = 300
```
**Note**: Large number increase may require a few minutes to be generated.

6. Run the **data summary and scoring** script with upload to the mongoDB

Use the R console and run the following command:
```R
setwd("./data-analyze/R_script")
source("HackDB01_data_scoring.R")
```

7. **Verify** that the MongoDB has been set according to the requirements 

The database should be composed of 3 collections

- `DriversTrucks`: drivers and trucks data
- `Goods`: trip details
- `score`: summary data and processed metrics

### Setup the server

1. **Disable the firewalls** on your computer
2. In a **python console**, in your app folder:
```python
 %run ./server/server.py
```

### Run the Webapp

*Need details how to setup and run the webapp*
#### dev:
1. Start Server Project and generate two routes
2. Cd Web project path
3. Run ```npm install```
4. Change ```serverUrl``` in src/config.js
5. Run ```npm run serve```
6. Open browser and access http://localhost:8080
#### production:
1. Cd Web project path
2. Run ```npm install```
3. Change ```serverUrl``` in src/config.js
4. Run ```npm run build``` and copy path dist into server project
5. Add static route in server project
6. Access route

## Usage

The UI proposes two pages:

* First page (Homepage)  
    Display ten drivers data and their summary score

* Second page (Driver Detail page) 
    Details about the driver and truck
    
    *Need details about navigation in the app*

## Video

http://player.youku.com/embed/XMzgxNzMwMDcyOA==

## Screenshot

![index](https://github.com/git-hacker/truck-security-rate/raw/master/Info/index.png)
![detail](https://github.com/git-hacker/truck-security-rate/raw/master/Info/detail.png)


## Scoring System

The scoring system is based on a 
According to the analysis of the driver's driving behavior, find out the factors affecting the driver's safe delivery behavior, analyze the factors that can cause the delivery safety of the truck, generate a large amount of data, and grade the driver's safety according to the research data.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgment

The developers would like to thank all the organizers of the Unleash Highway Logistics Hackathon for their awesome work.
All thanks to all the sponsors which supported the event.

## License
[MIT](https://choosealicense.com/licenses/mit/)
