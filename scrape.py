from datetime import datetime
import datetime as dt
import pytz
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://us.prairielearn.com/pl/login")
time.sleep(1)
driver.find_element("link text", "University of Illinois at Urbana-Champaign (UIUC)").click()
time.sleep(1)
driver.find_element("name", "loginfmt").send_keys("dodich3@illinois.edu")
time.sleep(1)
driver.find_element("id", "idSIButton9").click()
time.sleep(1)
driver.find_element("name", "passwd").send_keys("xBnb4mti#4mti")
driver.find_element("id", "idSIButton9").click()
time.sleep(1)
html = driver.page_source
parsed_html = BeautifulSoup(html, 'html.parser')
tds = parsed_html.find_all('td')
links = []
for td in tds:
    link = td.find('a')
    #print(link)
    if link:
        text = link.text.strip()
        href = link.get('href')
        links.append((href, text.split(":")))

# Print the list of hrefs
#print(links)
courses = {}
def course_deadlines(parsed_html, course_name):
    assignments = []
    html = driver.page_source
    parsed_html = BeautifulSoup(html, 'html.parser')
    assessments = parsed_html.find_all('tr')
    for assessment in assessments:
        # extract link and name
        link_tag = assessment.find('a', href=True)
        if link_tag is None:
            continue  # Skip assessments without links
        link = link_tag['href']
        name = assessment.find('a').text.strip()
        all_links = assessment.find_all('a')
        name = all_links[0].text.strip() + ' - ' + all_links[1].text.strip()

        # extract deadline table
        try:
            deadline_table = assessment.find('a', {'data-content': True})['data-content']
            deadline_table = BeautifulSoup(deadline_table, 'html.parser')
        except:
            continue

        # find most relevant deadline date
        deadline_rows = deadline_table.find_all('tr')[1:]
        most_relevant = None
        for row in deadline_rows:
            percentage = row.find_all('td')[0].text.strip()
            deadline_str = row.find_all('td')[2].text.strip()
            if deadline_str == '—' or deadline_str == '' or deadline_str is None:
                continue
            if 'CST' in deadline_str:
                deadline_str = deadline_str.replace(' (CST)', '')
            elif 'CDT' in deadline_str:
                deadline_str = deadline_str.replace(' (CDT)', '')
            deadline = datetime.strptime(deadline_str[:-3], '%Y-%m-%d %H:%M:%S')
            #
            if deadline >= datetime.now():
                # check if this deadline is the most relevant so far
                if most_relevant is None or deadline < most_relevant:
                    most_relevant = deadline
                    most_relevant_percentage = percentage

        if most_relevant == "None" or most_relevant is None:
            most_relevant_percentage = "0%"
        assignment = {
            'course_name': course_name,
            'assignment_name': name,
            'link': "https://us.prairielearn.com" + link,
            'most_relevant_date': most_relevant,
            'most_relevant_percentage': most_relevant_percentage
        }
        assignments.append(assignment)
        #print(f'{course_name}: {name}: {link} (deadline: {most_relevant}), percentage: {most_relevant_percentage}')
    courses[course_name] = assignments



for link in links:
    url_to_get = "https://us.prairielearn.com" + link[0]
    driver.get(url_to_get)
    content = driver.find_elements(By.CLASS_NAME, "content")
    course_deadlines(parsed_html, link[1][0])

sorted_assignments = {}
parsed_courses = []
for key in courses:
    filtered_courses = [c for c in courses[key] if c['most_relevant_date'] is not None]
    # Sort the filtered list of dictionaries by the 'most_relevant_date' key
    sorted_assignments[key] = sorted(filtered_courses, key=lambda x: x['most_relevant_date'])
    # parsed_courses += sorted_assignments[0:4]
parsed_courses = []
for key in courses:
    for assignment in sorted_assignments[key][0:4]:
        if not (assignment['most_relevant_percentage'] is None and assignment['most_relevant_percentage'] == '0%') and assignment['most_relevant_date'].date() <= (dt.date.today() + dt.timedelta(days=10)):
            parsed_courses.append(assignment)


def get_objects_by_date(data):
    today = dt.datetime.today().date()
    objects_with_same_date = []
    objects_with_closest_dates = []

    for course_name, assignments in data.items():
        for assignment in assignments:
            if assignment['most_relevant_date'] is not None and assignment['most_relevant_percentage'] != "0%":
                assignment_date = assignment['most_relevant_date'].date()
                diff = abs(today - assignment_date)

                if diff == dt.timedelta(days=0):
                    objects_with_same_date.append(assignment)
                else:
                    objects_with_closest_dates.append((assignment, diff))

    objects_with_closest_dates.sort(key=lambda x: x[1])
    closest_objects = [x[0] for x in objects_with_closest_dates][:4]
    print(closest_objects, objects_with_closest_dates)
    print("HELLLLLLo",objects_with_same_date)
    # print(objects_with_closest_dates)
    num_due_today = len(objects_with_same_date)
    if (num_due_today < 5):

        objects_with_same_date += closest_objects
        return objects_with_same_date
    else:
        print("it is returning closest_objecets")
        return closest_objects

# parsed_courses = get_objects_by_date(courses)

def make_script(course_name, index):
    script_text = """
        var table = document.querySelector('.table.table-sm.table-hover.table-striped tbody');
        var rows = table.querySelectorAll('tr');
    """

    assignment_list = ""

    for assignment in parsed_courses:
        if assignment['course_name'] == course_name:
            # Create a clickable link with the assignment name as the link text and the link as the URL
            link = "<a href={}>{}</a>".format(assignment['link'], assignment['assignment_name'])

            # Create a list of variables to include in the bullet point
            formatted_date = assignment['most_relevant_date'].strftime("%B %d, %Y")
            variables = [link, formatted_date]

            # Create a bullet point with the variables included
            bullet_point = "<li>{}</li>".format(" - ".join(str(v) for v in variables))

            # Add the bullet point to the assignment list
            assignment_list += bullet_point

    script_text += """
        var row = table.insertRow({});
        var cell = row.insertCell(0);
        var ul = document.createElement('ul');
        ul.innerHTML = '{}';
        cell.appendChild(ul);
        row.classList.add('new-row');
    """.format(index, assignment_list)

    script_text2 = """
        var style = document.createElement('style');
        style.innerHTML = '.new-row td { padding-left: 20px; font-size: 75%; }';
        document.head.appendChild(style);
    """

    driver.execute_script(script_text)
    driver.execute_script(script_text2)


driver.get("https://us.prairielearn.com")
html = driver.page_source
parsed_html = BeautifulSoup(html, 'html.parser')
tds = parsed_html.find_all('td')
index = -1
for td in tds:
    link = td.find('a')
    if link:
        index = index + 2
        text = link.text.strip()
        text = (text.split(":"))[0]
        make_script(text, index)

time.sleep(60)