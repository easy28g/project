import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Company 
from .views import CustomPagination
from unittest.mock import patch


client = APIClient()


product_list_url = reverse('product-list') 
product_detail_url = reverse('product-detail', args=[1])  
product_category_url = reverse('product-category', args=[1]) 


@pytest.fixture
def setup_products():
    Product.objects.create(name='Product 1', description='Description 1', price=10.99)
    Product.objects.create(name='Product 2', description='Description 2', price=15.99)
    

@pytest.fixture
def setup_company():
    Company.objects.create(name='Test Company')
    

@pytest.mark.django_db
def test_get_product_list(setup_products):
    response = client.get(product_list_url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2  


@pytest.mark.django_db
def test_get_product_category(setup_company):
    response = client.get(product_category_url)
    assert response.status_code == status.HTTP_200_OK
    assert 'company' in response.data
    assert response.data['company'] == 'Test Company' 


@pytest.mark.django_db
def test_get_product_list_pagination(setup_products):
    with patch.object(CustomPagination, 'page_size', 1): 
        response = client.get(product_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1 
        

@pytest.mark.django_db
def test_get_product_detail_invalid_id():
    invalid_url = reverse('product-detail', args=[100]) 
    response = client.get(invalid_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND
