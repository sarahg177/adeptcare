from django.db import models

# Create your models here.


class Carer(models.Model):
    """Choices"""
    Elderly_Care = 'Elderly_Care'
    Companionship = 'Companionship'
    Dementia = 'Dementia'
    Alzheimers = 'Alzhemiers'
    Parkinsons = 'Parkinsons'
    Stroke = 'Stroke'
    Brain_Injury = 'Brain_Injury'
    Spinal_Injury = 'Spinal_Injury'
    Visually_Impaired = 'Visually_Impaired'
    Diabetes = 'Diabetes'
    Metal_Health = 'Mental_Health'
    Palliative_Care = 'Palliative_Care'
    End_Of_Life = 'End_Of_Life'
    Physical_Disabilities = 'Physical_Disabilities'
    Learning_Disabilities = 'Learning_Disabilities'
    Catheter_Care = 'Catheter_Care'
    Peg_Feeding = 'Peg_Feeding'
    Stoma_Care = 'Stoma_Care'
    Colostomy_Care = 'Colostomy_Care'
    Post_Op_Care = 'Post_Op_Care'
    Personal_Care = 'Personal_Care'
    Housework = 'Housework'
    Shopping = 'Shopping'
    Medication_Administration = 'Medication_Administration'
    Food_Preparation = 'Food_Preparation'

    PRIMARY_CONDITION = [
        ('Elderly_Care', 'Elderly_Care'),
        ('Companionship', 'Companionship'),
        ('Dementia', 'Dementia'),
        ('Alzhemiers', 'Alzhemiers'),
        ('Parkinsons', 'Parkinsons'),
        ('Stroke', 'Stroke'),
        ('Brain_Injury', 'Brain_Injury'),
        ('Spinal_Injury', 'Spinal_Injury'),
        ('Visually_Impaired', 'Visually_Impaired'),
        ('Diabetes', 'Diabetes'),
        ('Mental_Health', 'Mental_Health'),
        ('Palliative_Care', 'Palliative_Care'),
        ('Enf_Of_Life', 'End_Of_Life'),
        ('Physical_Disabilities', 'Physical_Disabilities'),
        ('Learning_Disabilities', 'Learning_Disabilities'),
        ('Catheter_Care', 'Catheter_Care'),
        ('Peg_Feeding', 'Peg_Feeding'),
        ('Stoma_Care', 'Stoma_Care'),
        ('Colostomy_Care', 'Colostomy_Care'),
        ('Post_Op_Care', 'Post_Op_Care'),
    ]

    REQUIREMENTS = [
        ('Personal_Care', 'Personal_Care'),
        ('Housework', 'Housework'),
        ('Shopping', 'Shopping'),
        ('Medication_Administration', 'Medication_Administration'),
        ('Food_Preparation', 'Food_Preparation'),
    ]

    first_name = models.CharField(max_length=100, blank=False)

    last_name = models.CharField(max_length=100, blank=False)

    known_as = models.CharField(max_length=100, blank=False)

    telephone = models.CharField(max_length=12, blank=False)

    email = models.CharField(max_length=100, blank=False)

    short_bio = models.TextField(max_length=500, blank=False)

    image = models.ImageField(upload_to='img')



    """primary_condition = models.CharField(
        max_length=30,
        choices=PRIMARY_CONDITION,
        default='Post_Op_Care'
        )

    requirements = models.CharField(
        max_length=20,
        choices=REQUIREMENTS,
        default='Personal_Care'
        )"""


def __str__(self):
    return self.first_name
