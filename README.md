git develop branch 변경

# SSAFY Bigdata project [made by COSAT]

[**notion 프로젝트 내용 보러가기**](https://www.notion.so/COSAT-98905101fd0740808ed67f1c3551bfa9 "notion으로 이동") <br>
<br>
[**git flow reference**](https://k39335.tistory.com/82 "gitflow 참고")

---

## 프로젝트 명: 싸이코 (싸우자 이기자 코로나)

**개요** : 코로나 시대에 들어서면서 다수의 유동인구를 통한 감염병의 전파가 이슈가 되었습니다. 최대한 이동을 자제하는 것이 이상적이나 서로의 목적에 의해 이동은 불가피합니다. 그로인해 우리는 유동인구를 분산시키기 위한 코로나 예방 서비스를 만들고자 "싸이코" 프로젝트를 개발하게 되었습니다.

---

## Memo

협업필터링(CF) - 사용자 행동기록 활용
콘텐츠 기반 필터링(CB) - 항목 자체를 분석

_ensemble system_<br>
하이퍼 파라미터 최적화 방법

- TPE 알고리즘
- HyperOpt 알고리즘
- HyperBand 알고리즘

가중합이 잘 동작하지 않는 경우
(in 정보검색)

- 순위 결합(rank aggregation) 알고리즘
  - 상호 랭킹 결합
  - comb mnz

새로운 로직의 성능 측정<br>
가장 간단한 측정법 : 전후 비교법<br>

- 이 방법은 공정하지 않음(변수)<br>
  - 온라인 테스트를 통해 지표 측정 방법론이 공정함 <br>

---

## How to Run (in Skeleton code)

### Sub1

```sh
cd sub1
pip install -r requirements.txt
python parse.py
python analyse.py
python visualize.py
```

### Sub 2

**Backend**

```sh
cd sub2/backend
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py initialize
python manage.py runserver
```

**Frontend**

```sh
cd sub2/frontend
npm install
npm run serve
```


