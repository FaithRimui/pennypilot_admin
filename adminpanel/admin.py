from django.contrib import admin
from .models import User, Expense, Income, Budget, SavingsGoal

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'phone', 'created_at')
    search_fields = ('username', 'email')
    list_per_page = 20

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_id', 'user', 'amount', 'source', 'date_received')
    search_fields = ('user__username', 'source')
    raw_id_fields = ['user']  # Prevent big dropdown
    list_per_page = 20

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('expense_id', 'user', 'amount', 'category', 'date', 'expense_type')
    search_fields = ('category',)
    raw_id_fields = ['user']
    list_per_page = 20

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('budget_id', 'user', 'budget_amount', 'created_at')
    raw_id_fields = ['user']
    list_per_page = 20

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'goal_name', 'goal_amount', 'progress_amount', 'target_date')
    raw_id_fields = ['user']
    list_per_page = 20
