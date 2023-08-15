# Survey Engine

Survey engine is a Python based CLI application. It allows users to create new surveys or participate in existing surveys. Users can also check, where their responses fall compared to other survey participants. The users interact with different options in the web through a command line interface. 

[Here is the live version of my project](https://survey-engine-5260bd538ecd.herokuapp.com/)

![survey-engine multiscreen screenshot](https://github.com/fokhrun/survey-engine/blob/main/images/survey_engine_screenshot.png)

## How To

Using the application is quite straightforward. 

A user choose either to create a survey or participate in a survey. 

In the case of creating survey, a user gets a prompt to provide survey name, number of questions, and a set of question and response options. 

In the case of participating in a survey, a user can choose between two options: just participate and participate with statistic analysis report. For the case of just participating, a user given a prompt to choose from a predefined set of surveys. Then the user respond to the selected survey. In the case of participating with statistics, the additional process analyzes the response of the user compared to other responses and shares that result.

A user can create and participate unlimited number of surveys.

## Features

### Current Features

There are currently three features types of feature to survey-engine:

2. Creating a survey
2. Participating in a survey
3. Analysing survey responses

#### Create Survey

####

####

### Future Features

1. Currently the app takes survey anonymously. User profile should be saved and connected to surveys created and responed by users.
2. Geotagging the survey responses so that current responses can be mapped with the responses within the geolocation of the survey responders.
3. Leaderboard for top survey creators and responders.
4. Standalone survey analytics without participating.

## Data Model

Currently there are two main data models: 
1. Survey 
2. Survey Response 

### Survey

The survey class holds 
- the title of the survey
- a set of questions 
- corresponding response options. 

The class has the following methods: 
- to save survey question as a file 
- print survey questions in a terminal console
- load survey questions from a file

### Survey Response

The survey response class binds survey objects with chosen option from response options for each question in the survey. 
The class also has the following methods:
- save responses to a file
- load responses from a file
- calculate interquintile statistics from survey responses and map the current responses on the interquintile range

## Testing

I have tested the code and the deployed app manually. 
- Tested locally and in the heroku deployment through different path of the code. It works correctly to the best of the knowledge. Improper input, wrong type or out of range, is provided to validate the code and the app while doing the testing. 
- Evaluated PEP8 linter. All reported linting issues have been fixed. 

## Bugs

- Path to save survey data is hardcoded
- Survey files should have .survey extensions. No mechanism exists to enforce that.

### Solved bugs

- Constants were written in multiple places. It led to inconsistent paths for files. All constants moved to a single module. 
- The response of surveys were saved inside a loop, which led to rewriting of the same response multiple times. 
The saving of response has moved out of the loop.
- Filenames were taken from the survey title, which may include white spaces. This lead to issues when the files needs to be read later on. The issue was fixed by replacing the white space with undescore. The reverse is applied when the filename is used to display survey title. 
- Wrong input could be provided that leads to code to break while choosing survey. It is fixed to handle input within the correct range. 

### Remaining bugs

There is no graceful way to handle survey with the same title. If title matches an existing title, the app will replace the existing survey with the newly created ones. Ideally, survey with the same title should either get a prompt to use a different title or some additional random text should be added the survey title to make it unique.

### Validator Testing

- PEP8: All errors identified by [Code Institute's PEP8 web app](https://pep8ci.herokuapp.com) has been fixed.

## Deployment

### Preparation
- Your code must be placed in the run.py file
- Your dependencies must be placed in the requirements.txt file. Currently this project has no requirements.
- Use caution while editing other files. It may cause the code to be deployed incorrectly.
- To deploy in heroku, make sure to subscribe to "Eco Dynos Plan".
- Connect your GitHub account to Heroku.

### Steps
- Create a new app in [Heroku](https://dashboard.heroku.com/apps)
- Fill the form with the app name of your chosing ("pizza-engine" in this case) and "Europe" as the region.
- Select Settings. 
- Add two buildpacks from the Settings tab in the following sequence: 1) heroku/python, 2)heroku/nodejs.
- Add a Config Var called PORT. Set this to 8000.
- Select Deploy.
- Choose "GitHub" as your deployment method. Other options are fine too.
- Search the repo name in GitHub that you want to connect. Once the repo is found, connect the repo.
- Choose the branch you want to deploy. For the deployed app, we kept the "main" branch, which is the default choice.
- Click "Enable Automatic Deploys" that allows the app to be redeployed for every commit.
- Click "Deploy Branch" for the first manual push.
- Select "Open app" to verify that the app got deployed.

### Constraints
The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line. This design is left untouched from the [base repository](https://github.com/Code-Institute-Org/python-essentials-template).


## Credits
The heroku deployment is facilitated using [base repository](https://github.com/Code-Institute-Org/python-essentials-template) provided by Code Institute.