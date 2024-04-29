from django.http import JsonResponse
import joblib
from django.views.decorators.csrf import csrf_exempt
import json

# Sample data
#input_data1 = [[13.49, 4.12, 139452, 0.9, 69, 368, 2668]] 

# print("Predicted credit score:", predicted_score[0])
@csrf_exempt
def predict(request):
    print("Decimal Values::",request.body)
    data = json.loads(request.body)
    profit_margin = data.get('input1')
    return_on_total_assets = data.get('input2')
    credit_limit = data.get('input3')
    likelihood_of_failure_percentage = data.get('input4')
    no_of_employees = data.get('input5')
    gearing = data.get('input6')
    net_current_assets = data.get('input7')
    random_forest_model = joblib.load('crsbe/rf_model.pkl')
    input_data = [[profit_margin, return_on_total_assets,credit_limit, likelihood_of_failure_percentage, no_of_employees, gearing, net_current_assets]] 
    predicted_score = random_forest_model.predict(input_data)[0]
    predicted_score = predicted_score.item()
    if predicted_score < 50:
        risk = "high"
    elif predicted_score >= 80:
        risk = "low"
    else:
        risk = "medium"
    return JsonResponse({'predicted_score': predicted_score, 'credit_risk': risk})