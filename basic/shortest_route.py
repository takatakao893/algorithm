def search(goal, data): # goalから直接行ける場所までの最短距離を得る
    if goal == '吉祥寺': # 始点なら0を返す
        return 0.0
    else:
        prevdata = data.get(goal) # goalの直前の駅と距離の一覧(辞書型)
        w = [] # 最短距離の候補を記録する作業用のリスト
        for start in prevdata.keys(): # 直前の駅すべてについて
            # 直前の駅までの最短距離を再帰的に求める
            w.append(search(start, data) + prevdata.get(start)) # 最短距離の候補を記録
        return min(w) # 候補の中の最短のものを返す

distance = {'吉祥寺' : {'吉祥寺': 0.0},
            '明大前' : {'吉祥寺': 7.8},
            '下北沢' : {'明大前': 1.9},
            '新宿' : {'吉祥寺': 12.2, '明大前': 5.2, '下北沢': 4.9},
            '渋谷' : {'新宿': 3.4, '下北沢':3.0},
            '表参道' : {'渋谷': 1.3, '下北沢': 4.5}}
print(search('表参道', distance))
