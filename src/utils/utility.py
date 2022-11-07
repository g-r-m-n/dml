from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
#from linearmodels import IV2SLS, IVGMM, OLS
from statsmodels.sandbox.regression.gmm import IV2SLS, OLS
import doubleml as dml
import matplotlib.pyplot as plt
import sklearn.metrics as metrics 
from sklearn.base import clone
import numpy as np
import os
import pandas as pd


class model_object:
    
    def __init__(self,model_type):
        self.type = model_type
        # is dml model type?
        self.type_dml  =  self.type in ['dml-plr','dml-pliv','dml-irm','dml-iiv','naive-ml']
        # is linear regression model type?
        self.type_lreg =  self.type in ['2sls','ols','ols-partialed-out']
        
    def update_data(self, data) :  
        
        data = data.copy()
        if self.type_dml:
            # specify the ML models:
            learner_reg = RandomForestRegressor(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
            
            learner_class = RandomForestClassifier(n_estimators=100, max_features=20, max_depth=5, min_samples_leaf=2)
                
            iv_vars =[i for i in data.columns if i.lower().startswith('z')]    
            
            if self.type == 'dml-plr':
                
                obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
                
                #ml learner for the nuisance function l0(X)=E[Y|X]:
                self.ml_l = clone(learner_reg)
                
                #ml learner for the nuisance function m0(X)=E[D|X]:
                if len(np.unique(data['d'])) <= 10:  
                    self.ml_m = clone(learner_class)
                else:                    
                    self.ml_m = clone(learner_reg)
                
                self.model_obj  = dml.DoubleMLPLR(obj_dml_data, self.ml_l, self.ml_m)
            elif self.type == 'dml-pliv':
                
                obj_dml_data = dml.DoubleMLData(data, 'y', 'd', z_cols=iv_vars)
                
                #ml learner for the nuisance function l0(X)=E[Y|X]:
                self.ml_l = clone(learner_reg)
                
                #ml learner for the nuisance function m0(X)=E[Z|X]:
                self.ml_m = clone(learner_reg)
                
                #ml learner for the nuisance function r0(X)=E[D|X]:
                self.ml_r = clone(learner_reg)
                
                self.model_obj = dml.DoubleMLPLIV(obj_dml_data, self.ml_l, self.ml_m, self.ml_r)
                
            elif self.type == 'dml-irm':
                
                obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
                
                #ml learner for the nuisance function g0(X)=E[Y-Dθ0|X]:
                self.ml_g = clone(learner_reg)
                
                #ml learner for the nuisance function m0(X)=E[D|X]:
                self.ml_m = clone(learner_class)
                
                self.model_obj = dml.DoubleMLIRM(obj_dml_data, self.ml_g, self.ml_m)
                
            elif self.type == 'dml-iiv':

                obj_dml_data = dml.DoubleMLData(data, 'y', 'd', z_cols=iv_vars)
                
                #ml learner for the nuisance function g0(X)=E[Y-Dθ0|X]:
                self.ml_g = clone(learner_reg)
                
                #ml learner for the nuisance function m0(X)=E[Z|X]:
                self.ml_m = clone(learner_class)
                
                #ml learner for the nuisance function r0(X)=E[D|X]:
                self.ml_r = clone(learner_class)
                
                self.model_obj = dml.DoubleMLIIVM(obj_dml_data, self.ml_g, self.ml_m, self.ml_r)    
                
            elif self.type =='naive-ml':
                
                obj_dml_data = dml.DoubleMLData(data, 'y', 'd')
                
                #ml learner for the nuisance function l0(X)=E[Y|X]:
                self.ml_l = clone(learner_reg)
                    
                #ml learner for the nuisance function m0(X)=E[Z|X] or  m0(X)=E[D|X]:
                if len(np.unique(data['d'])) <= 10:  
                    self.ml_m = clone(learner_class)
                else:                    
                    self.ml_m = clone(learner_reg)
                    
                #ml learner for the nuisance function g0(X)=E[Y-Dθ0|X]:
                self.ml_g = clone(learner_reg)            
                
                self.model_obj = dml.DoubleMLPLR(obj_dml_data, self.ml_l, self.ml_m, self.ml_g, n_folds=2, apply_cross_fitting=True, score=non_orth_score_w_g)
                
            else:
                raise ValueError("model type not found.")
            
        if self.type =='ols':
            data.loc[:,'const'] = 1
            exog = [i for i in data.columns if i.lower().startswith('x')] + ['const'] 
            
            self.model_obj = OLS(endog=data.loc[:,'y'], exog = data.loc[:,['d']+exog])            
         
        if self.type =='ols-partialed-out':
            
            data.loc[:,'const'] = 1
            exog = [i for i in data.columns if i.lower().startswith('x')] + ['const'] 
            
            res_D_on_X = OLS(endog=data.loc[:,'d'], exog = data.loc[:,exog]).fit().resid 
            
            res_Y_on_X = OLS(endog=data.loc[:,'y'], exog = data.loc[:,exog]).fit().resid 
            data.loc[:,'res_D_on_X'] = res_D_on_X
            
            self.model_obj = OLS(endog=res_Y_on_X, exog = data.loc[:, ['res_D_on_X','const']] )  
          
        if self.type =='2sls':

            exog = [i for i in data.columns if i.lower().startswith('x')] 
            iv_vars =[i for i in data.columns if i.lower().startswith('z')]
            
            if 1 and len(iv_vars)==0:
                iv_vars = [i+'_sq' for i in exog]
                data[iv_vars] = data[exog]**2
                
            data.loc[:,'const'] = 1
            exog += ['const']   
            self.model_obj = IV2SLS(endog=data.loc[:,'y'], exog = data.loc[:,['d']+exog], instrument= data.loc[:,exog+iv_vars])
    
    def tune(self, param_grids, **kwargs):        
        if self.type_dml:
           self.model_obj.tune(param_grids, **kwargs)
         
       
    def fit(self):
        self.fitted_model = self.model_obj.fit()
        if self.type_dml:
            self.fitted_model.interval = self.model_obj.confint()
        if self.type_lreg :
            self.fitted_model.interval = self.fitted_model.conf_int()   
            self.fitted_model.coef = self.fitted_model.params
            
    def collect_results(self,results_rep,i_rep): 
        results_rep.loc[i_rep,'coef_'+self.type] = self.fitted_model.coef[0] 
        results_rep.loc[i_rep,'lower_bound_'+self.type] = self.fitted_model.interval.iloc[0,0] 
        results_rep.loc[i_rep,'upper_bound_'+self.type] = self.fitted_model.interval.iloc[0,1] 
        return  results_rep
    


def plot_ate_est(results_rep, theta, model_index, max_int_x = None, output_folder_plots = '', title1 = '', YLIM=[0,1], SAVE_OUTPUT = 0):
    #plt.style.use('ggplot')
    import matplotlib.pyplot as plt
    plt.rcParams['figure.figsize'] = (16.0, 16.0)
    plt.dpi = 100
    nn = len(results_rep)+1
    x = range(1,nn)
    if max_int_x is None:
        max_int_x = nn
        
    fig, axes = plt.subplots(nrows=len(model_index), sharex=True) 
    for ix_m, m in enumerate(model_index):
        model_name= m.lower()
        y = results_rep['coef_'+model_name]
        asymmetric_error = [results_rep['lower_bound_'+model_name].values-y, y-results_rep['upper_bound_'+model_name].values]
        
        axes[ix_m].errorbar(x, y, yerr=asymmetric_error, fmt='o')
        axes[ix_m].set_title(m.upper(), fontsize=16)
        axes[ix_m].hlines(theta, 1, max_int_x-1, color='red')
        if YLIM is not None:
            axes[ix_m].set_ylim([0.0, 1])
      
        #text size:
        labels = axes[ix_m].get_xticklabels() + axes[ix_m].get_yticklabels()
        for label in labels:
            #label.set_fontweight('bold')
            label.set_size('16')

    
    # Saving plot to pdf file
    if SAVE_OUTPUT:
        plt.savefig(output_folder_plots  +title1+'.pdf', dpi=plt.dpi,bbox_inches="tight")
        #plt.title(title1, fontsize=20)
        plt.savefig(output_folder_plots  +title1+ '.png', dpi=plt.dpi,bbox_inches="tight")


    plt.show()
    
    
def save_to_tex(df, output_folder_file_path, column_format='', caption='', label='', index=False, longtable=True):
    """
    Save a data table to LaTeX in the local folder.
    :param df: (dataframe) dataframe to be saved.
    :param output_folder_file_path: (string) path and file name in the local folder the dataframe is saved to.
    :param column_format: (string) the column format in LaTeX style of the table to be saved. If not provided, the column_format will be automatically generated
    :param caption: (string) the caption to be shown in LaTeX of the table to be saved.
    :param label: (string) the label to be shown in LaTeX of the table to be saved.
    :param index: (boolean) indicating whether the index of the dataframe should be saved.
    :param longtable: (boolean) indicating whether the dataframe should be saved in long format in LaTeX.
    :return True: (boolean)  .
    """
    df= df.copy()
    # convert to pandas dataframe if df is not:
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
    # create output folder if it does not exit:
    output_folder_path,_ = os.path.split(output_folder_file_path)
    os.makedirs(output_folder_path, exist_ok=True)
    # format column names
    df.columns = df.columns.str.replace("_", " ")
    df.columns = df.columns.str.replace("\n", "")
    if 0:
        df.columns = df.columns.str.capitalize()
    # determine the column format for the output Latex table
    if len(column_format)==0:
        column_format = ['L{'+str(len(df.columns[0])/1.5)+'cm}']+[ 'R{'+str(len(i)/1.5)+'cm}' for i in df.columns[1:] ]
    if index:
        if len(df.index.names)>1:
            df_index_names = df.index.names 
        else:
            df_index_names  = ['Index'] 
        column_format = [ 'L{'+str(len(i)/1.5)+'cm}' for i in  df_index_names ] +column_format
    # transform to string:
    column_format = ''.join(column_format)
    with open(output_folder_file_path+ '.tex', 'w') as texf:
        texf.write(df.to_latex(column_format=column_format, label=label,caption=caption, position='H', longtable=longtable, index=index,na_rep=''))
    return True
    
   
def error_stats(theta, y_pred):
    y_true = np.repeat(theta, len(y_pred))
    mean_absolute_error=metrics.mean_absolute_error(y_true, y_pred) 
    mse=metrics.mean_squared_error(y_true, y_pred) 
    #median_absolute_error=metrics.median_absolute_error(y_true, y_pred)
    #return {'MSE': round(mse,4),'RMSE': round(np.sqrt(mse),4),'MAE': round(mean_absolute_error,4), 'MEDIAN-AE':round(median_absolute_error,4) } 
    return {'RMSE': round(np.sqrt(mse),4),'MAE': round(mean_absolute_error,4), 'Bias':round(np.mean(y_pred-y_true),4) }    	


def get_res_stats(results_rep, model_index, theta, PRINT =1):
    if 0:#len(results_rep)<= 1:
        return []
    res_stats = pd.DataFrame()
    for m in model_index:
        res_stats = pd.concat( [res_stats, pd.DataFrame([error_stats(theta, results_rep['coef_'+m.lower()])],index=[m])], axis=0 )
        
    # add best performing model:
    res_stats2 = res_stats.copy()
    if 'Bias' in res_stats2.columns:
   	    res_stats2['Bias'] = abs(res_stats2['Bias'])
    res_stats.loc['Best',:] =  res_stats2.idxmin()
    if PRINT:
        print(res_stats)
    return res_stats


def non_orth_score_w_g(y, d, l_hat, m_hat, g_hat, smpls, *kwargs):
    """Non-orthotogonal score for partial linear model, i.e., the naive partial linear model."""
    u_hat = y - g_hat
    psi_a = -np.multiply(d, d)
    psi_b = np.multiply(d, u_hat)
    return psi_a, psi_b
