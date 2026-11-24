from django.db import models
from django.contrib.auth.models import User


class EventEnquiry(models.Model):

    # Event Type Choices
    EVENT_TYPES = [
        ('Wedding', 'Wedding'),
        ('Birthday Party', 'Birthday Party'),
        ('Engagement', 'Engagement'),
        ('Reception', 'Reception'),
        ('Anniversary', 'Anniversary'),
        ('Baby Shower', 'Baby Shower'),
        ('Housewarming', 'Housewarming'),
        ('Other', 'Other Celebrations'),
    ]

    # Contact Method Choices
    CONTACT_METHODS = [
        ('Phone', 'Phone Call'),
        ('Email', 'Email'),
        ('WhatsApp', 'WhatsApp'),
    ]

    # Event Duration Choices
    EVENT_DURATIONS = [
        ('One Day', 'One Day'),
        ('Two Days', 'Two Days'),
        ('Three Days', 'Three Days'),
        ('More Than Three Days', 'More Than Three Days'),
    ]

    # Enquiry Status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Contacted', 'Contacted'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    # Customer Information
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='event_enquiries'
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    contact_method = models.CharField(
        max_length=20,
        choices=CONTACT_METHODS,
        default='Phone'
    )

    # Event Information
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    event_date = models.DateField()

    event_location = models.CharField(max_length=255)

    guest_count = models.CharField(max_length=50)

    # Budget Information
    budget = models.CharField(max_length=100)

    event_duration = models.CharField(
        max_length=50,
        choices=EVENT_DURATIONS,
        default='One Day'
    )

    # Selected Services
    services = models.JSONField(default=list, blank=True)

    # Additional Requirements
    requirements = models.TextField(blank=True, null=True)

    # Enquiry Management
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.event_type}"
