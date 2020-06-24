from django.db import models

# Create your models here.
char = models.CharField
numb = models.IntegerField


class Car(models.Model):
    grz = models.CharField(max_length=9, unique=True)
    model = models.CharField(max_length=10, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    fuel_type = models.CharField(max_length=5, null=False, blank=True)
    vin = models.CharField(max_length=20, blank=True, null=True)
    certificate = models.CharField(max_length=20, blank=True, null=True)
    lease_payment = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    last_to = models.IntegerField(blank=True, null=True)
    next_to = models.IntegerField(blank=True, null=True)
    to_type = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.grz


class TO_History(models.Model):
    car_to_history = models.ForeignKey(
        Car, on_delete=models.DO_NOTHING, to_field='grz')
    to_type = models.IntegerField()
    mileage_current = models.IntegerField()
    mileage_next = models.IntegerField()

    class Meta:
        unique_together = ('car_to_history', 'to_type')


class Expences(models.Model):
    insurance = models.IntegerField()
    amortiz = models.IntegerField()
    tyres = models.IntegerField()


class Report(models.Model):
    date_from = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, to_field='grz')
    date_to = models.DateField()
    driver = char(max_length=50)
    shifts = numb()
    totalCred = numb()
    totalDeb = numb()
    salary = numb()
    gas = numb()
    cash = numb()
    cash_flow = numb()

    # @classmethod
    # def new_report(cls, **kwargs):
    #     report = cls(**kwargs)


class Margin(models.Model):
    profit = models.ForeignKey(Report, on_delete=models.DO_NOTHING)
    safe = models.IntegerField()
    amount = models.IntegerField
