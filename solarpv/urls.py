from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name='home'),
    path('portal/', views.portal_view, name='portal'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),    
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),


    # Product
    path('product_list/', views.product_list_view, name='list-products'),
    path('add_product/', views.add_product_view, name='add-product'),
    path('product_detail/<product_id>', views.product_detail_view, name='product-detail'),
    path('search_products/', views.search_products_view, name ='search-products'),
    path('product_search_results/', views.product_search_results_view, name ='product-search-results'),

    # Certificate
    path('certificate_list/', views.certificate_list_view, name='list-certificates'),
    path('add_certificate/', views.add_certificate_view, name='add-certificate'),
    path('certificate_detail/<certificate_id>', views.certificate_detail_view, name='certificate-detail'),
    path('search_certificates/', views.search_certificates_view, name ='search-certificates'),
    path('certificate_search_results/', views.certificate_search_results_view, name ='certificate-search-results'),

    # Service
    path('service_list/', views.service_list_view, name='list-services'),
    path('add_service/', views.add_service_view, name='add-service'),
    path('service_detail/<service_id>', views.service_detail_view, name='service-detail'),
    path('search_services/', views.search_services_view, name ='search-services'),
    path('service_search_results/', views.service_search_results_view, name ='service-search-results'),

    # Location
    path('location_list/', views.location_list_view, name='list-locations'),
    path('add_location/', views.add_location_view, name='add-location'),
    path('location_detail/<location_id>', views.location_detail_view, name='location-detail'),
    path('client_location_detail/<location_id>', views.client_location_detail_view, name='client-location-detail'),
    path('search_locations/', views.search_locations_view, name ='search-locations'),
    path('location_search_results/', views.location_search_results_view, name ='location-search-results'),

    # Client
    path('client_list/', views.client_list_view, name='list-clients'),
    path('add_client/', views.add_client_view, name='add-client'),
    path('client_detail/<client_id>', views.client_detail_view, name='client-detail'),
    path('search_clients/', views.search_clients_view, name ='search-clients'),
    path('client_search_results/', views.client_search_results_view, name ='client-search-results'),

    # Performance Data
    path('performance_data_list/', views.performance_data_list_view, name='list-performance-datas'),
    path('add_performance_data/', views.add_performance_data_view, name='add-performance-data'),
    path('performance_data_detail/<performance_data_id>', views.performance_data_detail_view, name='performance-data-detail'),
    path('search_performance_datas/', views.search_performance_datas_view, name ='search-performance-datas'),
    path('performance_data_search_results/', views.performance_data_search_results_view, name ='performance-data-search-results'),

    # Test Sequence Data
    path('test_sequence_list/', views.test_sequence_list_view, name='list-test-sequences'),
    path('add_test_sequence/', views.add_test_sequence_view, name='add-test-sequence'),
    path('test_sequence_detail/<test_sequence_id>', views.test_sequence_detail_view, name='test-sequence-detail'),
    path('search_test_sequences/', views.search_test_sequences_view, name ='search-test-sequences'),
    path('test_sequence_search_results/', views.test_sequence_search_results_view, name ='test-sequence-search-results'),

    # Test Standard Data
    path('test_standard_list/', views.test_standard_list_view, name='list-test-standards'),
    path('add_test_standard/', views.add_test_standard_view, name='add-test-standard'),
    path('test_standard_detail/<test_standard_id>', views.test_standard_detail_view, name='test-standard-detail'),
    path('search_test_standards/', views.search_test_standards_view, name ='search-test-standards'),
    path('test_standard_search_results/', views.test_standard_search_results_view, name ='test-standard-search-results'),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)