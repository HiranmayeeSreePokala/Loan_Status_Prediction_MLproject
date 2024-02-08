## Objective

The idea behind this ML project is to build an ML model and web application that the bank can use to classify if a user can be granted a loan or not.

## About Data

The dataset contains information about Loan Applicants. There are 12 independent columns and 1 dependent column. This dataset includes attributes like Loan ID, gender, if the loan applicant is married or not, the level of education, applicant’s income etc.

To load the training data in your colab, use the below command:

```bash
loan_dataset = pd.read_csv('Load Data.csv')
```

## Data Description
- **Loan_ID:** A unique ID assigned to every loan applicant
- **Gender:** Gender of the applicant (Male, Female)
- **Married:** The marital status of the applicant (Yes, No)
- **Dependents:** No. of people dependent on the applicant (0, 1, 2, 3+)
- **Education:** Education level of the applicant (Graduated, Not Graduated)
- **Self_Employed:** If the applicant is self-employed or not (Yes, No)
- **ApplicantIncome:** The amount of income the applicant earns
- **CoapplicantIncome:** The amount of income the co-applicant earns
- **LoanAmount:** The amount of loan the applicant has requested for
- **Loan_Amount_Term:** The no. of days over which the loan will be paid
- **Credit_History:** A record of a borrower's responsible repayment of debts (1 - has all debts paid, 0 - not paid)
- **Property_Area:** The type of location where the applicant’s property lies (Rural, Semiurban, Urban)

## Test Dataset

Load the test data "Loan_data.csv". You can load the data using the below command.

```bash
loan_dataset = pd.read_csv('train_u6lujuX_CVtuZ9i (1).csv')
```