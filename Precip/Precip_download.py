"""
Primitive automate download of file one by one from the
king county website using selenium module
"""
import selenium  
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = selenium.webdriver.Firefox()
#names browser for driver variable
browser.get('https://green2.kingcounty.gov/hydrology/DataDownload.aspx')
#opens up to website using FireFox and geckodriver for firefox

select = Select(browser.find_element_by_id("SiteDropDownList"))
#creates select variable to click on dropdown menu of specific weather station
select.select_by_visible_text('SERE')
#clicks on dropdown menu the specfic weather station via name
browser.find_element_by_id("ParameterDropDownList_sl").click()
#opens up the parameter dropdown menu
browser.find_element_by_id("ParameterDropDownList_0").click()
#selects the checkbox for the parameter thats first on the dropdown
#if wanting second or another, change the number at end to that specific one
browser.find_element_by_xpath("//input[@value='Submit']").click()
#hits the submit button after selecting parameters
#king county fills in the rest of the data such as start/end dates and reporting intervals
browser.find_element_by_id("ctl00_kcMasterPagePlaceHolder_DownloadContinuousDataUI").click()
#hits the download button
