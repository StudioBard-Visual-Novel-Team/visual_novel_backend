# 에필로그 – 방학식
# 7월 초 여름 방학식 → 해피 엔딩 3종 or 공통 새드 엔딩

label epilogue:
    scene black
    with fade
    centered "{size=+6}에필로그{/size}\n\n방학식"
    with dissolve
    pause 1.5

    scene bg classroom
    with fade

    "7월 초 여름 방학식"

    narrator "교실 안은 평소보다 들떠 있었다."
    narrator "누군가는 방학 계획을 이야기했고, 누군가는 실습 당번표를 확인했다."

    t "다들 한 학기 고생했다. 방학이라고 너무 풀어지지 말고, 실습 당번 있는 학생들은 일정 꼭 확인해라."

    narrator "방학식이 끝났다는 말과 함께 의자 끄는 소리가 이어졌다."
    narrator "나는 가방을 정리하며 며칠 전 공동 실습 평가를 떠올렸다."
    narrator "기울어진 화분을 함께 바로 세웠던 일. 잘못 꽂힌 이름표를 발견하고 처음부터 다시 확인했던 일. 고장 난 관수 장치를 나누어 점검했던 일."
    narrator "같은 과제를 했지만 누구와 함께했는지에 따라 남은 기억은 전혀 달랐다."
    narrator "그날 이후 마음 한쪽에 남아 있던 말이 있었다."

    if ending_promise_partner == "harin":
        jump ending_harin_happy
    elif ending_promise_partner == "yeonhee":
        jump ending_yeonhee_happy
    elif ending_promise_partner == "yuna":
        jump ending_yuna_happy
    else:
        jump ending_common_sad


# ---------- 서하린 해피 엔딩 「기다릴 수 있는 약속」 ----------
label ending_harin_happy:
    scene bg practice_room
    with fade

    narrator "방학식이 끝난 뒤 나는 하린이 말한 온실로 향했다."
    narrator "문을 열자 하린은 공동 실습 평가 때 함께 바로 세운 방울토마토 화분 앞에서 기다리고 있었다."

    show harin neutral at center
    with dissolve

    p "기다렸어?"
    h "조금요. 그래도 오늘은 제가 기다리겠다고 말한 거니까요."

    narrator "나는 하린 옆에 섰다. 기울어졌던 줄기는 새 지지대를 따라 곧게 서 있었다."

    h "평가 이후에 문제가 생기면 바로 기록했어요. 혼자 괜찮다고 넘기지 않고, 담당 선생님께도 말씀드렸고요."
    p "이제 먼저 말할 수 있게 됐네."

    narrator "하린은 잠시 잎 끝을 바라봤다."

    h "아직도 무서워요. 가까워진 사람이 떠날까 봐 걱정되는 것도 그대로예요."
    h "그래도 오늘은 기다리기만 하지 않으려고 선배를 불렀어요."

    narrator "그 말을 듣고 나도 더는 미룰 수 없다는 생각이 들었다."

    p "하린아."
    h "네."
    p "나는 너를 좋아해."

    narrator "하린의 손이 멈췄다. 나는 하린의 눈을 피하지 않고 말을 이었다."

    p "네가 힘든 걸 혼자 숨기지 않았으면 좋겠고, 좋은 일이 생기면 나한테도 먼저 알려줬으면 해."
    p "방학이 시작돼도 계속 만나고 싶어."

    narrator "하린은 놀란 표정으로 나를 바라봤다. 하지만 이번에는 시선을 피하지 않았다."

    h "저도 선배를 좋아해요."
    h "그래서 오늘 만나자고 했어요. 선배가 같은 마음이 아니어도, 이번에는 제 마음을 말하려고 했어요."
    p "내가 조금 먼저 말했네."

    narrator "하린은 작게 웃었다."

    p "다음 실습 당번 끝나고 해안가 도로 같이 걷자. 내가 먼저 연락할게."
    h "네. 기다릴게요."

    narrator "이번 기다림은 불안해서 혼자 견디는 기다림이 아니었다."
    narrator "다시 만날 날짜와, 먼저 연락하겠다는 약속이 있는 기다림이었다."

    hide harin
    with dissolve
    scene black
    with fade
    pause 1.0

    centered "{size=+4}― 서하린 해피 엔딩 ―{/size}\n\n「기다릴 수 있는 약속」"
    with dissolve
    pause 4.0

    jump ending_credits


# ---------- 강연희 해피 엔딩 「웃지 않아도 닿은 마음」 ----------
label ending_yeonhee_happy:
    scene bg classroom
    with fade

    narrator "방학식이 끝난 뒤에도 나는 자리에 남았다."
    narrator "교실에 있던 학생들이 하나둘 빠져나가고, 마지막으로 뒷문이 닫혔다."

    show yeonhee neutral at center
    with dissolve

    narrator "연희는 앞쪽 책상에 기대 서 있다가 나를 바라봤다."

    y "진짜 기다렸네."
    p "네가 기다리라고 했잖아."

    narrator "연희는 평소처럼 장난스럽게 웃으려 했다. 하지만 곧 그 웃음을 조금 내려놓았다."

    y "오늘은 장난처럼 넘기지 않으려고."

    narrator "연희는 내 앞자리 의자를 돌려 앉았다."

    y "공동 실습 평가 때 내가 실수했어도, 그게 내가 한 일을 전부 없애는 건 아니었잖아."
    y "네가 그렇게 말해 줘서 조금 알 것 같았어."
    p "뭘?"
    y "계속 웃기지 않아도, 계속 반응을 확인하지 않아도 괜찮을 때가 있다는 거."

    narrator "연희는 손끝으로 책상 모서리를 가볍게 두드렸다. 이번에는 내 표정을 살피며 말을 바꾸지 않았다."
    narrator "나는 잠시 숨을 고른 뒤 연희를 바라봤다."

    p "그러면 내가 먼저 말해도 돼?"

    narrator "연희는 조용히 고개를 끄덕였다."

    p "연희야. 나 너 좋아해."
    p "밝게 웃고 장난칠 때만이 아니라, 아무 말 없이 있을 때도 같이 있고 싶어."
    p "방학이 시작돼도 계속 만나고 싶어."

    narrator "연희는 한동안 아무 말 없이 나를 바라봤다. 그러다 천천히 웃었다."

    y "나도 너 좋아해. 오늘 부른 것도 그 말을 하려고 한 거야."
    y "근데 네가 먼저 말했네."
    p "미안. 순서 뺏었어?"
    y "아니. 나쁘지 않았어."

    narrator "연희는 자리에서 일어나 창밖을 바라봤다."

    y "방학 되면 다들 흩어지잖아. 그래서 조금 신경 쓰였어."
    p "그럼 방학 첫 주에 해안가 도로 같이 걷자. 날짜 정해서 내가 연락할게."
    y "재미있는 계획 없어도 괜찮아?"
    p "그냥 같이 걷고 싶어서 만나자는 거야."

    narrator "연희는 그 말을 듣고 편안하게 웃었다."

    y "응. 연락 기다릴게."

    narrator "둘 사이에 잠시 침묵이 생겼다. 하지만 이번에는 어느 쪽도 그 빈틈을 급하게 채우지 않았다."

    hide yeonhee
    with dissolve
    scene black
    with fade
    pause 1.0

    centered "{size=+4}― 강연희 해피 엔딩 ―{/size}\n\n「웃지 않아도 닿은 마음」"
    with dissolve
    pause 4.0

    jump ending_credits


# ---------- 차유나 해피 엔딩 「일이 없어도 이어지는 약속」 ----------
label ending_yuna_happy:
    scene bg classroom
    with fade

    narrator "방학식이 끝난 뒤 나는 학생회실로 향했다."
    narrator "문을 두드리자 안에서 선배의 목소리가 들렸다."

    sen "들어와."

    show yuna neutral at center
    with dissolve

    narrator "학생회실 책상 위에는 서류가 거의 없었다. 평소라면 회의록이나 축제 자료가 펼쳐져 있었을 자리였다."

    p "오늘은 정말 할 일이 없네요."
    sen "없다고 했잖아."

    narrator "선배는 창가에서 돌아서며 나를 바라봤다."

    sen "일이 없는데도 너와 따로 만나고 싶었어. 그래서 방학식까지 기다리라고 한 거야."

    narrator "나는 공동 실습 평가 때를 떠올렸다. 혼자 전부 확인하려던 선배가, 처음으로 내게 일부를 맡겼던 날이었다."

    p "선배."
    sen "응."
    p "저는 선배를 좋아해요."

    narrator "선배는 아무 말 없이 내 말을 기다렸다."

    p "도와드릴 일이 있을 때만이 아니라, 아무 이유 없이도 만나고 싶어요."
    p "방학 중에도 제가 먼저 연락해도 될까요?"

    narrator "선배는 잠시 시선을 내렸다. 그리고 다시 나를 바라봤다."

    sen "그 말을 들으려고 부른 건 아닐 텐데. 듣고 싶었던 것 같아."

    narrator "선배의 목소리는 평소처럼 차분했다. 하지만 그 안에는 숨기지 못한 떨림이 조금 있었다."

    sen "나도 너를 좋아해."
    sen "일을 맡길 수 있어서가 아니라, 네가 옆에 있는 게 편해서 만나고 싶어."
    p "그럼 다음에는 선배가 일을 만들지 않아도 되겠네요."
    sen "처음부터 보고 싶다고 연락하는 건 아직 익숙하지 않아."
    p "이번에는 제가 먼저 할게요."

    narrator "나는 휴대전화를 꺼내 일정표를 확인했다."

    p "다음 주에 시간 되는 날 알려주세요. 제가 연락해서 만나자고 할게요."
    sen "어디서?"
    p "학생회실 말고 해안가 도로에서요."

    narrator "선배는 짧게 고개를 끄덕였다."

    sen "연락 기다릴게."

    narrator "이번에는 업무도, 실습도, 맡은 역할도 없었다."
    narrator "그저 서로를 만나기 위한 약속만 남아 있었다."

    hide yuna
    with dissolve
    scene black
    with fade
    pause 1.0

    centered "{size=+4}― 차유나 해피 엔딩 ―{/size}\n\n「일이 없어도 이어지는 약속」"
    with dissolve
    pause 4.0

    jump ending_credits


# ---------- 공통 새드 엔딩 「기다리라는 말이 없던 날」 ----------
label ending_common_sad:
    scene bg classroom
    with fade

    narrator "방학식이 끝나자 학생들이 하나둘 교실을 빠져나갔다."
    narrator "나는 가방을 정리한 뒤 잠시 자리에 남았다."
    narrator "혹시 누군가가 나를 부르거나, 끝나고 기다려 달라고 했던 말을 다시 떠올리게 될 것 같았다."
    narrator "하지만 그런 약속은 없었다."
    narrator "온실에서 기다리겠다는 사람도 없었고, 교실에 남아달라고 한 사람도 없었다. 학생회실로 와달라는 말 역시 듣지 못했다."
    narrator "나는 휴대전화를 꺼냈다."
    narrator "하린과 연희, 선배의 이름이 연락처에 남아 있었다."
    narrator "내가 먼저 메시지를 보내면 만날 수도 있을 것이다."
    narrator "하지만 그동안 누군가가 보여준 마음을 확신할 만큼 가까워지지는 못했다."
    narrator "상대가 마음을 열려고 할 때 나는 안전한 말만 골랐다."
    narrator "한 걸음 더 다가갈 수 있었던 순간에도, 나는 애매한 거리를 남겨두었다."
    narrator "이제 와서 갑자기 좋아한다고 말하는 것이 내 감정만 앞세우는 일처럼 느껴졌다."
    narrator "결국 아무에게도 메시지를 보내지 못했다."

    scene bg coastal_road
    with fade

    narrator "교문을 나서자 여름이라 해는 아직 완전히 기울지 않았다."
    narrator "하늘에는 낮의 푸른빛이 남아 있었고, 해안가 도로 위로 따뜻한 바람이 불었다."
    narrator "누군가와 함께 이 길을 걸었던 기억은 분명했다."
    narrator "하지만 다음에 다시 만나자는 약속은 하나도 남아 있지 않았다."
    narrator "나는 다시 휴대전화를 확인했다. 새로운 메시지는 오지 않았다."
    narrator "잠시 빈 입력창을 바라보다가 화면을 껐다."
    narrator "말하지 않은 마음은 상대에게 전해지지 않는다."
    narrator "그리고 충분히 가까워지지 못한 관계에서는, 고백할 기회조차 자연스럽게 생기지 않았다."
    narrator "나는 혼자 해안가 도로를 걸었다."
    narrator "이번 여름에는 기다려 달라고 말해준 사람도, 내가 기다려주겠다고 약속한 사람도 없었다."

    scene black
    with fade
    pause 1.0

    centered "{size=+4}― 공통 새드 엔딩 ―{/size}\n\n「기다리라는 말이 없던 날」"
    with dissolve
    pause 4.0

    jump ending_credits


# ---------- 엔딩 종료 ----------
label ending_credits:
    scene black
    with fade

    centered "{size=+8}너에게 물주는 법{/size}\n\n{size=-2}― END ―{/size}"
    with dissolve
    pause 4.0

    return
