import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from sklearn.metrics import r2_score


def graph_animated(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    def animate(frame):
        ax.clear()
        
        year = str(2000 + frame)
        current_data = data[year].values
        
        bars = ax.barh(data['Countries'], current_data)
        
        ax.set_title(f'Aluminium Importation in {year}')
        ax.set_xlabel('Quantity in tonnes')
        ax.ticklabel_format(axis='x', style='plain')
        
        for i, v in enumerate(current_data):
            ax.text(v, i, f'{v:,.0f}', 
                    va='center', fontsize=8)

    anim = animation.FuncAnimation(fig, animate, 
                                frames=24, 
                                interval=300,
                                repeat=True)

    anim.save('country_data.gif', writer='pillow')

def country_graph(data, country):
    unpivot_data = data.melt(id_vars=['Countries'], var_name='Year', value_name='Quantity')
    country_data = unpivot_data[unpivot_data['Countries'] == country]
    country_data = country_data.drop('Countries', axis=1).reset_index(drop=True)
    return country_data

def import_evolution(data, country):
    unpivot_data = data.melt(id_vars=['Countries'], var_name='Year', value_name='Quantity')
    country_data = unpivot_data[unpivot_data['Countries'] == country]

    plt.figure(figsize=(10, 6))
    plt.plot(country_data['Year'], country_data['Quantity'], 'o-')
    plt.title('Aluminium Importation in ' + country)
    plt.xlabel('Year')
    plt.ylabel('Quantity in tonnes')
    plt.xticks(rotation=45, ha='right')
    plt.ticklabel_format(axis='y', style='plain')
    plt.show()

def linear_regression(data, country):
    country_data = country_graph(data, country)

    country_data['Year'] = country_data['Year'].apply(lambda x: int(x))

    reg = np.polyfit(country_data['Year'], country_data['Quantity'], deg=1)
    trend = np.polyval(reg, country_data['Year'])

    print(f'R2 Score: {r2_score(country_data["Quantity"], trend):.2f}')

    future_years = np.arange(country_data['Year'].max(), 2035)
    future_trend = np.polyval(reg, future_years)

    plt.scatter(country_data['Year'], country_data['Quantity'])
    plt.plot(country_data['Year'], trend)
    plt.plot(future_years, future_trend, linestyle='--', color='red')
    plt.title('Aluminium Importation in ' + country)
    plt.xlabel('Year')
    plt.ylabel('Quantity in tonnes')
    plt.xticks(rotation=45, ha='right')
    plt.ticklabel_format(axis='y', style='plain')
    plt.show()