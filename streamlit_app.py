# app.py
import streamlit as st
import datetime
import time
import pandas as pd

# -------------------------------------------------
# Hulk Hogan ASCII Art (unchanged)
hulk_hogan_art = """

⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟨🟨🟥🟨🟨🟨🟥🟨🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟨🟨🟥🟨🟨🟨🟥🟨🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
🟥🟥🟥🟥🟥🟥🟥⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨⬜🟧🟧🟧🟧⬜⬜⬜ 
⬜⬜🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟨🟨🟧🟧🟧🟫🟫🟧🟧🟧🟧🟧🟫🟫🟨🟨🟨🟧🟧🟧🟧🟧🟧⬜⬜ 
⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟧🟧🟧🟧🟫🟫🟧🟧🟧🟫🟫🟧🟨🟨⬜🟧🟧🟧🟧🟧🟧🟧⬜ 
⬜⬜⬜🟥🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟨🟧🟧🟧🟧🟫🟧🟧🟧🟧🟧🟫🟧🟨🟨⬜🟧🟧🟧🟧🟧🟧🟧⬜ 
⬜🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨⬜🟧🟧🟧🟧🟧🟧🟨⬜ 
🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟧🟧🟧🟨⬜⬜🟨🟨🟨🟨🟨🟨🟧 
⬜⬜⬜🟨🟧🟧🟧🟧🟧🟧🟧🟨🟨🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟧🟧🟨⬜⬜🟧🟨🟨🟨🟨🟧🟧 
⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟧🟧🟨🟨🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟨🟧🟨🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧 
⬜⬜⬜🟧🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟨🟧🟧🟧🟨🟧🟧🟧🟧🟧🟨🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧 
⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧 
⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟧🟧🟧🟧🟧🟧🟧🟧 
⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟧🟧⬜ 
⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟧⬜⬜ 
⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧⬜🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬛⬛🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟨🟨⬛⬛⬛⬛🟧🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟧🟧🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟧🟧🟧🟧🟨🟨🟨🟧🟧🟧🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟧🟧⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜ 
⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜ 
⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜ 
⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜ 
🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜ 
⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜ 
⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜ 
⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜ 
⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 
"""

# -------------------------------------------------
# Define 24-hour buckets: 6 AM → 6 PM (Day) and 6 PM → 6 AM (Night)
day_buckets = [
    ("6-7",  datetime.time(6,  0), datetime.time(7,  0)),
    ("7-8",  datetime.time(7,  0), datetime.time(8,  0)),
    ("8-9",  datetime.time(8,  0), datetime.time(9,  0)),
    ("9-10", datetime.time(9,  0), datetime.time(10, 0)),
    ("10-11",datetime.time(10, 0), datetime.time(11, 0)),
    ("11-12",datetime.time(11, 0), datetime.time(12, 0)),
    ("12-1", datetime.time(12, 0), datetime.time(13, 0)),
    ("1-2",  datetime.time(13, 0), datetime.time(14, 0)),
    ("2-3",  datetime.time(14, 0), datetime.time(15, 0)),
    ("3-4",  datetime.time(15, 0), datetime.time(16, 0)),
    ("4-5",  datetime.time(16, 0), datetime.time(17, 0)),
    ("5-6",  datetime.time(17, 0), datetime.time(18, 0)),
]

night_buckets = [
    ("6-7",  datetime.time(18, 0), datetime.time(19, 0)),
    ("7-8",  datetime.time(19, 0), datetime.time(20, 0)),
    ("8-9",  datetime.time(20, 0), datetime.time(21, 0)),
    ("9-10", datetime.time(21, 0), datetime.time(22, 0)),
    ("10-11",datetime.time(22, 0), datetime.time(23, 0)),
    ("11-12",datetime.time(23, 0), datetime.time(0,  0)),
    ("12-1", datetime.time(0,  0), datetime.time(1,  0)),
    ("1-2",  datetime.time(1,  0), datetime.time(2,  0)),
    ("2-3",  datetime.time(2,  0), datetime.time(3,  0)),
    ("3-4",  datetime.time(3,  0), datetime.time(4,  0)),
    ("4-5",  datetime.time(4,  0), datetime.time(5,  0)),
    ("5-6",  datetime.time(5,  0), datetime.time(6,  0)),
]

def minutes(t: datetime.time) -> int:
    return t.hour * 60 + t.minute

def apportion(periods, buckets):
    y = [0.0] * len(buckets)
    c = [0.0] * len(buckets)

    for p in periods:
        start, finish, coils, yield_ = p['start'], p['finish'], p['coils'], p['yield']

        # Handle overnight wrap (e.g., 11 PM → 1 AM)
        if start >= finish:
            # Assume overnight: finish is next day
            finish_min = minutes(finish) + 24 * 60
        else:
            finish_min = minutes(finish)
        start_min = minutes(start)

        dur_min = finish_min - start_min
        if dur_min <= 0: continue
        dur_h = dur_min / 60.0

        rate_coils = coils / dur_h
        rate_yield = yield_ / dur_h

        for i, (_, b_start, b_end) in enumerate(buckets):
            # Convert bucket to minutes (with wrap handling)
            b_start_min = minutes(b_start)
            b_end_min = minutes(b_end)
            if b_start_min >= b_end_min:
                b_end_min += 24 * 60

            # Overlap in minutes
            o_start = max(start_min, b_start_min)
            o_end = min(finish_min, b_end_min)
            o_min = max(0, o_end - o_start)
            o_h = o_min / 60.0

            c[i] += o_h * rate_coils
            y[i] += o_h * rate_yield

    return y, c

# -------------------------------------------------
# Page Flow
if 'page' not in st.session_state:
    st.session_state.page = 'splash'

# ---------- SPLASH ----------
if st.session_state.page == 'splash':
    st.title("J money cash money coil yield distribution distributer")
    if st.button("Let's begin"):
        st.session_state.page = 'shift'
        st.rerun()

# ---------- CHOOSE SHIFT ----------
elif st.session_state.page == 'shift':
    st.header("Select Shift")
    shift = st.radio("Which shift are you tracking?", ["Day (6 AM - 6 PM)", "Night (6 PM - 6 AM)"])
    if st.button("Next"):
        st.session_state.shift = "day" if "Day" in shift else "night"
        st.session_state.page = 'targets'
        st.rerun()

# ---------- TARGETS ----------
elif st.session_state.page == 'targets':
    st.header("Set Hourly Targets")
    target_yield = st.number_input("Target Yield per hour", min_value=0.0, step=0.1)
    target_coils = st.number_input("Target Coils per hour", min_value=0.0, step=1.0)
    if st.button("Next"):
        st.session_state.target_yield = target_yield
        st.session_state.target_coils = target_coils
        st.session_state.page = 'loading'
        st.rerun()

# ---------- LOADING ----------
elif st.session_state.page == 'loading':
    st.write("Loading the ultimate coil calculator…")
    st.markdown(f"```{hulk_hogan_art}```")
    ph = st.empty()
    bar = "0" * 24
    for i in range(len(bar)//2 + 1):
        left = bar[:i]
        right = left[::-1]
        ph.text(left.center(len(bar)) + right)
        time.sleep(0.08)
    time.sleep(0.5)
    st.session_state.page = 'entry'
    st.rerun()

# ---------- DATA ENTRY ----------
elif st.session_state.page == 'entry':
    if 'periods' not in st.session_state:
        st.session_state.periods = []

    st.header("Add Production Periods")

    c1, c2, c3 = st.columns(3)
    with c1:
        sh = st.selectbox("Start Hour", list(range(1,13)), key='sh')
    with c2:
        sm = st.number_input("Start Min", 0,59,0, key='sm')
    with c3:
        sa = st.selectbox("Start AM/PM", ["AM","PM"], key='sa')

    c4, c5, c6 = st.columns(3)
    with c4:
        eh = st.selectbox("Finish Hour", list(range(1,13)), key='eh')
    with c5:
        em = st.number_input("Finish Min", 0,59,0, key='em')
    with c6:
        ea = st.selectbox("Finish AM/PM", ["AM","PM"], key='ea')

    coils = st.number_input("Coils Ran", min_value=0.0, step=1.0, format="%g")
    yield_ = st.number_input("Finished Yield", min_value=0.0, step=0.1)

    if st.button("Add Period"):
        # Convert to 24h
        start_h = sh if sa == "AM" else sh + 12
        if sh == 12: start_h = 0 if sa == "AM" else 12
        finish_h = eh if ea == "AM" else eh + 12
        if eh == 12: finish_h = 0 if ea == "AM" else 12

        period = {
            'start': datetime.time(start_h, sm),
            'finish': datetime.time(finish_h, em),
            'coils': coils,
            'yield': yield_
        }
        st.session_state.periods.append(period)
        st.success("Period added!")

    if st.session_state.periods:
        st.subheader("Recorded Periods")
        for i, p in enumerate(st.session_state.periods, 1):
            s = p['start'].strftime('%I:%M %p')
            f = p['finish'].strftime('%I:%M %p')
            if p['start'] >= p['finish']:
                f += " (next day)"
            st.write(f"**{i}.** {s} → {f} | Coils: {p['coils']} | Yield: {p['yield']}")

    if st.button("Calculate Results"):
        st.session_state.page = 'results'
        st.rerun()

# ---------- RESULTS ----------
elif st.session_state.page == 'results':
    st.header("Hourly Breakdown")

    buckets = day_buckets if st.session_state.shift == "day" else night_buckets
    shift_name = "Day Shift (6 AM - 6 PM)" if st.session_state.shift == "day" else "Night Shift (6 PM - 6 AM)"

    yields, coils = apportion(st.session_state.periods, buckets)

    df = pd.DataFrame({
        "Hour": [b[0] for b in buckets],
        "Yield": [round(y, 2) for y in yields],
        "Coils": [round(c, 1) for c in coils]
    })
    total_yield = round(sum(yields), 2)
    total_coils = round(sum(coils), 1)
    df.loc[len(df)] = ["**TOTAL**", total_yield, total_coils]

    def style_val(val, target, is_total=False):
        if is_total or val in ["", "**TOTAL**"]: return ""
        v = float(val)
        return f"color: {'red' if v < target else 'green' if v > target else 'black'}"

    styled = (df.style
              .applymap(lambda v: style_val(v, st.session_state.target_yield), subset=['Yield'])
              .applymap(lambda v: style_val(v, st.session_state.target_coils), subset=['Coils'])
              .format({"Yield": "{:.2f}", "Coils": "{:.1f}"})
              .set_properties(**{'text-align': 'center'}))

    st.subheader(shift_name)
    st.dataframe(styled, use_container_width=True)

    if st.button("Start Over"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.session_state.page = 'splash'
        st.rerun()
