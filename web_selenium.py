from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://www.upm.es/politecnica_virtual")
try:
    elem = browser.find_element_by_class_name('bookcover')
    print("Found <%s> element with that class name!" % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
browser.close()
print("Navegador cerrado")
