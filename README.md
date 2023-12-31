# Survey Engine

The survey engine is a Python-based CLI application. It allows users to create new surveys or participate in existing surveys. Users can also check, where their responses fall compared to other survey participants. The users interact with different options on the web through a command line interface. 

[Here is the live version of my project](https://survey-engine-5260bd538ecd.herokuapp.com/)

![survey-engine multiscreen screenshot](https://github.com/fokhrun/survey-engine/blob/main/images/survey_engine_screenshot.png)

## How To

Using the application is quite straightforward. 

A user chooses either to create a survey or participate in a survey. 

In the case of creating a survey, a user gets a prompt to provide the survey name, number of questions, and a set of question and response options. 

In the case of participating in a survey, a user can choose between two options: just participate and participate with a statistical analysis report. In the case of just participating, a user is given a prompt to choose from a predefined set of surveys. Then the user responds to the selected survey. In the case of participating with statistics, the additional process analyzes the response of the user compared to other responses and shares that result.

The following screenshot provides the top-level menu for the app. 

![Top level menu](https://github.com/fokhrun/survey-engine/blob/main/images/top_menu.png)

A user can create and participate an unlimited number of surveys.

## Features

### Current Features

There are currently four features types of feature to survey-engine:

1. Creating a survey
2. Participating in a survey
3. Analysing survey responses

#### Creating a survey

When a user chooses to create a survey, the user is asked to provide the title of the survey. Then the user is asked to provide the expected number of questions in the survey. Based on that number, a repeated prompt is provided where the user first provides a question text and, then a set of response options as a set of strings separated by commas. This means all survey questions are multiple-choice question type. See the following screenshot as a demonstration of this feature. 

![Creating a survey](https://github.com/fokhrun/survey-engine/blob/main/images/create_survey.png)

#### Participating in a survey 

When a user selects plain participate in a survey, the user is provided a list of surveys. The user needs to choose the desired survey by providing the index number. Note that, each survey name is followed by another number, which basically shows how many questions are there in the survey. When a user has chosen a survey, the questions, and the response are iterated, where the user provides a response for each question. Note that, only one option can be selected and no question can be skipped. Check the following screenshot that demonstrates the feature.

![Participate in a survey](https://github.com/fokhrun/survey-engine/blob/main/images/participate_survey.png)

#### Analysing survey responses

This feature is similar to the previous feature, but it adds a process to analyze the response provided by the user against the response provided by other users. The analysis is based on [interquantile range](https://en.wikipedia.org/wiki/Interquartile_range), which is a typical choice to analyze survey results. Check the following screenshot that demonstrates the feature.

![Analysing survey response](https://github.com/fokhrun/survey-engine/blob/main/images/analyse_response.png)

### Future Features

1. Currently the app takes surveys anonymously. The user profile should be saved and connected to surveys created and responded to by users.
2. Geotagging the survey responses so that current responses can be mapped with the responses within the geolocation of the survey responders.
3. Leaderboard for top survey creators and responders.
4. Standalone survey analytics without participating.
5. More elegant CLI
6. Optional questions and multiple types of response options

## Data Model

Currently, there are two main data models: 
1. Survey 
2. Survey Response 

### Survey

The survey class holds 
- the title of the survey
- a set of questions 
- corresponding response options. 

The class has the following methods: 
- to save survey questions as a file 
- print survey questions in a terminal console
- load survey questions from a file

### Survey Response

The survey response class binds survey objects with chosen options from response options for each question in the survey. 
The class also has the following methods:
- save responses to a file
- load responses from a file
- calculate interquartile statistics from survey responses and map the current responses on the interquartile range

## Testing

I have tested the code and the deployed app manually. 
- Tested locally and in the Heroku deployment through different paths of the code. It works correctly to the best of my knowledge. Improper input, wrong type, or out-of-range, is provided to validate the code and the app while doing the testing. The following screenshot shows how incorrect input is handled:

![Handling incorrect input](https://github.com/fokhrun/survey-engine/blob/main/images/input_handling.png)


- Evaluated PEP8 linter. All reported linting issues have been fixed.

To test the code locally, run the following code, from the source code directory:
`python run.py`

## Bugs

### Solved bugs

- Constants were written in multiple places. It led to inconsistent paths for files. All constants moved to a single module. 
- The response to surveys were saved inside a loop, which led to the rewriting of the same response multiple times. 
The saving of response has moved out of the loop.
- Filenames were taken from the survey title, which may include white spaces. This lead to issues when the files need to be read later on. The issue was fixed by replacing the white space with an underscore. The reverse is applied when the filename is used to display the survey title. 
- Wrong input could be provided which led to CLI crashing while choosing a survey. It is fixed to handle input within the correct range. 

### Remaining bugs

- There is no graceful way to handle a survey with the same title. If the title matches an existing title, the app will replace the existing survey with the newly created one. Ideally, a survey with the same title should either get a prompt to use a different title or some additional random text should be added to the survey title to make it unique.

- Survey files should have .survey and .response extensions. No mechanism exists to enforce that.

### Validator Testing

- PEP8: All errors identified by [Code Institute's PEP8 web app](https://pep8ci.herokuapp.com) has been fixed.

## Deployment

### Preparation
- Your code must be placed in the run.py file
- Your dependencies must be placed in the requirements.txt file. Currently, this project has no requirements.
- Use caution while editing other files. It may cause the code to be deployed incorrectly.
- To deploy in Heroku, make sure to subscribe to the "Eco Dynos Plan".
- Connect your GitHub account to Heroku.

### Steps
- Create a new app in [Heroku](https://dashboard.heroku.com/apps)
- Fill the form with the app name of your choice ("pizza-engine" in this case) and "Europe" as the region.
- Select Settings. 
- Add two build packs from the Settings tab in the following sequence: 1) heroku/python, 2)heroku/nodejs.
- Add a Config Var called PORT. Set this to 8000.
- Select Deploy.
- Choose "GitHub" as your deployment method. Other options are fine too.
- Search the repo name in GitHub that you want to connect. Once the repo is found, connect the repo.
- Choose the branch you want to deploy. For the deployed app, we kept the "main" branch, which is the default choice.
- Click "Enable Automatic Deploys" which allows the app to be redeployed for every commit.
- Click "Deploy Branch" for the first manual push.
- Select "Open app" to verify that the app got deployed.

### Constraints
The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line. This design is left untouched from the [base repository](https://github.com/Code-Institute-Org/python-essentials-template).


## Credits
The Heroku deployment is facilitated using [base repository](https://github.com/Code-Institute-Org/python-essentials-template) provided by Code Institute.
