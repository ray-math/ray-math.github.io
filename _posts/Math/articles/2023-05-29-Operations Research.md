---
layout: post
title:  오퍼레이션 리서치 (Operations Research, OR)
date:   2023-05-29
categories: articles
tags: 
---

우리가 생각할 때, 스타벅스를 떠올리면 맛있는 커피와 편안한 분위기가 먼저 떠오릅니다. 그러나 스타벅스와 같은 상장기업들의 사업 모델은 무엇보다 회사의 수익을 극대화하도록 설계되어 있습니다. 이러한 관행은 기업의 문화와 인센티브 정책에 반영될 뿐만 아니라, 기업 운영 소프트웨어에도 깊이 스며들어 있죠.

이런 과정에서 특히 중요한 역할을 하는 것이 바로 **오퍼레이션 리서치 (OR)**입니다. 오퍼레이션 리서치는 응용수학의 한 분야로, 복잡한 시스템의 최적화를 목표로 합니다. 작물 재배 계획을 세우는 농부들, 사람과 물자의 효율적인 수송을 위해 고속도로 건설 계획을 세우는 토목공학자들에게 도움을 줄 수 있죠.


## 오퍼레이션 리서치 (OR)의 어원과 개념

"오퍼레이션 리서치(Operations Research, 줄여서 OR)"라는 용어는 사실 군사학에서 유래되었습니다. 제2차 세계대전 동안 연합군이 군사 작전을 최적화하기 위해 이를 적극적으로 활용했는데, 이 때 사용한 방법론들을 통틀어 "작전 연구"라는 뜻의 오퍼레이션 리서치라고 부르게 되었습니다.

OR은 결정적이거나 확률적인 복잡한 시스템을 수학적으로 모델링하고, 그 최적의 해결책을 찾는데 초점을 둡니다. 최적의 해결책이란 주어진 자원을 가장 효율적으로 활용하는 방법이며, 이를 찾기 위해 사용하는 방법 중 하나가 선형 프로그래밍입니다.

선형 프로그래밍은 복잡한 시스템의 목표함수와 제약 조건을 선형 방정식으로 표현하고, 이를 최적화하는 방법을 찾는 과정입니다. 이를 통해 복잡한 문제를 간소화하고, 계산이 가능한 형태로 바꾸어 해결합니다.

예를 들어, 한 기업이 최대 이익을 얻기 위해 얼마나 많은 제품을 생산해야 하는지 결정해야 한다면, 각 제품의 이익과 제작에 필요한 자원을 변수로 하는 선형 방정식을 세울 수 있습니다. 그리고 이를 최적화하는 방법을 찾는 것이 OR의 주요 목표가 됩니다.


## 선형 프로그래밍을 이용한 최적화 문제

자, 그럼 이제 위에서 언급한 기업의 제품 생산 문제를 구체적인 숫자로 예를 들어 설명해 보겠습니다.


가상의 기업이 제품 A, B, C를 생산한다고 가정합시다. 제품 A를 만드는 데는 자원 X가 3단위, 자원 Y가 4단위, 자원 Z가 2단위가 필요하고 제품 B를 만드는 데는 자원 X가 2단위, 자원 Y가 1단위, 자원 Z가 3단위가 필요하며, 제품 C를 만드는데는 자원 X가 4단위, 자원 Y가 3단위, 자원 Z가 2단위가 필요하다고 가정합시다. 또한 각 제품에서 얻을 수 있는 이익이 제품 A는 3000원, 제품 B는 2000원, 제품 C는 4000원이라고 가정합시다. 

기업은 총 자원 X 100단위, 자원 Y 120단위, 자원 Z 80단위를 어떻게 분배하여 최대 이익을 얻을 수 있는지 결정해야 합니다. 이 문제를 선형 프로그래밍 문제로 표현하면 다음과 같습니다.

목표 함수: 
$$maximize(3000A + 2000B + 4000C)$$


제약 조건:
- $3A + 2B + 4C  \le 100$
- $4A + B + 3C  \le 120$
- $2A + 3B + 2C \le 80$

변수가 2개인 연립일차부등식이라면 부등식의 영역 문제을 이용해 풀 수 있겠지만 실제 우리가 맞닥뜨릴 문제는 변수의 개수가 더 많고 복잡한 경우가 있어 펜과 종이만으로 해결하기는 어려운 감이 있습니다. 

## 선형 프로그래밍 문제의 해결법

이러한 선형 프로그래밍 문제를 해결하는 일반적인 방법은 **심플렉스 방법(Simplex Method)**입니다. 이 방법은 목표 함수의 값을 계속해서 증가시키거나 감소시키는 방식으로 최적의 해를 찾습니다.

문제를 다시 보겠습니다. 먼저, 이 문제를 표준형태로 바꾸어 보겠습니다. 선형 프로그래밍 문제를 표준형태로 바꾸기 위해, 각 제약 조건에 슬랙 변수(Slack variable)를 추가합니다. 슬랙 변수는 제약 조건이 등식으로 표현될 수 있게 하는 추가적인 변수입니다. 그래서 아래와 같은 형태로 문제를 다시 설정할 수 있습니다.

목표 함수:
$$maximize(3000A + 2000B + 4000C)$$

제약 조건:
- $3A + 2B + 4C + S_1 = 100$
- $4A + B + 3C + S_2 = 120$
- $2A + 3B + 2C + S_3 = 80$

### 초기 해 찾기
이제 초기 해를 찾습니다. 초기 해는 보통 슬랙 변수만을 고려하는 해로 선택합니다. 따라서 이 문제에서 초기 해는 A = 0, B = 0, C = 0, S1 = 100, S2 = 120, S3 = 80이 됩니다. 이 초기 해에 대한 목표 함수의 값은 0입니다.

### 비용 계수 계산
그 다음으로, 각 변수에 대한 비용 계수를 계산합니다. 이 비용 계수는 목표 함수의 각 항에서 해당 변수의 계수를 제외한 나머지 계수들의 합을 의미합니다. 이 경우, 비용 계수는 다음과 같이 계산됩니다.

비용 계수: A = 3000, B = 2000, C = 4000, S1 = 0, S2 = 0, S3 = 0

### 피벗 연산
비용 계수 중에서 가장 큰 값이 선택되어 피벗 열을 결정합니다. 이 경우, C의 비용 계수가 가장 크므로 C가 피벗 열이 됩니다. 다음으로, 각 제약 조건의 오른쪽 값(100, 120, 80)을 피벗 열의 값들로 나눠서 피벗 행을 결정합니다. 이 경우, 첫 번째 제약 조건에서 C의 계수로 100을 나눈 값이 가장 작으므로 첫 번째 제약 조건이 피벗 행이 됩니다. 따라서 피벗은 첫 번째 제약 조건의 C입니다.

### 새로운 테이블 생성
피벗을 기준으로 새로운 테이블을 생성합니다. 피벗 행의 모든 값을 피벗 값(4)로 나눕니다. 그리고 다른 행들은 피벗 열의 값을 0으로 만드는 연산을 수행합니다. 이 연산은 각 행에서 피벗 행을 빼는 것으로 수행됩니다.

### 반복
이제 새로운 테이블에서 비용 계수를 다시 계산하고, 다음 피벗을 찾아서 테이블을 업데이트합니다. 이 과정을 목표 함수의 값이 더 이상 증가하지 않을 때까지 반복합니다.

위 과정을 통해 선형 프로그래밍 문제의 최적해를 찾을 수 있습니다. 하지만 실제로는 이 과정이 매우 복잡하고 시간이 많이 소요될 수 있으므로, 대부분의 경우 컴퓨터 프로그램을 이용해서 이 과정을 자동화합니다.


## 교환비율 (Exchange Ratio)의 중요성
교환비율은 한 자원이 다른 자원으로 변환될 때의 비율을 의미합니다. 이 교환비율을 고려해야 하는 이유는 두 가지입니다.

첫째, 최적의 결정을 내리기 위해서입니다. 예를 들어, 기업은 한정된 자원을 가장 효과적으로 사용하여 이익을 최대화해야 합니다. 이때 어떤 자원을 다른 자원으로 교환할 것인지, 즉 어떤 자원을 얼마나 사용할 것인지 결정해야 합니다. 이런 결정을 내릴 때 교환비율을 고려하게 됩니다.

둘째, 공정한 거래를 위해서입니다. 교환비율은 거래에서 공정성을 보장하는 기준이 됩니다. 즉, 두 자원이 교환될 때 각자의 가치를 고려하여 합리적인 교환비율을 설정하게 되는데, 이는 거래의 공정성을 보장하는데 중요한 역할을 합니다.