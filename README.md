# PROFITLENS - FINANCIAL CALCULATOR

## Video demo: https://youtu.be/EdNdSyOwqHg

## Description:
Financial calculator is my final project for CS50P. The purpose of this project is to help small businesses to calculate more easily their revenues, total costs, profits, margins and break-evens by entering four variables: price per unit, number of units sold, cost per unit and fixed costs. I decided to create this kind of project because I am studying Economics in Bulgaria and I wanted to create something that combines Economics with Python. Also another thing that I had in mind was that I want to create a project that I can improve in the future when I acquire new knowledge and maybe some day it will be some kind of a useful app.

## Features
- Revenue calculation
- Total cost calculation
- Profit calculation
- Profit margin calculation
- Break-even point calculation
- Exporting financial results to a CSV file
- Input validation

## Financial Calculations
- Revenue is the total amount of money a business earns from selling goods or providing services before subtracting any expenses and it is equal to: price per unit multiplied by units sold.
- Total cost is the full sum of all fixed and variable expenses incurred to produce a product, run a service, or complete a purchase and it is equal to: fixed cost plus variable cost, where variable cost is equal to units sold multiplied be cost per unit.
- Profit is the financial gain that remains when a company's total revenue exceeds its total expenses, costs, and taxes over a specific period. It is equal to revenue minus total cost.
- Margin is a financial metric that shows the percentage of revenue a company keeps as profit after subtracting expenses. Margin = (Profit / Revenue) × 100
- Break-even point is the exact moment or level of activity where total revenue equals total costs, resulting in zero profit and zero loss.

## Files
- `project.py`: Contains the main program and calculation functions.
- `test_project.py`: Contains tests for the program.
- `requirements.txt`: Lists the external dependencies.
- `results.csv`: Stores the calculated financial results.

## Design Choices
I separated each formula in a different function because this way the code is cleaner and more readable and I can use these functions again in other projects in the future. In the break-even function I used math.ceil() because the result has to be rounded up to the next integer greater than or equal to the result. I am using a try-except blocks to handle invalid numerical input because firstly I want to check if the user is entering valid inputs before starting the calculations and I used ValueError messages in functions to inform the user what is wrong with the entered values. Also I decided to store the calculated results in a CSV file because this way it is easier for the user to read the results.

## How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in the project directory.
3. Install the required dependencies.
4. Run the program: python project.py
5. Enter the requested financial information.
6. Open `results.csv` to view the saved results.

## Testing
Run the tests using: pytest -v
The tests check whether the calculation functions
return the expected results and handle invalid inputs.
