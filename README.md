# Description
StratTester is a user-friendly web application designed for stock enthusiasts and traders. It provides a seamless platform to stay updated on the latest stock news and test various intra-day trading strategies.
# Tech Stack
Django |
React |
Python |
Javascript |
PostgreSQL |
pandas 
# ERD
![ERD Chart](README_images/ERD.png)

# RESTful Routing Chart
![RESTful Routing Chart](README_images/RESTfulchart.png)

# Wireframes
![Home Page](Wireframes/home.png)
![Create Test](Wireframes/createtest.png)
![Test Result](Wireframes/testresult.png)
![Past Tests](Wireframes/pasttests.png)
# User Stories
- AAU I want to be able to view stock related news
- AAU I want to be able to select a stock, trading strategy and date then see what the result (profit/loss) would have been
- AAU I want to view my past tests

# Goals
## MVP
- Display Stock News on home page
- Create a new test
- View data/results of that test
- View past tests

## Stretch Goals
- Test over multiple days
- Choose number of shares to trade with
- Display a chart of the stock tested on the day tested
- Let user define their own Stop Loss and Price Target
- Filter news by ticker
- Filter and Sort users past tests
- Aggregate data of users past tests
- Convert JavaScript -> TypeScript

## Daily Sprints
1. Research/Education on unfamiliar tech
2. Navbar, Stub-up each page, setup User Auth
3. Make navbar conditional on user, setup the APIs, get API data to render
4. Work on create_test form functionality & results page
5. Work on 'My Tests' page
6. Select stretch goal(s) to work on
7. Work on CSS