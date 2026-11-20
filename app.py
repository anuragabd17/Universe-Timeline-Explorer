
import streamlit as st
st.title("HELLO EARTH TEST 🌍")
from timeline import calculate_cosmic_day
from galaxy3d import create_galaxy
from planet_view import create_planet_scene
import streamlit.components.v1 as components
from solar_system import create_solar_system

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Universe Timeline Explorer",
    page_icon="🌌",
    layout="wide"
)

# ---------------- ANIMATED SPACE DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(ellipse at 20% 20%, #20134b 0%, transparent 40%),
        radial-gradient(ellipse at 80% 70%, #102c50 0%, transparent 40%),
        #050816;
    color: white;
}

/* Hide default Streamlit decoration */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Headings */

.hero-title {
    text-align: center;
    font-size:  fifty;
    font-size: 52px;
    font-weight: 900;
    background: linear-gradient(90deg, #8be9fd, #bd93f9, #ff79c6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 3s ease-in-out infinite alternate;
    margin-top: 30px;
}

.hero-subtitle {
    text-align: center;
    color: #c6c8e8;
    font-size: 18px;
    margin-bottom: 35px;
}

@keyframes glow {
    from { filter: drop-shadow(0 0 5px #8b5cf6); }
    to { filter: drop-shadow(0 0 22px #38bdf8); }
}

/* Animated stars */

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-image:
        radial-gradient(2px 2px at 20px 30px, white, transparent),
        radial-gradient(2px 2px at 150px 100px, #a78bfa, transparent),
        radial-gradient(1px 1px at 300px 200px, white, transparent),
        radial-gradient(2px 2px at 400px 50px, #38bdf8, transparent),
        radial-gradient(1px 1px at 500px 300px, white, transparent);
    background-size: 550px 350px;
    opacity: 0.45;
    animation: stars 35s linear infinite;
}

@keyframes stars {
    from { transform: translateY(0); }
    to { transform: translateY(-350px); }
}

/* Event cards */

.event-card {
    background: linear-gradient(145deg, #151d3b, #10152b);
    border: 1px solid #51418b;
    border-radius: 18px;
    padding: 22px;
    margin: 10px 0;
    min-height: 175px;
    transition: all 0.35s ease;
    animation: appear 0.8s ease both;
}

.event-card:hover {
    transform: translateY(-8px) scale(1.02);
    border-color: #a78bfa;
    box-shadow: 0 0 25px #7545c766;
}

.event-number {
    color: #a78bfa;
    font-size: 13px;
    letter-spacing: 2px;
}

.event-card h3 {
    color: #ffffff;
    margin: 12px 0;
}

.event-card p {
    color: #b8c0dd;
    font-size: 14px;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Detail panel */

.detail-box {
    background: linear-gradient(135deg, #1b2250, #121a35);
    border: 1px solid #8065d8;
    border-radius: 18px;
    padding: 25px;
    animation: appear 0.6s ease;
    line-height: 1.8;
}

.detail-box h2 {
    color: #c4b5fd;
}

.small-label {
    color: #a5b4fc;
    letter-spacing: 2px;
    font-size: 12px;
    font-weight: bold;
}

div[data-testid="stMetric"] {
    background: #151d38;
    border: 1px solid #51418b;
    padding: 18px;
    border-radius: 15px;
}

.stSelectbox label {
    color: #c4b5fd !important;
    font-weight: bold;
}

/* METEOR SHOWER ANIMATION */

/* BRIGHT CINEMATIC METEOR SHOWER */

.meteor-layer {
    position: fixed;
    inset: 0;
    overflow: hidden;
    pointer-events: none;
    z-index: 1;
}

.meteor {
    position: absolute;
    top: -25%;
    width: 4px;
    height: 160px;

    background: linear-gradient(
        to bottom,
        transparent,
        #7dd3fc,
        #ffffff,
        #ffffff
    );

    border-radius: 50%;
    opacity: 0;
    transform: rotate(45deg);

    filter:
        drop-shadow(0 0 5px #38bdf8)
        drop-shadow(0 0 12px #ffffff);

    animation: meteor-fall 3.5s linear infinite;
}

.meteor:nth-child(1) {
    left: 15%;
    animation-delay: 0s;
}

.meteor:nth-child(2) {
    left: 35%;
    animation-delay: 1.2s;
}

.meteor:nth-child(3) {
    left: 55%;
    animation-delay: 2.4s;
}

.meteor:nth-child(4) {
    left: 75%;
    animation-delay: 0.7s;
}

.meteor:nth-child(5) {
    left: 95%;
    animation-delay: 1.8s;
}

@keyframes meteor-fall {
    0% {
        transform: translate(0, 0) rotate(45deg);
        opacity: 0;
    }

    10% {
        opacity: 1;
    }

    65% {
        opacity: 0.9;
    }

    100% {
        transform: translate(-65vw, 110vh) rotate(45deg);
        opacity: 0;
    }
}

/* Keep website content above the meteors */

.stMainBlockContainer {
    position: relative;
    z-index: 2;
}


/* CINEMATIC BIG BANG EXPLOSION */

.bigbang-overlay {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    pointer-events: none;
    overflow: hidden;
    animation: explosion-fade 3s ease-out forwards;
    background: radial-gradient(
        circle at center,
        rgba(255,255,255,0.95) 0%,
        rgba(150,100,255,0.65) 8%,
        rgba(30,80,180,0.3) 25%,
        transparent 65%
    );
}

.bigbang-core {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: white;
    box-shadow:
        0 0 25px 15px white,
        0 0 70px 35px #a78bfa,
        0 0 130px 65px #38bdf8;
    transform: translate(-50%, -50%);
    animation: core-explode 2.5s ease-out forwards;
}

.bigbang-ring {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 30px;
    height: 30px;
    border: 5px solid #d8b4fe;
    border-radius: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 35px #a78bfa;
    animation: ring-expand 2.4s ease-out forwards;
}

.bigbang-particle {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #ffffff;
    box-shadow: 0 0 15px #60a5fa;
    animation: particle-burst 2.5s ease-out forwards;
}

@keyframes core-explode {
    0% { transform: translate(-50%, -50%) scale(0.1); opacity: 1; }
    25% { transform: translate(-50%, -50%) scale(7); opacity: 1; }
    100% { transform: translate(-50%, -50%) scale(35); opacity: 0; }
}

@keyframes ring-expand {
    0% { width: 20px; height: 20px; opacity: 1; }
    100% { width: 120vw; height: 120vw; opacity: 0; }
}

@keyframes particle-burst {
    0% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    100% { transform: translate(
        calc(-50% + var(--x)),
        calc(-50% + var(--y))
    ) scale(0.2); opacity: 0; }
}

@keyframes explosion-fade {
    0% { opacity: 1; }
    35% { opacity: 1; }
    100% { opacity: 0; }
}

@media (prefers-reduced-motion: reduce) {
    .bigbang-overlay,
    .bigbang-overlay * {
        animation-duration: 0.01ms !important;
    }
}
/* BIG BANG CINEMATIC ANIMATION */

.bigbang-overlay {
    position: fixed;
    inset: 0;
    z-index: 9999;
    pointer-events: none;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: bangFade 4s ease-out forwards;
}

.bigbang-core {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: white;
    box-shadow:
        0 0 30px white,
        0 0 80px #a855f7,
        0 0 150px #38bdf8;
    animation: coreBlast 2s ease-out forwards;
}

.bigbang-ring {
    position: absolute;
    width: 20px;
    height: 20px;
    border: 5px solid white;
    border-radius: 50%;
    box-shadow: 0 0 35px #a855f7;
    animation: ringBlast 3s ease-out forwards;
}

@keyframes coreBlast {
    0% { transform: scale(0.1); opacity: 1; }
    35% { transform: scale(8); opacity: 1; }
    100% { transform: scale(0.1); opacity: 0; }
}

@keyframes ringBlast {
    0% { transform: scale(0.1); opacity: 1; }
    100% { transform: scale(90); opacity: 0; }
}

@keyframes bangFade {
    0% { background: rgba(255,255,255,0.9); }
    20% { background: rgba(100,40,180,0.2); }
    100% { background: transparent; }
}

/* FIRST STARS FORMATION */

.stars-overlay {
    position: fixed;
    inset: 0;
    z-index: 9998;
    pointer-events: none;
    background: radial-gradient(
        circle,
        rgba(20, 15, 65, 0.35),
        transparent 75%
    );
    animation: starBackground 5s ease-out forwards;
}

.new-star {
    position: absolute;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #fff8c7;
    box-shadow:
        0 0 10px #fff,
        0 0 25px #ffd76a,
        0 0 55px #60a5fa;
    opacity: 0;
    animation: starAppear 2s ease-in-out infinite alternate;
}

.star-one { top: 25%; left: 20%; animation-delay: 0s; }
.star-two { top: 65%; left: 75%; animation-delay: 0.5s; }
.star-three { top: 35%; left: 60%; animation-delay: 1s; }
.star-four { top: 75%; left: 30%; animation-delay: 1.5s; }
.star-five { top: 45%; left: 85%; animation-delay: 2s; }
.star-six { top: 18%; left: 80%; animation-delay: 2.5s; }

@keyframes starAppear {
    0% {
        opacity: 0;
        transform: scale(0.2);
    }
    100% {
        opacity: 1;
        transform: scale(2.5);
    }
}

@keyframes starBackground {
    0% { opacity: 0; }
    30% { opacity: 1; }
    100% { opacity: 0; }
}

/* CINEMATIC COSMIC DAWN */

.cosmic-dawn-overlay {
    position: fixed;
    inset: 0;
    z-index: 9998;
    pointer-events: none;
    overflow: hidden;
    background:
        radial-gradient(ellipse at 50% 55%,
        rgba(30, 20, 75, 0.15),
        rgba(2, 4, 18, 0.92) 85%);
    animation: dawnScene 9s ease-in-out forwards;
}

.dawn-nebula {
    position: absolute;
    width: 85vw;
    height: 65vh;
    left: 7.5vw;
    top: 20vh;
    border-radius: 50%;
    background:
        radial-gradient(ellipse at 35% 50%,
        rgba(62, 91, 180, 0.45),
        transparent 48%),
        radial-gradient(ellipse at 65% 45%,
        rgba(120, 48, 145, 0.38),
        transparent 52%),
        radial-gradient(ellipse at 50% 65%,
        rgba(205, 130, 75, 0.25),
        transparent 45%);
    filter: blur(35px);
    opacity: 0;
    transform: scale(0.55);
    animation: nebulaFormation 8s ease-out forwards;
}

.dawn-core {
    position: absolute;
    top: 48%;
    left: 50%;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #ffffff;
    box-shadow:
        0 0 15px 5px rgba(255,255,255,0.9),
        0 0 45px 18px rgba(160,190,255,0.8),
        0 0 100px 45px rgba(100,120,255,0.4);
    opacity: 0;
    transform: scale(0);
    animation: firstStarIgnition 7s ease-out forwards;
}

.dawn-core::after {
    content: "";
    position: absolute;
    width: 170px;
    height: 170px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(
        circle,
        rgba(255,245,205,0.35),
        rgba(120,150,255,0.12) 35%,
        transparent 72%
    );
}

.dawn-horizon {
    position: absolute;
    bottom: -25%;
    left: 0;
    width: 100%;
    height: 60%;
    background: radial-gradient(
        ellipse at 50% 50%,
        rgba(90,105,205,0.25),
        rgba(65,35,120,0.12) 40%,
        transparent 72%
    );
    opacity: 0;
    animation: cosmicLight 8s ease-out forwards;
}

@keyframes dawnScene {
    0% { opacity: 0; }
    15% { opacity: 1; }
    75% { opacity: 1; }
    100% { opacity: 0; }
}

@keyframes nebulaFormation {
    0% {
        opacity: 0;
        transform: scale(0.55) rotate(-10deg);
    }
    35% {
        opacity: 0.9;
        transform: scale(1) rotate(5deg);
    }
    75% {
        opacity: 0.8;
        transform: scale(1.15) rotate(12deg);
    }
    100% {
        opacity: 0;
        transform: scale(1.35);
    }
}

@keyframes firstStarIgnition {
    0%, 35% {
        opacity: 0;
        transform: scale(0);
    }
    48% {
        opacity: 1;
        transform: scale(1);
    }
    65% {
        opacity: 1;
        transform: scale(1.5);
    }
    100% {
        opacity: 0;
        transform: scale(2.2);
    }
}

@keyframes cosmicLight {
    0%, 35% { opacity: 0; }
    65% { opacity: 1; }
    100% { opacity: 0; }
}

/* CINEMATIC BIG BANG */

.bigbang-cinema {
    position: fixed;
    inset: 0;
    z-index: 9999;
    overflow: hidden;
    pointer-events: none;
    background: radial-gradient(
        circle at center,
        #17102f 0%,
        #080817 48%,
        #01020a 100%
    );
    animation: bbScene 9s ease-out forwards;
}

.bb-flash {
    position: absolute;
    inset: 0;
    background: radial-gradient(
        circle at center,
        white 0%,
        rgba(190,205,255,0.9) 5%,
        rgba(105,90,220,0.35) 22%,
        transparent 60%
    );
    opacity: 0;
    animation: bbFlash 2s ease-out forwards;
}

.bb-singularity {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: white;
    box-shadow:
        0 0 25px 10px white,
        0 0 70px 30px #a5b4fc,
        0 0 140px 65px #7c3aed;
    transform: translate(-50%, -50%) scale(0);
    animation: bbIgnite 3s ease-out forwards;
}

.bb-wave {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 24px;
    height: 24px;
    border: 2px solid rgba(190,195,255,0.9);
    border-radius: 50%;
    transform: translate(-50%, -50%) scale(0.1);
    box-shadow: 0 0 25px rgba(130,120,255,0.8);
    animation: bbExpand 5s ease-out forwards;
}

.bb-wave.wave-two {
    animation-delay: 0.55s;
    border-color: rgba(255,190,140,0.8);
}

.bb-cloud {
    position: absolute;
    width: 100vw;
    height: 75vh;
    top: 12vh;
    left: 0;
    background:
        radial-gradient(ellipse at 35% 50%,
        rgba(85,95,220,0.38), transparent 45%),
        radial-gradient(ellipse at 65% 45%,
        rgba(150,65,190,0.32), transparent 48%),
        radial-gradient(ellipse at 50% 60%,
        rgba(235,150,100,0.18), transparent 50%);
    filter: blur(35px);
    opacity: 0;
    transform: scale(0.3);
    animation: bbCloudExpand 8s ease-out forwards;
}

.bb-particle {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #fff;
    box-shadow: 0 0 12px 4px #a5b4fc;
    opacity: 0;
    animation: bbParticle 4s ease-out forwards;
}

.bb-particle.p1 { --x: -42vw; --y: -30vh; }
.bb-particle.p2 { --x: 40vw; --y: -25vh; }
.bb-particle.p3 { --x: -35vw; --y: 32vh; }
.bb-particle.p4 { --x: 43vw; --y: 30vh; }
.bb-particle.p5 { --x: 5vw; --y: -42vh; }
.bb-particle.p6 { --x: -8vw; --y: 42vh; }
.bb-particle.p7 { --x: 25vw; --y: 12vh; }
.bb-particle.p8 { --x: -25vw; --y: -12vh; }

@keyframes bbScene {
    0% { opacity: 0; }
    8% { opacity: 1; }
    75% { opacity: 1; }
    100% { opacity: 0; }
}

@keyframes bbFlash {
    0% { opacity: 0; }
    12% { opacity: 1; }
    35% { opacity: 0.35; }
    100% { opacity: 0; }
}

@keyframes bbIgnite {
    0% { transform: translate(-50%,-50%) scale(0); opacity: 0; }
    20% { transform: translate(-50%,-50%) scale(2); opacity: 1; }
    55% { transform: translate(-50%,-50%) scale(0.5); opacity: 1; }
    100% { transform: translate(-50%,-50%) scale(0); opacity: 0; }
}

@keyframes bbExpand {
    0% { transform: translate(-50%,-50%) scale(0.1); opacity: 1; }
    100% { transform: translate(-50%,-50%) scale(90); opacity: 0; }
}

@keyframes bbCloudExpand {
    0% { opacity: 0; transform: scale(0.3); }
    35% { opacity: 1; transform: scale(1); }
    75% { opacity: 0.8; transform: scale(1.35); }
    100% { opacity: 0; transform: scale(1.7); }
}

@keyframes bbParticle {
    0% {
        opacity: 0;
        transform: translate(0,0) scale(0);
    }
    20% { opacity: 1; }
    100% {
        opacity: 0;
        transform: translate(var(--x),var(--y)) scale(1.5);
    }
}

</style>
""", unsafe_allow_html=True)


# ---------------- METEOR SHOWER ----------------

st.markdown("""
<div class="meteor-layer">
    <div class="meteor"></div>
    <div class="meteor"></div>
    <div class="meteor"></div>
    <div class="meteor"></div>
    <div class="meteor"></div>
</div>
""", unsafe_allow_html=True)


# ---------------- COSMIC EVENTS ----------------

universe_age = 13.8e9

events = [
    {
        "name": "The Big Bang",
        "emoji": "💥",
        "age": 13.8e9,
        "time": "13.8 billion years ago",
        "description": "The universe began expanding from an extremely hot and dense state. Space itself started expanding.",
        "fact": "The Big Bang was not an explosion into empty space. It was the expansion of space itself."
    },
    {
        "name": "First Atoms",
        "emoji": "⚛️",
        "age": 13.8e9 - 380000,
        "time": "380,000 years after the Big Bang",
        "description": "The universe cooled enough for electrons and nuclei to combine into neutral atoms. Light could travel freely through space.",
        "fact": "The oldest light we can observe today is called the Cosmic Microwave Background."
    },
    {
        "name": "First Stars",
        "emoji": "✨",
        "age": 13.6e9,
        "time": "Around 200 million years after the Big Bang",
        "description": "The first stars formed from clouds of hydrogen and helium. Their cores began producing heavier elements.",
        "fact": "Stars helped create many of the elements needed for planets and life."
    },
    {
        "name": "First Galaxies",
        "emoji": "🌌",
        "age": 13.3e9,
        "time": "Early universe",
        "description": "Gravity brought stars, gas and dark matter together to form the first galaxies.",
        "fact": "Galaxies contain enormous collections of stars, gas, dust and dark matter."
    },
    {
        "name": "Milky Way Develops",
        "emoji": "🌠",
        "age": 13.2e9,
        "time": "Over 13 billion years ago",
        "description": "Our home galaxy began forming and gradually developed into the huge spiral galaxy we know today.",
        "fact": "The Milky Way contains hundreds of billions of stars."
    },
    {
        "name": "Solar System",
        "emoji": "☀️",
        "age": 4.6e9,
        "time": "4.6 billion years ago",
        "description": "The Sun and planets began forming from a rotating cloud of gas and dust.",
        "fact": "The Solar System formed from the same cloud of material."
    },
    {
        "name": "Earth Forms",
        "emoji": "🌍",
        "age": 4.54e9,
        "time": "4.54 billion years ago",
        "description": "Earth formed as rocky material gradually collided and joined together around the young Sun.",
        "fact": "Earth is approximately 4.54 billion years old."
    },
    {
        "name": "Life on Earth",
        "emoji": "🧬",
        "age": 3.5e9,
        "time": "At least 3.5 billion years ago",
        "description": "Evidence of early life shows that simple organisms existed on Earth billions of years ago.",
        "fact": "All known life on Earth shares a common evolutionary history."
    },
    {
        "name": "Present Day",
        "emoji": "🚀",
        "age": 0,
        "time": "Today",
        "description": "Humans explore the universe using telescopes, spacecraft and scientific discoveries.",
        "fact": "The universe is still expanding!"
    }
]


# ---------------- HERO SECTION ----------------

st.markdown(
    '<div class="hero-title">🌌 UNIVERSE TIMELINE EXPLORER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">A Journey Through 13.8 Billion Years of Cosmic History</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown(
    '<p class="small-label">✦ THE STORY OF EVERYTHING</p>',
    unsafe_allow_html=True
)

st.header("Explore the Cosmic Timeline")

st.write(
    "Travel through the most important events in the history of our universe."
)


# ---------------- EVENT CARDS ----------------

for i in range(0, len(events), 3):

    columns = st.columns(3)

    for j, column in enumerate(columns):

        index = i + j

        if index < len(events):

            event = events[index]

            with column:

                st.markdown(f"""
                <div class="event-card">
                    <div class="event-number">EVENT {index + 1:02d}</div>
                    <h3>{event['emoji']} {event['name']}</h3>
                    <p>{event['time']}</p>
                </div>
                """, unsafe_allow_html=True)


# ---------------- EVENT SELECTION ----------------

st.divider()

st.markdown(
    '<p class="small-label">✦ DISCOVER THE UNIVERSE</p>',
    unsafe_allow_html=True
)

st.header("Explore an Event")

event_names = [event["name"] for event in events]

selected_name = st.selectbox(
    "Choose a cosmic event",
    event_names
)

selected_event = next(
    event for event in events
    if event["name"] == selected_name
)




# COSMIC EVENT ANIMATIONS

if "previous_event" not in st.session_state:
    st.session_state.previous_event = None


if selected_name != st.session_state.previous_event:

    if "big bang" in selected_name.lower():
        st.markdown("""
        <div class="bigbang-cinema">
            <div class="bb-flash"></div>
            <div class="bb-cloud"></div>
            <div class="bb-singularity"></div>
            <div class="bb-wave"></div>
            <div class="bb-wave wave-two"></div>
            <div class="bb-particle p1"></div>
            <div class="bb-particle p2"></div>
            <div class="bb-particle p3"></div>
            <div class="bb-particle p4"></div>
            <div class="bb-particle p5"></div>
            <div class="bb-particle p6"></div>
            <div class="bb-particle p7"></div>
            <div class="bb-particle p8"></div>
        </div>
        """, unsafe_allow_html=True)

    elif "first stars" in selected_name.lower():
        st.markdown("""
        <div class="cosmic-dawn-overlay">
            <div class="dawn-nebula"></div>
            <div class="dawn-core"></div>
            <div class="dawn-horizon"></div>
        </div>
        """, unsafe_allow_html=True)

    elif "first atoms" in selected_name.lower():
        st.markdown("""
        <style>
        .atom-scene {
            height: 280px;
            background: radial-gradient(circle, #14254d, #03040c);
            border-radius: 18px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .atom-container {
            position: relative;
            width: 130px;
            height: 130px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .atom {
            width: 35px;
            height: 35px;
            background: #58d8ff;
            border-radius: 50%;
            box-shadow: 0 0 35px #58d8ff;
        }

        .electron {
            position: absolute;
            width: 13px;
            height: 13px;
            background: white;
            border-radius: 50%;
            animation: atomOrbit 2s linear infinite;
        }

        @keyframes atomOrbit {
            from { transform: rotate(0deg) translateX(55px); }
            to { transform: rotate(360deg) translateX(55px); }
        }
        </style>

        <div class="atom-scene">
            <div class="atom-container">
                <div class="atom"></div>
                <div class="electron"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        
    
    
    elif "first galaxies" in selected_name.lower():
        st.markdown("""
        <style>
        .galaxy-scene {
            height: 380px;
            width: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 18px;
            background: #02040b;
            isolation: isolate;
        }

        .galaxy-photo {
            position: absolute;
            inset: -3%;
            background-image: url("https://commons.wikimedia.org/wiki/Special:FilePath/M101_-_Detail.jpg?width=1600");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            animation: galaxyZoom 8s ease-in-out infinite alternate;
            will-change: transform;
            filter: brightness(0.88) contrast(1.12) saturate(1.12);
        }

        .galaxy-vignette {
            position: absolute;
            inset: 0;
            background: radial-gradient(
                ellipse at center,
                transparent 35%,
                rgba(0, 0, 8, 0.65) 100%
            );
            animation: galaxyGlow 4s ease-in-out infinite alternate;
            pointer-events: none;
        }

        .galaxy-stars {
            position: absolute;
            inset: 0;
            background-image:
                radial-gradient(1px 1px at 12% 20%, white, transparent),
                radial-gradient(1px 1px at 82% 30%, white, transparent),
                radial-gradient(1.5px 1.5px at 25% 75%, white, transparent),
                radial-gradient(1px 1px at 90% 82%, white, transparent);
            opacity: 0.55;
            animation: galaxyStars 7s ease-in-out infinite alternate;
            pointer-events: none;
        }

        @keyframes galaxyZoom {
            from { transform: scale(1); }
            to { transform: scale(1.16); }
        }

        @keyframes galaxyStars {
            from {
                opacity: 0.2;
                transform: translate(0, 0);
            }
            to {
                opacity: 0.8;
                transform: translate(-8px, -15px);
            }
        }

        @keyframes galaxyGlow {
            from { opacity: 0.65; }
            to { opacity: 1; }
        }
        </style>

        <div class="galaxy-scene">
            <div class="galaxy-photo"></div>
            <div class="galaxy-stars"></div>
            <div class="galaxy-vignette"></div>
        </div>
        """, unsafe_allow_html=True)

    elif "milky way" in selected_name.lower():
        st.markdown("""
        <style>
        .milky-scene {
            height: 420px;
            width: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 18px;
            background: #00020a;
            isolation: isolate;
        }

        .milky-image {
            position: absolute;
            inset: -8%;
            background-image: url(
                "https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/2023/09/s/ssc2008-10a.tif?fit=clip&w=1600&h=1600"
            );
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            filter: brightness(1.15) contrast(1.15) saturate(1.3);
            animation: milkyDrift 16s ease-in-out infinite alternate;
            will-change: transform;
        }

        .milky-glow {
            position: absolute;
            inset: 0;
            background: radial-gradient(
                ellipse at center,
                transparent 25%,
                rgba(0, 0, 12, 0.2) 65%,
                rgba(0, 0, 8, 0.85) 100%
            );
            animation: milkyPulse 5s ease-in-out infinite alternate;
            pointer-events: none;
        }

        .milky-stars {
            position: absolute;
            inset: 0;
            background-image:
                radial-gradient(1px 1px at 15% 20%, white, transparent),
                radial-gradient(1.5px 1.5px at 75% 25%, white, transparent),
                radial-gradient(1px 1px at 35% 80%, white, transparent),
                radial-gradient(2px 2px at 88% 72%, white, transparent),
                radial-gradient(1px 1px at 55% 12%, white, transparent);
            animation: milkyTwinkle 4s ease-in-out infinite alternate;
            pointer-events: none;
        }

        @keyframes milkyDrift {
            from {
                transform: scale(1) rotate(-1deg);
            }
            to {
                transform: scale(1.18) rotate(1deg);
            }
        }

        @keyframes milkyPulse {
            from { opacity: 0.45; }
            to { opacity: 0.9; }
        }

        @keyframes milkyTwinkle {
            from { opacity: 0.25; }
            to { opacity: 0.9; }
        }
        </style>

        <div class="milky-scene">
            <div class="milky-image"></div>
            <div class="milky-stars"></div>
            <div class="milky-glow"></div>
        </div>
               """, unsafe_allow_html=True)

    elif "solar system" in selected_name.lower():

        
       components.html(
            """
            <style>
            .ss-scene {
                height: 460px;
                width: 100%;
                position: relative;
                overflow: hidden;
                border-radius: 18px;
                background: radial-gradient(ellipse at center, #17101d 0%, #080b18 48%, #01030a 100%);
            }

            .ss-stars {
                position: absolute;
                inset: 0;
                background-image:
                    radial-gradient(2px 2px at 10% 18%, white, transparent),
                    radial-gradient(2px 2px at 22% 76%, white, transparent),
                    radial-gradient(2px 2px at 85% 22%, white, transparent),
                    radial-gradient(2px 2px at 72% 85%, white, transparent),
                    radial-gradient(2px 2px at 48% 12%, white, transparent);
            }

            .ss-system {
                position: absolute;
                width: 660px;
                height: 420px;
                left: 50%;
                top: 50%;
                transform: translate(-50%, -50%);
            }

            .ss-sun {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 75px;
    height: 75px;
    transform: translate(-50%, -50%);
    border-radius: 50%;

    background: radial-gradient(
        circle at 35% 35%,
        #ffffff 0%,
        #fff7bd 15%,
        #ffd34e 40%,
        #ff8b25 70%,
        #b83210 100%
    );

    box-shadow:
        0 0 15px #fff2a8,
        0 0 35px #ffb347,
        0 0 75px #ff8b25,
        0 0 130px rgba(255, 100, 0, 0.55);

    z-index: 5;
    animation: sunPulse 3s ease-in-out infinite alternate;
}

@keyframes sunPulse {
    from {
        box-shadow:
            0 0 15px #fff2a8,
            0 0 35px #ffb347,
            0 0 75px #ff8b25,
            0 0 110px rgba(255, 100, 0, 0.4);
    }

    to {
        box-shadow:
            0 0 25px #fff2a8,
            0 0 50px #ffb347,
            0 0 100px #ff8b25,
            0 0 150px rgba(255, 100, 0, 0.65);
    }
}

            .ss-orbit {
    position: absolute;
    left: 50%;
    top: 50%;
    border: 1px solid rgba(180,195,220,.35);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    animation: none;
}



            .ss-planet {
    position: absolute;
    left: 0;
    top: 0;
    border-radius: 50%;

    offset-path: ellipse(50% 50% at 50% 50%);
    offset-anchor: 50% 50%;
    offset-rotate: 0deg;

    animation: ssPlanetOrbit linear infinite;
    animation-duration: inherit;
}

            .ss-mercury { width: 100px; height: 74px; animation-duration: 5s; }
            .ss-venus { width: 150px; height: 110px; animation-duration: 8s; }
            .ss-earth { width: 200px; height: 146px; animation-duration: 11s; }
            .ss-mars { width: 250px; height: 182px; animation-duration: 15s; }
            .ss-jupiter { width: 310px; height: 226px; animation-duration: 22s; }
            .ss-saturn { width: 380px; height: 276px; animation-duration: 28s; }
            .ss-uranus { width: 450px; height: 328px; animation-duration: 35s; }
            .ss-neptune { width: 520px; height: 378px; animation-duration: 43s; }

            .p-mercury { width: 9px; height: 9px; background: #aaa; }
            .p-venus { width: 15px; height: 15px; background: #d6a45e; }
            .p-earth { width: 17px; height: 17px; background: radial-gradient(circle at 30% 30%, #75d66b, #287ec0 55%, #09254f); box-shadow: 0 0 10px #4ba0ff; }
            .p-mars { width: 13px; height: 13px; background: #bd4e2d; }
            .p-jupiter { width: 31px; height: 31px; background: repeating-linear-gradient(0deg, #d8b18b 0 4px, #a76e4c 5px 8px); }
            .p-saturn { width: 25px; height: 25px; background: #d2b77e; }
            .p-uranus { width: 20px; height: 20px; background: #70c6d2; }
            .p-neptune { width: 20px; height: 20px; background: #2859cf; }

           
           @keyframes ssPlanetOrbit {
    from {
        offset-distance: 0%;
    }
    to {
        offset-distance: 100%;
    }
}

            @media (max-width: 700px) {
                .ss-system { transform: translate(-50%, -50%) scale(.72); }
            }
            </style>

            <div class="ss-scene">
                <div class="ss-stars"></div>
                <div class="ss-system">
                    <div class="ss-sun"></div>

                    <div class="ss-orbit ss-mercury"><div class="ss-planet p-mercury"></div></div>
                    <div class="ss-orbit ss-venus"><div class="ss-planet p-venus"></div></div>
                    <div class="ss-orbit ss-earth"><div class="ss-planet p-earth"></div></div>
                    <div class="ss-orbit ss-mars"><div class="ss-planet p-mars"></div></div>
                    <div class="ss-orbit ss-jupiter"><div class="ss-planet p-jupiter"></div></div>
                    <div class="ss-orbit ss-saturn"><div class="ss-planet p-saturn"></div></div>
                    <div class="ss-orbit ss-uranus"><div class="ss-planet p-uranus"></div></div>
                    <div class="ss-orbit ss-neptune"><div class="ss-planet p-neptune"></div></div>
                </div>
            </div>
            """,
height=700,
scrolling=False
)


    st.session_state.previous_event = selected_name


# ---------------- PYTHON + C CALCULATION ----------------

cosmic_day = calculate_cosmic_day(
    universe_age,
    selected_event["age"]
)

st.markdown(f"""
<div class="detail-box">
    <h2>{selected_event['emoji']} {selected_event['name']}</h2>
    <p><b>When:</b> {selected_event['time']}</p>
    <p>{selected_event['description']}</p>
    <p>💡 <b>Did you know?</b> {selected_event['fact']}</p>
</div>
""", unsafe_allow_html=True)

st.write("")
if selected_event["name"] == "Earth Forms":

    st.write(
        "Around 4.54 billion years ago, "
        "rocky material collided and gradually formed Earth."
    )

    components.html(
        """
        <html>
        <head>
        <style>
        body {
            margin: 0;
            background: #050817;
            font-family: Arial;
        }

        .scene {
            height: 500px;
            position: relative;
            overflow: hidden;
            border-radius: 18px;
            background: radial-gradient(ellipse, #28101b, #050817 75%);
        }

        .stars {
            position: absolute;
            inset: 0;
            background-image:
                radial-gradient(white 1px, transparent 1px),
                radial-gradient(#9dbaff 1px, transparent 1px);
            background-size: 65px 65px, 100px 100px;
            animation: stars 15s linear infinite;
        }

        .earth {
            position: absolute;
            width: 240px;
            height: 240px;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            background:
                radial-gradient(circle at 35% 30%, #ffd27a, transparent 25%),
                radial-gradient(circle at 65% 70%, #a91f0b, transparent 40%),
                radial-gradient(circle, #ff9b25, #d83a0b 60%, #240b15);
            box-shadow: 0 0 45px #ff5b1a, 0 0 100px #d83a0b;
            animation: pulse 3s ease-in-out infinite alternate;
        }

        .meteor {
            position: absolute;
            width: 65px;
            height: 3px;
            background: linear-gradient(90deg, transparent, orange, white);
            box-shadow: 0 0 12px orange;
            animation: fall 3s linear infinite;
        }

        .m1 { top: 10%; left: 5%; }
        .m2 { top: 25%; right: 5%; animation-delay: 1s; }
        .m3 { top: 0; left: 65%; animation-delay: 2s; }

        .caption {
            position: absolute;
            bottom: 22px;
            width: 100%;
            text-align: center;
            color: #ffd49a;
            font-size: 17px;
        }

        @keyframes pulse {
            from { box-shadow: 0 0 35px #ff5b1a; }
            to { box-shadow: 0 0 100px #ff9b25, 0 0 140px #d83a0b; }
        }

        @keyframes fall {
            0% { transform: translate(0, 0) rotate(25deg); opacity: 0; }
            15% { opacity: 1; }
            100% { transform: translate(250px, 250px) rotate(25deg); opacity: 0; }
        }

        @keyframes stars {
            to { transform: translateY(-65px); }
        }
        </style>
        </head>

        <body>
        <div class="scene">
            <div class="stars"></div>
            <div class="earth"></div>
            <div class="meteor m1"></div>
            <div class="meteor m2"></div>
            <div class="meteor m3"></div>
            <div class="caption">
                🌍 EARTH FORMATION • 4.54 BILLION YEARS AGO
            </div>
        </div>
        </body>
        </html>
        """,
        height=520,
        scrolling=False
    )

# ---------------- LIFE ON EARTH ANIMATION ----------------


# ---------------- 3D LIFE ON EARTH ANIMATION ----------------

if selected_event["name"] == "Life on Earth":

    st.write("🌊 3D Exploration: Ancient Deep Ocean")

    components.html(
        """
        <html>
        <head>
            <style>
                body {
                    margin: 0;
                    overflow: hidden;
                    background: #010817;
                }

                #ocean {
                    width: 100%;
                    height: 540px;
                    border-radius: 16px;
                    overflow: hidden;
                }

                canvas {
                    display: block;
                }

                #caption {
                    position: absolute;
                    bottom: 20px;
                    width: 100%;
                    text-align: center;
                    color: #b5edff;
                    font-family: Arial;
                    font-size: 15px;
                    letter-spacing: 2px;
                    text-shadow: 0 0 12px #00bfff;
                    pointer-events: none;
                }
            </style>
        </head>

        <body>
            <div id="ocean">
                <div id="caption">
                    ANCIENT OCEAN • ORIGINS OF LIFE
                </div>
            </div>

            <script type="module">
                import * as THREE from
                'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

                const container = document.getElementById("ocean");

                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0x010817);
                scene.fog = new THREE.FogExp2(0x03172b, 0.035);

                const camera = new THREE.PerspectiveCamera(
                    60,
                    container.clientWidth / container.clientHeight,
                    0.1,
                    100
                );

                camera.position.set(0, 5, 17);
                camera.lookAt(0, 2, 0);

                const renderer = new THREE.WebGLRenderer({
                    antialias: true
                });

                renderer.setSize(
                    container.clientWidth,
                    container.clientHeight
                );

                renderer.setPixelRatio(
                    Math.min(window.devicePixelRatio, 2)
                );

                renderer.toneMapping = THREE.ACESFilmicToneMapping;
                renderer.toneMappingExposure = 1.2;

                container.appendChild(renderer.domElement);

                // LIGHTING

                const ambient = new THREE.AmbientLight(
  0x163b55, 0.8
);
            
                scene.add(ambient);

                const blueLight = new THREE.PointLight(
    0x087ca8, 180, 38
);
                blueLight.position.set(0, 9, 3);
                scene.add(blueLight);

               const ventLight = new THREE.PointLight(
    0x16d9d0, 110, 18
);
                ventLight.position.set(0, 2, 1);
                scene.add(ventLight);

// CINEMATIC UNDERWATER LIGHT RAYS

const lightRays = [];

const rayMaterial = new THREE.MeshBasicMaterial({
    color: 0x55cfff,
    transparent: true,
    opacity: 0.09,
    side: THREE.DoubleSide,
    depthWrite: false
});

for (let i = 0; i < 7; i++) {

    const rayGeometry = new THREE.CylinderGeometry(
        0.12,
        0.9,
        11,
        16,
        1,
        true
    );

    const ray = new THREE.Mesh(
        rayGeometry,
        rayMaterial.clone()
    );

    ray.position.set(
        (i - 3) * 2.5,
        3.5,
        -3 - Math.random() * 3
    );

    ray.rotation.z = (Math.random() - 0.5) * 0.3;
    ray.rotation.x = (Math.random() - 0.5) * 0.2;

    scene.add(ray);
    lightRays.push(ray);
}

                // OCEAN FLOOR

                const floorGeometry = new THREE.PlaneGeometry(
                    45, 45, 50, 50
                );

                const positions = floorGeometry.attributes.position;

                for (let i = 0; i < positions.count; i++) {
                    positions.setZ(
                        i,
                        Math.random() * 0.7
                    );
                }

                floorGeometry.computeVertexNormals();

                const floorMaterial = new THREE.MeshStandardMaterial({
                    color: 0x182b32,
                    roughness: 1,
                    metalness: 0.1
                });

                const floor = new THREE.Mesh(
                    floorGeometry,
                    floorMaterial
                );

                floor.rotation.x = -Math.PI / 2;
                floor.position.y = -2;
                scene.add(floor);

                // ROCKS

                const rockMaterial = new THREE.MeshStandardMaterial({
                    color: 0x263b43,
                    roughness: 0.95
                });

                for (let i = 0; i < 35; i++) {
                    const rock = new THREE.Mesh(
                        new THREE.DodecahedronGeometry(
                            0.5 + Math.random() * 1.2, 0
                        ),
                        rockMaterial
                    );

                    rock.position.set(
                        (Math.random() - 0.5) * 28,
                        -1.8 + Math.random() * 0.3,
                        (Math.random() - 0.5) * 12
                    );

                    rock.scale.y = 0.5 + Math.random();
                    rock.rotation.set(
                        Math.random(),
                        Math.random(),
                        Math.random()
                    );

                    scene.add(rock);
                }

// PRIMITIVE MICROBIAL COLONIES

const colonies = [];

const colonyColors = [
    0x39e6c0,
    0x70ff9c,
    0x39bfff
];

for (let i = 0; i < 18; i++) {

    const colony = new THREE.Group();

    const cellCount = 8 + Math.floor(Math.random() * 12);

    const colonyColor = colonyColors[
        Math.floor(Math.random() * colonyColors.length)
    ];

    for (let j = 0; j < cellCount; j++) {

        const size = 0.06 + Math.random() * 0.09;

        const cell = new THREE.Mesh(
            new THREE.SphereGeometry(size, 10, 10),

            new THREE.MeshStandardMaterial({
                color: colonyColor,
                emissive: colonyColor,
                emissiveIntensity: 1.4,
                roughness: 0.6
            })
        );

        cell.position.set(
            (Math.random() - 0.5) * 0.9,
            Math.random() * 0.35,
            (Math.random() - 0.5) * 0.9
        );

        colony.add(cell);
    }

    colony.position.set(
        (Math.random() - 0.5) * 22,
        -1.35,
        (Math.random() - 0.5) * 9
    );

    scene.add(colony);

    colonies.push({
        mesh: colony,
        phase: Math.random() * Math.PI * 2
    });
}

                // HYDROTHERMAL VENTS

                const vents = [];

                for (let i = 0; i < 4; i++) {
                    const group = new THREE.Group();

                    const height = 2 + Math.random() * 1.4;

                    const chimney = new THREE.Mesh(
                        new THREE.CylinderGeometry(
                            0.25, 0.65, height, 8
                        ),
                        new THREE.MeshStandardMaterial({
                            color: 0x34464b,
                            roughness: 0.85
                        })
                    );

                    chimney.position.y = height / 2 - 1.8;
                    group.add(chimney);

                    const opening = new THREE.Mesh(
                        new THREE.TorusGeometry(0.28, 0.09, 8, 16),
                        new THREE.MeshStandardMaterial({
                            color: 0x142b32,
                            emissive: 0x075b62,
                            emissiveIntensity: 1.5
                        })
                    );

                    opening.position.y = height - 1.75;
                    opening.rotation.x = Math.PI / 2;
                    group.add(opening);

                    group.position.set(
                        (i - 1.5) * 3,
                        0,
                        -1 + Math.random() * 2
                    );

                    scene.add(group);
                    vents.push(group);
                }

                
// REALISTIC HYDROTHERMAL VENT SMOKE

const smokeParticles = [];

const smokeColors = [
    0x182d35,
    0x31515a,
    0x527d82,
    0x78a9a8
];

for (let i = 0; i < 450; i++) {

    const size = 0.07 + Math.random() * 0.16;

    const geometry = new THREE.SphereGeometry(
        size, 6, 6
    );

    const material = new THREE.MeshBasicMaterial({
        color: smokeColors[
            Math.floor(Math.random() * smokeColors.length)
        ],
        transparent: true,
        opacity: 0.12 + Math.random() * 0.2,
        depthWrite: false
    });

    const particle = new THREE.Mesh(
        geometry,
        material
    );

    particle.position.set(
        (Math.random() - 0.5) * 1.8,
        Math.random() * 7 - 1.5,
        (Math.random() - 0.5) * 1.8
    );

    scene.add(particle);

    smokeParticles.push({
        mesh: particle,
        speed: 0.008 + Math.random() * 0.018,
        drift: Math.random() * 0.01,
        startX: particle.position.x
    });
}

                
// REALISTIC MICROSCOPIC ORGANISMS

const organisms = [];

const organismColors = [
    0x51e5cf,
    0x8aff9c,
    0x49c5ff,
    0xc58aff
];

for (let i = 0; i < 35; i++) {

    const size = 0.07 + Math.random() * 0.09;

    const geometry = new THREE.SphereGeometry(
        size, 16, 16
    );

    const material = new THREE.MeshStandardMaterial({
        color: organismColors[
            Math.floor(Math.random() * organismColors.length)
        ],
        emissive: 0x087c75,
        emissiveIntensity: 1.5,
        roughness: 0.5
    });

    const organism = new THREE.Mesh(
        geometry,
        material
    );

    // Some organisms are rod-shaped
    const isRod = Math.random() > 0.5;

    if (isRod) {
        organism.scale.set(1.8, 0.65, 0.65);
    }

    organism.position.set(
        (Math.random() - 0.5) * 12,
        Math.random() * 5,
        (Math.random() - 0.5) * 6
    );

    scene.add(organism);

    organisms.push({
        mesh: organism,
        speed: 0.2 + Math.random() * 0.5,
        drift: Math.random() * 0.015,
        phase: Math.random() * Math.PI * 2,
        isRod: isRod
    });
}


                // BUBBLES

                const bubbles = [];

                for (let i = 0; i < 45; i++) {
                    const bubble = new THREE.Mesh(
                        new THREE.SphereGeometry(
                            0.035 + Math.random() * 0.05, 8, 8
                        ),
                        new THREE.MeshBasicMaterial({
                            color: 0x9ceaff,
                            transparent: true,
                            opacity: 0.5
                        })
                    );

                    bubble.position.set(
                        (Math.random() - 0.5) * 18,
                        Math.random() * 9 - 2,
                        (Math.random() - 0.5) * 10
                    );

                    scene.add(bubble);
                    bubbles.push(bubble);
                }

// GLOWING ORGANIC PARTICLES

const organicParticles = [];

const particleColors = [
    0x48ffe0,
    0x62baff,
    0x9affb5,
    0xc58aff
];

for (let i = 0; i < 100; i++) {

    const size = 0.025 + Math.random() * 0.045;

    const particle = new THREE.Mesh(
        new THREE.SphereGeometry(size, 8, 8),

        new THREE.MeshBasicMaterial({
            color: particleColors[
                Math.floor(Math.random() * particleColors.length)
            ],
            transparent: true,
            opacity: 0.35 + Math.random() * 0.5
        })
    );

    particle.position.set(
        (Math.random() - 0.5) * 18,
        Math.random() * 8,
        (Math.random() - 0.5) * 10
    );

    scene.add(particle);

    organicParticles.push({
        mesh: particle,
        speed: 0.003 + Math.random() * 0.008,
        phase: Math.random() * Math.PI * 2
    });
}

                // ANIMATION

                const clock = new THREE.Clock();

                function animate() {
                    requestAnimationFrame(animate);

                    const t = clock.getElapsedTime();

// Slowly moving underwater light rays

lightRays.forEach((ray, i) => {
    ray.rotation.z =
        Math.sin(t * 0.25 + i) * 0.12;

    ray.material.opacity =
        0.05 + Math.sin(t * 0.8 + i) * 0.025;
});

                    // Cinematic underwater camera movement

const zoom = Math.sin(t * 0.18) * 1.5;

camera.position.x = Math.sin(t * 0.15) * 2;
camera.position.y = 5 + Math.sin(t * 0.2) * 0.5;
camera.position.z = 17 - zoom;

camera.lookAt(
    Math.sin(t * 0.12) * 1.5,
    2.5,
    0
);

                    vents.forEach((vent, i) => {
                        vent.rotation.y =
                            Math.sin(t * 0.2 + i) * 0.08;
                    });

                    
// NATURAL RISING SMOKE MOVEMENT

smokeParticles.forEach((p, i) => {

    p.mesh.position.y += p.speed;

    p.mesh.position.x +=
        Math.sin(t * 0.5 + i) * p.drift;

    p.mesh.position.z +=
        Math.cos(t * 0.4 + i) * 0.002;

    p.mesh.scale.multiplyScalar(1.0005);

    if (p.mesh.position.y > 7) {

        p.mesh.position.y = -1.5;

        p.mesh.position.x =
            p.startX + (Math.random() - 0.5) * 1.5;

        p.mesh.position.z =
            (Math.random() - 0.5) * 1.8;

        p.mesh.scale.setScalar(1);
    }
});

                   
// NATURAL MICROORGANISM SWIMMING

organisms.forEach((o, i) => {

    o.mesh.position.x +=
        Math.sin(t * 0.7 + o.phase) * o.drift;

    o.mesh.position.y +=
        Math.cos(t * o.speed + o.phase) * 0.008;

    o.mesh.position.z +=
        Math.sin(t * 0.5 + o.phase) * 0.006;

    // Natural rotation
    o.mesh.rotation.x =
        Math.sin(t * 0.4 + o.phase) * 0.3;

    o.mesh.rotation.y += 0.008;

    // Keep organisms inside the underwater scene
    if (o.mesh.position.x > 7) {
        o.mesh.position.x = -7;
    }

    if (o.mesh.position.x < -7) {
        o.mesh.position.x = 7;
    }

    if (o.mesh.position.y > 7) {
        o.mesh.position.y = 0;
    }

    if (o.mesh.position.y < 0) {
        o.mesh.position.y = 7;
    }
});

// CELL DIVISION ANIMATION

organisms.forEach((o, i) => {

    // Each organism divides at its own interval
    if (o.nextDivision === undefined) {
        o.nextDivision = 8 + Math.random() * 15;
    }

    if (t > o.nextDivision && organisms.length < 65) {

        // Create a new daughter cell
        const daughter = o.mesh.clone();

        daughter.material = o.mesh.material.clone();

        daughter.position.copy(o.mesh.position);

        daughter.position.x += 0.15;

        daughter.scale.copy(o.mesh.scale);

        scene.add(daughter);

        organisms.push({
            mesh: daughter,
            speed: 0.2 + Math.random() * 0.5,
            drift: Math.random() * 0.015,
            phase: Math.random() * Math.PI * 2,
            isRod: o.isRod,
            nextDivision: t + 15 + Math.random() * 15
        });

        // Original cell moves slightly away
        o.mesh.position.x -= 0.15;

        // Prevent immediate repeated division
        o.nextDivision = t + 15 + Math.random() * 15;
    }
});

                    bubbles.forEach((b) => {
                        b.position.y += 0.025;

                        if (b.position.y > 8) {
                            b.position.y = -2;
                        }
                    });

                    renderer.render(scene, camera);
                }

                animate();

// FLOATING ORGANIC PARTICLE MOVEMENT

organicParticles.forEach((p, i) => {

// GENTLE MICROBIAL COLONY MOVEMENT

colonies.forEach((c) => {

    c.mesh.children.forEach((cell, i) => {

        cell.position.y +=
            Math.sin(t * 0.8 + c.phase + i) * 0.0008;

        cell.scale.setScalar(
            1 + Math.sin(t * 1.5 + i) * 0.06
        );
    });
});

    p.mesh.position.y += p.speed;

    p.mesh.position.x +=
        Math.sin(t * 0.5 + p.phase) * 0.003;

    p.mesh.position.z +=
        Math.cos(t * 0.4 + p.phase) * 0.002;

    // Gentle glowing effect
    p.mesh.material.opacity =
        0.3 + Math.sin(t * 2 + p.phase) * 0.2;

    if (p.mesh.position.y > 8) {
        p.mesh.position.y = -1;
    }
});

                // RESPONSIVE SIZE

                window.addEventListener("resize", () => {
                    const width = container.clientWidth;
                    const height = container.clientHeight;

                    camera.aspect = width / height;
                    camera.updateProjectionMatrix();

                    renderer.setSize(width, height);
                });
            </script>
        </body>
        </html>
        """,
        height=560,
        scrolling=False
    )


st.write("")
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Cosmic Calendar Day",
        f"{cosmic_day:.2f} / 365"
    )

with col2:
    st.metric(
        "Years Ago",
        f"{selected_event['age'] / 1e9:.3f} Billion"
    )

st.progress(min(max(cosmic_day / 365, 0.0), 1.0))

st.caption(
    "Cosmic Calendar calculation is performed using our C program through Python."
)


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<center>🌌 Universe Timeline Explorer | Made by CSE Students</center>",
    unsafe_allow_html=True
)

st.markdown(
    "<center><small>Explore the past. Understand the present. Imagine the future.</small></center>",
    unsafe_allow_html=True
)
st.markdown("---")

st.title("🌌 Explore the 3D Universe")

st.write(
    "Rotate, zoom and explore a procedurally generated spiral galaxy."
)

galaxy_fig = create_galaxy()

st.plotly_chart(
    galaxy_fig,
    use_container_width=True
)
st.markdown("---")


st.markdown("---")

st.title("☀️ Interactive 3D Solar System")

st.write(
    "Watch planets orbit around the Sun "
    "in an interactive 3D simulation."
)

solar_fig = create_solar_system()

st.plotly_chart(
    solar_fig,
    use_container_width=True,
    key="solar_system_animation"
)




# ---------------- EARTH FORMATION ANIMATION ----------------

if selected_name == "Earth Forms":

    st.markdown("---")
    st.write("🔥 Watch how the early Earth formed")
    st.write(
        "Around 4.54 billion years ago, "
        "rocky material collided and slowly formed our planet."
    )

    components.html(
        """
        <html>
        <head>
        <style>
        body {
            margin: 0;
            background: #050817;
            font-family: Arial, sans-serif;
            color: white;
        }

        .scene {
            height: 500px;
            width: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 18px;
            background:
                radial-gradient(ellipse at center,
                #24101b 0%, #0b1025 55%, #02040b 100%);
        }

        .stars {
            position: absolute;
            inset: 0;
            background-image:
                radial-gradient(white 1px, transparent 1px),
                radial-gradient(#9dbaff 1px, transparent 1px);
            background-size: 75px 75px, 115px 115px;
            animation: starMove 20s linear infinite;
        }

        .planet {
            position: absolute;
            width: 245px;
            height: 245px;
            left: 50%;
            top: 48%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            background:
                radial-gradient(circle at 35% 30%,
                    #ffd27a 0%, transparent 22%),
                radial-gradient(ellipse at 65% 70%,
                    #a91f0b 0%, transparent 35%),
                radial-gradient(circle at 45% 45%,
                    #ff9b25 0%, #d83a0b 45%,
                    #54120c 78%, #160b16 100%);
            box-shadow:
                0 0 35px #ff5b1a,
                0 0 85px #d83a0b,
                inset -25px -15px 35px #260812;
            animation: planetPulse 4s ease-in-out infinite;
        }

        .crust {
            position: absolute;
            width: 245px;
            height: 245px;
            left: 50%;
            top: 48%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            background:
                radial-gradient(ellipse at 25% 35%,
                    #4c2923 0%, transparent 22%),
                radial-gradient(ellipse at 75% 65%,
                    #27151d 0%, transparent 28%),
                radial-gradient(ellipse at 45% 85%,
                    #4a2119 0%, transparent 25%);
            animation: crustForm 8s ease-in-out infinite alternate;
        }

        .meteor {
            position: absolute;
            width: 65px;
            height: 3px;
            background: linear-gradient(90deg,
                transparent, #ffb34d, white);
            border-radius: 50%;
            box-shadow: 0 0 12px #ff781c;
            animation: meteorFall 3s linear infinite;
        }

        .m1 {
            top: 15%;
            left: 5%;
        }

        .m2 {
            top: 28%;
            right: 5%;
            animation-delay: 1.2s;
        }

        .m3 {
            top: 5%;
            left: 65%;
            animation-delay: 2s;
        }

        .impact {
            position: absolute;
            width: 35px;
            height: 35px;
            border: 2px solid #ffb14b;
            border-radius: 50%;
            left: 58%;
            top: 45%;
            animation: impactPulse 2s ease-out infinite;
        }

        .caption {
            position: absolute;
            bottom: 22px;
            width: 100%;
            text-align: center;
            color: #ffd49a;
            font-size: 17px;
            letter-spacing: 1px;
        }

        @keyframes planetPulse {
            0%, 100% { box-shadow: 0 0 35px #ff5b1a, 0 0 85px #d83a0b; }
            50% { box-shadow: 0 0 55px #ff9b25, 0 0 120px #e43b0b; }
        }

        @keyframes crustForm {
            from { opacity: 0.1; }
            to { opacity: 0.9; }
        }

        @keyframes meteorFall {
            0% { transform: translate(0, 0) rotate(25deg); opacity: 0; }
            15% { opacity: 1; }
            100% { transform: translate(250px, 250px) rotate(25deg); opacity: 0; }
        }

        @keyframes impactPulse {
            0% { transform: scale(0.5); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }

        @keyframes starMove {
            from { transform: translateY(0); }
            to { transform: translateY(-75px); }
        }
        </style>
        </head>

        <body>
        <div class="scene">
            <div class="stars"></div>
            <div class="planet"></div>
            <div class="crust"></div>
            <div class="meteor m1"></div>
            <div class="meteor m2"></div>
            <div class="meteor m3"></div>
            <div class="impact"></div>
            <div class="caption">
                🌍 EARTH FORMATION • 4.54 BILLION YEARS AGO
            </div>
        </div>
        </body>
        </html>
        """,
        height=520,
        scrolling=False
    )
