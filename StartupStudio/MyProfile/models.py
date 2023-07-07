from django.db import models
from datetime import date

# class Status(models.Model):
#     name_status = models.CharField(max_length=30, verbose_name="Status Name")
#
#     def __str__(self):
#         return self.name_status


class Profile(models.Model):

    # Common Fields
    photo = models.ImageField(upload_to='images/', blank=True)
    lastname = models.CharField(max_length = 30, help_text = "Введите фамилию", verbose_name="Last Name")
    firstname = models.CharField(max_length = 30, help_text = "Введите имя", verbose_name="First Name")
    sername = models.CharField(max_length = 30, help_text = "Введите отчество", verbose_name="Sername")
    birth_date = models.DateField(default=date.today, help_text = "Введите дату рождения", verbose_name="Birth date")
    skills = models.CharField(max_length=500, help_text="Заполните резюме", verbose_name="Skills")
    email = models.EmailField(max_length=254, help_text="Введите электронную почту", verbose_name="Email") # нужно подтягивать с регистрации
    contact_info = models.CharField(max_length=15, help_text="Введите номер телефона", verbose_name="Contact Information")
    links = models.CharField(max_length=300, help_text="Ссылки на социальные сети, для связи", blank=True, null=True, verbose_name="Links")
    extrainfo = models.CharField(max_length=300, help_text="Дополнительная информация", blank = True, null = True, verbose_name="Extra Information")

    # status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    status_id=models.CharField(max_length = 30, help_text = "Введите статус", verbose_name="Status Name")

    # Status Fields
    # for student
    direction = models.CharField(max_length=100, help_text="Введите направление обучения", verbose_name="Direction")
    graduate_date = models.DateField(default=date.today, help_text = "Введите дату поступления", verbose_name="Graduate Date")
    # for teacher and company
    company_title = models.CharField(max_length=100, help_text="Введите название компании", verbose_name="Company Title")
    company_info = models.CharField(max_length=300, help_text="Информация о компании", blank = True, null = True, verbose_name="Company Information")
    company_links = models.CharField(max_length=500, help_text="Укажите сайт компании", verbose_name="Company Information")
    job_title = models.CharField(max_length=100, help_text="Укажите свою должность", verbose_name="Job Title")
    department = models.CharField(max_length=30, help_text="Укажите свою кафедру", verbose_name="Department")

    def __str__(self):
        return self.email
    def __repr__(self)->str:
        return self.email
