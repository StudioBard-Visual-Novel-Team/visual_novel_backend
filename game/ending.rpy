# 임시 엔딩 - 3차 초안 이벤트 3 구간 종료
# 이후 스토리는 챕터 2 (학교 축제) 로 이어질 예정

label ending_summary:
    scene bg school_gate_sunset
    with fade
    play music "audio/title_music_1.mp3" fadein 2.0

    narrator "짧은 시간이었지만 남주는 세 사람과 조금씩 가까워졌다."
    narrator "누군가와는 우산을 나눠 썼고, 누군가와는 해안가를 걸었다."
    narrator "아직 방학까지는 시간이 남아 있다."

    scene black
    with fade
    pause 0.5

    # 호감도 요약
    centered "{size=+4}현재까지의 호감도{/size}\n\n서하린: [harin_affection]\n강연희: [yeonhee_affection]\n차유나: [yuna_affection]"
    with dissolve
    pause 3.0

    scene black
    with dissolve

    if harin_affection >= yeonhee_affection and harin_affection >= yuna_affection and harin_affection > 0:
        centered "{size=+3}가장 마음에 남은 사람: {color=#f7b8c9}서하린{/color}{/size}"
    elif yeonhee_affection >= harin_affection and yeonhee_affection >= yuna_affection and yeonhee_affection > 0:
        centered "{size=+3}가장 마음에 남은 사람: {color=#ffd977}강연희{/color}{/size}"
    elif yuna_affection >= harin_affection and yuna_affection >= yeonhee_affection and yuna_affection > 0:
        centered "{size=+3}가장 마음에 남은 사람: {color=#a3c8ff}차유나 선배{/color}{/size}"
    else:
        centered "{size=+3}아직 마음이 흔들릴 여지가 남아 있다.{/size}"
    with dissolve
    pause 3.0

    # 다음 챕터 예고 (학교 축제)
    scene bg festival
    with fade

    narrator "며칠 뒤."
    narrator "학교 곳곳에 축제 안내문이 붙기 시작했다."
    narrator "실습동 앞마당에는 부스 자리를 표시하는 흰 선이 그려졌고, 학생회는 분주해졌다."
    narrator "복도를 지나가는 사람들의 발걸음이 조금씩 들떠 있었다."

    p "(농업축제라… 여기선 어떤 걸 할지 조금 궁금하네.)"

    pause 1.0

    centered "{size=+6}다음 이야기{/size}\n\n{size=+2}챕터 2 – 농업축제{/size}"
    with dissolve
    pause 3.0

    scene bg festival
    with dissolve

    centered "{size=+8}To Be Continued...{/size}\n\n{size=-2}(3차 초안 · 이벤트 3까지의 데모 구간 종료){/size}"
    with dissolve
    pause 3.5

    return
