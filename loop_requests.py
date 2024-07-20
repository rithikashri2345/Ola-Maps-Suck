from send_ola_map_requests import ola_call
from geoloc_ola import get_loc

success=0
failed=0
same_prev = False
prev_response = {}

empty_count = 0

# while(True):
#     res = ola_call()

#     if res['status']=='ok':
#         success+=1
#         same_prev  = (prev_response == res)
#         prev_response = res
#         empty_prediction = (len(res['predictions'])==0)
#         if empty_prediction:
#             empty_count+=1
#             success-=1
#         elif same_prev:
#             print(res)
#             failed+=1
#             success-=1
#     print('Success count:',success,'| Failed count:',failed, '| Empty Prediction:', empty_count, '| Same Prev response?:', same_prev)


# prev = (77.5514796722512,12.922592358602232)
while(True):
    res = get_loc()

    if res['status']=='ok':
        success+=1
        same_prev  = (prev_response == res)
        prev_response = res
        empty_prediction = (len(res['results'])==0)
        if empty_prediction:
            empty_count+=1
            success-=1
        elif same_prev:
            print(res)
            failed+=1
            success-=1
    print('Success count:',success,'| Failed count:',failed, '| Empty Prediction:', empty_count, '| Same Prev response?:', same_prev)