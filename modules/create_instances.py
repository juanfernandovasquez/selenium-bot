import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Fxservice
from selenium.webdriver.firefox.options import Options as Fxoptions
from selenium.webdriver.edge.service import Service as edservice
from selenium.webdriver.edge.options import Options as edoptions



def create_instances(instances):
    drivers_file = os.path.join(os.path.abspath(''),"drivers")
    
    user_agents = [
        "Mozilla/5.0 (Wind  ows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/74.0.3729.157 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.132 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/79.0.3945.117 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
    ]

    instances = [1]*instances

    if len(instances)>0:
        chrome_drivers = []
        if len(instances)>=2:
            for i in range(0,2):
                options = webdriver.ChromeOptions()
                options.add_argument(f'user-agent={user_agents.pop()}')
                driver = webdriver.Chrome(os.path.join(drivers_file,'chromedriver.exe'),options=options)
                chrome_drivers.append(driver)
                instances.pop()
        
        edge_drivers = []
        if len(instances)>=2:
            for i in range(0,2):
                edge_driver = os.path.join(drivers_file,'msedgedriver.exe')
                edge_service = edservice(edge_driver)
                edge_options = edoptions()
                edge_options.add_argument("inprivate")
                edge_options.add_argument(f'user-agent={user_agents.pop()}')
                driver = webdriver.Edge(service=edge_service, options=edge_options)
                edge_drivers.append(driver)
                instances.pop()
        

        firefox_drivers = []
        if len(instances)>=2:
            for i in range(0,2):
                firefox_driver = os.path.join(drivers_file,'geckodriver.exe')
                firefox_service = Fxservice(firefox_driver)
                profile = webdriver.FirefoxProfile()
                profile.set_preference("general.useragent.override", user_agents.pop())
                driver = webdriver.Firefox(service=firefox_service, firefox_profile=profile)
                firefox_drivers.append(driver)
                instances.pop()
        

        if len(instances)>=1:
            for i in range(0,1):
                edge_driver = os.path.join(drivers_file,'msedgedriver.exe')
                edge_service = edservice(edge_driver)
                edge_options = edoptions()
                edge_options.add_argument("inprivate")
                edge_options.add_argument(f'user-agent={user_agents.pop()}')
                driver = webdriver.Edge(service=edge_service, options=edge_options)
                edge_drivers.append(driver)
                instances.pop()



    total_drivers = firefox_drivers + chrome_drivers + edge_drivers
    return total_drivers