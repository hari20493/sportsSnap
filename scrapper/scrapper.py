import requests
from bs4 import BeautifulSoup



class Scrapper:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()

    def get_soup(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def get_elements(self,element=None,class_name=None):
        if element and class_name:
            events = self.soup.find_all(element,class_name)
        elif element and not class_name:
            events = self.soup.find_all(element)
        elif class_name and not element:
            events = self.soup.find_all('div')
        else:
            raise Exception("No element or class_name provided")

        return events
    
    def get_elements_from_find_all(self,event=None,element=None,class_name=None):
        if event and element and class_name:
            event_data = event.find(element,class_name)
        else:
            raise Exception("Provide event, element and class_name")

        return event_data
    
if __name__ == "__main__":
    print(events_list)




