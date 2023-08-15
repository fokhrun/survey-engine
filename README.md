# Pizza Survey

One liner what it is?

A couple of sentence how users can interact with the app

[Here is the live version of my project](https://survey-engine-5260bd538ecd.herokuapp.com/)

## How To

## Features

### Current Features

### Future Features

## Data Model

## Testing

## Bugs

- Path to save survey data is hardcoded
- Survey files should have .survey extensions. No mechanism exists to enforce that.

### Solved bugs

### Remaining bugs

### Validator Testing

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