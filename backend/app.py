
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import calendar as cal
import random

st.set_page_config(page_title="근무 스케줄러", layout="wide")
st.title("📅 자동 근무 스케줄 생성기")

st.sidebar.header("입력 조건")
year = st.sidebar.number_input("📆 연도", min_value=2023, max_value=2100, value=datetime.now().year)
month = st.sidebar.selectbox("월 선택", list(range(1, 13)), index=datetime.now().month - 1)

people_input = st.sidebar.text_area("👥 전체 인원 (쉼표로 구분)", "윤, 수, 희, 차, 세, 송, 다, 아, 현, 지")
mandatory_input = st.sidebar.text_input("📌 매일 포함되어야 할 인원 (쉼표)", "윤, 수, 희, 차")

extra_input = st.sidebar.text_area("🔥 추가 근무 가능자 (이름:횟수, 쉼표로 구분)", "윤:2, 수:2, 희:2, 차:2, 지:2, 현:2, 세:1, 송:1, 다:1, 아:1")
vacation_input = st.sidebar.text_area("🏖️ 휴무 요청 (이름-날짜, 줄바꿈 구분)", "윤-5,6,10,11\n수-17,18,29\n희-11,12")

submit = st.sidebar.button("✅ 스케줄 생성")

def generate_schedule(year, month, people, mandatory, extra, vacations):
    days_in_month = cal.monthrange(year, month)[1]
    dates = [datetime(year, month, day) for day in range(1, days_in_month + 1)]
    available_days = {name: set(range(1, days_in_month + 1)) for name in people}
    person_schedule = {name: [] for name in people}
    extra_limit = {name: int(count) for name, count in extra.items()}
    extra_used = {name: 0 for name in people}

    for name, days in vacations.items():
        for day in days:
            if day in available_days.get(name, set()):
                available_days[name].remove(day)

    schedule = {}
    for date in dates:
        date_str = date.strftime('%Y-%m-%d')
        assigned = []

        random.shuffle(mandatory)
        for m in mandatory:
            if date.day in available_days[m] and len(assigned) < 2:
                assigned.append(m)
                person_schedule[m].append(date.day)

        candidates = [p for p in people if p not in assigned and date.day in available_days[p]]
        random.shuffle(candidates)
        for p in candidates:
            if len(assigned) >= 6:
                break
            prev_days = person_schedule[p][-2:]
            if prev_days and all(date.day - d <= 1 for d in prev_days):
                if len(prev_days) == 2:
                    if extra_used[p] >= extra_limit.get(p, 1):
                        continue
                    extra_used[p] += 1
            assigned.append(p)
            person_schedule[p].append(date.day)

        schedule[date_str] = assigned

    return schedule

if submit:
    people = [p.strip() for p in people_input.split(',') if p.strip()]
    mandatory = [m.strip() for m in mandatory_input.split(',') if m.strip()]
    extra = {e.split(':')[0].strip(): e.split(':')[1].strip() for e in extra_input.split(',') if ':' in e}
    vacations = {}
    for line in vacation_input.splitlines():
        if '-' in line:
            name, days = line.split('-')
            vacations[name.strip()] = [int(d.strip()) for d in days.split(',') if d.strip().isdigit()]

    schedule = generate_schedule(year, month, people, mandatory, extra, vacations)
    df = pd.DataFrame.from_dict(schedule, orient='index')
    df.columns = [f"근무자{i+1}" for i in range(df.shape[1])]
    st.subheader("✅ 생성된 스케줄")
    st.dataframe(df)
    st.download_button("📥 엑셀로 저장", df.to_csv(index=True).encode('utf-8-sig'), file_name=f"{year}_{month}_스케줄.csv")
