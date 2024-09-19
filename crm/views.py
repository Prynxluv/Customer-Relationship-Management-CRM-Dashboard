from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . forms import CreateUserForm, LoginForm, CreateInformationForm, UpdateInformationForm, CreateCustomerForm, UpdateCustomerForm, SkinCareInquiryForm, SkinCareReportForm, TreatmentListForm, TreatmentForm, ScheduleAppointmentForm, BookAppointmentForm, ReportForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from . models import Information, Customer, SkinCareInquiry, SkinCareReport, Treatment, TreatmentList, ScheduleAppointment, BookAppointment, Report
from django.contrib.auth.decorators import login_required



# Create your views here.



# ----- WEBSITE PAGE -----

def index(request):
    return render(request, 'crm/website/index.html')



# ----- HOME PAGE -----

def about(request):
    return render(request, 'crm/website/about.html')



# ----- CUSTOMERS APPOINTMENT BOOKING PAGE -----

def book(request):
    
    form = BookAppointmentForm()
    book_appointment = BookAppointment.objects.all()

    if request.method == "POST":

        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect ('successful')

    cards = Report.objects.all().order_by('-creation_date')
    context = {'form' : form, 'book_appointment' : book_appointment, 'cards' : cards}

    return render(request, 'crm/website/book.html', context)



# ----- SUCCESSFULLY BOOKED PAGE -----

def successful(request):

    successful = 'Your Action Was Successssful'
    context = {'successful' : successful}

    return render(request, 'crm/website/successful.html', context)



# ----- SUCCESSFULLY BOOKED PAGE -----

def customer_report(request):
    
    form = ReportForm()

    if request.method == "POST":

        form = ReportForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('successful')

    context = {'form' : form}

    return render(request, 'crm/website/report.html', context)



# ----- DASHBOARD PAGE -----

@login_required(login_url='login')
def dashboard(request):

    label = []
    data = []

    label_2 = []
    data_2 = []
    count_2 = []

    loyal_count = []

    queryset = Information.objects.order_by('-age')
    # queryset = Information.objects.order_by('-age')[:10]

# calculate 

    for record in queryset:
        label.append(record.customer.full_name)
        data.append(record.age)

    queryset_2 = Treatment.objects.all()

    for treatment in queryset_2:
        data_2.append(treatment.customer.full_name)
        count_2 = dict((i, data_2.count(i)) for i in data_2)

        if data in data_2 == 1:
            label_2.append(data_2)[:2]


# calculate the total number of customers that hve had treatment
   
    loyalty = dict((i, data_2.count(i)) for i in data_2)

    for i in loyalty:
        loyal_count.append(i)

    
    customers = Customer.objects.all().order_by('-creation_date')
    # customers = Customer.objects.all().order_by('-creation_date')[:1]
    total_customers = Customer.objects.all().count()
    total_treatments = Treatment.objects.all().count()
    cards = Report.objects.all().order_by('-creation_date')[:3]
    booked_appointment = BookAppointment.objects.all().count()
    report = Report.objects.all().count()


    context = {'customers' : customers,
               'total_customers' : total_customers,
               'total_treatments' : total_treatments,
               'label' : label,
               'data' : data, 
               'count_2' : count_2,
               'label_2' : label_2,
               'cards' : cards,
               'loyal_count' : loyal_count,
               'booked_appointment' : booked_appointment,
               'report' : report}
    
    return render(request, 'crm/dashboard/dashboard.html', context)




# ----- Customer Creation Page -----

@login_required(login_url='login')
def customers(request):


    data = []
    data_2 = []
    count = []
    label = []

    queryset = Treatment.objects.all()


    for treatment in queryset:
        data.append(treatment.customer.full_name)
        count = dict((i, data.count(i)) for i in data)
        
        if data in label == 1:
            label.append(data_2)


    customers = Customer.objects.all().order_by('-creation_date')
    total_customers = Customer.objects.all().count()
    cards = Report.objects.all().order_by('-creation_date')[:3]

    context = {'customers' : customers, 'count' : count, 'label' : label, 'total_customers' : total_customers, 'cards' : cards}

    return render(request, 'crm/customers/customers-list.html', context)


# ----- END -----




# ----- EROOR PAGE -----

@login_required(login_url='login')
def error_page(request):

    return render(request, 'crm/error_page.html')



# ----- CREATE USER, LOGIN AND LOGOUT -----


# ----- Registeration Page -----

def register(request):

    form = CreateUserForm()

    # if statement to check if a user exists, if one does then don't create a new user

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
    
    context =  {'form' : form}

    return render(request, 'crm/admin-user/register.html', context)



# ----- Login Page -----

def login(request):

    form = LoginForm()

    error_message = 'Admin User Does Not Exist or Credential Mismatched Pleace try again '

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")
        
        # else :

        #     return redirect ('error')


    context = {'form' : form, 'error_message' : error_message}

    return render (request, 'crm/admin-user/login.html', context)



# ----- User Logout Function -----

def logout(request):

    auth.logout(request)
    
    return redirect("login")

# ----- END -----



# ----- User Logout Function -----

# @login_required(login_url='login')
# def del_user(request):
#     user = request.User
#     user.delete()
#     redirect("login")


# ----- END -----




# ----- CURD CUSTOMER -----


# ----- Customer Creation Page -----

@login_required(login_url='login')
def create_customer(request):

    form = CreateCustomerForm()
    cards = Report.objects.all().order_by('-creation_date')[:3]

    if request.method == "POST":

        form = CreateCustomerForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")

    context = {'form' : form, 'cards' : cards}

    return render(request, 'crm/customers/create-customer.html', context)



# ----- View Customer ------

@login_required(login_url='login')
def view_customer(request, slug_url):


    customer = Customer.objects.get(slug=slug_url)

    name = customer.full_name


    label = []
    data = []
    count = []

    queryset = Treatment.objects.filter(customer__full_name=name)
    queryset_2 = TreatmentList.objects.all()

    total_treatment = Treatment.objects.filter(customer__full_name=name).count()
    cards = Report.objects.all().order_by('-creation_date')[:3]

    for treatment in queryset:
        data.append(treatment.treatment_list.treatment_name)
        count = dict((i, data.count(i)) for i in data)

    for treatment in queryset_2:
        label.append(treatment.treatment_name)
        
    
    context = {'customer' : customer, 'label' : label, 'count' : count, 'data' : data, 'total_treatment' : total_treatment, 'cards' : cards }

    return render(request, 'crm/customers/view-customer.html', context)



# ----- Update Customer -----

@login_required(login_url='login')
def update_customer(request, pk):

    customer = Customer.objects.get(id=pk)
    form = UpdateCustomerForm(instance=customer)
    cards = Report.objects.all().order_by('-creation_date')[:3]

    if request.method == "POST":
        form = UpdateCustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect("view-customer", customer.slug)
    
    context = {'form' : form, 'customer' : customer, 'cards' : cards}

    return render(request, 'crm/customers/update-customer.html', context)



# ----  Delete Customer -----

@login_required(login_url='login')
def delete_customer(request, pk):

    customer = Customer.objects.get(id=pk)
    customer.delete()

    return redirect("customers")

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- CRUD CUSTOMERS RECORD -----



# ----- Create Customers Information -----

@login_required(login_url='login')
def create_customer_information(request, slug_url):

    id = []
    id_name = []

    form = CreateInformationForm
    value = Customer.objects.filter(slug = slug_url).values_list('id', flat=True)
    customers_name = Customer.objects.filter(slug = slug_url)
    cards = Report.objects.all().order_by('-creation_date')[:3]

    for id in value:
        id = id

    for name in customers_name:
        id_name = name.full_name

    try:

        if request.method == "POST":

            form = CreateInformationForm(request.POST)

            if form.is_valid():
                form.save()

                # return redirect('customers')
                return redirect("view-customer-information", slug_url)
            
    except:
        return redirect('error')
    
    # print(id_name)

    context = {'form' : form, 'id' : id, 'id_name' : id_name, 'cards' : cards}

    return render(request, 'crm/customers-information/create-customers-information.html', context)



# ----- View Customers Information -----

@login_required(login_url='login')
def view_customer_information(request, slug_url):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    data = Information.objects.filter(slug = slug_url ).all().order_by('-creation_date')

    if data.exists():
        information = Information.objects.filter(slug = slug_url ).all().order_by('-creation_date')

    else:
        # information = Information.objects.get(slug = slug_url)
        return redirect('create-customer-information', slug_url)

    context = {'information' : information, 'cards' : cards}

    return render(request, 'crm/customers-information/view-customers-information.html', context)



# ----- Update Customer Information  -----

@login_required(login_url='login')
def update_customer_information(request, slug_url):

    name = []

    information = Information.objects.get(slug = slug_url)
    form = UpdateInformationForm(instance=information)
    customers_name = Customer.objects.filter(slug = slug_url)
    cards = Report.objects.all().order_by('-creation_date')[:3]

    for i in customers_name:
        name = i.full_name

    if request.method == "POST":
        form = UpdateInformationForm(request.POST, instance=information)

        if form.is_valid():
            form.save()
            return redirect("view-customer-information", information.slug)

    
    context = {'form' : form, 'information' : information, 'name' : name, 'cards' : cards}
    return render(request, 'crm/customers-information/update-customers-information.html', context)


# --  Delete Customer Information --

@login_required(login_url='login')
def delete_customer_information(request, slug_url):

    information = Information.objects.get(slug=slug_url)
    information.delete()
    return redirect("view-customer", information.slug)

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----




# ----- SKIN CARE INQUIRY -----



# -----  Create Skin Care Inquire Record -----

@login_required(login_url='login')
def create_skin_care_inquiry_record(request):

    form = SkinCareInquiryForm()
    cards = Report.objects.all().order_by('-creation_date')[:3]
    skin_care_inquiry = SkinCareInquiry.objects.all()

    if request.method == "POST":
        
        form = SkinCareInquiryForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('customers')

    context = {'form' : form, 'skin_care_inquiry' : skin_care_inquiry, 'cards' : cards}

    return render (request, 'crm/skin-care/create-skin-care-inquiry-record.html', context)



# -----  View List Of Skin Care Inquire Record -----

@login_required(login_url='login')
def skin_care_inquiry_record(request, slug_url):

    # try:
    #     skin_care_inquirys = SkinCareInquiry.objects.filter(customer__slug=slug_url).values().order_by('-creation_date')

    # except:
    #     return redirect ("create-skin-care-inquiry-record")
    
    cards = Report.objects.all().order_by('-creation_date')[:3]
    record = SkinCareInquiry.objects.filter(customer__slug=slug_url)

    if record :
        skin_care_inquirys = SkinCareInquiry.objects.filter(customer__slug=slug_url).values().order_by('-creation_date')
    else:
        return redirect ("create-skin-care-inquiry-record")
    
    
    filterset = []

    name = SkinCareInquiry.objects.filter(customer__slug=slug_url)
    for i in name:
        filterset = i.customer.full_name

    context = {'skin_care_inquirys' : skin_care_inquirys, 'filterset' : filterset, 'cards' : cards}
    
    return render (request, 'crm/skin-care/skin-care-inquiry-record.html', context)



# -----  View Specific Customers Skin Care Inquire Record -----

@login_required(login_url='login')
def view_skin_care_inquiry_record(request, pk):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    record = SkinCareInquiry.objects.get(id=pk)
    context = {'record' : record, 'cards' : cards}
    
    return render (request, 'crm/skin-care/view-skin-care-inquiry-record.html', context)



# -----  Delete Specific Customers Skin Care Inquire Record -----

@login_required(login_url='login')
def delete_skin_care_inquiry_record(request, pk):

    skin_care_inquiry_record = SkinCareInquiry.objects.get(id=pk)
    skin_care_inquiry_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- SKIN CARE REPORT -----



# --  Create Skin Care Inquire Record --

@login_required(login_url='login')
def create_skin_care_report(request):

    form = SkinCareReportForm()
    cards = Report.objects.all().order_by('-creation_date')[:3]

    skin_care_report = SkinCareReport.objects.all()

    if request.method == "POST":
        
        form = SkinCareReportForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('customers')

    context = {'form' : form, 'skin_care_report' : skin_care_report, 'cards' : cards}   

    return render (request, 'crm/skin-care/create-skin-care-report.html', context)



# --  View List Of Skin Care Report --

@login_required(login_url='login')
def skin_care_report(request, slug_url):

    record = SkinCareReport.objects.filter(customer__slug=slug_url)

    cards = Report.objects.all().order_by('-creation_date') 
    if record :
        skin_care_reports = SkinCareReport.objects.filter(customer__slug=slug_url).values().order_by('-creation_date')
    else:
        return redirect ("create-skin-care-report")
    
    filterset = []

    name = SkinCareReport.objects.filter(customer__slug=slug_url)
    for i in name:
        filterset = i.customer.full_name

    context = {'skin_care_reports' : skin_care_reports, 'filterset' : filterset, 'cards' : cards}

    
    return render (request, 'crm/skin-care/skin-care-report.html', context)



# --  View Specific Customers Skin Care Report --

@login_required(login_url='login')
def view_skin_care_report(request, pk):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    report = SkinCareReport.objects.get(id=pk)
    context = {'report' : report, 'cards' : cards}
    
    return render (request, 'crm/skin-care/view-skin-care-report.html', context)



# --  Delete Specific Customers Skin Care Report --

@login_required(login_url='login')
def delete_skin_care_report(request, pk):

    skin_care_report = SkinCareReport.objects.get(id=pk)
    skin_care_report.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- TREATEMENT LIST -----



# ----- Add Treatment -----

@login_required(login_url='login')
def add_treatment(request):

    form = TreatmentListForm()
    add_treatment = TreatmentList.objects.all()

    try:

        if request.method == "POST":
            
            form = TreatmentListForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect ('treatment-list')
            
    except:
        return redirect('error')
    
    cards = Report.objects.all().order_by('-creation_date')[:3]

    context = {'form' : form, 'add_treatment' : add_treatment, 'cards' : cards}

    return render (request, 'crm/treatments/add-treatment.html', context)



# -----  Treatment List -----

@login_required(login_url='login')
def treatment_list(request):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    treatment_lists = TreatmentList.objects.all().order_by('-creation_date')
    context = {'treatment_lists' : treatment_lists, 'cards' : cards}

    return render (request, 'crm/treatments/treatment-list.html', context)



# -----  Delete Treatment -----

@login_required(login_url='login')
def delete_treatment(request, pk):

    treatment_lists = TreatmentList.objects.get(id=pk)
    treatment_lists.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # return redirect("skin-care-inquiry-record")

# ----- END -----



# ----- TREATEMANTS -----



# ----- Add Customers Treatments -----

@login_required(login_url='login')
def add_customers_treatment(request):

    form = TreatmentForm()
    treatment = Treatment.objects.all()

    if request.method == "POST":
        form = TreatmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('treatments')
    
    cards = Report.objects.all().order_by('-creation_date')[:3]

    context = {'form' : form, 'treatment' : treatment, 'cards' : cards}

    return render (request, 'crm/treatments/add-customers-treatment.html', context)



# -----  View Specific Customers Treatment -----

@login_required(login_url='login')
def view_customers_treatment(request, slug_url):
 
    cards = Report.objects.all().order_by('-creation_date')[:3]
    loyalty = Treatment.objects.filter(customer__slug=slug_url).count()

    if loyalty == 0:
        loyal = 'Prospect Customer'

    elif loyalty == 1:
        loyal = 'First-time Customer'
    
    elif loyalty <= 4 :
        loyal = 'Repeat Customer'
    
    elif loyalty <= 9 :
        loyal = 'Regular Customer'
    
    elif loyalty <= 15 :
        loyal = 'Loyal Customer'
    
    elif loyalty <= 21 :
        loyal = 'Client'
    
    elif loyalty > 21 :
        loyal = 'Advocate'

    try:
        name = Treatment.objects.filter(customer__slug=slug_url)

        for i in name:
            filterset = i.customer.full_name

        customers_treatments = Treatment.objects.filter(customer__slug=slug_url).all().order_by('-creation_date')
        context = {'filterset' : filterset, 'customers_treatments' : customers_treatments, 'loyal' : loyal, 'loyalty' : loyalty, 'cards' : cards}
    
    except:
        return redirect('add-customers-treatment')

    
    return render (request, 'crm/treatments/view-customers-treatment.html', context)



# -----  All Treatment -----

@login_required(login_url='login')
def treatments(request):

    label = []
    data = []
    count = []

    # Name of customer
    name = []

    # Number of treatments
    number = []

    keys = []
    values = []


    queryset = Treatment.objects.all()
    queryset_2 = TreatmentList.objects.all()

    for treatment in queryset:
        data.append(treatment.treatment_list.treatment_name)
        count = dict((i, data.count(i)) for i in data)

        name.append(treatment.customer.full_name)
        number = dict((i, name.count(i)) for i in name)

    for i in number:
        keys.append(i)
        values.append(number[i])

    for treatment_list in queryset_2:
        label.append(treatment_list.treatment_name)

    treatments = Treatment.objects.all().order_by('-creation_date')
    cards = Report.objects.all().order_by('-creation_date')[:3]

    context = {'treatments' : treatments,
               'label' : label,
               'data' : data,
               'count' : count,
               'keys' : keys,
               'values' : values,
               'cards' : cards             
               }
    
    return render (request, 'crm/treatments/treatments.html', context)



# ----- View Treatment Details -----

@login_required(login_url='login')
def treatment_details(request, pk):

    try:
        treatment_details = Treatment.objects.get(id=pk)
    except:
        return redirect('treatments')
    
    cards = Report.objects.all().order_by('-creation_date')[:3]
    context = {'treatment_details' : treatment_details, 'cards' : cards}

    return render(request, 'crm/treatments/treatment-details.html', context)



# -----  Delete Specific Customers Treatment -----

@login_required(login_url='login')
def delete_customers_treatment(request, pk):

    treatment = Treatment.objects.get(id=pk)
    treatment.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- APPOINTMENTS -----

# a page to navigate between sceduled and booked appointments

# -----  Appointment -----

# @login_required(login_url='login')
# def appointments(request):
    
#     return render (request, 'crm/appointments/appointments.html', context)



# ----- SCHEDULE APPOINTMENT -----



# -----  Schedule Appointment -----

@login_required(login_url='login')
def schedule_appointment(request):

    form = ScheduleAppointmentForm()
    secheduled_appointments = ScheduleAppointment.objects.all()

    if request.method == "POST":
        
        form = ScheduleAppointmentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('scheduled-appointments')

    cards = Report.objects.all().order_by('-creation_date')[:3]
    context = {'form' : form, 'secheduled_appointments' : secheduled_appointments, 'cards' : cards}

    return render (request, 'crm/appointments/schedule-appointment.html', context)



# -----  View Customer Schedule -----

@login_required(login_url='login')
def view_customers_schedule(request, slug_url):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    customers_schedules = ScheduleAppointment.objects.filter(customer__slug=slug_url).all().order_by('-creation_date')
    context = {'customers_schedules' : customers_schedules, 'cards' : cards}

    return render (request, 'crm/appointments/view-customers-schedule.html', context)



# -----  View Scheduled Appointment -----

@login_required(login_url='login')
def view_scheduled_appointment(request, pk):

    try:
        scheduled_appointments = ScheduleAppointment.objects.get(id=pk)
    except:
        return redirect('scheduled-appointments')

    cards = Report.objects.all().order_by('-creation_date')[:3]
    context = {'scheduled_appointments' : scheduled_appointments, 'cards' : cards}

    return render(request, 'crm/appointments/view-scheduled-appointments.html', context)



# -----  Scheduled Appointment List -----

@login_required(login_url='login')
def scheduled_appointment_list(request):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    scheduled_appointments = ScheduleAppointment.objects.all().order_by('-creation_date')
    context = {'scheduled_appointments' : scheduled_appointments, 'cards' : cards}

    return render (request, 'crm/appointments/scheduled-appointments-list.html', context)



# -----  Delete Scheduled Appointmnets -----

@login_required(login_url='login')
def delete_customers_schedule(request, pk):

    scheduled_appointments = ScheduleAppointment.objects.get(id=pk)
    scheduled_appointments.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- BOOK APPOINTMENT -----



# -----  Book Appointment -----

@login_required(login_url='login')
def book_appointment(request):

    form = BookAppointmentForm()
    book_appointment = BookAppointment.objects.all()

    if request.method == "POST":

        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect ('booked-appointments')

    cards = Report.objects.all().order_by('-creation_date')[:3]
    context = {'form' : form, 'book_appointment' : book_appointment, 'cards' : cards}
    
    return render (request, 'crm/appointments/book-appointment.html', context)



# -----  View Booked Appointment -----

@login_required(login_url='login')
def view_booked_appointment(request, pk):

    try:
        booked_appointments = BookAppointment.objects.get(id=pk)
    except:
        return redirect('booked-appointments')
    
    cards = Report.objects.all().order_by('-creation_date')[:3]
    context = {'booked_appointments' : booked_appointments, 'cards' : cards} 

    return render(request, 'crm/appointments/view-booked-appointments.html', context)



# -----  Booked Appointment List -----

@login_required(login_url='login')
def booked_appointment_list(request):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    booked_appointments = BookAppointment.objects.all().order_by('-creation_date')
    context = {'booked_appointments' : booked_appointments, 'cards' : cards}

    return render (request, 'crm/appointments/booked-appointments-list.html', context)



# -----  Delete Booked Appointmnets -----

@login_required(login_url='login')
def delete_booked_appointment(request, pk):

    schedules_appointments = BookAppointment.objects.get(id=pk)
    schedules_appointments.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# ----- END -----



# ----- REPORT -----



# -----  Add Report -----


@login_required(login_url='login')
def add_report(request):

    form = ReportForm()
    cards = Report.objects.all().order_by('-creation_date')[:3]
    add_report = Report.objects.all()

    if request.method == "POST":

        form = ReportForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('reports')

    context = {'form' : form, 'add_report' : add_report, 'cards' : cards}
    
    return render (request, 'crm/reports/add-report.html', context)



# -----  Report List -----

@login_required(login_url='login')
def report_list(request):

    cards = Report.objects.all().order_by('-creation_date')[:3]
    reports = Report.objects.all().order_by('-creation_date')
    context = {'reports' : reports, 'cards' : cards}
    
    return render (request, 'crm/reports/report-list.html', context)



# -----  Cards List -----

@login_required(login_url='login')
def card(request):

    # cards = Report.objects.all().order_by('-creation_date')[:1]
    cards = Report.objects.all().order_by('-creation_date')
    context = {'cards' : cards}
    
    return render (request, 'crm/cards.html', context)



# -----  View Report -----

@login_required(login_url='login')
def view_report(request, pk):

    cards = Report.objects.all().order_by('-creation_date')
    report = Report.objects.get(id=pk)
    context = {'report' : report, 'cards' : cards}

    return render (request, 'crm/reports/view-report.html', context)

    # return redirect("skin-care-inquiry-record")



# -----  Delete Report -----

@login_required(login_url='login')
def delete_report(request, pk):

    delete_report = Report.objects.get(id=pk)
    delete_report.delete()

    return redirect("reports")

# ----- END -----



# ----- LOYALTY SYSTEM -----

@login_required(login_url='login')
def loyalty (request):

    label = []
    data = []
    count = []

    querysets = Treatment.objects.all()

    for query in querysets:

        data.append(query.customer.full_name)
        loyal_customers = dict((i, data.count(i)) for i in data)


    keys = []
    values = []
    valueNo = []
    
    for i in loyal_customers:

        keys.append(i)
        values.append(loyal_customers[i])

    # id = Customer.objects.only('id')
   
    customers_name = Customer.objects.values('id')
    name = str(customers_name)
    loyalty_counts = Treatment.objects.filter().count()
    customers = Treatment.objects.all()

    # for customer in customers:
    #     name = customer.customer.full_name

    #     if name.count(name) <= 1:
    #         loyalty = [name, 'Serious']


    print(loyalty )
    cards = Report.objects.all().order_by('-creation_date')

    context = {'loyal_customers' : loyal_customers,
               'loyalty_counts' : loyalty_counts,
               'count' : count,
               'label' : label,
               'keys' : keys,
               'values' : values,
               'cards' : cards,
               'loyalty' : loyalty
               }
    
    return render (request, 'crm/loyalty/loyalty.html', context)

# ----- END -----



# ----- SEARCH -----

@login_required(login_url='login')
def search(request):

    customers_details = Customer.objects.all()

    if request.GET.get('search', None):
        search_query = request.GET['search']
        customers_names = customers_details.filter(full_name__icontains=search_query)
        customers_emails = customers_details.filter(email__icontains=search_query)
        customers_phones = customers_details.filter(phone__icontains=search_query)
        cards = Report.objects.all().order_by('-creation_date')

        context = {'search_query' : search_query,
                   'customers_names' : customers_names,
                   'count_names' : customers_names.count(),
                   'customers_phones' : customers_phones,
                   'count_phones' : customers_phones.count(),
                   'customers_emails' : customers_emails,
                   'count_emails' : customers_emails.count(),
                   'cards' : cards
                   }

    return render(request, 'crm/search/search.html', context)


# ----- END -----



# ----- SETTINGS -----

@login_required(login_url='login')
def settings(request):


    cards = Report.objects.all().order_by('-creation_date')

    context = { 'cards' : cards}

    return render(request, 'crm/settings.html', context)


# ----- END -----


# ----- RESET -----


@login_required(login_url='login')
def reset(request):

    # delete_all_customer = Customer.objects.all()
    # delete_all_information = Information.objects.all()
    # delete_all_skin_care_inquiry = SkinCareInquiry.objects.all()
    # delete_all_skin_care_report = SkinCareReport.objects.all()
    # delete_all_treatment_list = TreatmentList.objects.all()
    # delete_all_treatment = Treatment.objects.all()
    # delete_all_schedule_appointment = ScheduleAppointment.objects.all()
    # delete_all_booked_appointment = BookAppointment.objects.all()
    # delete_all_report = Report.objects.all()

    # delete_all_customer.delete()
    # delete_all_information.delete()
    # delete_all_skin_care_inquiry.delete()
    # delete_all_skin_care_report.delete()
    # delete_all_treatment_list.delete()
    # delete_all_treatment.delete()
    # delete_all_schedule_appointment.delete()
    # delete_all_booked_appointment.delete()
    # delete_all_report.delete()

    return redirect("dashboard")




