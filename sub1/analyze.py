from sub1.parse import load_dataframes
import pandas as pd
import shutil


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group = stores_reviews.groupby(["store", "store_name"])
    score_filter = scores_group.filter(lambda x: len(x) >= min_reviews).reset_index()
    scores = score_filter.groupby(["store", "store_name"]).mean()
    sorting_scores = scores.sort_values(["score"], ascending=[False])
    return sorting_scores.head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group = stores_reviews.groupby(["store", "store_name"]).count()
    result = scores_group.sort_values(["id_x"], ascending=[False])
    return result.head(n=n).reset_index()


def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    user_group = dataframes["reviews"].sort_values(["user"]).groupby(["user"]).count()
    user_sort = user_group.sort_values(["id"], ascending=[False])
    return user_sort.head(n=n).reset_index()


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    stores_most_scored = sort_stores_by_score(data)

    print("[최고 평점 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_scored.iterrows():
        print(
            "{rank}위: {store}({score}점)".format(
                rank=i + 1, store=store.store_name, score=store.score
            )
        )
    print(f"\n{separater}\n\n")

    stores_most_reviewed = get_most_reviewed_stores(data)

    print("[최다 리뷰 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_reviewed.iterrows():
        print(
            "{rank}위: {store}({review}개)".format(
                rank=i + 1, store=store.store_name, review=store.id_y
            )
        )
    print(f"\n{separater}\n\n")

    get_most_active = get_most_active_users(data)

    print("[최다 리뷰 유저]")
    print(f"{separater}\n")
    for i, users in get_most_active.iterrows():
        print(
            "{rank}위: {user}번유저({review}개)".format(
                rank=i + 1, user=users.user, review=users.id
            )
        )
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
