from flask import Flask, session, app, render_template, request, Markup
import sys, io, re
import os, base64
from io import StringIO
from datetime import datetime
import time

app = Flask(__name__)

# get root path for account in cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# survey page
@app.route("/", methods=['POST', 'GET'])
def survey_page():
    message = ''
    #first_name = ''
    #last_name = ''
    #email = ''
    #gender = ''
    question1 = ''
    question2 = ''
    question3 = ''
    question4 = ''
    question5 = ''
    question6 = ''
    question7 = ''
    question8 = ''
    question9 = ''
    question10 = ''
    question11 = ''
    question12 = ''
    question13 = ''
    question14 = ''
    question15 = ''
    question16 = ''
    question17 = ''
    question18 = ''
    question19 = ''
    question20 = ''
    question21 = ''
    question22 = ''
    question23 = ''
    question24 = ''
    question25 = ''
    question26 = ''
    question27 = ''
    question28 = ''
    question29 = ''
    question30 = ''
    question31 = ''
    question32 = ''
    question33 = ''
    question34 = ''
    question35 = ''
    question36 = ''
    question37 = ''
    question38 = ''
    question39 = ''
    question40 = ''
    question41 = ''
    question42 = ''
    # are_you_happy = 'Choose one...'
    # tell_us_more = ''
    # Family_checked = ''
    # Friends_checked = ''
    # Colleagues_checked = ''
    # this is a list so create a string to append into csv file
    recommend_this_to_string = ''


    if request.method == 'POST':

        # # check that we have all the required fields to append to file
        # are_you_happy = request.form['are_you_happy']
        # recommend_this_to = request.form.getlist('recommend_this_to')
        # tell_us_more = request.form['tell_us_more']
        # # remove special characters from input for security
        # tell_us_more = re.sub(r"[^a-zA-Z0-9]","",tell_us_more)

        # first_name = request.form['first_name']
        # last_name = request.form['last_name']
        # email = request.form['email']
        # date_of_birth = request.form['date_of_birth']

        questionList = []
        for n in range(1, 43):
            if f"question{n}" in request.form:
                questionList.append(request.form[f"question{n}"])
            else:
                questionList.append('')

        # # optional fields
        # if date_of_birth=='':
        #     date_of_birth = 'NA'
        # #if 'gender' in request.form:
        # #    gender = request.form['gender']
        # #else:
        # #    gender = 'NA'


        # # check that essential fields have been filled
        message = ''
        missing_required_answers_list = []
        # if are_you_happy == 'Choose one...':
        #     missing_required_answers_list.append('Are you happy?')
        # if len(recommend_this_to) == 0:
        #     missing_required_answers_list.append('Who would you recommend this survey to?')
        # else:

        #     for val in recommend_this_to:
        #         recommend_this_to_string += val + ' '
        #         if val == 'Family':
        #             Family_checked = 'checked'
        #         if val == 'Friends':
        #             Friends_checked = 'checked'
        #         if val == 'Colleagues':
        #             Colleagues_checked = 'checked'

        if len(questionList) < 42:
            missing_required_answers_list.append('You skipped a question')
        # #Lol
        # if question1 == '':
        #      missing_required_answers_list.append('Question 1')
        # if question2 == '':
        #      missing_required_answers_list.append('Question 2')
        # if question3 == '':
        #      missing_required_answers_list.append('Question 3')
        # if question4 == '':
        #      missing_required_answers_list.append('Question 4')
        # if question5 == '':
        #      missing_required_answers_list.append('Question 5')
        # if question6 == '':
        #      missing_required_answers_list.append('Question 6')
        # if question7 == '':
        #      missing_required_answers_list.append('Question 7')
        # if question8 == '':
        #      missing_required_answers_list.append('Question 8')
        # if question9 == '':
        #      missing_required_answers_list.append('Question 9')
        # if question10 == '':
        #      missing_required_answers_list.append('Question 10')
        # if question11 == '':
        #      missing_required_answers_list.append('Question 11')
        # if question12 == '':
        #      missing_required_answers_list.append('Question 12')
        # if question13 == '':
        #      missing_required_answers_list.append('Question 13')
        # if question14 == '':
        #      missing_required_answers_list.append('Question 14')
        # if question15 == '':
        #      missing_required_answers_list.append('Question 15')
        # if question16 == '':
        #      missing_required_answers_list.append('Question 16')
        # if question17 == '':
        #      missing_required_answers_list.append('Question 17')
        # if question18 == '':
        #      missing_required_answers_list.append('Question 18')
        # if question19 == '':
        #      missing_required_answers_list.append('Question 19')
        # if question20 == '':
        #      missing_required_answers_list.append('Question 20')
        # if question21 == '':
        #      missing_required_answers_list.append('Question 21')
        # if question22 == '':
        #      missing_required_answers_list.append('Question 22')
        # if question23 == '':
        #      missing_required_answers_list.append('Question 23')
        # if question24 == '':
        #      missing_required_answers_list.append('Question 24')
        # if question25 == '':
        #      missing_required_answers_list.append('Question 25')
        # if question26 == '':
        #      missing_required_answers_list.append('Question 26')
        # if question27 == '':
        #      missing_required_answers_list.append('Question 27')
        # if question28 == '':
        #      missing_required_answers_list.append('Question 28')
        # if question29 == '':
        #      missing_required_answers_list.append('Question 29')
        # if question30 == '':
        #      missing_required_answers_list.append('Question 30')
        # if question31 == '':
        #      missing_required_answers_list.append('Question 31')
        # if question32 == '':
        #      missing_required_answers_list.append('Question 32')
        # if question33 == '':
        #      missing_required_answers_list.append('Question 33')
        # if question34 == '':
        #      missing_required_answers_list.append('Question 34')
        # if question35 == '':
        #      missing_required_answers_list.append('Question 35')
        # if question36 == '':
        #      missing_required_answers_list.append('Question 36')
        # if question37 == '':
        #      missing_required_answers_list.append('Question 37')
        # if question38 == '':
        #      missing_required_answers_list.append('Question 38')
        # if question39 == '':
        #      missing_required_answers_list.append('Question 39')
        # if question40 == '':
        #      missing_required_answers_list.append('Question 40')
        # if question41 == '':
        #      missing_required_answers_list.append('Question 41')
        # if question42 == '':
        #      missing_required_answers_list.append('Question 42')

        # if tell_us_more == '':
        #     missing_required_answers_list.append('Tells us more')
        # if first_name == '':
        #     missing_required_answers_list.append('First name')
        # if last_name == '':
        #     missing_required_answers_list.append('Last name')
        # if email == '':
        #     missing_required_answers_list.append('Email')


        if len(missing_required_answers_list) > 0:
            # return back a string with missing fields
            message = '<div class="w3-row-padding w3-padding-16 w3-center"><H3>You missed the following question(s):</H3><font style="color:red;">'
            for ms in missing_required_answers_list:
                message += '<BR>' + str(ms)
            message += '</font></div>'
        else:
            # append survey answers to file

            # create a unique timestamp for this entry
            entry_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


            # save to file and send thank you note
            with open(BASE_DIR + '/surveys/survey_samp_1.csv','a+') as myfile: # use a+ to append and create file if it doesn't exist
                questionString = ",".join(questionList)
                #print(questionString)
                myfile.write(
                    # str(entry_time) + ',' +
                    # str(last_name) + ',' +
                    # str(email) + ',' +
                    # str(date_of_birth) + ',' +
                    # str(are_you_happy) + ',' +
                    # str(recommend_this_to_string) + ',' +
                    # str(tell_us_more) + ',' +
                    str(questionString)
                    # str(question1) + ',' +
                    # str(question2) + ',' +
                    # str(question3) + ',' +
                    # str(question4) + ',' +
                    # str(question5) + ',' +
                    # str(question6) + ',' +
                    # str(question7) + ',' +
                    # str(question8) + ',' +
                    # str(question9) + ',' +
                    # str(question10) + ',' +
                    # str(question11) + ',' +
                    # str(question12) + ',' +
                    # str(question13) + ',' +
                    # str(question14) + ',' +
                    # str(question15) + ',' +
                    # str(question16) + ',' +
                    # str(question17) + ',' +
                    # str(question18) + ',' +
                    # str(question19) + ',' +
                    # str(question20) + ',' +
                    # str(question21) + ',' +
                    # str(question22) + ',' +
                    # str(question23) + ',' +
                    # str(question24) + ',' +
                    # str(question25) + ',' +
                    # str(question26) + ',' +
                    # str(question27) + ',' +
                    # str(question28) + ',' +
                    # str(question29) + ',' +
                    # str(question30) + ',' +
                    # str(question31) + ',' +
                    # str(question32) + ',' +
                    # str(question33) + ',' +
                    # str(question34) + ',' +
                    # str(question35) + ',' +
                    # str(question36) + ',' +
                    # str(question37) + ',' +
                    # str(question38) + ',' +
                    # str(question39) + ',' +
                    # str(question40) + ',' +
                    # str(question41) + ',' +
                    # str(question42) + ','
                    + '\n')

            # return thank-you message
            message = '<div class="w3-row-padding w3-padding-16 w3-center"><H2><font style="color:blue;">Thank you for taking the time to complete this survey</font></H2></div>'


    return render_template('survey.html',
        message = Markup(message),
        #first_name = first_name,
        #last_name = last_name,
        #email = email,
        #gender = gender,
        question1 = question1,
        question2 = question2,
        question3 = question3,
        question4 = question4,
        question5 = question5,
        question6 = question6,
        question7 = question7,
        question8 = question8,
        question9 = question9,
        question10 = question10,
        question11 = question11,
        question12 = question12,
        question13 = question13,
        question14 = question14,
        question15 = question15,
        question16 = question16,
        question17 = question17,
        question18 = question18,
        question19 = question19,
        question20 = question20,
        question21 = question21,
        question22 = question22,
        question23 = question23,
        question24 = question24,
        question25 = question25,
        question26 = question26,
        question27 = question27,
        question28 = question28,
        question29 = question29,
        question30 = question30,
        question31 = question31,
        question32 = question32,
        question33 = question33,
        question34 = question34,
        question35 = question35,
        question36 = question36,
        question37 = question37,
        question38 = question38,
        question39 = question39,
        question40 = question40,
        question41 = question41,
        question42 = question42)
        # tell_us_more = tell_us_more,
        # Family_checked = Family_checked,
        # Friends_checked = Friends_checked,
        # Colleagues_checked = Colleagues_checked,
        # are_you_happy = are_you_happy)