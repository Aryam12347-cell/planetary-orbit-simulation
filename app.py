import streamlit as st

st.set_page_config(
    page_title="SPACE MISSION",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
}

.stApp {
    background:
    radial-gradient(circle at 15% 20%, #192b59 0%, transparent 30%),
    radial-gradient(circle at 85% 70%, #30164d 0%, transparent 30%),
    #050b19;
    color: white;
}

header, footer {visibility: hidden;}

.hero {
    text-align: center;
    padding: 65px 20px 35px;
    border: 1px solid #28446e;
    border-radius: 25px;
    background: linear-gradient(135deg, #101e3b, #11132c);
    box-shadow: 0 0 35px #142d58;
}

.hero h1 {
    color: #8de3ff;
    font-size: 55px;
    font-weight: 900;
    letter-spacing: 4px;
}

.hero p {
    color: #c6d7f5;
    font-size: 19px;
}

.stButton > button {
    background: linear-gradient(90deg, #1769aa, #7446b8);
    color: white;
    border: 1px solid #75cfff;
    border-radius: 14px;
    height: 50px;
    font-weight: bold;
    width: 100%;
}

.card {
    background: #111d35;
    border: 1px solid #263f67;
    border-radius: 18px;
    padding: 22px 12px;
    text-align: center;
    min-height: 145px;
    margin-bottom: 12px;
}

.card h3 { color: #8de3ff; }
.card p { color: #c5d1e8; font-size: 14px; }

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div style="font-size:65px;">🚀</div>
    <h1>SPACE MISSION</h1>
    <p>مهمتك تبدأ من هنا ... اكتشف الكون، واستكشف الكواكب!</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("<h2 style='text-align:center;color:#8de3ff'>🌌 مركز قيادة المستكشفين</h2>",
            unsafe_allow_html=True)

if st.button("🚀 ابدأ المهمة"):
    st.session_state.started = True

if st.session_state.get("started", False):
    st.success("مرحبًا بك في رحلتك الفضائية! استعد للاستكشاف.")

st.write("")
st.markdown("<h3 style='text-align:center;color:white'>اختر وجهتك</h3>",
            unsafe_allow_html=True)

sections = [
    ("🪐", "استكشاف الكواكب", "اكتشف الكواكب وأسرارها"),
    ("🚀", "الرحلات الفضائية", "انطلق في رحلات بين الكواكب"),
    ("🌞", "محاكاة المدارات", "شاهد حركة الكواكب حول الشمس"),
    ("💻", "مختبر البرمجة الرياضية", "برمج مركبتك باستخدام Python"),
    ("🏆", "المهام والتحديات", "أنجز المهام واجمع النقاط"),
]

cols = st.columns(3)

for i, (emoji, title, description) in enumerate(sections):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card">
            <div style="font-size:35px">{emoji}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;color:#7186aa;margin-top:35px'>
SPACE MISSION | EXPLORE • PROGRAM • DISCOVER
</p>
""", unsafe_allow_html=True)
