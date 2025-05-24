from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import requests
import urllib.parse


def scrape_devops_certification(url, output_filename="devops_certification_details.txt", image_output_dir="images"):
    """
    Visits the given URL, extracts specific content using Selenium, saves it to a text file,
    downloads the certification image, and saves the image URL to the text file.
    """
    # Set up Chrome options for a headless browser
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=3")  # Suppress logs

    # Specify the path to your ChromeDriver executable
    # Replace 'path/to/chromedriver' with the actual path or ensure chromedriver is in PATH
    try:
        service = Service("path/to/chromedriver")  # e.g., Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Error setting up ChromeDriver service: {e}")
        print("Attempting to initialize without service object (if chromedriver is in PATH)...")
        driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        print(f"Successfully visited: {url}")

        # Extract content from specific elements
        content = []

        # Extract header information
        try:
            header = driver.find_element(By.CLASS_NAME, "certification-header")
            header_text = header.text
            content.append(header_text)
        except Exception as e:
            print(f"Could not find certification-header: {e}")

        # Extract certification description
        try:
            description = driver.find_element(By.CLASS_NAME, "certification-description")
            description_text = description.text
            content.append(description_text)
        except Exception as e:
            print(f"Could not find certification-description: {e}")

        # Extract image URL and download the image
        image_url = ""
        try:
            image_element = driver.find_element(By.CLASS_NAME, "certification-image").find_element(By.TAG_NAME, "img")
            image_url = image_element.get_attribute("src")
            # Parse the URL to handle relative paths
            if image_url.startswith("/"):
                base_url = urllib.parse.urljoin(url, "/")
                image_url = urllib.parse.urljoin(base_url, image_url.lstrip("/"))

            # Add image URL to content
            content.append(f"Image URL: {image_url}")

            # Create directory for image if it doesn't exist
            if not os.path.exists(image_output_dir):
                os.makedirs(image_output_dir)

            # Get the image filename from the URL
            image_filename = os.path.join(image_output_dir, os.path.basename(image_url))

            # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(image_filename, "wb") as img_file:
                    img_file.write(response.content)
                print(f"Image successfully saved to '{image_filename}'")
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
        except Exception as e:
            print(f"Could not download image or retrieve image URL: {e}")
            content.append("Image URL: Not found")

        # Save the extracted content and image URL to a text file
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write("\n\n".join(content))
        print(f"Content and image URL successfully saved to '{output_filename}'")


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        if 'driver' in locals() and driver is not None:
            driver.quit()
            print("Browser closed.")


if __name__ == "__main__":
    website_url = "https://shaxzodbek.com/certifications/devops-engineer-certification/"
    scrape_devops_certification(website_url)
