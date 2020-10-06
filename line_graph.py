def net_profit_graph_data(request):
    from dateutil import relativedelta
    from operator import add,sub
    import numpy as np
    from datetime import date, timedelta
    data_dict={}
    m = datetime.datetime.now().month
    y = datetime.datetime.now().year
    ndays = (date(y, m + 1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    date_list = [(d1 + timedelta(days=i)).strftime('%d-%b') for i in range(delta.days + 1)]
    if date_list is not None:
        
        recived_amount_list=[3254,3435,2345,8690,9074,1234,5432,6735,9090,3245,6777,4523]
        repayment_amount_list=[3245,6545,1245,9823,6453,4567,8745,2567,3544,3333,9777,1245]
        seller_amount_list=[2121,3333,5555,2222,9999,6789,5554,6667,7668,7767,2345,5432]
        logistic_amount_list=[2367,2378,9498,3478,5957,3643,9777,3562,3783,3847,9994,4657]
        net_profit_list=list(map(sub,list(map(add, recived_amount_list, repayment_amount_list)),list(map(add, seller_amount_list, 		logistic_amount_list))))

    data_dict["recived_amount_list"]=recived_amount_list;
    data_dict["repayment_amount_list"]=repayment_amount_list;
    data_dict["seller_amount_list"]=seller_amount_list;
    data_dict["logistic_amount_list"]=logistic_amount_list;
    data_dict["net_profit_list"]=net_profit_list;
    data_dict["date_list"]=date_list;

    return HttpResponse(json.dumps(data_dict))
