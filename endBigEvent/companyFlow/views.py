from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.


from companyFlow.models import CompanyFlow
from django.db.models import Q
from datetime import date

# def selectByCompany(request):
#
#
#     return HttpResponse('company')

def selectByCompany(request):
    # 假设要查询的具体时间（这里示例为2024-01-01这个日期）
    specific_date = date(2024, 1, 1)
    # 流向值，假设为0
    specific_flow_direction = 0   # 0表示入省份； 1表示出省份
    # 专业公司名称示例
    specific_company = '成研'
    # 业务类型示例
    specific_business_type = '其他'

    try:
        # 通过模型类的objects属性进行查询，使用filter方法精确匹配各个字段的值
        result = CompanyFlow.objects.filter(
            time_column=specific_date,
            flow_direction=specific_flow_direction,
            professional_company=specific_company,
            business_type=specific_business_type
        ).first()
        if result:
            byte_count = result.byte_count
            return render(request, 'index.html', {'byte_count': byte_count})
        else:
            return render(request, 'index.html', {'message': '未找到符合条件的数据'})
    except:
        return render(request, 'index.html', {'message': '查询过程出现错误'})

def selectByTime(request):
    # 假设要查询的具体时间（这里示例为2024-01-01这个日期）
    specific_date = date(2024, 1, 1)
    # 流向值，假设为0
    # specific_flow_direction = 0   # 0表示入省份； 1表示出省份
    # 专业公司名称示例
    specific_company = '成研'
    # 业务类型示例
    # specific_business_type = '其他'

    try:
        result = CompanyFlow.objects.filter(
            time_column=specific_date,
        )
        companies = result.values_list('professional_company', flat=True).distinct()  ## 专业公司类型
        data=[]
        for i in range(len(companies)):
            info = {
                "company": companies[i],
                "homeIn": 0,
                "homeOut": 0,
                "specialIn": 0,
                "specialOut": 0,
                "otherIn": 0,
                "otherOut": 0
            }
            info['homeIn']= sum([record.byte_count for record in result if record.professional_company == companies[i]
                                 and record.flow_direction == 0 and record.business_type == '家企宽用户'])  ## 0流入
            info['homeOut'] = sum([record.byte_count for record in result if record.professional_company == companies[i]
                                  and record.flow_direction == 1 and record.business_type == '家企宽用户'])  ## 0流入
            info['specialIn'] = sum([record.byte_count for record in result if record.professional_company == companies[i]
                                  and record.flow_direction == 0 and record.business_type == '专线用户'])  ## 0流入
            info['specialOut'] = sum([record.byte_count for record in result if record.professional_company == companies[i]
                                  and record.flow_direction == 1 and record.business_type == '专线用户'])  ## 0流入
            info['otherIn'] = sum([record.byte_count for record in result if record.professional_company == companies[i]
                                  and record.flow_direction == 0 and record.business_type == '其他'])  ## 0流入
            info['otherOut'] = sum([record.byte_count for record in result if record.professional_company == companies[i]
                                  and record.flow_direction == 1 and record.business_type == '其他'])  ## 0流入
            data.append(info)


        requestData = {
            "code": 0,
            "message": "success",
            "data": data
        }
        return JsonResponse(data=requestData)
        # 通过模型类的objects属性进行查询，使用filter方法精确匹配各个字段的值
        result = CompanyFlow.objects.filter(
            time_column=specific_date,
            professional_company=specific_company,
        )
        ## 查出有哪些专业公司
        companies = CompanyFlow.objects.filter(
            time_column=specific_date
        ).values_list('professional_company', flat=True).distinct()
        data_list=[]
        for i in range(len(companies)):
            ## 查出专业公司相关数据
            result = CompanyFlow.objects.filter(
                time_column=specific_date,
                professional_company=specific_company,
            )
            ##  流向为0，业务类型为专线用户，字节数和
            sum_bytes = sum([record.byte_count for record in result if
                             record.flow_direction == 0 and record.business_type == '专线用户'])
        return HttpResponse(result)
        return JsonResponse(result, safe=True)
        # if result:
        #     byte_count = result.byte_count
        #     return render(request, 'index.html', {'byte_count': byte_count})
        # else:
        #     return render(request, 'index.html', {'message': '未找到符合条件的数据'})
    except:
        data = {
            "code": 1,
            "message": "failed",
            "data": []
        }
        return JsonResponse(data=data)


def testCompanyFlow(request):

    data = {
        "code": 0,
        "message": "success",
        "data": [
            {
                "company": "成研",
                "homeIn": 73,
                "homeOut": 90,
                "specialIn": 100,
                "specialOut": 74,
                "otherIn": 94,
                "otherOut": 37
            },
            {
                "company": "咪咕",
                "homeIn": 97,
                "homeOut": 93,
                "specialIn": 84,
                "specialOut": 42,
                "otherIn": 79,
                "otherOut": 85
            },
            {
                "company": "上研",
                "homeIn": 1,
                "homeOut": 13,
                "specialIn": 30,
                "specialOut": 28,
                "otherIn": 29,
                "otherOut": 34
            }
        ]
    }
    return JsonResponse(data, safe=True)
    # response.content = data
    # return response