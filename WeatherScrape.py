from msedge.selenium_tools import Edge, EdgeOptions
import time as t
import sys

# Global variables:

# Options for Microsoft Edge
options = EdgeOptions()
options.use_chromium = True
# Headless Mode
options.add_argument('headless')
# Disabling Log
options.add_argument('--log-level=3')
# Disabling every log
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Driver Path
path = r'C:\Users\farma\Downloads\edgedriver\msedgedriver.exe'
# Driver Config
driver = Edge(options=options, executable_path=path)


def fetcher():
    # Fetch Logic
    url = 'https://weather.com/en-IN/'
    # Launching the URL
    driver.get(url)
    # Waiting for the site to fully load.
    t.sleep(3)
    # Finding elements: Search Input
    searcher = driver.find_element_by_xpath('//*[@id="LocationSearch_input"]')
    searcher.click()
    # Sending search input.
    searcher.send_keys(SearchString)
    # Waiting for search results to appear.
    t.sleep(2.5)

    # Getting exact location from search results:
    locationStr = driver.find_element_by_xpath(
        '//*[@id="LocationSearch_listbox-0"]')
    print('')
    print('⚡ Location:',
          locationStr.text+'.😍')

    # Selecting result.
    searcher = driver.find_element_by_id('LocationSearch_listbox-0')
    searcher.click()
    tempFinder = driver.find_element_by_class_name(
        'CurrentConditions--tempValue--3KcTQ')
    print('')
    # Printing the fetched data.
    print("⚡ Current weather in", SearchString.capitalize(),
          "is:", tempFinder.text+"C🌡"+'\n')
    # Forecast for the day:
    # Morning:
    foreCastMorn = driver.find_element_by_xpath(
        '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("⚡ Today's Forecast for", SearchString.capitalize()+':'+"\n")
    print('⚡ Morning:', foreCastMorn.text+"C"+'\n')
   # Afternoon
    foreCastAftn = driver.find_element_by_xpath(
        '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[2]/a/div[1]/span')
    print("⚡ Afternoon:", foreCastAftn.text+"C"+'\n')
   # Evening:
    foreCastEve = driver.find_element_by_xpath(
        '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[3]/a/div[1]/span')
    print("⚡ Evening:", foreCastEve.text+"C"+'\n')
    # Overnight:
    foreCastOvernight = driver.find_element_by_xpath(
        '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[4]/a/div[1]/span')
    print("⚡ Overnight:", foreCastOvernight.text+"C"+'\n')
    # Air Quality Index
    airQualityIndex = driver.find_element_by_class_name(
        'DonutChart--innerValue--k2Z7I')
    airQualityIndexLevel = driver.find_element_by_class_name(
        'AirQualityText--severity--1VMr2')
    print("😷 Air Quality Index of", SearchString.capitalize() +
          ":", airQualityIndex.text, airQualityIndexLevel.text.upper()+'\n')
    # Closing browser connection.
    driver.close()


print('')
SearchString = input("⏩ Enter Location: ")
print('')
print("🔃 Please wait while the details are being fetched...")
if len(SearchString) == 0:
    print("Please enter location!")
    sys.exit()
else:
    fetcher()
# End of the script.
