import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if scores.empty:
        return pd.DataFrame(columns=['score', 'rank'])
    df = scores.sort_values(by='score', ascending=False)
    score_rank = []
    cur_score = 1e5
    cur_rank = 0
    for row in df.itertuples(index=bool):
        if row.score == cur_score:
            score_rank.append([cur_score, cur_rank])
        else:
            cur_score = row.score
            cur_rank += 1
            score_rank.append([cur_score, cur_rank])
    return pd.DataFrame(data=score_rank, columns=['score', 'rank'])


if __name__ == '__main__':
    # data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    # data = []
    data = [[1,0]]
    scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
    print(order_scores(scores))