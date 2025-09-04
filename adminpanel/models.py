from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'users'


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    expense_type = models.CharField(max_length=20, choices=[('fixed', 'Fixed'), ('miscellaneous', 'Miscellaneous')])

    class Meta:
        managed = False
        db_table = 'expenses'


class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    budget_amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'budget'


class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100)
    date_received = models.DateField()

    class Meta:
        managed = False
        db_table = 'income'


class SavingsGoal(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings_goals')
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    progress_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_name = models.CharField(max_length=255)
    target_date = models.DateField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'savings_goals'


class AdminLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=100)
    action = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_logs'


class OtpCode(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    otp_code = models.CharField(max_length=10)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'otp_codes'


class PasswordReset(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    reset_token = models.CharField(max_length=255)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'password_resets'
