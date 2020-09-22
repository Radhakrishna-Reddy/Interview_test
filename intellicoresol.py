from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

try:
    driver = webdriver.Chrome("C:\\Users\\radhakrishna_reddy\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
    products=[] #List to store name of the product
    prices=[] #List to store price of the product
    driver.get("https://www.flipkart.com/all/apple~brand/pr?sid=all")
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('a',href=True, attrs={'class':"niH0FQ _36Fcw_"}:
                      name=a.find('div', attrs={'class':'_2_KrJI'})
                      price=a.find('div', attrs={'class':'_2lQ_WZ'})
                      products.append(name.text)
                      prices.append(price.text)
    CSV_data = pd.DataFrame({'Device details':products,'Price':prices})df.to_csv('products.csv', index=False, encoding='utf-8')
                      )
    print(CSV_data)

except FileNotFoundError:
        print("Wrong file or file path")
