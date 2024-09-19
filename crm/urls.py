
from django.urls import path
from . import views

urlpatterns = [
    
# ----- customers relationship management website 

    path('', views.index, name=''),



# ----- CRM HOME PAGE -----

    # path('home', views.about, name='home'),

# ------ About Page ------

    path('about', views.about, name='about'),

# ------ Customers Book Appointment Page ------

    path('book-an-appointment', views.book, name='book'),

# ------ Customers Book Appointment Success Page ------

    path('successful', views.successful, name='successful'),

# ------ Customers Report Page ------

    path('report', views.customer_report, name='customer-report'),



# ----- CRM ADMIN USER PAGE -----



# ----- Login -----

    path('login', views.login, name="login"),


# -----Logout -----

    path('logout', views.logout, name="logout"),


# ----- Register -----

    path('register', views.register, name="register"),


# ----- CRM DASHBOARD PAGE -----

    path('dashboard', views.dashboard, name='dashboard'),



# ----- CRUDE CUSTOMER -----


# ----- Create Customer -----

    path('create-customer', views.create_customer, name="create-customer"),

# ----- Update Customer -----

    path('update-customer/<int:pk>', views.update_customer, name="update-customer"),

# ----- Delete Customer -----

    path('delete-customer/<int:pk>', views.delete_customer, name="delete-customer"),

# ----- View Customer -----

    path('view-customer/<str:slug_url>', views.view_customer, name="view-customer"),

# ----- View All Customers -----

    path('customers', views.customers, name="customers"),



# ----- CRUD CUSTOMERS RECORD -----


    
# ----- Create Customers Information -----

    # path('create-customer-information', views.create_customer_information, name="create-customer-information"),

    path('create-customer-information/<str:slug_url>', views.create_customer_information, name="create-customer-information"),

# ----- Customers Information Exists -----
    
    path('error', views.error_page, name="error"),
    
# ----- View Specific Customers Information -----

    path('view-customer-information/<str:slug_url>', views.view_customer_information, name="view-customer-information"),

# ----- Update Specific Customers Information -----

    path('update-customer-information/<str:slug_url>', views.update_customer_information, name="update-customer-information"),

# ----- Delete Specific Customers Information -----

    path('delete-customer-information/<str:slug_url>', views.delete_customer_information, name="delete-customer-information"),


    
# ----- SKIN CARE INQUIRY RECORD -----



# ----- Create Customers Skin Care Inquiry Record -----

    path('create-skin-care-inquiry-record', views.create_skin_care_inquiry_record, name="create-skin-care-inquiry-record"),

# ----- Skin Care Inquiry Records -----

    path('skin-care-inquiry-records/<str:slug_url>', views.skin_care_inquiry_record, name="skin-care-inquiry-records"),

# ----- View Specific Customers Skin Care Inquiry Record -----

    path('view-skin-care-inquiry-record/<int:pk>', views.view_skin_care_inquiry_record, name="view-skin-care-inquiry-record"),

# ----- Delete Specific Customers Skin Care Inquiry Record -----

    path('delete-skin-care-inquiry-record/<int:pk>', views.delete_skin_care_inquiry_record, name="delete-skin-care-inquiry-record"),



# ----- SKIN CARE REPORT -----



# ----- Create Customers Skin Care Report -----

    path('create-skin-care-report', views.create_skin_care_report, name="create-skin-care-report"),

# ----- Skin Care Reports -----

    path('skin-care-report/<str:slug_url>', views.skin_care_report, name="skin-care-report"),

# ----- View Specific Customers Skin Care Report -----
    
    path('view-skin-care-report/<int:pk>', views.view_skin_care_report, name="view-skin-care-report"),

# ----- Delete Specific Customers Skin Care Report -----

    path('delete-skin-care-report/<int:pk>', views.delete_skin_care_report, name="delete-skin-care-report"),



# ----- TREATEMENTS -----



# add, view and delete the list of treatment services offffered by the firm

# ----- Add Treatment -----

    path('add-treatment', views.add_treatment, name="add-treatment"),

# ----- Treatment Lists -----

    path('treatment-list', views.treatment_list, name="treatment-list"),

# ----- Delete Treatment -----

    path('delete-treatment/<int:pk>', views.delete_treatment, name="delete-treatment"),



# ----- CUSTOMERS TREATMENT -----

    

# ----- Add Customers Treatment -----

    path('add-customers-treatment', views.add_customers_treatment, name="add-customers-treatment"),

# ----- View Lists Of Customers Treatment -----

    path('treatments', views.treatments, name="treatments"),

# ----- Specific Customers Treatment -----

    path('treatment-details/<int:pk>', views.treatment_details, name="treatment-details"),

    # path('treatment-details', views.treatment_details, name="treatment-details"),

# ----- View Specific Customers Treatment -----

    path('view-treatment/<str:slug_url>', views.view_customers_treatment, name="view-treatment"),

# ----- Delete Customers Treatment -----

    path('delete-customers-treatment/<int:pk>', views.delete_customers_treatment, name="delete-customers-treatment"),



# ----- LOYALTY -----

    path('loyalty', views.loyalty, name="loyalty"),



# ----- APPOINTMNETS -----

    # path('appointments', views.appointments, name="appointments"),



# ----- SCHEDULE APPOINTMNET -----



# ----- Schedule an Appointment -----

    path('schedule-appointment', views.schedule_appointment, name="schedule-appointment"),

# ----- Scheduled Appointments -----

    path('scheduled-appointments', views.scheduled_appointment_list, name="scheduled-appointments"),

# ----- View Scheduled Appointments -----
    
    path('view-scheduled-appointment/<int:pk>', views.view_scheduled_appointment, name="view-scheduled-appointment"),

# ----- View CUstomers Scheduled Appointments -----

    path('view-customers-schedule/<str:slug_url>', views.view_customers_schedule, name="view-customers-schedule"),

# ----- Delete Scheduled Appointments -----

    path('delete-customers-schedule/<int:pk>', views.delete_customers_schedule, name="delete-customers-schedule"),



# ----- BOOK APPOINTMNET -----



# ----- Book an Appointment -----

    path('book-appointment', views.book_appointment, name="book-appointment"),

# ----- View Booked Appointment -----

    path('view-booked-appointment/<int:pk>', views.view_booked_appointment, name="view-booked-appointment"),

# ----- Booked Appointments Lists

    path('booked-appointments', views.booked_appointment_list, name="booked-appointments"),

# ----- Delete Booked Appointement -----

    path('delete-booked-appointment/<int:pk>', views.delete_booked_appointment, name="delete-booked-appointment"),



# ----- REPORT -----



# report are complaints or notes made by the customer

# ----- Add Report -----

    path('add-report', views.add_report, name="add-report"),

# ----- View Report -----

    path('view-report/<int:pk>', views.view_report, name="view-report"),

# ----- Reports Lists -----

    path('reports', views.report_list, name="reports"),

# ----- Delete Report -----

    path('delete-report/<int:pk>', views.delete_report, name="delete-report"),



# ----- SEARCH -----

    path('search', views.search, name='search'),


# ----- SETTINGS -----

    path('settings', views.settings, name='settings'),


# ----- RESET -----

    path('reset', views.reset, name='reset'),




]

