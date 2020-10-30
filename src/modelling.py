from fbprophet import Prophet
import pandas as pd

def make_base_model(train, test):
    '''
    Creates base model

    Parameters
    ----------
    train : pandas series
    test : pandas series

    Returns: 
    --------
    prophet : fbprophet model
    forecast : dataframe
    test_forecast : dataframe
    '''

    prophet = Prophet()
    prophet.fit(train)
    test_forecast = prophet.predict(df=test)

    return prophet, test_forecast


def make_model_wth_regressors(train, test):
    '''
    Creates model with additional regressors

    Parameters
    ----------
    train : pandas series
    test : pandas series

    Returns: 
    --------
    prophet : fbprophet model
    forecast : dataframe
    test_forecast : dataframe
    '''

    prophet = Prophet(yearly_seasonality=False)
    # add regressors
    prophet.add_regressor('during_world_fin_crisis', mode='additive')
    prophet.add_regressor('during_oil_gas_crash', mode='additive')
    prophet.fit(train)
    test_forecast = prophet.predict(df=test)

    return prophet, test_forecast