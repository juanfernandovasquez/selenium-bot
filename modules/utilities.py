def send_drivers_to_link(drivers, link):
    for driver in drivers:
        driver.get(link)

def close_drivers(dvrs):
    for dr in dvrs:
        dr.close()