---
layout: post
title:  자기 자신을 만들어 내는식
date:   2023-08-14
categories: shorts
tags:
---
{% raw %}

여러분은 이 식이 어떤 의미를 갖고 있는지 아시나요?

$$\frac{1}{2} < \left\lfloor \mathrm{mod}\left(\left\lfloor \frac{y}{17}\right\rfloor 2^{-17\lfloor x\rfloor - \mathrm{mod}(\lfloor y\rfloor, 17)},2\right)\right\rfloor$$

이 식은 수학자 Jeff Tupper가 발표한 공식으로, 그래프를 통해 자기 자신을 그리는 놀라운 성질을 가지고 있습니다. 

python을 이용해 그림이 예쁘게 나올 수 있게 $x, y, k$값의 값을 설정한 후 그림을 그려보면

![Tupper's Self-Referential Formula : 자기참조 공식 (tistory.com)](https://blog.kakaocdn.net/dn/tyGie/btsrdjytUjg/nSjCKxBqcDm3YBbnu38x60/img.png)

```python
from math import floor

def tuppers_formula(x, y):
    return 0.5 < floor((y // 17 // 2 ** (17 * floor(x) + floor(y) % 17)) % 2)

k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719

for y in range(k, k+17):
    for x in range(105, -1, -1):
        if tuppers_formula(x, y):
            print('@', end='')
        else:
            print(' ', end='')
    print('')
```

출력화면이 처음 작성한 식과 같은 것을 알 수 있습니다.


{% endraw %}
