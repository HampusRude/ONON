# -*- coding: utf-8 -*-
import requests
import json
import os
from app import db
from app.q_dict import question_id_dict
from app.models import Responses

### Retrives json data from survey monkey
def get_survey_data(url):
    access_token = os.environ['SM_ACCESS_TOKEN']

    s = requests.Session()
    s.headers.update({
        "Authorization": "Bearer %s" % access_token,
        "Content-Type": "application/json"
    })

    # ID = 153577588
    res = s.get(url)
    if res != None:
        return res
    else:
        return {'Error':'Could not reach Survey Monkey'}

### Retrieves responses and answers from json data and returns a list of dictionarys
def get_all_responses(data, string_dict):
    list_of_responses = []
    responses = (data.get("data")) # Returns a list. Each item in this list will become an entry into the db table responses
    for response in responses:
        response_dictionary = {}        # The key is the question and the value is the respondents answer

        response_dictionary["response_id"] = str(response.get("id")) # Makes the UID smaller to store in db
        response_dictionary["timestamp"] = response.get("date_modified")     # Retrieves timestamp for the response

        pages = response.get("pages")   # A list with the answers for the different pages in the form
        for page in pages:
            questions = page.get("questions")   # A list with a set of questions and corresponding answer
            if questions:
                for answers in questions:
                    answer = answers.get("answers")
                    q_id = answers.get("id")            # retrieves the questions survey monkey id
                    q = question_id_dict[q_id]        # retrives the db question id
                    ans = []
                    for data in answer:
                        if data.get("text"):
                            ans.append(data.get("text"))
                        elif data.get("choice_id"):
                            ans.append(string_dict[data.get("choice_id")])
                    ans_string = ", ".join(str(x) for x in ans)
                    response_dictionary[q] = ans_string       # saves according to db schema
        list_of_responses.append(response_dictionary)
    return list_of_responses

### Converts json data of strings to a manageable dictionary
def get_string_dict(data):
    description = {}    # Initilise an empty dictionary, will be filled up by get_all_strings
    weight = {}
    get_all_strings(data, "id", description, weight)    # Recursive function that finds all strings with key = 'id'
    for key in description:
        w = weight[key]
        if w != 0:
            description[key] = w
    return description

### Recursive funtion that finds json objects based on key and returns string related to key
### Used for finding the text string related to an answer ID
def get_all_strings(myjson, key, description, weight):
    if type(myjson) is dict:
        for jsonkey in myjson:
            if type(myjson[jsonkey]) in (list, dict):
                get_all_strings(myjson[jsonkey], key, description, weight)
            elif jsonkey == key:
                if 'headings' in myjson:
                    a_list = myjson['headings']
                    a_dict = a_list[0]
                    description[myjson[jsonkey]] = str(a_dict['heading'])
                    weight[myjson[jsonkey]] = 0
                if 'text' in myjson:
                    description[myjson[jsonkey]] = myjson['text']
                    if 'weight' in myjson:
                        weight[myjson[jsonkey]] = myjson['weight']
                    else:
                        weight[myjson[jsonkey]] = 0
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                get_all_strings(item, key, description, weight)


def update_db(rl):
    # Get the list of response_ids in database
    db_res = Responses.query.all()
    db_res_id = []
    for res in db_res:
        db_res_id.append(res.response_id)

    new_res_id = []
    # For each response in the list responses, create an object and add to database
    for res in rl:
        obj = Responses(**res)
        new_res_id.append(obj.response_id)
        if obj.response_id not in db_res_id:
            db.session.add(obj)
            print("Added response " + str(obj.response_id) + " to database")
        else:
            print("Response " + str(obj.response_id) + " already in database")

    # For each response in the db, if it is not on survey monkey, remove from db
    # Primarily neeeded in the initial testing phase when many dummy-responses were made
    for id in db_res_id:
        if id not in new_res_id:
            obj = Responses.query.filter_by(response_id=id).first()
            print("Removed response " + str(obj.response_id) + " from database")
            db.session.delete(obj)
    db.session.commit()

### Combines the response list and details dictionary to something readable to verify data
def print_data(rl, dd):
    for response in rl:         # returns a dictionary for each unique response
        print(" --- New response --- ")
        for line in response:   # For each key (question id) in the dictionary of responses
            if line != 'response_id' and line != 'timestamp':
                answer = response[line]
                question = dd[line]
                print(str(question) + " | " + str(answer))
            else:
                print("--" + str(line))

### The whole lifecycle of updating the database with new responses
def retrieve_data():
    # Retrieve the responses from SurveyMonkey
    responses_url = "https://api.surveymonkey.com/v3/surveys/160620263/responses/bulk"
    responses = get_survey_data(responses_url)    # Retrieve data from surveymonkey
    responses_parsed = json.loads(responses.text)               # Parse json response from server

    # Retrieve details on the structure of the form on SurveyMonkey
    details_url = "https://api.surveymonkey.com/v3/surveys/160620263/details"
    details = get_survey_data(details_url)    # Retrieve data from surveymonkey
    details_parsed = json.loads(details.text)               # Parse json response from server
    details_dict = get_string_dict(details_parsed)          # A dict with ids and corresponding strings

#    q_id_dict = question_id_dict    # question_id_dict is a global variable, this line is for clarification

    response_list = get_all_responses(responses_parsed, details_dict)    # A list of dicts with individual responses

    update_db(response_list)

def get_response_data (response, string_dict):
    response_dictionary = {}  # The key is the question and the value is the respondents answer
    response_dictionary["response_id"] = str(response.get("id"))  # Makes the UID smaller to store in db
    response_dictionary["timestamp"] = response.get("date_modified")  # Retrieves timestamp for the response
    pages = response.get("pages")  # A list with the answers for the different pages in the form
    for page in pages:
        questions = page.get("questions")  # A list with a set of questions and corresponding answer
        if questions:
            for answers in questions:
                answer = answers.get("answers")
                q_id = answers.get("id")  # retrieves the questions survey monkey id
                q = question_id_dict[q_id]  # retrives the db question id
                ans = []
                for data in answer:
                    if data.get("text"):
                        ans.append(data.get("text")[:498])  # Limit char-len of text to 500 chars
                    elif data.get("choice_id"):
                        ans.append(string_dict[data.get("choice_id")])
                ans_string = ", ".join(str(x) for x in ans)
                response_dictionary[q] = ans_string  # saves according to db schema
    return response_dictionary

def add_response(response_id):
    # Retrieve the responses from SurveyMonkey
    response_url = "https://api.surveymonkey.com/v3/surveys/160620263/responses/%s/details" % str(response_id)
    details_url = "https://api.surveymonkey.com/v3/surveys/160620263/details"
    try:
        response = get_survey_data(response_url)  # Retrieve data from surveymonkey
        details = get_survey_data(details_url)  # Retrieve data from surveymonkey
    except:
        print("Connection error")
    response_parsed = json.loads(response.text)               # Parse json response from server

    # Details on the structure of the form on SurveyMonkey
    details_parsed = json.loads(details.text)               # Parse json response from server
    details_dict = get_string_dict(details_parsed)          # A dict with ids and corresponding strings
    try:
        res = get_response_data(response_parsed, details_dict)

        # Get the list of response_ids in database
        db_res = Responses.query.all()
        db_res_id = []  # List of ids retrieved from site.db
        for res in db_res:
            db_res_id.append(res.response_id)
        obj = Responses(**res)
        if obj.response_id not in db_res_id:
            db.session.add(obj)
            db.session.commit()
            print("Added response %s to database" % (str(obj.response_id)))
        else:
            print("Response %s already in database" % (str(obj.response_id)))
    except:
        print("An exception occured")


def main():
    retrieve_data()
    res_list = [10310404153, 10312578983]
    for i in res_list:
        add_response(i)

if __name__ == "__main__":
    main()


