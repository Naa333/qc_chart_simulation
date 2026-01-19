import pandas as pd
import numpy as np
import plotly

#create 7 numpy arrays for the x values
#sodium (ref: 135 to 145 mmol/L)
rng = np.random.default_rng(42)
na= rng.integers(low=130, high=152, size=15)

#potassium (ref: 3.5 to 5.2 mmol/L)
rng2= np.random.default_rng(42)
k= np.round(rng2.uniform(low= 3.2, high= 5.9, size= 15), 1)

#chloride (ref: 96-106 mmol/L)
rng3 = np.random.default_rng(42)
chl = rng3.integers(low= 93, high= 111, size= 15)

#CO2 (ref: 23–29 mEq/L (mmol/L))
rng4 = np.random.default_rng(42)
co2 = rng4.integers(low= 22, high= 35, size= 15)

#BUN (ref: 6-20 mmol/L)
rng5= np.random.default_rng(42)
bun= rng5.integers(low= 2, high= 150, size= 15)

#glucose (ref: 70–100 mg/dL)
rng6= np.random.default_rng(42)
glu= rng6.integers(low= 60, high= 102, size= 15)

#creatinine (ref:  0.6–1.3 mg/dL)
rng7= np.random.default_rng(42)
creat= np.round(rng7.uniform(low= 0.6, high= 2.5, size= 15), 1)

#calcium (ref:  8.5–10.2 mg/dL)
rng8= np.random.default_rng(42)
ca= np.round(rng8.uniform(low= 2.9, high= 15.2, size= 15), 1)

#create a pandas series for the labels
#labels= pd.Series(index= ["sodium", "potassium", "chloride", "carbon_dioxide", "blood_urea_nitrogen", "glucose", "creatinine", "calcium"])

#create a df
qc_df= pd.DataFrame({"sodium": na, 
                    "potassium": k,
                    "chloride": chl,
                    "carbon_dioxide": co2,
                    "blood_urea_nitrogen": bun,
                    "glucose": glu,
                    "creatinine": creat,
                    "calcium": ca
                    })
print(qc_df.head(5))


#calculate standard deviation
stds= qc_df.std()

#find +- standard deviations
plus_one_std= stds + 1
print(plus_one_std)
#plot graphs!