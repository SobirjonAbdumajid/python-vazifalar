# # # # # # # import requests
# # # # # # # from bs4 import BeautifulSoup

# # # # # # # url = 'https://kun.uz/news/main'  # Ruxsat berilgan saytni tanlang
# # # # # # # response = requests.get(url)
# # # # # # # soup = BeautifulSoup(response.text, 'html.parser')

# # # # # # # # Misol uchun, saytdan barcha <h1> teglarini olish
# # # # # # # h1_tags = soup.find_all('h1')
# # # # # # # for h1 in h1_tags:
# # # # # # #     print(h1.text)



# # # # # # import requests
# # # # # # from bs4 import BeautifulSoup

# # # # # # # Sahifaga so'rov yuborish
# # # # # # sahifa = "https://uzum.uz/uz/product/ogil-bolalar-uchun-tolstovka-diva-kids-25366"
# # # # # # r = requests.get(sahifa)

# # # # # # # HTML-ni tahlili
# # # # # # soup = BeautifulSoup(r.text, "html.parser")  # HTML-ni tahlili


# # # # # # # somsa_class = input("Qanday ma'lumot olmoqchisiz: ")

# # # # # # # topish
# # # # # # news = soup.find_all(class_="title")

# # # # # # for i in range(len(news)):
# # # # # #     print(news[i].text)
# # # # # # # print(len(news))


# # # # # # from bs4 import BeautifulSoup
# # # # # # import requests
# # # # # # from sites import siteLinks



# # # # # # for i in range(len(siteLinks)):

# # # # # #     url = siteLinks[i]
# # # # # #     page = requests.get(url)
# # # # # #     soup = BeautifulSoup(page.text, 'html.parser')

# # # # # #     with open(f'{i}-website.html', 'w') as file:
# # # # # #         file.write(soup)




# from bs4 import BeautifulSoup
# import requests
# import os
# import time
# from sites import siteLinks

# # Ensure the directory exists
# directory = 'websites'
# if not os.path.exists(directory):
#     os.makedirs(directory)

# # Assuming 'siteLinks' is a list of website URLs
# for i, url in enumerate(siteLinks):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#         response = requests.get(url, headers=headers, timeout=10)  # Adding a timeout
#         response.raise_for_status()  # will throw an exception for 4XX/5XX status
#         soup = BeautifulSoup(response.text, 'html.parser')

#         with open(os.path.join(directory, f'{i}-website.html'), 'w', encoding='utf-8') as file:
#             file.write(str(soup))

#         time.sleep(1)  # Pause for a second between requests to avoid rate limits

#     except requests.exceptions.RequestException as e:
#         print(f"Failed to retrieve {url}: {str(e)}")





# # # # # # import pandas as pd
# # # # # # from playwright.sync_api import sync_playwright


# # # # # # def main():
# # # # # #     with sync_playwright() as p:
# # # # # #         page_url = fr"https://kun.uz/"
# # # # # #         browser = p.chromium.launch(headless=False)
# # # # # #         page = browser.new_page()
# # # # # #         page.goto(page_url, timeout=600000)
# # # # # #         _count = page.locator('//div[@class="small-cards__default-text"]').all()
# # # # # #         print(f"{len(_count)} ta bor")
# # # # # #         _list = []
# # # # # #         for i in _count:
# # # # # #             phone_link_element = i.locator(
# # # # # #                 '//a[contains(@onclick, "showPhonePopup")]').first  # Find the link with the onclick
# # # # # #             onclick_value = phone_link_element.get_attribute('onclick')
# # # # # #             phone_parts = onclick_value.split(',')
# # # # # #             area_code = phone_parts[1].strip("' ")  # Remove quotes and spaces
# # # # # #             phone_number = phone_parts[0].strip("' ")
# # # # # #             full_phone_number = f"+998 {area_code} {phone_number}"
# # # # # #             _dict = {"name": i.locator('//a[@class="organizationName blueText"]').inner_text(),
# # # # # #                      "address": i.locator('//p[@class="address"]').inner_text().replace('Address: ',''),
# # # # # #                      "telephone": full_phone_number[:15]}
# # # # # #             _list.append(_dict)
# # # # # #         df = pd.DataFrame(_list)
# # # # # #         # df.to_excel("data3.xlsx", index=False)
# # # # # #         df.to_csv("data3.csv", index=False)
# # # # # #         browser.close()


# # # # # # if __name__ == "__main__":
# # # # # #     main()

# # -----------------------------------------------------------------------------------------------------------------------------


# # import pandas as pd
# # from playwright.sync_api import sync_playwright

# # def scrape_books():
# #     # Start Playwright in a context manager
# #     with sync_playwright() as p:
# #         # Launch a headless Chromium browser
# #         browser = p.chromium.launch(headless=True)
# #         page = browser.new_page()  # Open a new browser page

# #         # Navigate to the target webpage
# #         page.goto('https://asaxiy.uz/')

# #         # Wait for the page to load necessary elements
# #         page.wait_for_selector('div.book')

# #         # Use Playwright to extract book data
# #         books = page.query_selector_all('div.book')
# #         book_list = []

# #         # Iterate through each book block and extract details
# #         for book in books:
# #             title = book.query_selector('h3.title').text_content().strip()
# #             author = book.query_selector('span.author').text_content().strip()
# #             price = book.query_selector('span.price').text_content().strip()

# #             # Append each book's data to the list as a dictionary
# #             book_list.append({
# #                 'Title': title,
# #                 'Author': author,
# #                 'Price': price
# #             })

# #         # Close the browser
# #         browser.close()

# #         # Convert the list of dictionaries into a DataFrame
# #         df = pd.DataFrame(book_list)

# #         # Save the DataFrame to a CSV file
# #         df.to_csv('books_data.csv', index=False)

# #         print("Data scraped and saved to books_data.csv")

# # # Call the function to execute the scraping
# # if __name__ == '__main__':
# #     scrape_books()



# # -----------------------------------------------------------------------------------------------------------------------------




# # # # # # from playwright.sync_api import sync_playwright

# # # # # # def scrape_books_by_classes():
# # # # # #     with sync_playwright() as p:
# # # # # #         browser = p.chromium.launch(headless=True)
# # # # # #         page = browser.new_page()
# # # # # #         # Increase the timeout for page loading
# # # # # #         page.goto('https://asaxiy.uz/product/knigi', timeout=60000)

# # # # # #         # Correcting the class selector
# # # # # #         books = page.query_selector_all('.produrct__item-prices--wrapper')  # Example: use a dot for class, correct typo if any
# # # # # #         for book in books:
# # # # # #             # Assuming corrected class names below, ensure no spaces in class names
# # # # # #             price = book.query_selector('span').text_content().strip() if book.query_selector('.product__item-price.product-main-price-id-67861') else "No price"

# # # # # #             print(f"Price: {price}")

# # # # # #         browser.close()

# # # # # # if __name__ == '__main__':
# # # # # #     scrape_books_by_classes()




# # -----------------------------------------------------------------------------------------------------------------------------




# # from playwright.sync_api import sync_playwright

# # def scrape_product_details():
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=True)  # Use headless=False if you want to see the browser
# #         page = browser.new_page()
# #         page.goto('https://asaxiy.uz/product/knigi', timeout=60000)  # Ensure the URL is correct

# #         # Wait for the product items to load on the page
# #         page.wait_for_selector('.product__item')

# #         # Fetch all product items
# #         products = page.query_selector_all('.product__item')

# #         for product in products:
# #             # Extract title
# #             title_element = product.query_selector('.product__item__info-title')
# #             title = title_element.text_content().strip() if title_element else "Title not found"

# #             # Extract price
# #             price_element = product.query_selector('.product__item-price')
# #             price = price_element.text_content().strip() if price_element else "Price not found"

# #             print(f"Title: {title}, Price: {price}")

# #         browser.close()

# # if __name__ == '__main__':
# #     scrape_product_details()


# # -----------------------------------------------------------------------------------------------------------------------------




# # # # # from playwright.sync_api import sync_playwright

# # # # # def scrape_product_price():
# # # # #     with sync_playwright() as p:
# # # # #         # Launch the browser in headless mode
# # # # #         browser = p.chromium.launch(headless=True)
# # # # #         page = browser.new_page()
        
# # # # #         # Navigate to the specific product page
# # # # #         page.goto('https://uzum.uz/uz/pruduct', timeout=60000)  # Update with the correct URL
        
# # # # #         # Wait for the product price element to load on the page
# # # # #         page.wait_for_selector('.product-card-price', timeout=60000)  # Adjust class name as needed
        
# # # # #         # Select the element that contains the product price and extract its text
# # # # #         price_element = page.query_selector('.product-card-price')
# # # # #         if price_element:
# # # # #             price = price_element.text_content().strip()
# # # # #             print(f"Price: {price}")
# # # # #         else:
# # # # #             print("Price element not found")

# # # # #         # Close the browser
# # # # #         browser.close()

# # # # # if __name__ == '__main__':
# # # # #     scrape_product_price()


# # # # import pandas as pd
# # # # from playwright.sync_api import sync_playwright

# # # # def scrape_products(url):
# # # #     with sync_playwright() as p:
# # # #         # Launch browser
# # # #         browser = p.chromium.launch(headless=False)  # Set headless=False if you want to see the browser
# # # #         page = browser.new_page()

# # # #         # Go to the page
# # # #         page.goto(url)

# # # #         # Extract product details
# # # #         products = []
# # # #         # This selector should match the overall container of each product  
# # # #         product_elements = page.query_selector_all(".product-card-price-info")

# # # #         for product_element in product_elements:
# # # #             # name = product_element.query_selector(".").inner_text()
# # # #             price = product_element.query_selector(".card-info-block is-vertical").inner_text()
# # # #             products.append({
# # # #                 'Price': price
# # # #             })

# # # #         # Close browser
# # # #         browser.close()

# # # #         return products

# # # # def main():
# # # #     url = 'https://uzum.uz/uz/pruduct'  # Change to your target URL
# # # #     product_data = scrape_products(url)
# # # #     df = pd.DataFrame(product_data)
# # # #     print(df)
# # # #     df.to_csv("product_data.csv", index=False)  # Save the data to a CSV file

# # # # if __name__ == "__main__":
# # # #     main()




# # # import pandas as pd
# # # from playwright.sync_api import sync_playwright

# # # def main() -> None:
# # #     with sync_playwright() as p:
# # #         link: str = "https://uzum.uz/uz/category/elektronika-savdosi--554?currentPage=2"
# # #         browser = p.chromium.launch(headless=False)
# # #         page = browser.new_page()
# # #         page.goto(link, timeout=600000)

# # #         # Wait for the products to load
# # #         page.wait_for_selector('.product-card', timeout=60000)

# # #         products = page.query_selector_all('.product-card')
# # #         _list = []

# # #         for product in products:
# # #             try:
# # #                 name = product.query_selector('.subtitle-item').inner_text()  # type: ignore
# # #                 # Use the text__price id to get the price
# # #                 price = product.query_selector('[data-test-id="text__price"]').inner_text()  # type: ignore
# # #                 _dict = {
# # #                     "name": name,
# # #                     "price": price
# # #                 }
# # #                 _list.append(_dict)
# # #             except Exception as e:
# # #                 print(f"Error scraping product: {e}")

# # #         df = pd.DataFrame(_list)
# # #         df.to_excel("uzum_data.xlsx", index=False)
# # #         df.to_csv("data3.csv", index=False)
# # #         print(f"Scraped {len(_list)} products")

# # #         browser.close()

# # # if __name__ == "__main__":
# # #     main()




# # import os
# # from playwright.sync_api import sync_playwright
# # from sites import siteLinks

# # def save_webpage_html(url, i, directory='html'):
# #     # Ensure the directory exists
# #     os.makedirs(directory, exist_ok=True)

# #     # Initialize Playwright and start a browser
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=True)  # Run headless for automation
# #         page = browser.new_page()

# #         # Go to the specified URL
# #         try:
# #             page.goto(url, timeout=60000)
# #         except Exception as e:
# #             print(f"An error occurred: {str(e)}")
# #     # Optionally, retry or handle the error accordingly

# #         # Get the HTML content of the page
# #         html_content = page.content()

# #         # Define the path for the HTML file
# #         filename = os.path.join(directory, f'{i}-webpage.html')

# #         # Save the HTML content to a file
# #         with open(filename, 'w', encoding='utf-8') as file:
# #             file.write(html_content)

# #         # Close the browser
# #         browser.close()

# #     print(f'HTML content has been saved to {filename}')

# # # Example usage:
# # if __name__ == "__main__":
# #     for i in range(len(siteLinks)):
# #         url = siteLinks[i]  # Replace with your target URL
# #         save_webpage_html(url, i)





# # import pandas
# # from playwright.sync_api import sync_playwright

# # def main() -> None:
# #     with sync_playwright() as p:
# #         link: str = "https://uzum.uz/uz"
# #         browser = p.chromium.launch(headless=False)
# #         page = browser.new_page()
# #         page.goto(link, timeout=600000)

# #         # Wait for the products to load
# #         page.wait_for_selector('.product-card', timeout=60000)

# #         products = page.query_selector_all('.product-card')
# #         _list = []

# #         for product in products:
# #             try:
# #                 name = product.query_selector('.subtitle-item').inner_text()  # type: ignore
# #                 price = product.query_selector('[data-test-id="text__price"]').inner_text()  # type: ignore
# #                 previousPrice = product.query_selector('[data-test-id="text__old-price"]').inner_text()  # type: ignore
# #                 text_rating = product.query_selector('[data-test-id="text__rating"]').inner_text()  # type: ignore
# #                 _dict = {
# #                     "name": name,
# #                     "price": price,
# #                     "previous price": previousPrice,
# #                     "text rating": text_rating,
# #                 }
# #                 _list.append(_dict)
# #             except Exception as e:
# #                 print(f"Error scraping product: {e}")

# #         df = pandas.DataFrame(_list)
# #         df.to_excel("uzum_data.xlsx", index=False)
# #         df.to_csv("data.csv", index=False)
# #         print(f"Scraped {len(_list)} products")

# #         browser.close()

# # if __name__ == "__main__":
# #     main()



# # import pandas as pd
# # from playwright.sync_api import sync_playwright
# # from sites import site_configs

# # import pandas as pd
# # from playwright.sync_api import sync_playwright

# # def main() -> None:
# #     all_products = []
# #     with sync_playwright() as p:
# #         for site_name, config in site_configs.items():
# #             browser = p.chromium.launch(headless=False)
# #             page = browser.new_page()
# #             page.goto(config['url'], timeout=600000)

# #             # Wait for the products to load
# #             page.wait_for_selector(config['product_selector'], timeout=60000)

# #             products = page.query_selector_all(config['product_selector'])
# #             _list = []

# #             for product in products:
# #                 try:
# #                     name = product.query_selector(config['name_selector']).inner_text()
# #                     price = product.query_selector(config['price_selector']).inner_text()
# #                     _dict = {
# #                         "name": name,
# #                         "price": price
# #                     }
# #                     _list.append(_dict)
# #                 except Exception as e:
# #                     print(f"Error scraping product on {site_name}: {e}")

# #             all_products.extend(_list)
# #             browser.close()
# #             print(f"Scraped {len(_list)} products from {site_name}")

# #     df = pd.DataFrame(all_products)
# #     df.to_csv("data.csv", index=False)
# #     print("Data saved to data.csv")

# # if __name__ == "__main__":
# #     main()






# # # def main() -> None:
# # #     with sync_playwright() as p:
# # #         link: str = "https://uzum.uz/uz/"
# # #         browser = p.chromium.launch(headless=False)
# # #         page = browser.new_page()
# # #         page.goto(link, timeout=600000)

# # #         # Wait for the products to load
# # #         page.wait_for_selector('.product-card', timeout=60000)

# # #         products = page.query_selector_all('.product-card')
# # #         _list = []

# # #         for product in products:
# # #             try:
# # #                 name = product.query_selector('.subtitle-item').inner_text()  # type: ignore
# # #                 # Use the text__price id to get the price
# # #                 price = product.query_selector('[data-test-id="text__price"]').inner_text()  # type: ignore
# # #                 _dict = {
# # #                     "name": name,
# # #                     "price": price
# # #                 }
# # #                 _list.append(_dict)
# # #             except Exception as e:
# # #                 print(f"Error scraping product: {e}")

# # #         df = pd.DataFrame(_list)
# # #         # df.to_excel("uzum_data.xlsx", index=False)
# # #         df.to_csv("data.csv", index=False)
# # #         print(f"Scraped {len(_list)} products")

# # #         browser.close()

# # # if __name__ == "__main__":
# # #     main()





























# # from playwright.sync_api import sync_playwright

# # def scrape_product_details():
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=True)  # Use headless=False if you want to see the browser
# #         page = browser.new_page()
# #         page.goto('https://asaxiy.uz/product/knigi', timeout=60000)  # Ensure the URL is correct

# #         # Wait for the product items to load on the page
# #         page.wait_for_selector('.product__item')

# #         # Fetch all product items
# #         products = page.query_selector_all('.product__item')

# #         for product in products:
# #             # Extract title
# #             title_element = product.query_selector('.product__item__info-title')
# #             title = title_element.text_content().strip() if title_element else "Title not found"

# #             # Extract price
# #             price_element = product.query_selector('.product__item-price')
# #             price = price_element.text_content().strip() if price_element else "Price not found"

# #             print(f"Title: {title}, Price: {price}")

# #         browser.close()

    
# # for k, v in site_configs.items():
# #     print(k, v['url'])
    
    
import pandas as pd
from playwright.sync_api import sync_playwright
from sites import site_configs

def main() -> None:
    with sync_playwright() as p:
        for k, v in site_configs.items():
            link: str = v['url']
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(link, timeout=600000)

        # Wait for the products to load
            page.wait_for_selector(v["wait_for_selector"], timeout=60000)

            products = page.query_selector_all(v["wait_for_selector"])
            _list = []

            for product in products:
                try:
                    name = product.query_selector(v["query_selector1"]).inner_text()  # type: ignore
                    # Use the text__price id to get the price
                    price = product.query_selector(v["query_selector2"]).inner_text()  # type: ignore
                    _dict = {
                        "name": name,
                        "price": price
                    }
                    _list.append(_dict)
                except Exception as e:
                    print(f"Error scraping product: {e}")

            df = pd.DataFrame(_list)
            # df.to_excel("uzum_data.xlsx", index=False)
            df.to_csv(f"{k}.csv", index=False)
            print(f"Scraped {len(_list)} products")

            browser.close()

if __name__ == "__main__":
    main()







# # import pandas as pd
# # from playwright.sync_api import sync_playwright
# # from sites import site_configs

# # def scrape_product_details():
# #     product_list = []
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=True)  # You can set headless=False to see the browser
# #         page = browser.new_page()
# #         for k, v in site_configs.items():
# #             pass
# #             page.goto(v['url'], timeout=60000)  # Ensure the URL is correct

# #         # Wait for the product items to load on the page
# #             page.wait_for_selector(v['wait_for_selector'], timeout=60000)

# #         # Fetch all product items
# #             products = page.query_selector_all(v['wait_for_selector'])

# #             for product in products:
# #                 try:
# #                     # Extract title
# #                     title_element = product.query_selector(v["query_selector1"])
# #                     title = title_element.text_content().strip() if title_element else "Title not found"

# #                     # Extract price
# #                     price_element = product.query_selector(v["price_selector2"])
# #                     price = price_element.text_content().strip() if price_element else "Price not found"

# #                     # Append product details to list
# #                     product_list.append({"Title": title, "Price": price})

# #                 except Exception as e:
# #                     print(f"Error scraping product details: {e}")

# #             # Save product data to a DataFrame and then to CSV
# #             df = pd.DataFrame(product_list)
# #             df.to_csv(f"{k}.csv", index=False)
# #             print(f"Scraped {len(product_list)} products")

# #             browser.close()

# # if __name__ == "__main__":
# #     scrape_product_details()



# # # for k, v in site_configs.items():
# # #     print(k, v['url'])