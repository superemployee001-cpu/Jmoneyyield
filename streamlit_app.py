# app.py
import streamlit as st
from datetime import datetime, timedelta
import itertools
import random

st.set_page_config(page_title="J-Money Yield", layout="centered")

# === SPLASH PAGE ===
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.markdown(
        """
        <div style="text-align: center; padding: 50px;">
            <h1 style="font-size: 3em; color: #1E90FF; font-weight: bold;">
                J-money cash money yield distribution distributer
            </h1>
            <p style="font-size: 1.3em; color: #555;">
                The dopest yield splitter in the game 💸
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 START THE MONEY FLOW", use_container_width=True):
            st.session_state.started = True
            st.rerun()
    st.stop()

# === MAIN APP ===
st.markdown(
    "<h1 style='text-align: center; color: #1E90FF;'>J-MONEY YIELD DISTRIBUTOR</h1>",
    unsafe_allow_html=True
)

# === Inputs ===
col1, col2 = st.columns(2)
with col1:
    time_range = st.text_input("Time Range", "8am-5pm")
    total_yield = st.number_input("Total Yield", value=1250.0, step=1.0)
with col2:
    target_coils = st.number_input("Target Coils", value=9, min_value=1)
    target_weight = st.number_input("Target Weight", value=1200.0, step=1.0)

# === Job Tickets ===
st.subheader("Add Job Tickets (One Per Hour)")
job_cols = st.columns(3)
with job_cols[0]:
    job_ticket = st.text_input("Job #", placeholder="JT-1001", key="job_input")
with job_cols[1]:
    coil_weight = st.number_input("Coil Weight (lbs)", min_value=0.1, value=150.0, key="weight_input")
with job_cols[2]:
    add_btn = st.button("Add Job")

if 'jobs' not in st.session_state:
    st.session_state.jobs = []

if add_btn and job_ticket.strip():
    st.session_state.jobs.append((job_ticket.strip(), coil_weight))
    st.success(f"Added {job_ticket}")
    st.rerun()

# Show jobs
if st.session_state.jobs:
    st.write("**Current Jobs:**")
    for i, (j, w) in enumerate(st.session_state.jobs):
        cols = st.columns([1, 4, 2, 1])
        cols[0].write(f"**{i+1}.**")
        cols[1].write(f"`{j}`")
        cols[2].write(f"**{w} lbs**")
        if cols[3].button("❌", key=f"del_{i}"):
            st.session_state.jobs.pop(i)
            st.rerun()

    if st.button("🗑️ Clear All Jobs"):
        st.session_state.jobs = []
        st.rerun()

# === RUN BUTTON ===
if st.button("💰 RUN J-MONEY DISTRIBUTION", type="primary", use_container_width=True):
    try:
        # Parse time range
        start_str, end_str = [s.strip().lower() for s in time_range.split('-')]
        fmt = '%I%p' if any(x in start_str for x in ['am','pm']) else '%H'
        start = datetime.strptime(start_str, fmt)
        end = datetime.strptime(end_str, fmt)
        if end <= start:
            end += timedelta(days=1)
        hours = []
        cur = start
        while cur < end:
            hours.append(cur)
            cur += timedelta(hours=1)

        jobs = st.session_state.jobs
        if len(jobs) == 0:
            st.error("Add at least one job ticket!")
            st.stop()
        if len(jobs) != len(hours):
            st.error(f"Need **{len(hours)}** jobs (one per hour), got **{len(jobs)}**.")
            st.stop()

        rates = [w for _, w in jobs]
        total_rate = sum(rates)
        if total_rate == 0:
            st.error("Total coil weight can't be zero.")
            st.stop()

        per_coil_target = target_weight / target_coils
        total_allocated = 0
        results = []

        for (job, w), h in zip(jobs, hours):
            y = total_yield * w / total_rate
            total_allocated += y
            good = y >= per_coil_target
            results.append((h, job, w, y, good))

        # === RESULTS ===
        st.success(f"**DISTRIBUTION COMPLETE** – {len(results)} coils processed!")
        st.divider()

        green_count = sum(1 for _,_,_,_,g in results if g)
        st.markdown(f"### 🟢 **{green_count} GREEN BOXES** | 🔴 **{len(results)-green_count} RED**")

        for h, job, w, y, good in results:
            color = "🟢" if good else "🔴"
            pct = y / total_yield * 100
            st.markdown(
                f"**{h.strftime('%-I%p')}** | `{job}` | {w:.1f} lbs → **{y:.1f}** {color} **({pct:.1f}%)**"
            )

        # === SECRET OPTIMIZE ===
        with st.expander("Secret Mode: Optimize for MAX GREEN (Ctrl+Alt+O)"):
            if st.button("RUN OPTIMIZER"):
                best_green = -1
                best_order = None
                perms = [random.sample(jobs, len(jobs)) for _ in range(1000)] if len(jobs) > 7 else itertools.permutations(jobs)

                for perm in perms:
                    rs = [w for _, w in perm]
                    tr = sum(rs)
                    green = sum(1 for w in rs if total_yield * w / tr >= per_coil_target)
                    if green > best_green:
                        best_green = green
                        best_order = perm

                if best_order:
                    st.balloons()
                    st.success(f"**BEST ORDER: {best_green} GREEN BOXES!**")
                    for j, w in best_order:
                        st.write(f"→ `{j}` ({w} lbs)")
                    if st.button("Use This Order"):
                        st.session_state.jobs = list(best_order)
                        st.rerun()
                else:
                    st.info("No better order found.")

    except Exception as e:
        st.error(f"Error: {e}")

# === Footer ===
st.markdown("---")
st.caption("Made with 💸 by J-Money | Add to Home Screen for App Mode!")
