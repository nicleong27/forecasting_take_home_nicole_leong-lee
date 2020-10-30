import matplotlib.pyplot as plt
plt.style.use('ggplot')

import seaborn as sns
sns.set_style('darkgrid')


def plot_line(x, y, title, xlabel, ylabel, ax):
    '''
    Plots line graph

    Parameters
    ----------
    x : pandas series
    y : pandas series
    title: string
    xlabel: string
    ylabel: string

    Returns: 
    --------
    None
    '''

    plt.plot(x, y, alpha=0.8, color='tab:blue')
    plt.title(title, fontsize=25)
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()


def plot_mult_lines_groupby(groups, title, xlabel, ylabel, ax):
    '''
    Plots multiple line graphs on one plot based on groupby

    Parameters
    ----------
    x : pandas series
    y : pandas series
    title: string
    xlabel: string
    ylabel: string

    Returns: 
    --------
    None
    '''

    ax.set_prop_cycle(color=['tab:blue', 'tab:orange', 'tab:green', 'tab:red',
        'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray',
        'tab:olive', 'tab:cyan'])

    for key, group in groups:
        ax.plot(group.month, group.y, label=key)

    plt.legend(fontsize=13, bbox_to_anchor=(1.05, 1))
    plt.title(title, fontsize=25)
    ax.set_xlabel(xlabel, fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()


def compare_test_forecast(test_x, test_y, forecast_x, forecast_y, title, ax):
    '''
    Plots line graphs comparing test set vs predicted values from model

    Parameters
    ----------
    test_x : pandas series
    test_y : pandas series
    forecast_x : pandas series
    forecast_y : pandas series
    title : string

    Returns: 
    --------
    None
    '''
    
    plt.plot(test_x, test_y, color='red', label='Test')
    plt.plot(forecast_x, forecast_y, color='tab:blue', label='Forecast')
    plt.legend(fontsize=13)

    plt.title(title, fontsize=25)
    ax.set_xlabel('Month', fontsize=20)
    ax.set_ylabel('Price', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()