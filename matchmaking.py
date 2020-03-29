# Problem statement: Based on the input parameters, recommend the most suitable credit card holder to the customer from best fit to worst.

import json

# sample data(start)
# sample customer input
requests = {
    1 : {
        'Name': 'Mary','Amount': '666','Offer': '20','Date': '2020-03-20','Time': 'Now','Card': 'HangSeng_enJoycard',
        'Merchant': 'Pizza Hut','Category': 'Food','Note': 'Dinner for group of 4' },
    2 : {
        'Name': 'Mindy','Amount': '260','Offer': '30','Date': '2020-03-20','Time': 'Now','Card': 'HSBC_Mastercard',
        'Merchant': '1935 Restaurant','Category': 'Food','Note': 'Lunch with Andrew' }
    # feel free to add more when see fit...
}

# sample credit card holder
credit_card_holders = {
    1 : {'Name': 'Tom','Cards_owned': 'HangSeng_enJoycard','Commission': '5'  },
    2 : {'Name': 'Toby','Cards_owned': 'HangSeng_enJoycard','Commission': '6' }
}
# sample types of credit cards in our database
available_cards = {
    'HSBC_Mastercard' : {
        #format:        covered restaurant name:      discount %, minimum spending requirement
        '1935 Restaurant' : ['10', '800'],
        'Amazake' : ['10', None],
        'Baan Thai': ['10', None],
        'Viva La Vida': ['25', '500']
    },
    'HangSeng_enJoycard' : {
        #format:       covered restaurant name:      discount %, minimum spending requirement
        'Pizza Hut' : ['10', None],
        'Cafe Deco Pizzeria' : ['15', '500'],
        'PHD': ['10', None],
        'Luna Cake': ['10', None]
    }
}
# sample data(end)

# helper functions
# test if the payment amount is within the acceptable price range specified by the credit card holder
def isInAcceptablePriceRange(amount,lowerlimit,upperlimit):
    if int(amount) >= lowerlimit and int(amount) <= upperlimit:
        return True
    else:
        return False

# check if the payment amount satisifies the minimum spending requirement
# for testing pre-entered requests in the requests list
def isEligibleForDiscount(i,cardName,merchant):
    if int(requests[i]['Amount']) >= int(available_cards[cardName][merchant][1]) or available_cards[cardName][merchant][1] == None:
        return True
    else:
        return False

# check if the payment amount satisifies the minimum spending requirement
# for testing user input request
def isEligibleForDiscountModified(request,cardName,merchant):
    if int(request['Amount']) >= int(available_cards[cardName][merchant][1]) or available_cards[cardName][merchant][1] == None:
        return True
    else:
        return False


# create a candidate list that matches the credit card type
def findCandidates(cardName):
    candidate_list = []
    for i in range(1,len(credit_card_holders) + 1):
        candidate_info = []
        if cardName in credit_card_holders[i].values():
            candidate_info.append(credit_card_holders[i]['Name'])
            candidate_info.append(credit_card_holders[i]['Commission'])
            candidate_list.append(candidate_info)
        else:
            continue
    return candidate_list

# sort the candidate list by ascending order
def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 


# main code begins (choose either testing case 1 or 2 )
def main():
    # TESTING CASE 1 (start): getting Input from Users
    # simulate user input
    data = {}
    data['Name'] = input('Name: ')
    data['Amount'] = input('Amount: ')
    data['Offer'] = input('Offer: ')
    data['Date'] = input('Date: ')
    data['Time'] = input('Time: ')
    data['Card'] = input('Card: ')
    data['Merchant'] = input('Merchant: ')
    data['Category'] = input('Category: ')
    data['Note'] = input('Note: ')
    convert = json.dumps(data)
    request = json.loads(convert)

    # test if merchant in the credit card supporting companies
    if request['Merchant'] in available_cards[request['Card']]:

        # test if transaction fee >= minimum spending requirement && transaction fee in Acceptable Price Range == True
        if (isEligibleForDiscountModified(request,request['Card'],request['Merchant']) == True) and (isInAcceptablePriceRange(request['Amount'],100,1000) == True):
            
            # sort the list from the lowest commission willing to receieve to highest.
            candidate_list = findCandidates(request['Card'])
            print(Sort(candidate_list))
        else:
            print('You cannot use the discount or your amount is not in the credit card holders acceptable price range')

    else:
        print('It is not supported.') 

    # TESTING CASE 1 (end)  

    ## TESTING CASE 2 (start): using sample data from data.json (uncomment for use)
    
    # for i in range(1,len(requests) + 1):
    #     # if merchant in card.key
    #     if requests[i]['Merchant'] in available_cards[requests[i]['Card']]:
    #         # if transaction fee >= minimum spending requirement && transaction fee in Acceptable Price Range == True
    #         if (isEligibleForDiscount(i,requests[i]['Card'],requests[i]['Merchant']) == True) and (isInAcceptablePriceRange(requests[i]['Amount'],100,1000) == True):
    #             # sort the list based on lowest commission willing to receieve.
    #             candidate_list = findCandidates(requests[1]['Card'])
    #             print(Sort(candidate_list))
    #         else:
    #             print('You cannot use the discount or your amount is not in the credit card holders acceptable price range')

    #     else:
    #         print('It is not supported.')

    ## TESTING CASE 2 (end)

if __name__ == "__main__":
    main()