import json
from django.shortcuts import render
from .models import Admissions_data
from django.http import JsonResponse
from django.core.paginator import Paginator

op_to_lookup = {
    'equal': 'exact',
    'not_equal': 'exact',
    'like': 'contains',
    'not_like': 'contains',
    'starts_with': 'startswith',
    'ends_with': 'endswith',
    'less': 'lt',
    'less_or_equal': 'lte',
    'greater': 'gt',
    'greater_or_equal': 'gte',
    'between': 'range',
    'not_between': 'range',
    'select_equals': 'exact',
    'select_not_equals': 'exact',
    'select_any_in': 'in',
    'select_not_any_in': 'in',
}

def index(request):
	return render(request,'yingding/index.html')


def test(request):
	return render(request,'yingding/test.html')


def zytb(request):
	admissions_data_fields = [{'name':field.name,'label':field.verbose_name} for field in Admissions_data._meta.fields]
	return render(request,'yingding/admissions_data.html',{'admissions_data_fields':admissions_data_fields})

def analyse_student_informations(student_informations):
    if student_informations is None:
        grade_query = Admissions_data.objects.all()
        final_query = grade_query
    else:
        grade = student_informations['grade']
        grade_query = Admissions_data.objects.filter(line_2021__range = (grade-20,grade+5))

        preferred_subject = student_informations['preferred_subject']
        preferred_subject_query = Admissions_data.objects.filter(preferred_subject__in = [preferred_subject])

        recleaning_subject = student_informations['recleaning_subject'].split(',')
        hua_sheng_group = ['不限','化学','生物','化学和生物','化学或生物','化学或思想政治','化学或地理','地理或化学','生物或思想政治','生物或地理']
        hua_di_group = ['不限','化学','地理','化学或生物','化学或思想政治','化学和地理','化学或地理','地理或化学','生物或地理','思想政治或地理']
        hua_zhen_group = ['不限','化学','思想政治','化学或生物','化学和思想政治','化学或思想政治','化学或地理','地理或化学','生物或思想政治','思想政治或地理']
        sheng_di_group = ['不限','生物','地理','化学或生物','化学或地理','地理或化学','生物或思想政治','生物和地理','生物或地理','思想政治或地理']
        sheng_zhen_group = ['不限','生物','思想政治','化学或生物','化学或思想政治','生物和思想政治','生物或思想政治','生物或地理','思想政治或地理']
        di_zhen_group = ['不限','思想政治','地理','化学或思想政治','化学或地理','地理或化学','生物或思想政治','生物或地理','思想政治和地理','思想政治或地理']
        if len(recleaning_subject) == 2:            
            if recleaning_subject == ['化学','生物'] or recleaning_subject == ['生物','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_sheng_group)
            elif recleaning_subject == ['化学','地理'] or recleaning_subject == ['地理','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_di_group)
            elif recleaning_subject == ['化学','地理'] or recleaning_subject == ['地理','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_di_group)
            elif recleaning_subject == ['化学','地理'] or recleaning_subject == ['地理','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_di_group)
            elif recleaning_subject == ['化学','地理'] or recleaning_subject == ['地理','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_di_group)
            elif recleaning_subject == ['化学','地理'] or recleaning_subject == ['地理','化学']:
                recleaning_subject_query = Admissions_data.objects.filter(recleaning_subject__in = hua_di_group)
            else:
                recleaning_subject_query = grade_query & preferred_subject_query
        else:
            pass


        intention_area = student_informations['intention_area'].split(',')
        intention_area_query = Admissions_data.objects.filter(provinces__in = intention_area)

        final_query = grade_query & preferred_subject_query & recleaning_subject_query & intention_area_query
    return final_query


def admissions_data_filter_api(request):
    data = json.loads(request.body.decode())
    page = data.get('page', 1)
    per_page = data.get('perpage', 10)

    student_informations = data.get('student_informations')
    admissions_datas = analyse_student_informations(student_informations)
    admissions_datas = admissions_datas.order_by('-line_2021')
    paginator = Paginator(admissions_datas, 50)
    page_obj = paginator.get_page(page)

    data = {
        'status': 0,
        'msg': 'ok',
        'data': {
            'total': admissions_datas.count(),
            'items': list(page_obj.object_list.values())
        }
    }
    return JsonResponse(data)

