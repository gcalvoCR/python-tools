import pandas as pd

def main():
  print("Hello, World!")

  sympsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_13_(2001%E2%80%9302)')

  print(f'Number of tables --> {len(sympsons)}')
  print(sympsons[1])

if __name__== "__main__" :
  main()