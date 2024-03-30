import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company


client = APIClient()


company_list_url = reverse('company-list')  
company_detail_url = reverse('company-detail', args=[1]) 
 

@pytest.fixture
def setup_companies():
    Company.objects.create(
        name='Company 1',
        description='Description 1',
        country='Country 1',
        settlement_city='City 1',
        street='Street 1',
        opening_hours='08:00-18:00'
    )
    Company.objects.create(
        name='Company 2',
        description='Description 2',
        country='Country 2',
        settlement_city='City 2',
        street='Street 2',
        opening_hours='09:00-17:00'
    )
    

@pytest.mark.django_db
def test_get_company_list(setup_companies):
    response = client.get(company_list_url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2 


@pytest.mark.django_db
def test_get_company_detail_invalid_id():
    invalid_url = reverse('company-detail', args=[100]) 
    response = client.get(invalid_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
