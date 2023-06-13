from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Configure the Selenium web driver
path_driver= 'C:\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path_driver)

# Open the webpage
url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
driver.get(url)

# Wait for the desired content to load
driver.implicitly_wait(15)

# Scraping product listing pages
product_urls = []
product_names = []
product_prices = []
ratings = []
review_counts = []

while True:
    try:
        # Find the elements containing the product details
        product_elements = driver.find_elements_by_css_selector('[class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"]')
        
        # Extract information from each product element
        for element in product_elements:
            data=[]
            # Extract product URL
            product_url = element.find_element_by_css_selector('[class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute('href')
            data.append(product_url)
            
            # Extract product name
            product_name = element.find_element_by_css_selector('[class="a-size-medium a-color-base a-text-normal"]').text
            data.append(product_name)
            
            # Extract product price
            product_price = element.find_element_by_css_selector('[class="a-price-whole"]').text
            if product_price:
                data.append(product_price)
            else:
                data.append('N/A')
            
            # Extract product rating
            rating = element.find_element_by_css_selector('[class="a-icon-alt"]').get_attribute('textContent')
            if rating:
                data.append(rating)
            else:
                data.append('N/A')
            
            # Extract product review count
            review_count = element.find_element_by_css_selector('[class="a-size-base s-underline-text"]').text
            if review_count:
                data.append(review_count)
            else:
                data.append('N/A')

            if 'N/A' not in data:
                product_urls.append(product_url)
                product_names.append(product_name)
                product_prices.append(product_price)
                ratings.append(rating)
                review_counts.append(review_count)
                
        next_button = driver.find_element_by_xpath('//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
        new_url = next_button.get_attribute('href')
        driver.get(new_url)
        driver.implicitly_wait(15)
    except:
        break

# Create a DataFrame with the extracted data
data = {
    'Product URL': product_urls,
    'Product Name': product_names,
    'Product Price': product_prices,
    'Rating': ratings,
    'Review Count': review_counts
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('Amazon products.xlsx', index=False)

# Close the driver
driver.quit()
