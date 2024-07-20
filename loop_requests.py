from send_ola_map_requests import ola_call

success=0
failed=0
same_prev = False
prev_response = {}

while(True):
    res = ola_call()

    if res['status']=='ok':
        success+=1
    same_prev  = (prev_response == res)
    prev_response = res
    empty_prediction = (len(res['predictions'])==0)
    if empty_prediction:
        failed+=1
        success-=1
    elif same_prev:
        print(res)
        failed+=1
        success-=1
    print('Success count:',success,'| Failed count:',failed, '| Empty Prediction?:', empty_prediction, '| Same Prev response?:', same_prev)