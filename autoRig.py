import time
from selenium import webdriver

def main(rigRound:int=0, rigMax:int=0):
    print(f"doing {rigMax} rounds")
    print(f"round: {rigRound}")
    polls = {
            "poll1": '//*[@id="option-05ZdRzJQVn6"]',
            "poll2": '//*[@id="option-eNg6Dv4deyA"]',
            "poll3": '//*[@id="option-BJnXLVlaLnv"]',
        }
    school_polls = {
            "afterski": '//*[@id="option-NMnQk5M7MZ6"]',
            "VM":       '//*[@id="option-DwyooDrRxyA"]',
            "juletema": '//*[@id="option-eNg6D9kx3yA"]',
        }
    global driver
    driver = webdriver.Firefox()
    #school_url = "https://strawpoll.com/polls/kogjv3NP3g6/"
    url = "https://strawpoll.com/polls/61gDB8rvRyw"
    print(f"going to {url}")
    driver.get(url)
    print("finding consent button")
    time.sleep(1)
    driver.find_element_by_class_name("fc-button-label").click()
    print("clicking poll option 1")
    time.sleep(1)
    driver.find_element_by_xpath(polls["poll1"]).click()
    print("finding vote button")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/form/div[8]/div/div[2]/button").click()

try:
    rigMax = 2
    for i in range(2):
        #consent()
        main(i,rigMax)
        driver.close()
except Exception as e:
    driver.close()
    print(e)