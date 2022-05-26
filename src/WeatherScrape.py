from msedge.selenium_tools import Edge, EdgeOptions
import time
import sys as system

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
path = 'path/to/browser/driver'
# Driver Config
driver = Edge(options=options, executable_path=path)


def getWeather(city):
    # Fetch Logic
    url = 'https://weather.com/en-IN/'
    # Launching the URL
    driver.get(url)
    # Waiting for the site to fully load.
    time.sleep(3.5)
    # Finding elements: Search Input
    searcher = driver.find_element_by_xpath('//*[@id="LocationSearch_input"]')
    searcher.click()
    # Sending search input.
    searcher.send_keys(enteredCity)
    # Waiting for search results to appear.
    time.sleep(3.5)

    # Getting exact location from search results:
    locationStr = driver.find_element_by_xpath(
        '//*[@id="LocationSearch_listbox-0"]')
    print('')
    print('⚡ Showing results for:',
          locationStr.text+'.😍')

    # Selecting result.
    searcher = driver.find_element_by_id('LocationSearch_listbox-0')
    searcher.click()
    tempFinder = driver.find_element_by_class_name(
        'CurrentConditions--tempValue--3a50n')
    print('')
    # Printing the fetched data.
    print("⚡ Current weather in", enteredCity.capitalize(),
          "is:", tempFinder.text+"C🌡"+'\n')
    # Forecast for the day:
    # Morning:
    foreCastMorn = driver.find_element_by_xpath(
        '//*[@id="WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a"]/section/div/ul/li[1]/a/div[1]/span')
    print("⚡ Today's Forecast for", enteredCity.capitalize()+':'+"\n")
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
        'DonutChart--innerValue--2rO41')
    airQualityIndexLevel = driver.find_element_by_class_name(
        'AirQualityText--severity--1fu5k')
    print(
        f"😷 Air Quality Index of {enteredCity.capitalize()}: {airQualityIndex.text}, {airQualityIndexLevel.text.upper()}.\n")
    # Closing browser connection.
    driver.close()


print('')
enteredCity = input("⏩ Enter Location: ")
print('')
print("🔃 Please wait while the Weather is being fetched...")
if len(enteredCity) == 0:
    print("Please enter location!")
    system.exit()
else:
    getWeather(enteredCity)
# End of the script.
