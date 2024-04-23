import os
import requests

def fetchAndSaveToFile(url, path):
    try:#This try block starts error handling. Inside it, we make an HTTP GET request to the specified URL using requests.get(url) and store the response object in the variable response.
        response = requests.get(url)
        if response.status_code == 200:
            #to check if response was sucessfull
            os.makedirs(os.path.dirname(path), exist_ok=True)
            #This line ensures that the directory where we want to save the file exists. It creates the directory if it doesn't exist (exist_ok=True).
            with open(path, "wb") as f:
                #binary write mode ("wb"), which is suitable for writing binary data such as the content of a webpage.
                f.write(response.content)
                #we write the binary content of the response (response.content) to the file opened earlier.
            print("File saved successfully.")
        else:
            print("Failed to fetch the URL:", url)
    except Exception as e:
        print("An error occurred:", e)

url = "https://timesofindia.indiatimes.com/city/mumbai"
fetchAndSaveToFile(url, "data/times.html")
