"""Models file for the tracker app."""

from django.db import models


class Client(models.Model):
    """Client model representing the company or individual paying out for a task."""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    """Project model for storing details about projects."""

    name = models.CharField(max_length=100)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE
    )  # TODO: is this actuall preferable? Perhaps projects could outlive clients?
    description = models.TextField()
    start_date = models.DateField()
    estimated_hours = models.DecimalField(max_digits=10, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    billable = models.BooleanField(default=False)
    billable_rate = models.DecimalField(max_digits=10, decimal_places=2)
    flat_fee = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class TimeEntry(models.Model):
    """Span of time spent working on a project, or some other task"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=140)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
