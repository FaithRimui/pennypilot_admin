from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import mysql.connector
import bcrypt

@csrf_exempt
@require_POST
def api_admin_login(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='financetracker'
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM admins WHERE email = %s", (email,))
        admin = cursor.fetchone()
        conn.close()

        if admin and bcrypt.checkpw(password.encode('utf-8'), admin['password_hash'].encode('utf-8')):
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)


def admin_home(request):
    return HttpResponse("<h1 style='color:pink; text-align:center;'>Welcome to the Penny Pilot Admin Panel</h1>")
