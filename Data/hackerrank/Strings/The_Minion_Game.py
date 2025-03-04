vowels = ['A','E','I','O','U']

def minion_game(s):
    vowels = 'AEIOU'
    s = s.upper()

    p1_name, p2_name = 'Stuart', 'Kevin'
    score_p1_con, score_p2_vow = 0, 0
    
    for i in range(len(s)):
        score = len(s) - i
        if s[i] in vowels:
            score_p2_vow += score
        else:
            score_p1_con += score

    # Exibir o vencedor
    if score_p1_con > score_p2_vow:
        print(p1_name, score_p1_con)
    elif score_p1_con < score_p2_vow:
        print(p2_name, score_p2_vow)
    else:
        print('Draw')
        
