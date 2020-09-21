import itertools
from collections import Counter
from sub1.parse import load_dataframes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium as fol

def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


def show_store_categories_graph(dataframes, n=100):
    """
    Tutorial: 전체 음식점의 상위 `n`개 카테고리 분포를 그래프로 나타냅니다.
    """

    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)
    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )

    # 그래프로 나타냅니다
    chart = sns.barplot(x="category", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 카테고리 분포")
    plt.show()


def show_store_review_distribution_graph(dataframes, n=100):
    """
    Req. 1-3-1 전체 음식점의 리뷰 개수 분포를 그래프로 나타냅니다. 
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group_temp = stores_reviews.groupby(["store", "store_name"]).count()
    scores_group = scores_group_temp.head(n=n).reset_index()

    # 그래프로 나타냅니다
    chart = sns.barplot(x="store_name", y="id_x", data=scores_group)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 리뷰 분포")
    plt.show()


def show_store_average_ratings_graph(dataframes, n=100):
    """
    Req. 1-3-2 각 음식점의 평균 평점을 그래프로 나타냅니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group_temp = stores_reviews.groupby(["store", "store_name"]).mean()
    scores_group = scores_group_temp.head(n=n).reset_index()

    # 그래프로 나타냅니다
    chart = sns.barplot(x="store_name", y="score", data=scores_group)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 평균 평점 분포")
    plt.show()


def show_user_review_distribution_graph(dataframes, n=100):
    """
    Req. 1-3-3 전체 유저의 리뷰 개수 분포를 그래프로 나타냅니다.
    """
    user_group = dataframes["reviews"].sort_values(["user"]).groupby(["user"]).count()
    user_sort = user_group.sort_values(["id"], ascending=[False]).head(n=n).reset_index()

    # 그래프로 나타냅니다
    chart = sns.barplot(x="user", y="id", data=user_sort)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("유저 리뷰 개수 분포")
    plt.show()


def show_user_age_gender_distribution_graph(dataframes, n=100):
    """
    Req. 1-3-4 전체 유저의 성별/나이대 분포를 그래프로 나타냅니다.
    """
    user_group = dataframes["reviews"].sort_values(["user"]).groupby(["user"])
    user_sort = user_group.head(n=n).reset_index()
    user_age_sort = user_sort.sort_values(["born_year"])
    # 그래프로 나타냅니다
    chart = sns.countplot(data=user_age_sort, x="born_year", hue="gender")
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("유저 성별/나이대 분포")
    plt.show()


def show_stores_distribution_graph(dataframes, n=1000):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    store_group = dataframes["stores"]
    storess = store_group.head(n=n).reset_index()

    # 지도에 나타냅니다
    m = fol.Map(location=[36.105882, 128.419668], zoom_start=10)
    for i, stores in storess.iterrows():
        fol.Marker(location=[stores.latitude, stores.longitude], popup="Marker A",
                   icon=fol.Icon(icon='cloud')).add_to(m)
    m.save('map.html')


def main():
    set_config()
    data = load_dataframes()

    # 음식점 카테고리 분포
    # show_store_categories_graph(data)

    # 음식점 리뷰 분포
    # show_store_review_distribution_graph(data)

    # 음식점 평균 평점 그래프
    # show_store_average_ratings_graph(data)

    # 음식점 리뷰 갯수 분포
    # show_user_review_distribution_graph(data)

    # 유저별 나이대/성별 분포
    # show_user_age_gender_distribution_graph(data)

    # 각 음식점의 위치 분포
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
