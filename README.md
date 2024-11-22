# ML-for-finance
Application of ML models in finance

=========================================================================================================
Note: This is a personal initiative to support my application for the data scientist role. 

=========================================================================================================

Exercise:
Using these two datasets (datasets are described below), build a model that predicts whether the request for quote is going 
to be won or not by the bank, given the price quoted and other information provided in the datasets or derived from them 
(feature engineering).

Dataset A: 
rfqs.csv:  - date_time: date and time at which the quote is requested.  
Instrument: the bond for which the customer has requested a price
client: client code (anonymized) 
price: price quoted to the client by the bank 
mid: market mid-price of the bond captured by the bank's system at the time of the operation  
vol_MM: amount requested by the client (in millions of euros).  
dv01: sensitivity of the bond to variations in its yield (a measure of risk of the bond)  
num_dealers: number of banks from whom the client has requested a quote  
side: 1 if it is buy -1 if it is sell (from the point of view of the bank, not the client)  
won: 0 if the bank did not close the operation, 1 if it did.  

Dataset B: mids.csv:  
date_time: day and time of the market mid-price of the bond  
mid: market mid-price of the bond provided by a data provider with greater reliability than our platform, sampled with a frequency of 5 minutes  
instrument: the bond for which the market price is provided 

=========================================================================================================

The project is divided into two main parts: Data Analysis and Machine Learning Model Development.

Data Analysis:
For an overview, please refer to the DataAnalysis.pdf document.
For a more detailed exploration, you can review the accompanying Python script, DataAnalysis.ipynb.

Machine Learning Model Construction:
The implementation details are provided in the ModelConstruction.ipynb script.
