def dotask(df):
    col = ['Journey Name', 'Team Name', 'Form Number', 'Rating', 'Remarks', 'Sub Categories', 'Sentiment']
    import pandas as pd
    import numpy as np
    import re
    import string
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    from nltk.tokenize import word_tokenize
    ps = PorterStemmer()
    #df = pd.read_excel("D:\ICICI Sep.xlsx")
    #df

    def transform_text(text):
        text = text.lower()
        text = nltk.word_tokenize(text)

        y = []
        for i in text:
            if i.isalnum():
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)

        text = y[:]
        y.clear()

        for i in text:
            y.append(ps.stem(i))

        return (" ".join(y))

    df['Remarks'] = df['Remarks'].astype(str)
    df['transformed_text'] = df['Remarks'].apply(transform_text)
    #df
    df['transformed_text'] = df['transformed_text'].astype(str)
    df['words in text'] = df['transformed_text'].apply(lambda x: len(word_tokenize(x)))
    #df
    df['transformed_text'] = df['transformed_text'].replace('', np.NaN)
    #df
    df.dropna(subset=['transformed_text'], how='all', inplace=True)
    #df
    df['Categories'] = ''
    Satisfied_Customers = ['good', 'all good', 'satisfied', 'already satisfied', 'excellent service', 'excellent',
                           'great support', 'really helpful', ' hassle free', 'easy process', 'great job',
                           'good behaviour', 'fine', 'thank you', 'well done', 'doing great job', 'keep it up',
                           'simple', 'quick', 'nice excutive', 'very simple', 'easy', 'awesome', 'wanderful',
                           'good opportunity', 'user friendly', 'happy']
    App_performance_Issues_latency = ['log in', 'internet banking', 'mobile banking', 'mobile app', 'linking', 'slow',
                                      'password', 'varification', 'interface', 'account', 'generation', 'captcha',
                                      'captcha entry', 'pin', 'activate', 'log out']
    Need_Information_regarding_stocks_and_share = ['stocks', 'shares', 'investment', 'investor']
    Relationship_Management_related_Issues = ['appoint', 'relationship manager', 'interactive', 'reach out']
    Poor_Customer_Service = ['too tedious', 'irritating', ' inexperienced', 'hire', 'customer care', 'need call',
                             'executive', 'bad experience', 'unable', 'help', 'unsupportive', 'not happy', 'worst',
                             'extremly bad', 'not responding', 'very bad', 'not satisfactory', 'poor services',
                             'pathetic', 'improve', 'horrible', 'lousy', 'hopeless', 'not solved', 'must solve']
    Need_Customer_support = ['customer care', 'call back', 'call me', 'service customer', 'provide proper information',
                             'pohone help', 'service', 'answer all queries', 'call', 'answer', 'call center']
    High_Charges = ['high charges', 'transaction charges', 'securities charges', 'very high']
    High_brokerage = ['high brokerage', 'brokerage', 'brokerage plan']
    Suggestion_in_App_Performance = ['make easy', 'make fast', 'kindly educate', 'make the process', 'should made',
                                     'please make']
    Difficulty_in_selling_and_purchasing_share = ['portfoio related', 'selling', 'purchasing', 'buy', 'sell',
                                                  'purchashe']
    Trade_related_Issues = ['trading']
    Account_opening_and_activation = ['account opening', 'create account', 'add account', 'add demat', 'account opened',
                                      'activation']
    Transaction_Issue = ['debit', 'credit', 'transaction', 'transfer', 'money', 'transanct', 'debited', 'credited',
                         'money losses']
    Daily_chart_related_issues = ['chart', 'graphs', 'graphic interface']
    Account_closing = ['freeze', 'close', 'delete', 'permanently close', ]
    Mutual_Fund = ['mutual funds', 'mutual fund']
    Issues_in_maintaining_contract = ['contract', 'contracts', 'contract notes', 'contracts notes', 'contract note']
    Investment_related_Issues = ['investment', 'invest']
    Delay_in_Services = ['took lot time', 'taking much time', 'minimize the time']
    Margin_money = ['margin', 'margin requirment', 'margin required', 'margin recommendations', 'margin trading',
                    'margin system']
    Equity_Service = ['investment advisory', 'actively trading investing', 'return', 'investment', 'rotation', 'equity',
                      'booked investment', 'fixed investment']
    #df
    df.reset_index(drop=True, inplace=True)

    for i in range(0, len(df.transformed_text)):
        if any(word in df.transformed_text[i] for word in Satisfied_Customers):
            df['Categories'][i] = 'Satisfied Customers'

        elif any(word in df.transformed_text[i] for word in App_performance_Issues_latency):
            df['Categories'][i] = 'App performance Issues/latency'

        elif any(word in df.transformed_text[i] for word in Need_Information_regarding_stocks_and_share):
            df['Categories'][i] = 'Need Information regarding stocks and share'

        elif any(word in df.transformed_text[i] for word in Relationship_Management_related_Issues):
            df['Categories'][i] = 'Relationship Management related Issues '

        elif any(word in df.transformed_text[i] for word in Poor_Customer_Service):
            df['Categories'][i] = 'Poor Customer Service'

        elif any(word in df.transformed_text[i] for word in Need_Customer_support):
            df['Categories'][i] = 'Need Customer support'

        elif any(word in df.transformed_text[i] for word in High_Charges):
            df['Categories'][i] = 'High Charges'

        elif any(word in df.transformed_text[i] for word in High_brokerage):
            df['Categories'][i] = 'High brokerage'

        elif any(word in df.transformed_text[i] for word in Suggestion_in_App_Performance):
            df['Categories'][i] = 'Suggestion in App Performance'

        elif any(word in df.transformed_text[i] for word in Difficulty_in_selling_and_purchasing_share):
            df['Categories'][i] = 'Difficulty in selling and purchasing share'

        elif any(word in df.transformed_text[i] for word in Trade_related_Issues):
            df['Categories'][i] = 'Trade related Issues'

        elif any(word in df.transformed_text[i] for word in Account_opening_and_activation):
            df['Categories'][i] = 'Account opening and activation '

        elif any(word in df.transformed_text[i] for word in Transaction_Issue):
            df['Categories'][i] = 'Transaction Issue'

        elif any(word in df.transformed_text[i] for word in Daily_chart_related_issues):
            df['Categories'][i] = 'Daily chart related issues'

        elif any(word in df.transformed_text[i] for word in Account_closing):
            df['Categories'][i] = 'Account closing'
        elif any(word in df.transformed_text[i] for word in Mutual_Fund):
            df['Categories'][i] = 'Mutual Fund'
        elif any(word in df.transformed_text[i] for word in Issues_in_maintaining_contract):
            df['Categories'][i] = 'Issues in maintaining contract'
        elif any(word in df.transformed_text[i] for word in Investment_related_Issues):
            df['Categories'][i] = 'Investment related Issues'
        elif any(word in df.transformed_text[i] for word in Delay_in_Services):
            df['Categories'][i] = 'Delay in Services'
        elif any(word in df.transformed_text[i] for word in Margin_money):
            df['Categories'][i] = 'Margin money'

        elif any(word in df.transformed_text[i] for word in Equity_Service):
            df['Categories'][i] = 'Equity Service'
        else:
            df['Categories'][i] = 'Generic comment'
        df['Categories'].value_counts()
        #df
        #df.to_excel(r"\\192.168.4.12\Product_Development\DATA SCIENCE(RCR)\Smruti\ICICI SEPTEMBER4.xlsx")
    df= df.sample(frac=1).reset_index(drop=True)
    df['Categories'] = df['Categories'].replace('', np.nan, regex=True)
    df['Categories'] = df['Categories'].replace(np.nan, 'Unproductive comment')
    df['Sub Categories'] = df['Sub Categories'].replace('', np.nan, regex=True)
    df['Sub Categories'] = df['Sub Categories'].replace(np.nan, 'Not available')
    df['NPS CAT'] = ""
    df['Rating'] = df['Rating'].astype(int)
    detractor = df[df['Rating'] < 7]
    detractor['NPS CAT'] = "Detractor"
    promoter = df[df['Rating'] > 8]
    promoter['NPS CAT'] = "Promoter"
    passive = df[(df['Rating'] < 9) & (df['Rating'] > 6)]
    passive['NPS CAT'] = "Passive"
    df1 = pd.concat([detractor, promoter, passive])
    Promoter_count = len(df1[df1['NPS CAT'] == 'Promoter'])
    Passive_count = len(df1[df1['NPS CAT'] == 'Passive'])
    Detractor_count = len(df1[df1['NPS CAT'] == 'Detractor'])
    df1['Total Nps Score'] = ''
    df1['Total Nps Score'] = (Promoter_count - Detractor_count) / (
            Promoter_count + Passive_count + Detractor_count) * 100
    col = ['mobile', 'zone', 'city', 'state', 'Rating', 'Remarks', 'Cleaned_Remarks', 'Categories', 'Sub Categories',
           'NPS CAT', 'Total Nps Score']
    global df_2
    df_2 = pd.DataFrame(columns=col)

    for i in df1['Categories'].unique():
        j = i
        j = df1[df1['Categories'] == i]
        detractor = j[j['Rating'] < 7]
        detractor['NPS CAT'] = "Detractor"
        promoter = j[j['Rating'] > 8]
        promoter['NPS CAT'] = "Promoter"
        passive = j[(j['Rating'] < 9) & (j['Rating'] > 6)]
        passive['NPS CAT'] = "Passive"

        frames = [detractor, promoter, passive]
        a = pd.concat(frames)
        Promoter_count = len(a[a['NPS CAT'] == 'Promoter'])
        Passive_count = len(a[a['NPS CAT'] == 'Passive'])
        Detractor_count = len(a[a['NPS CAT'] == 'Detractor'])

        a['Total Nps Score Cat Wise'] = ''
        a['Total Nps Score Cat Wise'] = (Promoter_count - Detractor_count) / (Promoter_count + Passive_count
                                                                              + Detractor_count) * 100
        frames = [df_2, a]
        df_2 = pd.concat(frames)
    #         global data
    #         data = df_final.append(df_2)

    # df_2.to_excel(r'D:\Ritesh_2022\Bhim\Bhim_model_based_approach\testing.xlsx')
    return df_2




