from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from functions import createEvent
from functions import createCalendar
from functions import insertEvent
from functions import readDictionaryIntoList
from authenticator import authenticate
import datetime
import os

if os.stat("token.json").st_size == 0:
    print('File is empty')
    authenticate()
else:
    print('File is not empty')

# Set up the Google Calendar API service object
creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])
service = build('calendar', 'v3', credentials=creds)

# Define the event details
courses = {'CS 225': [{'course_name': 'CS 225', 'assignment_name': 'POTD0', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4963038/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD1', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4963040/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD2', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4963041/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD3', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5015836/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD4', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5015864/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD5', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5023872/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD6', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4982152/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD7', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4982149/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD8', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5037664/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD9', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5039733/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD10', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5040624/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD11', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5015867/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD12', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5096974/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD13', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5107437/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD14', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5124155/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD15', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5136462/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD16', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5136465/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD17', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5153458/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD18', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5170494/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD19', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5177004/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD20', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5187683/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD21', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5197215/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD22', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5218416/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD23', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5233828/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD24', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5239036/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD25', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5252086/', 'most_relevant_date': datetime.datetime(2023, 6, 30, 0, 0), 'most_relevant_percentage': 'None'}, {'course_name': 'CS 225', 'assignment_name': 'POTD26', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5256854/', 'most_relevant_date': datetime.datetime(2023, 2, 26, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 225', 'assignment_name': '', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment/2326419/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#1', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4971022/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#2', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4979275/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#3', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4984783/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#4', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4996657/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#5', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/4999220/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E7#6', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5001135/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': '', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment/2326422/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#1', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5156806/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#2', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5156920/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#3', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5172203/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#4', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5191792/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#5', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5197031/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#6', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5208843/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#7', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5214400/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'E9#8', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5214806/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'CS 225', 'assignment_name': 'MP1', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment_instance/5174410/', 'most_relevant_date': datetime.datetime(2023, 2, 27, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 225', 'assignment_name': 'Lab4', 'link': 'https://us.prairielearn.com/pl/course_instance/130633/assessment/2333282/', 'most_relevant_date': datetime.datetime(2023, 2, 26, 23, 59, 59), 'most_relevant_percentage': '100%'}], 'CS 361': [{'course_name': 'CS 361', 'assignment_name': 'HW1', 'link': 'https://us.prairielearn.com/pl/course_instance/130040/assessment/2333422/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 10, 59, 59), 'most_relevant_percentage': '100%'}], 'MATH 257': [{'course_name': 'MATH 257', 'assignment_name': 'CL0.3', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325347/', 'most_relevant_date': datetime.datetime(2023, 3, 28, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL1', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4968403/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL2', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4993263/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL2', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5044183/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL3', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5044279/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL4', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5143226/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CL5', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5244951/', 'most_relevant_date': datetime.datetime(2023, 2, 27, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL6', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325386/', 'most_relevant_date': datetime.datetime(2023, 3, 10, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL7', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325387/', 'most_relevant_date': datetime.datetime(2023, 3, 27, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL8', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325388/', 'most_relevant_date': datetime.datetime(2023, 4, 3, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL9', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325390/', 'most_relevant_date': datetime.datetime(2023, 4, 17, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL10', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325377/', 'most_relevant_date': datetime.datetime(2023, 4, 24, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CL11', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325378/', 'most_relevant_date': datetime.datetime(2023, 5, 1, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW1', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4979280/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW2', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4989988/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW3', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5049861/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW4', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5143232/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW5', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5203769/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW6', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325358/', 'most_relevant_date': datetime.datetime(2023, 3, 23, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW7', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325359/', 'most_relevant_date': datetime.datetime(2023, 3, 30, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW8', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325360/', 'most_relevant_date': datetime.datetime(2023, 4, 13, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW9', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325361/', 'most_relevant_date': datetime.datetime(2023, 4, 20, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW10', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325352/', 'most_relevant_date': datetime.datetime(2023, 4, 27, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'CHW11', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4968399/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '110%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW1', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/4985618/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW2', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5115479/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW3', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5057988/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW4', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5115478/', 'most_relevant_date': None, 'most_relevant_percentage': '0%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW5', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5183194/', 'most_relevant_date': datetime.datetime(2023, 2, 28, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'MATH 257', 'assignment_name': 'HW6', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment/2325373/', 'most_relevant_date': datetime.datetime(2023, 2, 28, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'MATH 257', 'assignment_name': 'E1', 'link': 'https://us.prairielearn.com/pl/course_instance/130110/assessment_instance/5218694/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': 'None'}], 'CS 233': [{'course_name': 'CS 233', 'assignment_name': 'READ0', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4993271/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE14', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325538/', 'most_relevant_date': datetime.datetime(2023, 3, 7, 8, 30), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE15', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325542/', 'most_relevant_date': datetime.datetime(2023, 3, 9, 8, 30), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE12', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5241604/', 'most_relevant_date': datetime.datetime(2023, 2, 28, 8, 30), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE13', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325536/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 8, 30), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB07.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325599/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 20, 0), 'most_relevant_percentage': '105%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB07.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325600/', 'most_relevant_date': datetime.datetime(2023, 3, 5, 20, 0), 'most_relevant_percentage': '103%'}, {'course_name': 'CS 233', 'assignment_name': 'GA11', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5228387/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC6', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325529/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 8, 30), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE11', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5197431/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB06.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5218708/', 'most_relevant_date': datetime.datetime(2023, 2, 26, 20, 0), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB06.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5239276/', 'most_relevant_date': datetime.datetime(2023, 2, 26, 20, 0), 'most_relevant_percentage': '103%'}, {'course_name': 'CS 233', 'assignment_name': '', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325618/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ3#1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5191824/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ3#2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5247485/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ3#3', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5247546/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ3#4', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5247594/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ3#5', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5247970/', 'most_relevant_date': datetime.datetime(2023, 3, 2, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'GA09', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5168831/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'GA10', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5191912/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC5', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5246140/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE09', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5129800/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE10', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5129806/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB05.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5169601/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB05.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5194769/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'GA07', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5107968/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'GA08', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5130996/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC4', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5152011/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE07', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5070602/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE08', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5107949/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB04.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5104926/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB04.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5116105/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': '', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325612/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5009849/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5097143/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#3', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5107507/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#4', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5107877/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#5', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5109110/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#6', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5109316/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#7', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5111516/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#8', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5111853/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#9', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112134/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#10', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112323/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#11', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112487/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#12', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112530/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#13', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112581/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#14', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5112837/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#15', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5113033/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ2#16', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5113848/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'GA05', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5050746/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'GA06', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5071194/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC3', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5070600/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE05', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5049011/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE06', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5049607/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB03.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5072231/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB03.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5075648/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PEER0', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5046739/', 'most_relevant_date': datetime.datetime(2023, 3, 20, 23, 59, 59), 'most_relevant_percentage': '100%'}, {'course_name': 'CS 233', 'assignment_name': 'GA03', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4999847/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'GA04', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5016584/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5023430/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE03', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4990811/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE04', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5009846/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB02.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4999807/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB02.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/5006385/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': '', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment/2325609/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4961237/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4969723/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#3', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4971133/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#4', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4991311/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#5', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4991397/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#6', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4991402/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#7', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4991452/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'PQ1#8', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4993277/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'GA01', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4957656/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'GA02', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4971624/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'XC1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4974608/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE00', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4953757/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE01', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4953759/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'PRE02', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4953760/', 'most_relevant_date': datetime.datetime(2023, 5, 3, 23, 59, 59), 'most_relevant_percentage': '80%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB01.1', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4957897/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB01.2', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4962227/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}, {'course_name': 'CS 233', 'assignment_name': 'LAB01.2.extra', 'link': 'https://us.prairielearn.com/pl/course_instance/130303/assessment_instance/4961057/', 'most_relevant_date': datetime.datetime(2023, 5, 31, 23, 59, 59), 'most_relevant_percentage': '0%'}]}

plCalendarId = createCalendar()

# Call the Calendar API to create the event
list = readDictionaryIntoList(courses)
eventsInCalendar = service.events().list(calendarId=plCalendarId).execute()["items"]
titlesList = {}
for event in eventsInCalendar:
    titlesList[event["summary"]] = 1

for item in list:
    insertEvent(item, plCalendarId, titlesList)
    # print(f'Event created: {item.get("htmlLink")}')