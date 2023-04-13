import pandas as pd
import numpy as np
""" 
## Example 
bar = yfinance or inclusive bar["High"]  bar["Low"] bar["Close"] 
positive_di , negative_di   =   pdi_ndi(bar ,  period= 14 )
"""

def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
     
def atr ( bar , period ):
  
  high_low, high_close, low_close  = np.array(bars["High"]-bars["Low"],dtype=np.float16 ) , 
  np.array(abs(bars["High"]-bars["Close"].shift()),dtype=np.float16 ) , 
    np.array(abs(bars["Low"]-bars["Close"].shift() ),dtype=np.float16 )
    
  true_range = np.amax (np.hstack( (high_low, high_close, low_close) ).reshape(-1,3),axis=1 )
  avg_true_range = sma(true_range , period)  # takes average for 14 period  
  return avg_true_range 

# returning "true_range" is optional not needed. 

def pdi_ndi(bar ,  period):

    _ , true_range  = atr(bar , period )
    highs , lows =   np.array(abs(bar["High"] - bar["High"].shift(1)), dtype=np.float16)  
    , np.array(abs(bar["Low"].shift(1) - bar["Low"]), dtype=np.float16 )
    condition_pdm = highs > lows
    condition_ndm = lows  > highs 
    pdm = np.where(condition_pdm, highs , 0.0 )
    ndm = np.where(condition_ndm, lows , 0.0 )

    pdm , ndm = sma(pdm , period ) , sma(ndm , period )
    pdm_smoothed = ema(pdm , period )
    ndm_smoothed = ema(ndm , period )
    tr_smoothed  = ema(true_range , period )

    pdi = ( pdm_smoothed / tr_smoothed ) * 100
    ndi = ( ndm_smoothed / tr_smoothed ) * 100
    
    return  pdi ,  ndi
