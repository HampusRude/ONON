# -*- coding: utf-8 -*-
import requests
import json
import pickle
import psycopg2
from app.q_dict import question_id_dict
from app import db
from app.models import User, Responses


### Saves a python object to external file
def save_obj(obj, file_name):
    with open("obj/" + file_name + ".pkl", "wb") as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

###  Loads a python object from an external file
def load_obj(file_name):
    with open("obj/" + file_name + ".pkl", "rb") as file:
        return pickle.load(file)

### Connects to database
def connect(db_name, user, password):
    print("LOG_TAG: connect()")
    conn = psycopg2.connect("dbname=%s user=%s password=%s" % (db_name, user, password))
    db = conn.cursor()
    return db, conn

### Disconnects from database
def disconnect(db, conn):
    print("LOG_TAG: disconnect()")
    db.close()
    conn.close()

### Retrives json data from survey monkey
def get_survey_data(url, access_token):

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
        print("LOG_TAG: Retrieving new response")
        response_dictionary = {}        # The key is the question and the value is the respondents answer

        response_dictionary["response_id"] = int(response.get("id")) % 2**31 # Makes the UID smaller to store in db
        response_dictionary["timestamp"] = response.get("date_modified")     # Retrieves timestamp for the response

        pages = response.get("pages")   # A list with the answers for the different pages in the form
        for page in pages:
            questions = page.get("questions")   # A list with a set of questions and corresponding answer
            if questions:
                for answers in questions:
                    answer = answers.get("answers")
                    q_id = answers.get("id")       # retrieves the questions survey monkey id
                    q = question_id_dict[q_id]
                    ans = []
                    for data in answer:
                        if data.get("text"):
                            ans.append(data.get("text"))
                        elif data.get("choice_id"):
                            ans.append(string_dict[data.get("choice_id")])
                    response_dictionary[q] = ans
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

### writes response data to database table responses
def write_db_responses(db, responses, q_id_dict):
    # Clear table before writing new entries
    db.mogrify("DELETE FROM responses")
    print("LOG_TAG: Deleted all entries to db")

    for response in responses:
        print("LOG_TAG: Writing new customer response set...")
        response_id = str(response["response_id"])

        # TODO: Improve the timestamp format
        timestamp = "'" + str(response["timestamp"]) + "'"
        initial_command = "INSERT INTO responses(response_id, timestamp) VALUES (%s, %s)" % (response_id, timestamp)
        print(db.mogrify(initial_command))

        for q_id in response:
            if q_id in q_id_dict:
                column = q_id_dict[q_id]
                data = '"' + str(response[q_id]) + '"'

            # TODO: Istället för att updatera n ggr, formatera en sträng och updatera en gång

            if column != "response_id" and column != "timestamp":
                command = "UPDATE responses SET %s = %s WHERE response_id = %s;" % (column, data, response_id)
                print(command)
                #db.mogrify(command)
    return True

def write_responses(responses, q_id_dict):
    # Clear table before writing new entries

    # For each response in the list responses, create an object and add to database
    for response in responses:
        #    db.session.add(object)
        #    db.session.commit()
        pass

### Combines the response list and details dictionary to something readable to verify data
def print_data(rl, sd):
    for response in rl:         # returns a dictionary for each unique response
        i = -7
        for line in response:   # For each key (question id) in the dictionary of responses
            print(" --- New response --- ")
            i += 1
            if line != 'response_id' and line != 'timestamp':
                answer = response[line]
                question = sd[line]
                print("q" + str(i) + ": " + str(line) + " # " + str(question))

def main():
    access_token = "CFuvukyd7PyT8d8NDMhT9ofBcsgJ8FOmKZl2Wqmc0E5jzmCCDMjhvSzuKlHUYmz0PCXep2Ze1e1wGKLH4ljAL7TDLc1zfv1V.FQUPoJUBKWuQHqHsi6Y9XCCHsljjkJq"

    # Retrieve the responses from SurveyMonkey
    responses_url = "https://api.surveymonkey.com/v3/surveys/157901927/responses/bulk"
    responses = get_survey_data(responses_url, access_token)    # Retrieve data from surveymonkey
    responses_parsed = json.loads(responses.text)               # Parse json response from server

    # Retrieve details on the structure of the form on SurveyMonkey
    details_url = "https://api.surveymonkey.com/v3/surveys/157901927/details"
    details = get_survey_data(details_url, access_token)    # Retrieve data from surveymonkey
    details_parsed = json.loads(details.text)               # Parse json response from server
    details_dict = get_string_dict(details_parsed)          # A dict with ids and corresponding strings

    q_id_dict = question_id_dict    # question_id_dict is a global variable, this line is for clarification

    response_list = get_all_responses(responses_parsed, details_dict)    # A list of dicts with individual responses

    #print_data(response_list, details_dict)

    res_1 = response_list[0]
    res_id = res_1["response_id"]
    obj = Responses(**res_1)
    db.session.add(obj)
    db.session.commit()
"""
    for response in response_list:
        obj = Responses(**response)
        db.session.add(obj)
        for k in response:
            print(str(k) + " " + str(response[k]))
    db.session.commit()

    try:
        num_rows_deleted = db.session.query(Responses).delete()
        db.session.commit()
        print(num_rows_deleted)
    except:
        db.session.rollback()
"""

"""
    # Connect and publish the retrieved data to the database
    db, conn = connect("survey", "postgres", "johand6c")

    write_responses(db, response_list, q_id_dict)
    print("Responses written to database")

#    print_data(res, strings)

    disconnect(db, conn)
"""

if __name__ == "__main__":
    main()

# TODO: Implement SQLAlchemy
# ToDo  Format timestamp and send to database
