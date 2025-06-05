# API Testing Guide

This guide provides instructions for testing all endpoints of the Credit Management System API.

## Testing Tools
1. cURL (Command Line)
2. Browser (Chrome/Firefox)
3. API Testing Tools (Optional):
   - Postman
   - REST Client (Chrome Extension)

## Testing Sequence
Follow these steps in order to test the complete flow:

1. Fill Data
   - Use the fill-data endpoint to populate the database
   - See: 1_fill_data.txt

2. Register Customer
   - Create a new customer
   - Save the returned customer_id
   - See: 2_register.txt

3. Check Eligibility
   - Use the saved customer_id to check loan eligibility
   - See: 3_check_eligibility.txt

4. Create Loan
   - If eligible, create a loan
   - Save the returned loan_id
   - See: 4_create_loan.txt

5. View Loan Details
   - View single loan details using loan_id
   - See: 5_view_loan.txt

6. View All Customer Loans
   - View all loans for a customer using customer_id
   - See: 6_view_loans.txt

## Important Notes
- Always start with the fill-data endpoint
- Save the customer_id and loan_id from responses
- Replace example IDs (48648, 1) with actual IDs from your responses
- Check response status codes and messages
- Verify data consistency across endpoints

## Common Issues
1. Database not initialized
   - Solution: Run fill-data endpoint first
2. Invalid customer_id
   - Solution: Register a new customer first
3. Invalid loan_id
   - Solution: Create a loan first
4. Loan not approved
   - Check eligibility criteria
   - Verify customer's credit score and history

## Testing Tips
1. Test with different scenarios:
   - Valid and invalid inputs
   - Edge cases
   - Error conditions
2. Verify response formats
3. Check error messages
4. Test data consistency
5. Verify business logic

For detailed information about each endpoint, refer to the individual text files:
- 1_fill_data.txt
- 2_register.txt
- 3_check_eligibility.txt
- 4_create_loan.txt
- 5_view_loan.txt
- 6_view_loans.txt 