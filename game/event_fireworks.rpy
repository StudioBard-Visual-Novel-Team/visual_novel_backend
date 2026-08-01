# 이벤트 씬 6.5 – 축제 후반, 불꽃놀이
# 이벤트 씬 6(메이드 카페)에서 선택한 히로인이 그대로 이어짐

label event_fireworks:
    scene bg school_fireworks
    with fade
    play music "audio/festival_music_2.mp3" fadein 2.0

    narrator "축제 후반, 운동장 방송에서 곧 불꽃놀이를 시작한다는 안내가 흘러나왔다."
    narrator "운동장 주변 조명이 하나씩 꺼졌다. 발사 직전의 짧은 정적이 내려앉자 학생들의 목소리도 자연스럽게 낮아졌다."
    narrator "어둠 속에서 불꽃이 올라가는 빛이 보였고, 조금 늦게 발사음이 운동장을 울렸다."

    $ fireworks_partner = maid_partner

    if maid_partner == "harin":
        jump fireworks_harin
    elif maid_partner == "yeonhee":
        jump fireworks_yeonhee
    elif maid_partner == "yuna":
        jump fireworks_yuna
    else:
        jump fireworks_end


# ---------- 서하린 루트 ----------
label fireworks_harin:
    narrator "하린은 사람이 적은 운동장 뒤쪽에서 기다리고 있었다."

    h "사람이 많아서 뒤쪽에 있었어요. 선배가 못 찾을까 봐 조금 걱정했는데…… 와주셨네요."
    p "찾아서 다행이야. 여기서 같이 보자."

    narrator "첫 불꽃이 실제로 하늘에서 터지는 순간, 하린의 얼굴 위로 밝은 빛이 번졌다."
    narrator "하린은 큰 소리에 어깨를 움츠렸다가 내 옆으로 조금 가까이 섰다."

    h "소리는 아직 놀라운데, 같이 보니까 괜찮아요."
    p "사람이 많아도 다음에는 내가 먼저 찾을게."

    narrator "하린은 하늘에서 시선을 떼지 않은 채 무심코 대답했다."

    h "그럼 다음에도 기다릴게요."

    narrator "하린은 뒤늦게 자신이 한 말의 의미를 알아차린 듯 입술을 살짝 다물었다. 하지만 말을 취소하거나 변명하지 않았다."
    narrator "첫 번째 불꽃의 잔광이 사라지고, 다음 불꽃을 준비하는 소리가 멀리서 들렸다."

    p "다음에도 오래 기다리게 하지는 않을게."

    narrator "하린은 작게 고개를 끄덕인 뒤 다시 하늘을 올려다봤다."

    $ harin_affection += 1

    jump fireworks_end


# ---------- 강연희 루트 ----------
label fireworks_yeonhee:
    play music "audio/Kang_yeonhee_bgm_1.mp3" fadein 2.0

    narrator "연희는 운동장 중앙에서 밝은 얼굴로 하늘을 바라보고 있었다. 내가 다가가자 말없이 옆자리를 비워줬다."
    narrator "첫 불꽃이 터지는 순간 연희의 눈이 크게 빛났다."

    y "와, 진짜 예쁘다."

    narrator "연희는 내 반응을 확인하려 하지 않고 불꽃이 번지는 모습을 끝까지 바라봤다."

    p "오늘은 조용히 보고 있네."
    y "무엇을 봤는지보다 누구랑 같이 있었는지가 중요하니까."

    narrator "연희는 말한 뒤 웃음으로 덮거나 장난을 덧붙이지 않았다. 대신 내 옆에서 같은 하늘을 바라봤다."
    narrator "첫 불꽃이 사라지자 잠시 어둠이 돌아왔고, 우리의 발소리와 숨소리만 가까이 들렸다."

    p "오늘은 오래 기억날 것 같아."
    y "나도. 누구랑 봤는지까지."

    $ yeonhee_affection += 1

    jump fireworks_end


# ---------- 차유나 루트 ----------
label fireworks_yuna:
    narrator "선배는 사람들보다 조금 떨어진 운동장 가장자리에 서 있었다."

    p "선배, 옆에 있어도 돼요?"
    sen "응. 여기서 봐."

    narrator "첫 불꽃이 터지는 순간 선배의 옆얼굴에 밝은 빛이 스쳤다."
    narrator "선배는 놀라지 않고 불꽃이 퍼지는 모양을 천천히 눈으로 따라갔다."

    p "학생회 일 때문에 여기 계신 거예요?"
    sen "아니. 일은 끝났어."
    p "일이 없어도요?"
    sen "일이 없어도."

    narrator "선배는 그 말의 의미를 설명하지 않았다. 나도 바로 고백이나 약속으로 정하지 않고, 옆에 머물렀다."
    narrator "첫 불꽃의 빛이 사라지고 다음 발사까지 짧은 어둠이 이어졌다."

    p "그럼 다음 불꽃도 여기서 같이 볼게요."
    sen "마음대로 해."

    narrator "허락과 다르지 않은 짧은 대답이 어둠 속에 남았다."

    $ yuna_affection += 1

    jump fireworks_end


# ---------- 불꽃놀이 이벤트 종료 ----------
label fireworks_end:
    stop music fadeout 2.0

    scene black
    with fade
    pause 1.0

    jump chapter3
