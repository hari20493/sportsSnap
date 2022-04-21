from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import datetime
from scrapper.scrapper import Scrapper

def index(request):
    return render(request, 'index.html')

def scrapData():
    soup_class = Scrapper(url="https://www.formula1.com/en/racing/2022.html")
    events = soup_class.get_elements("a","event-item-wrapper") 
    date = datetime.datetime.today()
    year = date.strftime("%Y")

    events_list = []
    for e in events:
        events_dict = {}
        rounds = soup_class.get_elements_from_find_all(event=e,element="legend",class_name="card-title")
        start_date = soup_class.get_elements_from_find_all(event=e,element="span",class_name="start-date")
        end_date = soup_class.get_elements_from_find_all(event=e,element="span",class_name="end-date")
        month = soup_class.get_elements_from_find_all(event=e,element="span",class_name="month-wrapper")
        event_place = soup_class.get_elements_from_find_all(event=e,element="div",class_name="event-place")
        event_title = soup_class.get_elements_from_find_all(event=e,element="div",class_name="event-title")
        race_status = soup_class.get_elements_from_find_all(event=e, element="span", class_name="finish-wrapper")
        
        month_split = month.text.split("-")
        if len(month_split) > 1:
            month_valid = month_split[1]
        else:
            month_valid = month_split[0]

        date_string = end_date.text + " " + month_valid +" "+ str(year)

        date_object = datetime.datetime.strptime(date_string, "%d %b %Y")
        
        if race_status or date_object < date:
            events_dict["race_status"] = "Complete"
        else:
            events_dict["race_status"] = "Upcoming"
        
        events_dict["round"] = rounds.text
        events_dict["start_date"] = start_date.text
        events_dict["end_date"] = end_date.text
        events_dict["month"] = month.text
        events_dict["event_place"] = event_place.text
        events_dict["event_title"] = event_title.text

        if rounds.text != "TESTING" and events_dict["race_status"] == 'Complete':
            events_dict["leaderboard"] = {}
            for i in range(1,4):

                position = soup_class.get_elements_from_find_all(event=e,element="div",class_name="position-"+str(i))
            
                pos_driver = soup_class.get_elements_from_find_all(event=position,element="span",class_name="f1-uppercase")

                events_dict["leaderboard"]["position_"+str(i)] = pos_driver.text
        
        if rounds.text != "TESTING" and events_dict["race_status"] != 'Complete':
            hero_img_data = soup_class.get_elements_from_find_all(event=e,element="picture",class_name="hero-track").find('img')['data-src']
            events_dict['track_img'] = hero_img_data
        else:
            events_dict['track_img'] = None

        events_list.append(events_dict)
    return events_list
    


class F1SchedulesView(TemplateView):
    template_name = 'schedules.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedules'] = scrapData()
        print(context['schedules'])
        return context  