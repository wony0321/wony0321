# LPS 테이블 만들기(라이브에서 2번째로 소개해준 내용)
# 접두와 접미 비교해가며 pattern 찾는 로직

def make_LPS(pattern):  # pattern은 비교대상 문자열
    M = len(pattern)
    LPS = [0] * M       # Longest proper prefix which is also suffix

    same_p_idx = 0  # 동일 패턴 인덱스
    idx = 1         # 패턴 체크 인덱스

    while idx < M:
        if pattern[same_p_idx] == pattern[idx]: # 같은 패턴을 가지고 있으면
            same_p_idx += 1                     # 같은 패턴을 발견해서 1증가
            LPS[idx] = same_p_idx               # 일치하는 인덱스가 존재해서 LPS 값 추가
            idx += 1                            # 다음 자리를 확인하기 위해 증가
        else:       # 일치하는 패턴이 없을 때
            if same_p_idx != 0:                 # 현재 동일 패턴이 있으면
                same_p_idx = LPS[same_p_idx-1]  # 패턴을 하나씩 줄이면서 동일 패턴이 있는지 확인
                # 이전 LPS 값을 이용해서 동일 패턴이 맞는지 확인
            else:
                LPS[idx] = 0                    # 일치하지 않기에 0
                idx += 1                        # 패턴 인덱스 1 증가

    return LPS
make_LPS('abcdabcef')   # [0, 0, 0, 0, 1, 2, 3, 0, 0]
make_LPS('AAACAAAA')    # [0, 1, 2, 0, 1, 2, 3, 3]


def KMP(P, T):  # P = pattern, T = target
    M = len(P)  # pattern (찾고자 하는 패턴 문장 짧은 문장)
    N = len(T)  # target (패턴이 있는지 확인하려는 긴 문장)
    LPS = make_LPS(P)   # LPS 테이블 만들기(전처리)

    p_idx = 0
    t_idx = 0

    while t_idx < N and p_idx < M:
        if P[p_idx] == T[t_idx]:   # 같은 문자인가?
            # 다음 문자를 체크
            p_idx += 1
            t_idx += 1
        else:
            if p_idx != 0:
                p_idx = LPS[p_idx - 1]    # 이전 값이 동일한 패턴의 갯수 (그만큼 비교하지 않고 패턴을 찾을 수 있음)
            t_idx += 1      # 처음부터 틀렸다면 t_idx만 하나 증가시키면 됨
    # 패턴과 일치하는 문자열이 있는지 확인
    if p_idx == M:  # 찾음
        # 찾은 문자열의 시작 인덱스 반환
        return t_idx - p_idx    # target의 시작 인덱스 나옴
    else:
        return -1
    # 함수에서는 되도록이면 return 타입을 맞추는 것이 좋음

target = 'XXXAAACAAAA'  # 3 예상
pattern = 'AAACAAAA'
result = KMP(pattern, target)
print(result)