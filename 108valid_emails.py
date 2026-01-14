import pandas as pd

def valid_rules(row):
    email = row['mail']
    rule1 = email[0].isalpha()

    valid_chs = {'_', '.', '-'}
    lst = email.split('@', 1)
    print(lst)
    rule2 = all(ch.isalnum() or ch in valid_chs for ch in lst[0])
    rule3 = lst[1] == 'leetcode.com' if len(lst)==2 else False
    return all([rule1, rule2, rule3])

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users.apply(valid_rules, axis=1)]
    return df

if __name__ == '__main__':
    data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'], [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'], [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'], [7, 'Shapiro', '.shapo@leetcode.com']]
    users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype({'user_id':'int64', 'name':'object', 'mail':'object'})
    print(valid_emails(users))