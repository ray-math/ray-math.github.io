---
layout: post
title:  모든 것을 알기위한 열쇠, 독립
date:   2023-08-11
categories: scripts
tags:
---
{% raw %}

**독립**이라는 단어는 일상적인 언어에서 "서로 관련이 없다"라는 의미로 사용되곤 합니다. 하지만 그 의미 때문에 확률과 통계에서 독립의 개념을 배울 때 한 사건이 다른 사건과 아무런 관련이 없음을 의미한다고 착각하기 쉽습니다. 하지만 수학에서 독립은 한 사건의 발생이 다른 사건의 발생 확률에 영향을 미치지 않는 것을 의미합니다. 다시 말해, 어떤 조건에서든지 확률이 일정하게 유지되는 성질이죠.

두 사건 $A$와 $B$가 독립이라는 개념을 조건부 확률식을 이용해 나타내면

$$ P(A \vert B) = P(A) $$

라 할 수 있습니다. $A$가 일어날 확률은 $B$가 일어난다고 해도 바뀌지 않는다는 거죠, 따라서 $A$와 $B$가 독립이라면 증명하지 않아도 아래 식들 또한 자명해집니다.

$$\begin{align*}
P(A \vert B^c) = P(A)\\
P(B \vert A) = P(B)\\
P(B \vert A^c) = P(B)\\ 
\end{align*}$$

이 개념을 처음 접하는 학생들은 문제에 바로 적용하기에는 어려움이 있어 학교에서는 조건부 확률의 성질을 이용해 필요충분조건인 식을 가르치죠.  

$$\begin{align*}
&P(A|B) = P(A) \\
&\Rightarrow \frac{P(A \cap B)}{P(B)} = P(A) \left( \because P(A|B) = \frac{P(A \cap B)}{P(B)} \right)\\
&\Rightarrow P(A \cap B) = P(A) \cdot P(B) 
\end{align*}$$

그래서 독립이란 교집합을 곱셈으로 구할 수 있다 정도로만 생각하고 끝내기 쉽상입니다. 하지만 이러한 식은 독립이 갖고 있는 의미를 전혀 반영하지 못합니다. 독립은 하나의 변수가 다른 변수에 미치는 영향을 고려하지 않아도 되므로, 분석을 단순화할 수 있다는 큰 장점이 있습니다. 표본들이 독립이라는 가정 하에, 평균, 분산 등의 통계량을 추정하기 용이하여 모집단에 대한 일반화가 가능하죠.

## 독립개념을 확장하기
우선 독립의 필요충분 조건을 다시 보도록 하겠습니다.  이 식 자체로도 굉장히 깔끔하지만 저는 이 식의 변수를 조금 줄여보도록 하겠습니다. 

$$P(A \cap B) = P(A) \cdot P(B)$$ 

확률의 정의를 사용하면 전체 사건 $S$에 대해 각각의 확률을 집합의 원소의 수를 이용해 정의할 수 있습니다.

$$
\begin{align*}
P(A) &= \frac{n(A)}{n(S)} \\
P(B) &= \frac{n(B)}{n(S)} \\
P(A \cap B) &= \frac{n(A \cap B)}{n(S)}
\end{align*}
$$

이제 두 사건 $A$와 $B$가 독립이므로 독립의 필요충분조건 식에 확률을 대입한 후에 양변에 전체 사건의 경우의 수$n(S)$를 곱하여 정리하면 $n(S)$에 대한 식을 얻을 수 있습니다.

$$\begin{align*}
\frac{n(A \cap B)}{n(S)} &= \left( \frac{n(A)}{n(S)} \right) \cdot \left( \frac{n(B)}{n(S)} \right) \\
\Rightarrow n(A) \cdot n(B) &= n(A \cap B) \cdot n(S) \\
\Rightarrow \frac{n(A) \cdot n(B)}{n(A \cap B)} &= n(S)
\end{align*}$$

예를 들어보죠. $1$부터 $8$까지의 카드가 있을 때, 집합$A$와 $B$를 다음과 같이 정의하겠습니다.

- $A=\{ 1,2,3,4\}$
- $B=\{3,4,5,6\}$
  
이 두 집합은 독립일까요? 

#### 확률을 이용한 독립성 확인
확률을 계산하면 $P(A)$와 $P(B)$의 곱이 $P(A \cap B)$와 같으므로 독립이라고 할 수 있습니다.

$$\begin{align*}
P(A) &= \frac{n(A)}{n(S)} = \frac{4}{8} = \frac{1}{2} \\
P(B) &= \frac{n(B)}{n(S)} = \frac{4}{8} = \frac{1}{2} \\
P(A \cap B) &= \frac{n(A \cap B)}{n(S)} = \frac{2}{8} = \frac{1}{4}
\end{align*}$$

#### 비율을 이용한 독립성 확인
또는 $A$가 일어날 확률은 전체의 절반이고 $B$안에서나 밖에서나 이러한 확률값이 변함없이 비율이 일정하게 유지되므로 독립이라고 할 수도 있죠.

$$\begin{align*}
P(A|B) &= \frac{P(A \cap B)}{P(B)} = \frac{n(A \cap B)}{n(B)} = \frac{2}{4}= \frac{1}{2} = P(A) \\
P(A|B^c) &= \frac{P(A \cap B^c)}{P(B^c)} =  \frac{n(A \cap B^c)}{n(B)} = \frac{2}{4}= \frac{1}{2} = P(A)
\end{align*}$$

#### 전체 경우의 수로 확인
아니면 방금 유도한 공식을 이용해 전체 사건의 경우의 수를 유도하는 공식에 대입해 독립성을 판단해도 좋습니다.

$$\frac{n(A) \cdot n(B)}{n(A \cap B)} = \frac{4 \times 4}{2} = 8 = n(S)$$

어떤 경우를 사용해도 독립이라는 성질은 변함이 없죠.


## 일부를 이용해 전체를 유도하는 방법
앞서 보았듯 독립이란 조건을 이용하면 집합 $A$와 $B$만으로도 전체 사건의 경우의 수 즉, 전체 집합의 원소의 개수를 구할 수 있습니다. 예를 들어보죠. 

$$n(S)=\frac{n(A) \cdot n(B)}{n(A \cap B)} $$

코드 작성은 어려운 작업 중 하나입니다. 특히 복잡한 프로젝트에서는 수많은 줄의 코드가 얽혀 있으며, 그 중 하나라도 잘못되면 전체 시스템이 작동하지 않을 수 있죠. 이런 상황에서 모든 오류를 찾는 것은 정말 어려운 일입니다. 만약 $10$만 줄의 복잡한 코드가 실행되지 않는 상황이 발생했다고 해보겠습니다. 프로그래머 두 명, A와 B가 이 문제를 해결하기 위해 A는 코드의 앞부분을, B는 뒷부분을 분석하기로 했습니다. 두 프로그래머는 각각 자신의 부분에서 오류를 찾을 것입니다. A는 $50$개의 오류를 발견했고, B는 $40$개의 오류를 발견했습니다. 다행히 두 프로그래머가 분석한 부분에 중복되는 영역이 있었고, 이 중복 영역에서 둘 다 발견한 오류는 $10$개였습니다. 여기서 우리는 독립성을 사용할 수 있습니다. 두 프로그래머의 작업은 독립적이므로, 오류 발견은 독립 사건으로 볼 수 있습니다.

$$ n(S) = \frac{n(A) \cdot n(B)}{n(A \cap B)} = \frac{50 \times 40}{10} = 200 $$

따라서 A가 발견한 오류와 B가 발견한 오류를 곱하고, 그 결과를 둘 다 발견한 오류로 나누면 결과적으로 전체 코드에서의 오류 개수는 $200$개로 추정할 수 있습니다. 여기서 한 발 더 나아가 보겠습니다. 현재 발견한 코드의 오류 개수는 중복 영역에서 발견한 오류를 한 번만 세어야 하므로 합집합 개념을 이용해 표현할 수 있습니다.

$$ n(A \cup B) = 50 + 40 - 10 = 80 $$

A와 B가 현재 발견한 오류의 개수는 총 $80$개이고 따라서 두 프로그래머가 앞으로 전체 코드에서 발견해야 할 오류의 개수가 $120$개 라는 것을 정확하게 파악할 수 있습니다.

$$ n((A \cup B)^c)=n(S) - n(A \cup B) = 200 - 80 = 120 $$

이 과정을 일반화 해보죠. 먼저 전체 오류의 개수와 현재 발견한 오류의 개수를 구하는 식은 다음과 같이 정의했습니다.

$$ n(S) = \frac{n(A) \cdot n(B)}{n(A \cap B)} $$
$$ n(A \cup B) = n(A) + n(B) - n(A \cap B) $$

앞으로 찾아야 할 오류의 개수는 합집합의 여집합이므로 계산하는 식에 위의 두 식을 대입할 수 있습니다.

$$ n((A \cup B)^c) = n(S) - n(A \cup B) = \frac{n(A) \cdot n(B)}{n(A \cap B)} - (n(A) + n(B) - n(A \cap B)) $$

두 프로그래머가 찾은 오류 중 중복되지 않은 오류의 개수를 각각 $n(A - B)$와 $n(B - A)$로 표현하고, 둘 다 찾은 오류의 개수를 $n(A \cap B)$로 표현하면, 앞으로 찾아야 할 오류의 개수는 다음과 같이 계산됩니다

$$\begin{align*}
n((A \cup B)^c) &= \frac{n(A) \cdot n(B) - n(A \cap B) \cdot (n(A) + n(B) - n(A \cap B))}{n(A \cap B)} \\
&= \frac{n(A) \cdot n(B) - n(A \cap B) \cdot n(A) - n(A \cap B) \cdot n(B) + (n(A \cap B))^2}{n(A \cap B)} \\
&= \frac{n(A) \cdot n(B) - n(A) \cdot n(A \cap B) - n(B) \cdot n(A \cap B) + n(A \cap B) \cdot n(A \cap B)}{n(A \cap B)} \\
&= \frac{(n(A) - n(A \cap B)) \cdot (n(B) - n(A \cap B))}{n(A \cap B)}\\
&= \frac{(n(A- B)) \cdot (n(B-A))}{n(A \cap B)}
\end{align*}$$

이렇게 정리된 식을 통해 앞으로 찾아야 할 오류의 개수를 계산할 수 있습니다. 만약 A와 B와 각각 자신들만 찾은 오류가 많고, 둘 다 찾아낸 오류의 개수가 작다면, 여전히 많은 오류가 남아 있을 것이라는 것을 알 수 있습니다. 또한 이 식에는 두 프로그래머가 얼마나 오류를 잘 찾아내는지 몰라도 독립적이라는 성질만으로 꽤 정확한 추측을 할 수 있음을 보여주죠.

## 포획-재포획법
자연의 세계에서는 종종 숨겨진 것들을 발견하고 이해하려는 노력이 필요합니다. 그리고 앞서 소개한 방법은 포획-재포획법이라 불리는 방법으로 독립이라는 성질을 이용해 전체 사례를 추정할 수 있게하죠. 

한 예를 더 들어보겠습니다. 특정 질병의 발병률을 정확하게 파악하는 것은 그 질병의 예방과 치료에 있어 중요한 역할을 합니다. 하지만 실제로는 모든 환자를 대상으로 검사하기 어려운 경우가 많습니다. 이런 상황에서 두 개의 독립된 검사 방법을 사용하여 질병의 실제 발병률을 추정하는 방법을 살펴보겠습니다.

먼저, 검사 방법 A와 B를 도입해보겠습니다. 검사 방법 A는 특정 지역의 환자 중 $100$명을 대상으로 질병을 진단하고, $30$명이 양성 판정을 받았다고 가정해봅시다. 검사 방법 B도 동일한 지역의 환자 중 $100$명을 대상으로 질병을 진단하고, $25$명이 양성 판정을 받았다고 해봅시다. 두 검사 방법이 중복되는 환자가 있을 수 있으며, 이 중복 영역에서 둘 다 양성 판정을 받은 환자는 $10$명이라고 가정하겠습니다.

이제 두 검사 방법의 독립성을 이용하여 전체 발병률을 추정해보겠습니다. 포획-재포획법을 사용하여 전체 발병률을 계산하면 다음과 같이 됩니다.

$$\begin{align*}
n(S) &= \frac{30 \times 25}{10} = 75\\
n((A \cup B)^c) &= \frac{(30 - 10) \cdot (25 - 10)}{10} = 30
\end{align*}$$

이 수식은 전체 환자 중 질병에 걸린 환자의 수가 $75$명임을 추정하게 해줍니다. 또한, 각 검사 방법에서만 양성 판정을 받은 환자의 수를 계산하면 현재까지 발견된 환자 수는 $45$명이고, 앞으로 찾아야 할 환자 수는 $30$명임을 의미합니다. 이러한 추정을 통해 의료진은 진단과 치료 계획을 더 효과적으로 수립할 수 있습니다. 특정 질병의 실제 발병률을 추정하는 것은 어려운 과제지만, 독립을 이용하면 단순화하고 정확한 추정을 할 수 있게 해줍니다.

이 방법은 두 개 이상의 독립된 시장 조사를 통해 특정 제품의 잠재 고객 수나 특정 지역의 소비자 행동을 분석하거나 독립된 데이터를 활용하여 누락된 정보나 알려지지 않은 정보를 예측할 수도 있습니다. 독립은 이처럼 다양한 분야에서 복잡한 문제를 해결하는 강력한 도구로 자리 잡았습니다. 여러분도 일상에서 독립된 정보를 통해 더 정확한 판단을 내릴 수 있는데 도움이 되길 바랍니다. 
{% endraw %}