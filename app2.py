import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

st.set_page_config(
    page_title="SPACE MISSION",
    page_icon="🚀",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "home"

if "points" not in st.session_state:
    st.session_state.points = 0

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
    padding: 45px 15px;
    border: 1px solid #28446e;
    border-radius: 25px;
    background: linear-gradient(135deg, #101e3b, #11132c);
}
.hero h1 {
    color: #8de3ff;
    font-size: 48px;
    font-weight: 900;
}
.hero p {color: #c6d7f5; font-size: 18px;}
.card {
    background: #111d35;
    border: 1px solid #31558a;
    border-radius: 18px;
    padding: 15px;
    text-align: center;
}
h1, h2, h3 {color: #8de3ff;}
.stButton > button {
    background: linear-gradient(90deg, #1769aa, #7446b8);
    color: white;
    border: 1px solid #75cfff;
    border-radius: 12px;
    min-height: 48px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)


def go_home():
    st.session_state.page = "home"


def page_title(title, description):
    st.markdown(f"<h1 style='text-align:center'>{title}</h1>",
                unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;color:#c6d7f5'>{description}</p>",
                unsafe_allow_html=True)
    st.button("⬅️ العودة إلى الواجهة الرئيسية", on_click=go_home)
    st.divider()


# الواجهة الرئيسية
if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <div style="font-size:60px">🚀</div>
        <h1>SPACE MISSION</h1>
        <p>مهمتك تبدأ من هنا ... اكتشف الكون، واستكشف الكواكب!</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center'>🌌 مركز قيادة المستكشفين</h2>",
                unsafe_allow_html=True)

    st.markdown("<h3 style='text-align:center;color:white'>اختر وجهتك</h3>",
                unsafe_allow_html=True)

    sections = [
        ("🪐", "استكشاف الكواكب", "planets"),
        ("🚀", "الرحلات الفضائية", "journeys"),
        ("🌞", "محاكاة المدارات", "orbits"),
        ("💻", "مختبر البرمجة الرياضية", "lab"),
        ("🏆", "المهام والتحديات", "challenges")
    ]

    cols = st.columns(3)

    for i, (emoji, title, key) in enumerate(sections):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <div style="font-size:40px">{emoji}</div>
                <h3>{title}</h3>
            </div>
            """, unsafe_allow_html=True)

            if st.button("افتح القسم", key=f"open_{key}"):
                st.session_state.page = key
                st.rerun()

    st.markdown(
        f"<h3 style='text-align:center'>🏅 نقاط المستكشف: {st.session_state.points}</h3>",
        unsafe_allow_html=True
    )


# القسم الأول: استكشاف الكواكب
elif st.session_state.page == "planets":

    page_title("🪐 استكشاف الكواكب", "تعرف على كواكب المجموعة الشمسية")

    planets = {
        "عطارد": "أقرب الكواكب إلى الشمس، ويتميز بصغر حجمه.",
        "الزهرة": "ثاني كواكب المجموعة الشمسية، وله غلاف جوي كثيف.",
        "الأرض": "كوكبنا، ويتميز بوجود الماء والحياة.",
        "المريخ": "يعرف بالكوكب الأحمر بسبب لون سطحه.",
        "المشتري": "أكبر كواكب المجموعة الشمسية.",
        "زحل": "يشتهر بحلقاته الجميلة.",
        "أورانوس": "كوكب عملاق جليدي ويميل محوره بشكل كبير.",
        "نبتون": "أبعد الكواكب عن الشمس."
    }

    selected = st.selectbox("اختر كوكبًا:", list(planets.keys()))

    st.markdown(f"""
    <div class="card">
        <h2>🪐 {selected}</h2>
        <p>{planets[selected]}</p>
    </div>
    """, unsafe_allow_html=True)


# القسم الثاني: الرحلات الفضائية
elif st.session_state.page == "journeys":

    page_title("🚀 الرحلات الفضائية", "اختر وجهة رحلتك الافتراضية")

    planet_names = ["عطارد", "الزهرة", "الأرض", "المريخ",
                    "المشتري", "زحل", "أورانوس", "نبتون"]

    distances = {
        "عطارد": 0.39, "الزهرة": 0.72, "الأرض": 1.00,
        "المريخ": 1.52, "المشتري": 5.20, "زحل": 9.58,
        "أورانوس": 19.2, "نبتون": 30.05
    }

    destination = st.selectbox("إلى أي كوكب تريد الذهاب؟", planet_names)

    if st.button("🚀 انطلق في الرحلة"):
        st.success(f"تم تحديد وجهتك: كوكب {destination}")
        st.info(
            f"متوسط بُعد {destination} عن الشمس هو "
            f"{distances[destination]} وحدة فلكية."
        )
        st.caption("هذه رحلة تعليمية افتراضية وليست محاكاة لمسار حقيقي.")


# القسم الثالث: محاكاة المدارات
elif st.session_state.page == "orbits":

    page_title("🌞 محاكاة المدارات", "شاهد نموذجًا مبسطًا لحركة الكواكب حول الشمس")

    angle = st.slider("غيّر زاوية حركة الكواكب:", 0, 360, 45)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_facecolor("#071126")
    fig.patch.set_facecolor("#071126")

    ax.scatter(0, 0, color="yellow", s=350, label="الشمس")

    orbit_data = [
        ("عطارد", 1.0, "#aaaaaa"),
        ("الزهرة", 1.5, "#e5b56b"),
        ("الأرض", 2.1, "#42a5f5"),
        ("المريخ", 2.7, "#e57373")
    ]

    theta = np.linspace(0, 2 * np.pi, 300)

    for name, radius, color in orbit_data:
        ax.plot(radius*np.cos(theta), radius*np.sin(theta),
                color=color, alpha=0.5)

        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))

        ax.scatter(x, y, color=color, s=90, label=name)

    ax.set_aspect("equal")
    ax.legend(facecolor="#15233d", labelcolor="white")
    ax.set_title("نموذج المدارات حول الشمس", color="white")
    ax.tick_params(colors="white")
    st.pyplot(fig)
    st.info("غيّري زاوية الحركة ولاحظي تغيّر مواقع الكواكب في النموذج.")


# القسم الرابع: مختبر البرمجة الرياضية
elif st.session_state.page == "lab":

    page_title("💻 مختبر البرمجة الرياضية",
               "تحكمي بمركبة افتراضية باستخدام مفاهيم Python")

    speed = st.slider("سرعة المركبة الافتراضية:", 1, 20, 5)
    direction = st.slider("زاوية الاتجاه:", 0, 360, 45)
    time = st.slider("زمن المحاكاة:", 1, 10, 3)

    if st.button("احسب حركة المركبة"):

        radians = math.radians(direction)

        x = speed * math.cos(radians) * time
        y = speed * math.sin(radians) * time

        distance = math.sqrt(x**2 + y**2)

        st.success("تم تنفيذ المحاكاة الافتراضية!")

        c1, c2, c3 = st.columns(3)
        c1.metric("الموقع الأفقي", f"{x:.2f}")
        c2.metric("الموقع الرأسي", f"{y:.2f}")
        c3.metric("المسافة", f"{distance:.2f}")

        st.write("رسم مسار المركبة:")

        fig, ax = plt.subplots()
        ax.plot([0, x], [0, y], marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("المسار الافتراضي للمركبة")
        ax.grid(True)
        st.pyplot(fig)

        st.caption(
            "استخدمنا الدوال المثلثية والجذر التربيعي من مكتبة math."
        )


# القسم الخامس: المهام والتحديات
elif st.session_state.page == "challenges":

    page_title("🏆 المهام والتحديات", "اختبر معلوماتك الفضائية")

    st.write("**السؤال الأول:** ما أكبر كواكب المجموعة الشمسية؟")

    answer = st.radio(
        "اختر الإجابة:",
        ["الأرض", "المشتري", "المريخ", "عطارد"],
        key="quiz_answer"
    )

    if st.button("تحقق من الإجابة"):
        if answer == "المشتري":
            st.success("إجابة صحيحة! أحسنت 👏")
            if not st.session_state.get("quiz_done", False):
                st.session_state.points += 10
                st.session_state.quiz_done = True
        else:
            st.error("حاول مرة أخرى!")

    st.write(f"🏅 مجموع نقاطك: {st.session_state.points}")
