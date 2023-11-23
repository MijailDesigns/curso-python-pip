import utils 
import read_csv
import charts
import pandas as pd

def run():
  data = read_csv.read_csv('./data.csv')
  # data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  # countries = list(map(lambda x: x['Country/Territory'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  country = input('introduce el nombre del pais: ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    keys, values = utils.get_population(country)
    print(keys, values)
    charts.generate_bar_chart(country['Country/Territory'], keys, values)
  

if __name__ == '__main__':
  run()