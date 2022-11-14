import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def login_sample_user():
    element = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/form/div[4]/div[2]/button")
    element.send_keys(Keys.RETURN)
    time.sleep(1)


def load_client_data():
    load = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/button")
    load.send_keys(Keys.RETURN)
    time.sleep(1)


def create_clients():
    create = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/button[1]")
    create_results = open('results/create_results_2.txt', 'w+')
    for i in range(100):
        time.sleep(1)
        create.send_keys(Keys.RETURN)
        time_create = \
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/label[1]/span").text.split(
                ': ')[1]
        create_results.write(f'{i+1}, {time_create}\n')


def read_client():
    read = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/button[2]")
    read_results = open('results/read_results.txt', 'w+')
    for i in range(100):
        time.sleep(1)
        read.send_keys(Keys.RETURN)
        time_read = \
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/label[2]/span").text.split(
                ': ')[1]
        read_results.write(f'{i + 1}, {time_read}\n')


def update_client():
    update = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/button[3]")
    update_results = open('results/update_results.txt', 'w+')
    for i in range(100):
        time.sleep(1)
        update.send_keys(Keys.RETURN)
        time_update = \
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/label[3]/span").text.split(
                ': ')[1]
        update_results.write(f'{i + 1}, {time_update}\n')


def delete_client():
    id_input = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/span/input")
    delete = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/button[4]")
    delete_results = open('results/delete_results.txt', 'w+')
    for i in range(100):
        time.sleep(1)
        client_id = 100 - i
        id_input.send_keys(str(client_id))
        time.sleep(1)
        delete.send_keys(Keys.RETURN)
        time_delete = \
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div[3]/label[4]/span").text.split(
                ': ')[1]
        delete_results.write(f'{i + 1}, {time_delete}\n')
        id_input.clear()


if __name__ == '__main__':
    driver.get("https://personal-j9nmhmsb.outsystemscloud.com/UI")
    time.sleep(3)
    login_sample_user()
    load_client_data()
    # create_clients()
    # read_client()
    # update_client()
    # delete_client()

