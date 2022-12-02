from tqdm import tqdm
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import argparse

parser = argparse.ArgumentParser(
            prog="autoRig",
            description="a program to bot strawpolls",
            epilog="made by @Tr4shL0rd"
        )
parser.add_argument(
            "--headless",
            dest="headless",
            action="store_true",
            default=True,
            help="headless mode"
        )
parser.add_argument(
            "-a",
            dest="amount",
            action="store",
            type=int,
            default=10,
            help="amount of rounds to run"
        )
parser.add_argument(
            "-p",
            dest="poll",
            action="store",
            default="poll1",
            help="poll option to bot"
        )
args = parser.parse_args()

def main(rigRound:int=0, rigMax:int=0):
    options = Options()
    options.headless = args.headless
    polls = {
            "poll1": '//*[@id="option-05ZdRzJQVn6"]',
            "poll2": '//*[@id="option-eNg6Dv4deyA"]',
            "poll3": '//*[@id="option-BJnXLVlaLnv"]',
        }
    #school_url = "https://strawpoll.com/polls/kogjv3NP3g6/"
    school_polls = {
            "afterski": '//*[@id="option-NMnQk5M7MZ6"]',
            "VM":       '//*[@id="option-DwyooDrRxyA"]',
            "juletema": '//*[@id="option-eNg6D9kx3yA"]',
        }
    global driver
    driver = webdriver.Firefox(options=options)
    url = "https://strawpoll.com/polls/61gDB8rvRyw"
    # going to url
    driver.get(url)
    # finding consent button
    time.sleep(1)
    driver.find_element_by_class_name("fc-button-label").click()
    # clicking poll 
    time.sleep(1)
    driver.find_element_by_xpath(polls[args.poll]).click()
    # finding vote button
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/form/div[8]/div/div[2]/button").click()

try:
    base_time = 8
    print(f"doing {args.amount} rounds")
    for i in tqdm(range(args.amount)):
        main(i,args.amount)
        driver.close()
except Exception as e:
    driver.close()
    print(e)