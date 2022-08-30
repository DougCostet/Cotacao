from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def cotacaodl():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://google.com")
    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação dolar')
    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
    dl = driver.find_element('xpath',
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
    dl=float(dl)
    return dl


def cotacaoeu():
    tot=0
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.google.com.br/')
    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação Euro')
    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
    eu = driver.find_element('xpath',
                             '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute(
        'data-value')
    tot+=1
    return eu


def cotacaobt():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.google.com.br/')

    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
        'Cotação Bitcoin')
    driver.find_element('xpath',
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
    bt = driver.find_element('xpath',
                             '//*[@id="crypto-updatable_2"]/div[3]/div[5]/div[2]/input').get_attribute('value')
    return bt
    