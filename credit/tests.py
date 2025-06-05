from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Loan
from datetime import date, timedelta
import datetime

class ViewLoanTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Create a test customer
        self.customer = Customer.objects.create(
            customer_id=12345,
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            age=30,
            monthly_salary=50000,
            approved_limit=100000
        )
        
        # Create test loans
        self.loan1 = Loan.objects.create(
            customer=self.customer,
            loan_id=1,
            loan_amount=50000,
            interest_rate=10,
            tenure=12,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=365),
            emis_paid_on_time=0,
            monthly_repayment=5000
        )
        
        self.loan2 = Loan.objects.create(
            customer=self.customer,
            loan_id=2,
            loan_amount=30000,
            interest_rate=8,
            tenure=6,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=180),
            emis_paid_on_time=0,
            monthly_repayment=3000
        )

    def test_view_single_loan_success(self):
        """Test successful retrieval of a single loan"""
        url = reverse('view-loan', kwargs={'loan_id': 1})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['loan_id'], 1)
        self.assertEqual(response.data['loan_amount'], 50000)
        self.assertEqual(response.data['interest_rate'], 10)
        self.assertEqual(response.data['tenure'], 12)

    def test_view_nonexistent_loan(self):
        """Test viewing a loan that doesn't exist"""
        url = reverse('view-loan', kwargs={'loan_id': 999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Loan not found.')

    def test_view_all_loans_success(self):
        """Test successful retrieval of all loans for a customer"""
        url = reverse('view-loans', kwargs={'customer_id': 12345})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return both loans
        
        # Verify the loans are ordered correctly (if any ordering is specified)
        loan_ids = [loan['loan_id'] for loan in response.data]
        self.assertIn(1, loan_ids)
        self.assertIn(2, loan_ids)

    def test_view_loans_nonexistent_customer(self):
        """Test viewing loans for a customer that doesn't exist"""
        url = reverse('view-loans', kwargs={'customer_id': 99999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Customer not found.')

    def test_view_loans_empty_customer(self):
        """Test viewing loans for a customer with no loans"""
        # Create a new customer with no loans
        new_customer = Customer.objects.create(
            customer_id=54321,
            first_name="Jane",
            last_name="Smith",
            phone_number="9876543210",
            age=25,
            monthly_salary=40000,
            approved_limit=80000
        )
        
        url = reverse('view-loans', kwargs={'customer_id': 54321})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # Should return empty list

    def test_view_loans_expired_filter(self):
        """Test that expired loans are not returned"""
        # Create an expired loan
        expired_loan = Loan.objects.create(
            customer=self.customer,
            loan_id=3,
            loan_amount=20000,
            interest_rate=12,
            tenure=6,
            start_date=date.today() - timedelta(days=365),
            end_date=date.today() - timedelta(days=180),
            emis_paid_on_time=6,
            monthly_repayment=2000
        )
        
        url = reverse('view-loans', kwargs={'customer_id': 12345})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        loan_ids = [loan['loan_id'] for loan in response.data]
        self.assertNotIn(3, loan_ids)  # Expired loan should not be in response
