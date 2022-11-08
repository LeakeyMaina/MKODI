[![Continous Integration](https://github.com/LeakeyMaina/MKODI/actions/workflows/CI.yml/badge.svg)](https://github.com/LeakeyMaina/MKODI/actions/workflows/CI.yml)
# MKODI

MKODI is a cloud based rental property management system that enables Landlords to manage their rental properties, receive digital rental payments from their tenants and comply with the Kenya Revenue Authority Monthly Rental Income Tax remitance requirements.

The system is composed of the following modules

1. Rental Property management module
This module is used to register and manage new landlords and their respective properties and tenants . It enables a landlord to maintain tenancy records for their properties
    Landlord Information
    Properties Records
    Tenant Records

2. Rent collection management Module
This module integrates with  MPESA API'S <https://developer.safaricom.co.ke/> to enable landlord's to receive mpesa rental payments from their tenants. It maintains a tenant's rental payment records and automates overdue payment reminders as well as receipts for payments received.
    Rental Payments Records

3. Rental Income Tax management module
This module maintains a landlord's financial and accounting records for their properties and  enables a landlord to comply with the Kenya Revenue Authority Monthly Rental Income Tax filing requirements <https://www.kra.go.ke/individual/filing-paying/types-of-taxes/residential-rental-income>
    Rental Tax Records
    Rental Tax calculator
    Rental Tax Transmitter

4. Tenancy Ratings module
The system maintains and queries a tenant's rental payments and tenancy records . Based on these records, the system is able to issue tenancy ratings and recommendations. This enables landlords to vet potential tenants via their tenancy credit score.
